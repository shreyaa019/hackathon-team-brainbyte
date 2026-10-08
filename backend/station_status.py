"""
station_status.py — Real-time station status & blocked-path simulation

Features:
  • Track which edges/paths are currently blocked (maintenance, crowd, etc.)
  • Simulate random disruptions for demo/testing
  • Facility operational status (toilets, lifts, etc.)
  • Crowd density per platform (simulated)
  • API-ready status snapshots
"""

from __future__ import annotations
import random, time, threading
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Optional, Set, Tuple

from station_graph import Node, Edge


IST = timezone(timedelta(hours=5, minutes=30))


@dataclass
class FacilityStatus:
    """Operational status of a single facility."""
    node_id: str
    facility_type: str
    name: str
    operational: bool = True
    status_message: str = "Operational"
    status_message_kn: str = "ಕಾರ್ಯನಿರತ"
    status_message_hi: str = "चालू"
    last_updated: str = ""


@dataclass
class BlockedPath:
    """A currently blocked edge."""
    from_node: str
    to_node: str
    reason: str = "Maintenance"
    reason_kn: str = "ನಿರ್ವಹಣೆ"
    reason_hi: str = "रखरखाव"
    blocked_since: str = ""
    estimated_clear: str = ""       # ISO timestamp or empty


@dataclass
class PlatformCrowdLevel:
    """Simulated crowd density for a platform."""
    platform_number: int
    crowd_level: str = "low"        # low | moderate | high | very_high
    estimated_people: int = 0


@dataclass
class StationSnapshot:
    """Complete station status at a point in time."""
    timestamp: str
    blocked_paths: List[BlockedPath] = field(default_factory=list)
    facility_statuses: List[FacilityStatus] = field(default_factory=list)
    platform_crowds: List[PlatformCrowdLevel] = field(default_factory=list)
    announcements: List[Dict] = field(default_factory=list)


class StationStatusManager:
    """
    Manages the live status of Mysuru Junction.
    In production this would be backed by sensors/feeds;
    here we provide simulation + manual overrides.
    """

    def __init__(self, nodes: Dict[str, Node], edges: List[Edge]):
        self._nodes = nodes
        self._edges = edges
        self._blocked: Dict[Tuple[str, str], BlockedPath] = {}
        self._facility_overrides: Dict[str, FacilityStatus] = {}
        self._platform_crowds: Dict[int, PlatformCrowdLevel] = {}
        self._announcements: List[Dict] = []
        self._lock = threading.Lock()

        # Initialise default crowd levels
        for p in range(1, 7):
            self._platform_crowds[p] = PlatformCrowdLevel(
                platform_number=p, crowd_level="low", estimated_people=random.randint(5, 30)
            )

    # ── Blocked paths ───────────────────────────────────────────────────

    def block_path(
        self,
        from_node: str,
        to_node: str,
        reason: str = "Maintenance",
        reason_kn: str = "ನಿರ್ವಹಣೆ",
        reason_hi: str = "रखरखाव",
        estimated_clear: str = "",
    ) -> BlockedPath:
        with self._lock:
            bp = BlockedPath(
                from_node=from_node,
                to_node=to_node,
                reason=reason,
                reason_kn=reason_kn,
                reason_hi=reason_hi,
                blocked_since=datetime.now(IST).isoformat(),
                estimated_clear=estimated_clear,
            )
            self._blocked[(from_node, to_node)] = bp
            # Also mark the edge object for immediate routing impact
            for e in self._edges:
                if (e.from_node == from_node and e.to_node == to_node) or \
                   (e.bidirectional and e.from_node == to_node and e.to_node == from_node):
                    e.blocked = True
            return bp

    def unblock_path(self, from_node: str, to_node: str):
        with self._lock:
            self._blocked.pop((from_node, to_node), None)
            self._blocked.pop((to_node, from_node), None)
            for e in self._edges:
                if (e.from_node == from_node and e.to_node == to_node) or \
                   (e.from_node == to_node and e.to_node == from_node):
                    e.blocked = False

    def get_blocked_edges(self) -> Set[Tuple[str, str]]:
        with self._lock:
            result = set()
            for k in self._blocked:
                result.add(k)
                result.add((k[1], k[0]))  # both directions
            return result

    # ── Facility status ─────────────────────────────────────────────────

    def set_facility_status(
        self,
        node_id: str,
        operational: bool,
        message: str = "",
        message_kn: str = "",
        message_hi: str = "",
    ):
        with self._lock:
            node = self._nodes.get(node_id)
            if not node or not node.facility_type:
                return
            self._facility_overrides[node_id] = FacilityStatus(
                node_id=node_id,
                facility_type=node.facility_type,
                name=node.name,
                operational=operational,
                status_message=message or ("Operational" if operational else "Out of service"),
                status_message_kn=message_kn or ("ಕಾರ್ಯನಿರತ" if operational else "ಸೇವೆಯಲ್ಲಿಲ್ಲ"),
                status_message_hi=message_hi or ("चालू" if operational else "सेवा बंद"),
                last_updated=datetime.now(IST).isoformat(),
            )

    def get_facility_statuses(self) -> List[FacilityStatus]:
        with self._lock:
            statuses = []
            for nid, node in self._nodes.items():
                if node.facility_type:
                    if nid in self._facility_overrides:
                        statuses.append(self._facility_overrides[nid])
                    else:
                        statuses.append(FacilityStatus(
                            node_id=nid,
                            facility_type=node.facility_type,
                            name=node.name,
                            operational=True,
                            last_updated=datetime.now(IST).isoformat(),
                        ))
            return statuses

    # ── Platform crowd ──────────────────────────────────────────────────

    def update_crowd(self, platform: int, level: str, people: int):
        with self._lock:
            self._platform_crowds[platform] = PlatformCrowdLevel(
                platform_number=platform, crowd_level=level, estimated_people=people
            )

    # ── Announcements ───────────────────────────────────────────────────

    def add_announcement(self, message: str, message_kn: str = "", message_hi: str = "", priority: str = "info"):
        with self._lock:
            self._announcements.append({
                "message": message,
                "message_kn": message_kn,
                "message_hi": message_hi,
                "priority": priority,
                "timestamp": datetime.now(IST).isoformat(),
            })
            # Keep only last 20
            self._announcements = self._announcements[-20:]

    # ── Snapshot ────────────────────────────────────────────────────────

    def snapshot(self) -> StationSnapshot:
        with self._lock:
            return StationSnapshot(
                timestamp=datetime.now(IST).isoformat(),
                blocked_paths=list(self._blocked.values()),
                facility_statuses=self.get_facility_statuses(),
                platform_crowds=list(self._platform_crowds.values()),
                announcements=list(self._announcements),
            )

    # ── Simulation ──────────────────────────────────────────────────────

    def simulate_random_disruption(self) -> Dict:
        """Simulate a random path blockage or facility outage for demo."""
        event_type = random.choice(["blocked_path", "facility_down", "crowd_surge"])

        if event_type == "blocked_path":
            # Pick a random edge that involves stairs or subway
            candidates = [e for e in self._edges if e.path_type in ("stairs", "subway") and not e.blocked]
            if candidates:
                edge = random.choice(candidates)
                reasons = [
                    ("Wet floor — cleaning in progress", "ಒದ್ದೆ ನೆಲ — ಸ್ವಚ್ಛತೆ ನಡೆಯುತ್ತಿದೆ", "गीला फर्श — सफाई चल रही है"),
                    ("Maintenance work", "ನಿರ್ವಹಣೆ ಕೆಲಸ", "रखरखाव कार्य"),
                    ("Overcrowding — temporarily closed", "ಅತಿಯಾದ ಜನಸಂದಣಿ — ತಾತ್ಕಾಲಿಕವಾಗಿ ಮುಚ್ಚಲಾಗಿದೆ", "अत्यधिक भीड़ — अस्थायी रूप से बंद"),
                ]
                r_en, r_kn, r_hi = random.choice(reasons)
                bp = self.block_path(edge.from_node, edge.to_node, r_en, r_kn, r_hi)
                return {
                    "event": "blocked_path",
                    "detail": f"Blocked: {edge.from_node} → {edge.to_node}",
                    "reason": r_en,
                }

        elif event_type == "facility_down":
            facility_nodes = [n for n in self._nodes.values()
                              if n.facility_type in ("lift", "toilet", "escalator")]
            if facility_nodes:
                node = random.choice(facility_nodes)
                self.set_facility_status(node.id, False, "Temporarily out of service",
                                         "ತಾತ್ಕಾಲಿಕವಾಗಿ ಸೇವೆಯಲ್ಲಿಲ್ಲ", "अस्थायी रूप से सेवा बंद")
                return {
                    "event": "facility_down",
                    "detail": f"{node.name} is temporarily out of service",
                    "node_id": node.id,
                }

        elif event_type == "crowd_surge":
            platform = random.randint(1, 6)
            level = random.choice(["moderate", "high", "very_high"])
            people = {"moderate": random.randint(50, 100),
                      "high": random.randint(100, 200),
                      "very_high": random.randint(200, 400)}[level]
            self.update_crowd(platform, level, people)
            return {
                "event": "crowd_surge",
                "detail": f"Platform {platform} crowd level: {level} ({people} people)",
                "platform": platform,
            }

        return {"event": "none", "detail": "No disruption generated"}

    def reset_all(self):
        """Clear all disruptions — return to default state."""
        with self._lock:
            for e in self._edges:
                e.blocked = False
            self._blocked.clear()
            self._facility_overrides.clear()
            self._announcements.clear()
            for p in range(1, 7):
                self._platform_crowds[p] = PlatformCrowdLevel(
                    platform_number=p, crowd_level="low",
                    estimated_people=random.randint(5, 30)
                )
