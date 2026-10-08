"""
main.py — RailSaathi Backend Server

Smart Navigation API for Mysuru Junction Railway Station.

Endpoints:
  /                              → health/info
  /health                        → health check

  /api/route                     → find navigation route
  /api/route/voice               → route with full voice/visual directions

  /api/facilities                → list all facilities
  /api/facilities/{facility_type}→ filter by type (toilet, lift, etc.)
  /api/facilities/nearest        → find nearest facility from a location

  /api/station/status            → full station status snapshot
  /api/station/blocked-paths     → current blocked paths
  /api/station/simulate          → trigger random disruption (demo)
  /api/station/block-path        → manually block a path
  /api/station/unblock-path      → manually unblock a path
  /api/station/reset             → reset all disruptions

  /api/nodes                     → list all navigable nodes
  /api/nodes/platforms           → list platform nodes only
  /api/nodes/entrances           → list entrance/exit nodes

  /api/translations              → get UI strings for a language
  /api/languages                 → list supported languages
"""

from __future__ import annotations

from dataclasses import asdict
from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from station_graph import build_station_graph, Node
from pathfinding import find_route, RouteResult
from station_status import StationStatusManager
from voice_directions import (
    generate_voice_route,
    narration_script,
    ssml_full_script,
    SUPPORTED_LANGUAGES,
)
from translations import t, get_all_strings, SUPPORTED_LANGS


# ── Initialise app & graph ──────────────────────────────────────────────

app = FastAPI(
    title="RailSaathi API",
    description="Smart indoor navigation API for Mysuru Junction Railway Station. "
                "Supports accessible routing, voice directions, multilingual output, "
                "and real-time station status simulation.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Build the station graph (loaded once at startup)
NODES, EDGES = build_station_graph()
status_manager = StationStatusManager(NODES, EDGES)


# ── Pydantic request/response models ───────────────────────────────────

class RouteRequest(BaseModel):
    origin: str
    destination: str
    mode: str = "normal"            # normal | accessible | elder
    lang: str = "en"                # en | kn | hi


class BlockPathRequest(BaseModel):
    from_node: str
    to_node: str
    reason: str = "Maintenance"
    reason_kn: str = "ನಿರ್ವಹಣೆ"
    reason_hi: str = "रखरखाव"


class FacilityStatusRequest(BaseModel):
    node_id: str
    operational: bool
    message: str = ""
    message_kn: str = ""
    message_hi: str = ""


class AnnouncementRequest(BaseModel):
    message: str
    message_kn: str = ""
    message_hi: str = ""
    priority: str = "info"


# ── Helper ──────────────────────────────────────────────────────────────

def _node_to_dict(node: Node, lang: str = "en") -> dict:
    """Serialise a Node, picking the right language name."""
    d = asdict(node)
    if lang == "kn" and node.name_kn:
        d["display_name"] = node.name_kn
        d["display_description"] = node.description_kn or node.description
    elif lang == "hi" and node.name_hi:
        d["display_name"] = node.name_hi
        d["display_description"] = node.description_hi or node.description
    else:
        d["display_name"] = node.name
        d["display_description"] = node.description
    return d


def _route_to_dict(result: RouteResult, lang: str = "en") -> dict:
    """Serialise a RouteResult."""
    steps_list = []
    for s in result.steps:
        sd = asdict(s)
        # Pick language-specific instruction
        if lang == "kn":
            sd["display_instruction"] = s.instruction_kn or s.instruction
        elif lang == "hi":
            sd["display_instruction"] = s.instruction_hi or s.instruction
        else:
            sd["display_instruction"] = s.instruction
        steps_list.append(sd)

    origin_node = NODES.get(result.origin)
    dest_node = NODES.get(result.destination)

    return {
        "found": result.found,
        "origin": result.origin,
        "origin_name": _node_to_dict(origin_node, lang)["display_name"] if origin_node else result.origin,
        "destination": result.destination,
        "destination_name": _node_to_dict(dest_node, lang)["display_name"] if dest_node else result.destination,
        "total_distance_m": round(result.total_distance, 1),
        "estimated_time_seconds": round(result.estimated_time_seconds, 0),
        "estimated_time_display": _format_time_display(result.estimated_time_seconds, lang),
        "accessibility_mode": result.accessibility_mode,
        "steps": steps_list,
        "path_node_ids": result.path_node_ids,
        "warnings": result.warnings,
    }


def _format_time_display(seconds: float, lang: str) -> str:
    mins = max(1, int(seconds // 60))
    if lang == "kn":
        return f"ಸುಮಾರು {mins} ನಿಮಿಷ"
    elif lang == "hi":
        return f"लगभग {mins} मिनट"
    return f"About {mins} min"


# ═══════════════════════════════════════════════════════════════════════
#  ENDPOINTS
# ═══════════════════════════════════════════════════════════════════════

# ── Root & Health ───────────────────────────────────────────────────────

@app.get("/", tags=["General"])
def home():
    return {
        "app": "RailSaathi",
        "message": "RailSaathi backend is running!",
        "version": "1.0.0",
        "station": "Mysuru Junction (MYS)",
        "endpoints": {
            "route": "/api/route",
            "voice_route": "/api/route/voice",
            "facilities": "/api/facilities",
            "station_status": "/api/station/status",
            "nodes": "/api/nodes",
            "translations": "/api/translations",
            "languages": "/api/languages",
        },
    }


@app.get("/health", tags=["General"])
def health():
    return {
        "status": "healthy",
        "station": "Mysuru Junction",
        "nodes_count": len(NODES),
        "edges_count": len(EDGES),
    }


# ── Route API ───────────────────────────────────────────────────────────

@app.post("/api/route", tags=["Navigation"])
def get_route(req: RouteRequest):
    """
    Find the best route between two nodes.

    **Modes:**
    - `normal` — shortest path
    - `accessible` — avoids stairs, uses lifts & ramps only
    - `elder` — penalises stairs, prefers lifts & ramps
    """
    if req.origin not in NODES:
        raise HTTPException(400, detail=t("error_invalid_node", req.lang) + f" Origin: {req.origin}")
    if req.destination not in NODES:
        raise HTTPException(400, detail=t("error_invalid_node", req.lang) + f" Destination: {req.destination}")
    if req.mode not in ("normal", "accessible", "elder"):
        raise HTTPException(400, detail="Mode must be one of: normal, accessible, elder")

    blocked = status_manager.get_blocked_edges()

    result = find_route(
        NODES, EDGES,
        origin=req.origin,
        destination=req.destination,
        mode=req.mode,
        blocked_edges=blocked,
        lang=req.lang,
    )

    if not result.found:
        raise HTTPException(404, detail=t("error_no_route", req.lang))

    return _route_to_dict(result, req.lang)


@app.post("/api/route/voice", tags=["Navigation", "Voice"])
def get_route_with_voice(req: RouteRequest):
    """
    Find route AND generate full voice/visual navigation package.
    Returns route + SSML, narration script, direction icons.
    """
    if req.origin not in NODES:
        raise HTTPException(400, detail=t("error_invalid_node", req.lang) + f" Origin: {req.origin}")
    if req.destination not in NODES:
        raise HTTPException(400, detail=t("error_invalid_node", req.lang) + f" Destination: {req.destination}")

    blocked = status_manager.get_blocked_edges()
    result = find_route(NODES, EDGES, req.origin, req.destination, req.mode, blocked, req.lang)

    if not result.found:
        raise HTTPException(404, detail=t("error_no_route", req.lang))

    origin_node = NODES[req.origin]
    dest_node = NODES[req.destination]

    # Pick display names
    if req.lang == "kn":
        o_name = origin_node.name_kn or origin_node.name
        d_name = dest_node.name_kn or dest_node.name
    elif req.lang == "hi":
        o_name = origin_node.name_hi or origin_node.name
        d_name = dest_node.name_hi or dest_node.name
    else:
        o_name = origin_node.name
        d_name = dest_node.name

    voice = generate_voice_route(
        result.steps, result.total_distance, result.estimated_time_seconds,
        o_name, d_name, req.lang,
    )

    route_dict = _route_to_dict(result, req.lang)
    route_dict["voice"] = {
        "language": voice.language,
        "language_name": voice.language_name,
        "bcp47_code": voice.bcp47_code,
        "intro_text": voice.intro_text,
        "intro_ssml": voice.intro_ssml,
        "summary_text": voice.summary_text,
        "summary_ssml": voice.summary_ssml,
        "estimated_time_display": voice.estimated_time_display,
        "narration_script": narration_script(voice),
        "ssml_full": ssml_full_script(voice),
        "steps": [
            {
                "step_number": vs.step_number,
                "text": vs.text,
                "ssml": vs.ssml,
                "direction_icon": vs.direction_icon,
                "path_icon": vs.path_icon,
                "distance_m": vs.distance_m,
                "landmark": vs.landmark,
                "accessibility_warning": vs.accessibility_warning,
            }
            for vs in voice.steps
        ],
    }

    return route_dict


# ── Facility API ────────────────────────────────────────────────────────

@app.get("/api/facilities", tags=["Facilities"])
def list_facilities(lang: str = Query("en", description="Language: en, kn, hi")):
    """List all station facilities with operational status."""
    statuses = status_manager.get_facility_statuses()
    status_map = {s.node_id: s for s in statuses}

    facilities = []
    for nid, node in NODES.items():
        if node.facility_type:
            st = status_map.get(nid)
            facilities.append({
                **_node_to_dict(node, lang),
                "operational": st.operational if st else True,
                "status_message": (
                    st.status_message_kn if lang == "kn" and st else
                    st.status_message_hi if lang == "hi" and st else
                    st.status_message if st else
                    t("status_operational", lang)
                ),
            })

    return {"facilities": facilities, "count": len(facilities)}


@app.get("/api/facilities/{facility_type}", tags=["Facilities"])
def get_facilities_by_type(
    facility_type: str,
    lang: str = Query("en"),
):
    """
    Get facilities of a specific type.
    Types: toilet, ticket_counter, waiting_hall, help_desk,
           drinking_water, lift, ramp, escalator, parking
    """
    statuses = status_manager.get_facility_statuses()
    status_map = {s.node_id: s for s in statuses}

    results = []
    for nid, node in NODES.items():
        if node.facility_type == facility_type:
            st = status_map.get(nid)
            results.append({
                **_node_to_dict(node, lang),
                "operational": st.operational if st else True,
                "status_message": (
                    st.status_message_kn if lang == "kn" and st else
                    st.status_message_hi if lang == "hi" and st else
                    st.status_message if st else
                    t("status_operational", lang)
                ),
            })

    if not results:
        raise HTTPException(404, detail=f"No facilities of type '{facility_type}' found.")

    return {"facility_type": facility_type, "facilities": results, "count": len(results)}


@app.get("/api/facilities/nearest/{facility_type}", tags=["Facilities"])
def nearest_facility(
    facility_type: str,
    from_node: str = Query(..., description="Your current node ID"),
    mode: str = Query("normal"),
    lang: str = Query("en"),
):
    """Find the nearest facility of a given type from your location."""
    if from_node not in NODES:
        raise HTTPException(400, detail=t("error_invalid_node", lang))

    blocked = status_manager.get_blocked_edges()
    best_route = None
    best_dist = float("inf")

    for nid, node in NODES.items():
        if node.facility_type == facility_type:
            result = find_route(NODES, EDGES, from_node, nid, mode, blocked, lang)
            if result.found and result.total_distance < best_dist:
                best_dist = result.total_distance
                best_route = result

    if not best_route:
        raise HTTPException(404, detail=f"No reachable {facility_type} found from {from_node}")

    return {
        "nearest_facility": _node_to_dict(NODES[best_route.destination], lang),
        "route": _route_to_dict(best_route, lang),
    }


# ── Station Status API ─────────────────────────────────────────────────

@app.get("/api/station/status", tags=["Station Status"])
def station_status(lang: str = Query("en")):
    """Get full station status snapshot (blocked paths, facilities, crowds)."""
    snap = status_manager.snapshot()

    blocked = []
    for bp in snap.blocked_paths:
        from_n = NODES.get(bp.from_node)
        to_n = NODES.get(bp.to_node)
        blocked.append({
            "from_node": bp.from_node,
            "from_name": _node_to_dict(from_n, lang)["display_name"] if from_n else bp.from_node,
            "to_node": bp.to_node,
            "to_name": _node_to_dict(to_n, lang)["display_name"] if to_n else bp.to_node,
            "reason": bp.reason_kn if lang == "kn" else bp.reason_hi if lang == "hi" else bp.reason,
            "blocked_since": bp.blocked_since,
            "estimated_clear": bp.estimated_clear,
        })

    facilities = []
    for fs in snap.facility_statuses:
        facilities.append({
            "node_id": fs.node_id,
            "name": fs.name,
            "facility_type": fs.facility_type,
            "operational": fs.operational,
            "status_message": fs.status_message_kn if lang == "kn" else fs.status_message_hi if lang == "hi" else fs.status_message,
            "last_updated": fs.last_updated,
        })

    crowds = []
    for pc in snap.platform_crowds:
        crowds.append({
            "platform_number": pc.platform_number,
            "crowd_level": pc.crowd_level,
            "estimated_people": pc.estimated_people,
        })

    announcements = []
    for a in snap.announcements:
        announcements.append({
            "message": a.get(f"message_{lang}", a.get("message", "")),
            "priority": a.get("priority", "info"),
            "timestamp": a.get("timestamp", ""),
        })

    return {
        "timestamp": snap.timestamp,
        "blocked_paths": blocked,
        "blocked_paths_count": len(blocked),
        "facility_statuses": facilities,
        "platform_crowds": crowds,
        "announcements": announcements,
    }


@app.get("/api/station/blocked-paths", tags=["Station Status"])
def blocked_paths(lang: str = Query("en")):
    """Get currently blocked paths only."""
    snap = status_manager.snapshot()
    blocked = []
    for bp in snap.blocked_paths:
        from_n = NODES.get(bp.from_node)
        to_n = NODES.get(bp.to_node)
        blocked.append({
            "from_node": bp.from_node,
            "from_name": _node_to_dict(from_n, lang)["display_name"] if from_n else bp.from_node,
            "to_node": bp.to_node,
            "to_name": _node_to_dict(to_n, lang)["display_name"] if to_n else bp.to_node,
            "reason": bp.reason_kn if lang == "kn" else bp.reason_hi if lang == "hi" else bp.reason,
            "blocked_since": bp.blocked_since,
        })
    return {"blocked_paths": blocked, "count": len(blocked)}


@app.post("/api/station/block-path", tags=["Station Status"])
def block_path(req: BlockPathRequest):
    """Manually block a path (for testing / admin)."""
    if req.from_node not in NODES or req.to_node not in NODES:
        raise HTTPException(400, detail="Invalid node ID(s)")

    bp = status_manager.block_path(
        req.from_node, req.to_node,
        req.reason, req.reason_kn, req.reason_hi,
    )
    return {"status": "blocked", "detail": asdict(bp)}


@app.post("/api/station/unblock-path", tags=["Station Status"])
def unblock_path(req: BlockPathRequest):
    """Unblock a previously blocked path."""
    status_manager.unblock_path(req.from_node, req.to_node)
    return {"status": "unblocked", "from": req.from_node, "to": req.to_node}


@app.post("/api/station/simulate", tags=["Station Status"])
def simulate_disruption():
    """Trigger a random disruption for demo/testing."""
    event = status_manager.simulate_random_disruption()
    return {"status": "simulated", "event": event}


@app.post("/api/station/reset", tags=["Station Status"])
def reset_station():
    """Reset all disruptions to default state."""
    status_manager.reset_all()
    return {"status": "reset", "message": "All disruptions cleared"}


@app.post("/api/station/facility-status", tags=["Station Status"])
def update_facility_status(req: FacilityStatusRequest):
    """Update operational status of a facility."""
    if req.node_id not in NODES:
        raise HTTPException(400, detail="Invalid node ID")
    status_manager.set_facility_status(
        req.node_id, req.operational,
        req.message, req.message_kn, req.message_hi,
    )
    return {"status": "updated", "node_id": req.node_id, "operational": req.operational}


@app.post("/api/station/announcement", tags=["Station Status"])
def add_announcement(req: AnnouncementRequest):
    """Add a station announcement."""
    status_manager.add_announcement(
        req.message, req.message_kn, req.message_hi, req.priority,
    )
    return {"status": "added", "message": req.message}


# ── Nodes API ───────────────────────────────────────────────────────────

@app.get("/api/nodes", tags=["Nodes"])
def list_nodes(lang: str = Query("en")):
    """List all navigable nodes in the station."""
    return {
        "nodes": [_node_to_dict(n, lang) for n in NODES.values()],
        "count": len(NODES),
    }


@app.get("/api/nodes/platforms", tags=["Nodes"])
def list_platforms(lang: str = Query("en")):
    """List platform nodes only."""
    platforms = [_node_to_dict(n, lang) for n in NODES.values() if n.node_type == "platform"]
    return {"platforms": platforms, "count": len(platforms)}


@app.get("/api/nodes/entrances", tags=["Nodes"])
def list_entrances(lang: str = Query("en")):
    """List entrance and exit nodes."""
    entrances = [_node_to_dict(n, lang) for n in NODES.values() if n.node_type in ("entrance", "exit")]
    return {"entrances": entrances, "count": len(entrances)}


@app.get("/api/nodes/{node_id}", tags=["Nodes"])
def get_node(node_id: str, lang: str = Query("en")):
    """Get details of a specific node."""
    if node_id not in NODES:
        raise HTTPException(404, detail=t("error_invalid_node", lang))
    return _node_to_dict(NODES[node_id], lang)


# ── Translation API ────────────────────────────────────────────────────

@app.get("/api/translations", tags=["i18n"])
def get_translations(lang: str = Query("en")):
    """Get all UI translation strings for a language."""
    if lang not in SUPPORTED_LANGS:
        raise HTTPException(400, detail=f"Unsupported language: {lang}. Supported: {SUPPORTED_LANGS}")
    return {
        "language": lang,
        "strings": get_all_strings(lang),
    }


@app.get("/api/languages", tags=["i18n"])
def list_languages():
    """List supported languages."""
    return {
        "languages": [
            {"code": "en", "name": "English",  "native": "English"},
            {"code": "kn", "name": "Kannada",  "native": "ಕನ್ನಡ"},
            {"code": "hi", "name": "Hindi",    "native": "हिन्दी"},
        ],
    }