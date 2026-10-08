"""
pathfinding.py — Dijkstra & A* based route engine for RailSaathi

Supports:
  • Shortest path (Dijkstra)
  • Accessible-only path (avoids stairs, uses lifts/ramps)
  • Elder-friendly path (prefer ground-level, shorter walks)
  • Avoidance of blocked/disrupted paths
  • Turn-by-turn direction generation
"""

from __future__ import annotations
import heapq, math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

from station_graph import Node, Edge, build_adjacency


@dataclass
class RouteStep:
    """One step in a turn-by-turn navigation sequence."""
    instruction: str               # e.g. "Walk 25 m along Platform 1"
    instruction_kn: str = ""
    instruction_hi: str = ""
    from_node: str = ""
    to_node: str = ""
    distance: float = 0.0          # metres
    path_type: str = "normal"
    level: str = "ground"
    landmark: str = ""              # nearby landmark for orientation
    direction: str = "straight"     # straight | left | right | up | down
    accessibility_note: str = ""


@dataclass
class RouteResult:
    """Complete route from origin → destination."""
    found: bool
    origin: str
    destination: str
    total_distance: float = 0.0
    estimated_time_seconds: float = 0.0   # walking ~1.2 m/s normal, ~0.8 m/s elderly
    steps: List[RouteStep] = field(default_factory=list)
    path_node_ids: List[str] = field(default_factory=list)
    accessibility_mode: str = "normal"
    warnings: List[str] = field(default_factory=list)


# ── Dijkstra's algorithm ────────────────────────────────────────────────

def dijkstra(
    adj: Dict[str, List[Tuple[str, float, Edge]]],
    start: str,
    end: str,
    elder_mode: bool = False,
) -> Tuple[Optional[List[str]], float]:
    """
    Standard Dijkstra. Returns (path, total_distance).
    In elder_mode, stairs get a 3x penalty to discourage them.
    """
    if start not in adj or end not in adj:
        return None, float("inf")

    dist = {start: 0.0}
    prev = {}
    pq = [(0.0, start)]
    visited: Set[str] = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            break

        for v, w, edge in adj[u]:
            if v in visited:
                continue
            cost = w
            # Elder mode: penalise stairs heavily
            if elder_mode and edge.path_type == "stairs":
                cost *= 3.0
            # Slight preference for lifts/ramps in elder mode
            if elder_mode and edge.path_type in ("lift", "ramp"):
                cost *= 0.5

            nd = d + cost
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    if end not in prev and start != end:
        return None, float("inf")

    # Reconstruct path
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = prev.get(cur)
        if cur is None:
            return None, float("inf")
    path.append(start)
    path.reverse()
    return path, dist.get(end, float("inf"))


# ── Direction generation ────────────────────────────────────────────────

_PATH_TYPE_VERB = {
    "normal":     ("Walk",       "ನಡೆಯಿರಿ",      "चलिए"),
    "stairs":     ("Take stairs","ಮೆಟ್ಟಿಲುಗಳನ್ನು ಬಳಸಿ", "सीढ़ियाँ लीजिए"),
    "ramp":       ("Use ramp",   "ರ‍್ಯಾಂಪ್ ಬಳಸಿ",  "रैंप का उपयोग करें"),
    "lift":       ("Take lift",  "ಲಿಫ್ಟ್ ತೆಗೆದುಕೊಳ್ಳಿ", "लिफ्ट लीजिए"),
    "subway":     ("Walk through subway", "ಸಬ್‌ವೇ ಮೂಲಕ ನಡೆಯಿರಿ", "सबवे से चलिए"),
    "escalator":  ("Take escalator", "ಎಸ್ಕಲೇಟರ್ ತೆಗೆದುಕೊಳ್ಳಿ", "एस्केलेटर लीजिए"),
    "fob_bridge": ("Walk across bridge", "ಸೇತುವೆ ಮೇಲೆ ನಡೆಯಿರಿ", "पुल पर चलिए"),
}

def _infer_direction(nodes: Dict[str, Node], prev_id: Optional[str], cur_id: str, next_id: str) -> str:
    """Heuristic direction based on coordinate changes."""
    cur = nodes[cur_id]
    nxt = nodes[next_id]
    dx = nxt.x - cur.x
    dy = nxt.y - cur.y

    # Level changes
    if nxt.level != cur.level:
        if nxt.level in ("fob",):
            return "up"
        if nxt.level in ("subway",):
            return "down"
        if cur.level in ("fob", "subway"):
            return "up" if nxt.level == "ground" and cur.level == "subway" else "down" if cur.level == "fob" else "straight"

    if abs(dx) < 1 and abs(dy) < 1:
        return "straight"
    angle = math.degrees(math.atan2(dx, dy))  # 0=north
    if -45 <= angle <= 45:
        return "straight"  # north-ish
    elif angle > 45 and angle < 135:
        return "right"
    elif angle < -45 and angle > -135:
        return "left"
    return "straight"


def generate_directions(
    path: List[str],
    nodes: Dict[str, Node],
    edges: List[Edge],
    lang: str = "en",
) -> List[RouteStep]:
    """Convert a node-path into human-readable turn-by-turn directions."""
    if not path or len(path) < 2:
        return []

    # Build quick edge lookup
    edge_map: Dict[Tuple[str, str], Edge] = {}
    for e in edges:
        edge_map[(e.from_node, e.to_node)] = e
        if e.bidirectional:
            edge_map[(e.to_node, e.from_node)] = e

    steps: List[RouteStep] = []
    for idx in range(len(path) - 1):
        a, b = path[idx], path[idx + 1]
        edge = edge_map.get((a, b))
        if not edge:
            continue

        pt = edge.path_type
        dist = edge.distance
        verb_en, verb_kn, verb_hi = _PATH_TYPE_VERB.get(pt, ("Walk", "ನಡೆಯಿರಿ", "चलिए"))

        dest_node = nodes[b]
        prev_id = path[idx - 1] if idx > 0 else None
        direction = _infer_direction(nodes, prev_id, a, b)

        # English instruction
        instr_en = f"{verb_en} {dist:.0f}m to {dest_node.name}"
        if direction in ("left", "right"):
            instr_en = f"Turn {direction}, then {verb_en.lower()} {dist:.0f}m to {dest_node.name}"
        elif direction == "up":
            instr_en = f"{verb_en} going up to {dest_node.name}"
        elif direction == "down":
            instr_en = f"{verb_en} going down to {dest_node.name}"

        # Kannada instruction
        dest_kn = dest_node.name_kn or dest_node.name
        dir_kn = {"left": "ಎಡಕ್ಕೆ ತಿರುಗಿ", "right": "ಬಲಕ್ಕೆ ತಿರುಗಿ", "up": "ಮೇಲೆ", "down": "ಕೆಳಗೆ"}.get(direction, "")
        instr_kn = f"{dir_kn + ', ' if dir_kn else ''}{verb_kn} {dist:.0f}ಮೀ {dest_kn} ಗೆ"

        # Hindi instruction
        dest_hi = dest_node.name_hi or dest_node.name
        dir_hi = {"left": "बाएँ मुड़ें", "right": "दाएँ मुड़ें", "up": "ऊपर", "down": "नीचे"}.get(direction, "")
        instr_hi = f"{dir_hi + ', ' if dir_hi else ''}{verb_hi} {dist:.0f}मी {dest_hi} तक"

        acc_note = ""
        if not edge.accessible:
            acc_note = f"⚠ This segment uses {pt} and may not be accessible."

        steps.append(RouteStep(
            instruction=instr_en,
            instruction_kn=instr_kn,
            instruction_hi=instr_hi,
            from_node=a,
            to_node=b,
            distance=dist,
            path_type=pt,
            level=dest_node.level,
            landmark=dest_node.name,
            direction=direction,
            accessibility_note=acc_note,
        ))

    return steps


# ── Main routing function ───────────────────────────────────────────────

def find_route(
    nodes: Dict[str, Node],
    edges: List[Edge],
    origin: str,
    destination: str,
    mode: str = "normal",            # normal | accessible | elder
    blocked_edges: Optional[Set[Tuple[str, str]]] = None,
    lang: str = "en",
) -> RouteResult:
    """
    Find the best route through Mysuru Junction.

    Modes:
      normal     — shortest path, any path type
      accessible — only edges marked accessible=True (lifts, ramps, level walks)
      elder      — penalise stairs, prefer lifts/ramps
    """
    accessible_only = (mode == "accessible")
    elder_mode = (mode == "elder")

    adj = build_adjacency(nodes, edges, accessible_only=accessible_only, blocked_edges=blocked_edges)

    path, total_dist = dijkstra(adj, origin, destination, elder_mode=elder_mode)

    if path is None:
        return RouteResult(
            found=False, origin=origin, destination=destination,
            accessibility_mode=mode,
            warnings=["No route found. Some paths may be blocked or inaccessible."],
        )

    steps = generate_directions(path, nodes, edges, lang=lang)

    # Actual distance (sum of real edge weights, not penalised)
    edge_map = {}
    for e in edges:
        edge_map[(e.from_node, e.to_node)] = e
        if e.bidirectional:
            edge_map[(e.to_node, e.from_node)] = e

    real_dist = 0.0
    for i in range(len(path) - 1):
        e = edge_map.get((path[i], path[i+1]))
        if e:
            real_dist += e.distance

    # Walking speed estimate
    speed = 0.8 if mode in ("accessible", "elder") else 1.2  # m/s
    est_time = real_dist / speed

    warnings = []
    if mode == "accessible":
        has_stairs = any(s.path_type == "stairs" for s in steps)
        if has_stairs:
            warnings.append("Route includes stairs despite accessible mode — no alternative available.")

    return RouteResult(
        found=True,
        origin=origin,
        destination=destination,
        total_distance=real_dist,
        estimated_time_seconds=est_time,
        steps=steps,
        path_node_ids=path,
        accessibility_mode=mode,
        warnings=warnings,
    )
