"""
station_graph.py — Mysuru Junction Navigation Graph

This module encodes the full station layout as a weighted, directed graph.
Every node is a navigable point (platform, facility, junction, entrance/exit).
Every edge carries:
  • distance   (metres, approximate)
  • accessible (bool — True if wheelchair / elderly safe)
  • path_type  ("normal" | "stairs" | "ramp" | "lift" | "subway" | "escalator")
  • level      ("ground" | "fob" | "subway")

Co-ordinate system  (for 2-D map rendering):
  x → east  (0 at west boundary)
  y → north (0 at south boundary, i.e. main entrance)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import copy


# ── Node & Edge data classes ──────────────────────────────────────────────

@dataclass
class Node:
    id: str
    name: str                       # human-readable label
    name_kn: str = ""               # Kannada name
    name_hi: str = ""               # Hindi name
    node_type: str = "junction"     # platform | facility | entrance | exit | junction | parking
    platform_number: Optional[int] = None
    x: float = 0.0                  # map x-coordinate (metres from west)
    y: float = 0.0                  # map y-coordinate (metres from south)
    level: str = "ground"           # ground | fob | subway
    facility_type: Optional[str] = None   # toilet | ticket_counter | waiting_hall | help_desk | drinking_water | lift | escalator | ramp
    accessible: bool = True         # is the node itself accessible?
    description: str = ""
    description_kn: str = ""
    description_hi: str = ""


@dataclass
class Edge:
    from_node: str
    to_node: str
    distance: float                 # metres
    accessible: bool = True         # wheelchair / elderly safe?
    path_type: str = "normal"       # normal | stairs | ramp | lift | subway | escalator | fob_bridge
    bidirectional: bool = True
    blocked: bool = False           # runtime — for simulation


# ── Build the Mysuru Junction graph ─────────────────────────────────────

def build_station_graph() -> Tuple[Dict[str, Node], List[Edge]]:
    """Return (nodes_dict, edges_list) for Mysuru Junction."""

    nodes: Dict[str, Node] = {}
    edges: List[Edge] = []

    def N(id, name, **kw):
        nodes[id] = Node(id=id, name=name, **kw)

    def E(a, b, dist, **kw):
        edges.append(Edge(from_node=a, to_node=b, distance=dist, **kw))

    # ─────────────────────────────────────────────────────────────────────
    # 1.  ENTRANCES & EXITS
    # ─────────────────────────────────────────────────────────────────────
    N("entrance_main",   "Main Entrance (East)",
      name_kn="ಮುಖ್ಯ ಪ್ರವೇಶದ್ವಾರ (ಪೂರ್ವ)", name_hi="मुख्य प्रवेश द्वार (पूर्व)",
      node_type="entrance", x=50, y=0,
      description="Main entrance from the city side (east)",
      description_kn="ನಗರದ ಕಡೆಯಿಂದ ಮುಖ್ಯ ಪ್ರವೇಶದ್ವಾರ",
      description_hi="शहर की ओर से मुख्य प्रवेश द्वार")

    N("exit_west",       "Exit (West)",
      name_kn="ನಿರ್ಗಮನ (ಪಶ್ಚಿಮ)", name_hi="निकास (पश्चिम)",
      node_type="exit", x=20, y=5,
      description="Western exit towards city side")

    N("exit_east",       "Exit (East)",
      name_kn="ನಿರ್ಗಮನ (ಪೂರ್ವ)", name_hi="निकास (पूर्व)",
      node_type="exit", x=75, y=5,
      description="Eastern exit near auto/bus stand")

    N("parking_west",    "Parking (West)",
      name_kn="ಪಾರ್ಕಿಂಗ್ (ಪಶ್ಚಿಮ)", name_hi="पार्किंग (पश्चिम)",
      node_type="parking", x=5, y=90,
      description="Western parking area")

    N("reserved_parking", "Reserved Parking",
      name_kn="ಮೀಸಲು ಪಾರ್ಕಿಂಗ್", name_hi="आरक्षित पार्किंग",
      node_type="parking", x=8, y=5,
      description="Reserved parking area near west exit")

    N("auto_bus_stand",  "Auto / Bus Stand (East)",
      name_kn="ಆಟೋ / ಬಸ್ ನಿಲ್ದಾಣ (ಪೂರ್ವ)", name_hi="ऑटो / बस स्टैंड (पूर्व)",
      node_type="exit", x=85, y=5,
      description="Auto-rickshaw and bus stand on east side")

    N("auto_bus_stand_north", "Auto / Bus Stand (East-North)",
      name_kn="ಆಟೋ / ಬಸ್ ನಿಲ್ದಾಣ (ಪೂರ್ವ-ಉತ್ತರ)", name_hi="ऑटो / बस स्टैंड (पूर्व-उत्तर)",
      node_type="exit", x=85, y=85,
      description="Auto-rickshaw and bus stand on east-north side")

    # ─────────────────────────────────────────────────────────────────────
    # 2.  RAMPS (accessible entrance paths)
    # ─────────────────────────────────────────────────────────────────────
    N("ramp_west",  "Ramp (West)",
      name_kn="ರ‍್ಯಾಂಪ್ (ಪಶ್ಚಿಮ)", name_hi="रैंप (पश्चिम)",
      node_type="facility", facility_type="ramp", x=30, y=3, accessible=True,
      description="Wheelchair ramp on the west side of main entrance")

    N("ramp_east",  "Ramp (East)",
      name_kn="ರ‍್ಯಾಂಪ್ (ಪೂರ್ವ)", name_hi="रैंप (पूर्व)",
      node_type="facility", facility_type="ramp", x=65, y=3, accessible=True,
      description="Wheelchair ramp on the east side of main entrance")

    # ─────────────────────────────────────────────────────────────────────
    # 3.  MAIN CONCOURSE (ground level)
    # ─────────────────────────────────────────────────────────────────────
    N("concourse_center", "Main Concourse",
      name_kn="ಮುಖ್ಯ ಕಾನ್ಕೋರ್ಸ್", name_hi="मुख्य कॉनकोर्स",
      node_type="junction", x=50, y=20,
      description="Central concourse area of the station building")

    N("concourse_west", "Concourse (West Junction)",
      name_kn="ಕಾನ್ಕೋರ್ಸ್ (ಪಶ್ಚಿಮ)", name_hi="कॉनकोर्स (पश्चिम)",
      node_type="junction", x=30, y=20)

    N("concourse_east", "Concourse (East Junction)",
      name_kn="ಕಾನ್ಕೋರ್ಸ್ (ಪೂರ್ವ)", name_hi="कॉनकोर्स (पूर्व)",
      node_type="junction", x=70, y=20)

    N("concourse_south", "Concourse (South Junction)",
      name_kn="ಕಾನ್ಕೋರ್ಸ್ (ದಕ್ಷಿಣ)", name_hi="कॉनकोर्स (दक्षिण)",
      node_type="junction", x=50, y=12)

    N("concourse_north", "Concourse (North Junction)",
      name_kn="ಕಾನ್ಕೋರ್ಸ್ (ಉತ್ತರ)", name_hi="कॉनकोर्स (उत्तर)",
      node_type="junction", x=50, y=28)

    # ─────────────────────────────────────────────────────────────────────
    # 4.  STATION BUILDING FACILITIES
    # ─────────────────────────────────────────────────────────────────────
    N("waiting_hall_north", "Waiting Hall (North)",
      name_kn="ಕಾಯುವ ಸಭಾಂಗಣ (ಉತ್ತರ)", name_hi="प्रतीक्षालय (उत्तर)",
      node_type="facility", facility_type="waiting_hall", x=30, y=85,
      description="Northern waiting hall inside station building")

    N("waiting_hall_south", "Waiting Hall (South)",
      name_kn="ಕಾಯುವ ಸಭಾಂಗಣ (ದಕ್ಷಿಣ)", name_hi="प्रतीक्षालय (दक्षिण)",
      node_type="facility", facility_type="waiting_hall", x=65, y=85,
      description="Southern waiting hall inside station building")

    N("ticket_counters", "Ticket Counters",
      name_kn="ಟಿಕೆಟ್ ಕೌಂಟರ್‌ಗಳು", name_hi="टिकट काउंटर",
      node_type="facility", facility_type="ticket_counter", x=45, y=88,
      description="Main ticket booking counters")

    N("toilet_male", "Toilet (Male)",
      name_kn="ಶೌಚಾಲಯ (ಪುರುಷ)", name_hi="शौचालय (पुरुष)",
      node_type="facility", facility_type="toilet", x=25, y=78,
      description="Men's toilet in station building")

    N("toilet_female", "Toilet (Female)",
      name_kn="ಶೌಚಾಲಯ (ಮಹಿಳಾ)", name_hi="शौचालय (महिला)",
      node_type="facility", facility_type="toilet", x=25, y=72,
      description="Women's toilet in station building")

    N("help_desk", "Help Desk",
      name_kn="ಸಹಾಯ ಕೇಂದ್ರ", name_hi="सहायता केंद्र",
      node_type="facility", facility_type="help_desk", x=65, y=78,
      description="Information and help desk")

    N("drinking_water", "Drinking Water",
      name_kn="ಕುಡಿಯುವ ನೀರು", name_hi="पीने का पानी",
      node_type="facility", facility_type="drinking_water", x=68, y=72,
      description="Drinking water facility")

    N("station_building_center", "Station Building (Center)",
      name_kn="ನಿಲ್ದಾಣ ಕಟ್ಟಡ", name_hi="स्टेशन भवन",
      node_type="junction", x=50, y=82)

    # ─────────────────────────────────────────────────────────────────────
    # 5.  FOB-1 (Foot Over Bridge 1 — West side)
    # ─────────────────────────────────────────────────────────────────────
    # FOB-1 ground-level stair entries (one per platform strip)
    for i, py in [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]:
        N(f"fob1_stairs_p{i}", f"FOB-1 Stairs at Platform {i}",
          name_kn=f"FOB-1 ಮೆಟ್ಟಿಲುಗಳು ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i}",
          name_hi=f"FOB-1 सीढ़ियाँ प्लेटफ़ॉर्म {i}",
          node_type="junction", x=30, y=py, level="ground",
          platform_number=i, accessible=False,
          description=f"Staircase entry to FOB-1 from Platform {i}")

    # FOB-1 bridge-level nodes
    for i, py in [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]:
        N(f"fob1_bridge_p{i}", f"FOB-1 Bridge above Platform {i}",
          name_kn=f"FOB-1 ಸೇತುವೆ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i}",
          name_hi=f"FOB-1 पुल प्लेटफ़ॉर्म {i}",
          node_type="junction", x=30, y=py, level="fob",
          platform_number=i, accessible=False)

    # FOB-1 Concourse connection
    N("fob1_concourse", "FOB-1 Concourse Entry",
      name_kn="FOB-1 ಕಾನ್ಕೋರ್ಸ್ ಪ್ರವೇಶ", name_hi="FOB-1 कॉनकोर्स प्रवेश",
      node_type="junction", x=30, y=68, level="ground")

    N("fob1_bridge_concourse", "FOB-1 Bridge at Concourse",
      name_kn="FOB-1 ಸೇತುವೆ ಕಾನ್ಕೋರ್ಸ್", name_hi="FOB-1 पुल कॉनकोर्स",
      node_type="junction", x=30, y=68, level="fob")

    # Lift at FOB-1 (between P4 and P5)
    N("lift_fob1_ground", "Lift (FOB-1) Ground",
      name_kn="ಲಿಫ್ಟ್ (FOB-1) ನೆಲ", name_hi="लिफ्ट (FOB-1) ज़मीन",
      node_type="facility", facility_type="lift", x=30, y=45, level="ground",
      accessible=True,
      description="Lift at FOB-1 between Platform 4 and Platform 5")

    N("lift_fob1_upper", "Lift (FOB-1) Upper",
      name_kn="ಲಿಫ್ಟ್ (FOB-1) ಮೇಲೆ", name_hi="लिफ्ट (FOB-1) ऊपर",
      node_type="facility", facility_type="lift", x=30, y=45, level="fob",
      accessible=True)

    # ─────────────────────────────────────────────────────────────────────
    # 6.  FOB-2 (Foot Over Bridge 2 — East side)
    # ─────────────────────────────────────────────────────────────────────
    for i, py in [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]:
        N(f"fob2_stairs_p{i}", f"FOB-2 Stairs at Platform {i}",
          name_kn=f"FOB-2 ಮೆಟ್ಟಿಲುಗಳು ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i}",
          name_hi=f"FOB-2 सीढ़ियाँ प्लेटफ़ॉर्म {i}",
          node_type="junction", x=65, y=py, level="ground",
          platform_number=i, accessible=False)

    for i, py in [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]:
        N(f"fob2_bridge_p{i}", f"FOB-2 Bridge above Platform {i}",
          name_kn=f"FOB-2 ಸೇತುವೆ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i}",
          name_hi=f"FOB-2 पुल प्लेटफ़ॉर्म {i}",
          node_type="junction", x=65, y=py, level="fob",
          platform_number=i, accessible=False)

    N("fob2_concourse", "FOB-2 Concourse Entry",
      name_kn="FOB-2 ಕಾನ್ಕೋರ್ಸ್ ಪ್ರವೇಶ", name_hi="FOB-2 कॉनकोर्स प्रवेश",
      node_type="junction", x=65, y=68, level="ground")

    N("fob2_bridge_concourse", "FOB-2 Bridge at Concourse",
      name_kn="FOB-2 ಸೇತುವೆ ಕಾನ್ಕೋರ್ಸ್", name_hi="FOB-2 पुल कॉनकोर्स",
      node_type="junction", x=65, y=68, level="fob")

    # Lift at Subway side (east, near FOB-2)
    N("lift_subway_ground", "Lift (Subway) Ground",
      name_kn="ಲಿಫ್ಟ್ (ಸಬ್‌ವೇ) ನೆಲ", name_hi="लिफ्ट (सबवे) ज़मीन",
      node_type="facility", facility_type="lift", x=65, y=45, level="ground",
      accessible=True,
      description="Lift at subway entrance near Platform 4/5")

    N("lift_subway_lower", "Lift (Subway) Lower",
      name_kn="ಲಿಫ್ಟ್ (ಸಬ್‌ವೇ) ಕೆಳಗೆ", name_hi="लिफ्ट (सबवे) नीचे",
      node_type="facility", facility_type="lift", x=65, y=45, level="subway",
      accessible=True)

    # ─────────────────────────────────────────────────────────────────────
    # 7.  SUBWAY (underground, connecting all platforms)
    # ─────────────────────────────────────────────────────────────────────
    # Subway entrance at each platform + concourse
    for i, py in [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]:
        N(f"subway_entry_p{i}", f"Subway Entry at Platform {i}",
          name_kn=f"ಸಬ್‌ವೇ ಪ್ರವೇಶ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i}",
          name_hi=f"सबवे प्रवेश प्लेटफ़ॉर्म {i}",
          node_type="junction", x=50, y=py, level="ground",
          platform_number=i,
          description=f"Subway stairs entry from Platform {i}")

    for i, py in [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]:
        N(f"subway_under_p{i}", f"Subway under Platform {i}",
          name_kn=f"ಸಬ್‌ವೇ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i} ಕೆಳಗೆ",
          name_hi=f"सबवे प्लेटफ़ॉर्म {i} के नीचे",
          node_type="junction", x=50, y=py, level="subway",
          platform_number=i)

    N("subway_concourse_entry", "Subway Concourse Entry",
      name_kn="ಸಬ್‌ವೇ ಕಾನ್ಕೋರ್ಸ್ ಪ್ರವೇಶ", name_hi="सबवे कॉनकोर्स प्रवेश",
      node_type="junction", x=50, y=65, level="ground")

    N("subway_under_concourse", "Subway under Concourse",
      name_kn="ಸಬ್‌ವೇ ಕಾನ್ಕೋರ್ಸ್ ಕೆಳಗೆ", name_hi="सबवे कॉनकोर्स के नीचे",
      node_type="junction", x=50, y=65, level="subway")

    # ─────────────────────────────────────────────────────────────────────
    # 8.  PLATFORMS (walking nodes along each platform)
    # ─────────────────────────────────────────────────────────────────────
    for i, py in [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]:
        ptype = "Side" if i in (1, 6) else "Island"
        N(f"platform_{i}_west", f"Platform {i} ({ptype}) — West End",
          name_kn=f"ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i} — ಪಶ್ಚಿಮ",
          name_hi=f"प्लेटफ़ॉर्म {i} — पश्चिम",
          node_type="platform", platform_number=i, x=5, y=py,
          description=f"Western end of Platform {i} ({ptype})")

        N(f"platform_{i}_center", f"Platform {i} ({ptype}) — Center",
          name_kn=f"ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i} — ಮಧ್ಯ",
          name_hi=f"प्लेटफ़ॉर्म {i} — मध्य",
          node_type="platform", platform_number=i, x=50, y=py,
          description=f"Center of Platform {i} ({ptype})")

        N(f"platform_{i}_east", f"Platform {i} ({ptype}) — East End",
          name_kn=f"ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ {i} — ಪೂರ್ವ",
          name_hi=f"प्लेटफ़ॉर्म {i} — पूर्व",
          node_type="platform", platform_number=i, x=90, y=py,
          description=f"Eastern end of Platform {i} ({ptype})")

    # ─────────────────────────────────────────────────────────────────────
    #  EDGES — Entrance & Concourse connectivity
    # ─────────────────────────────────────────────────────────────────────

    # Entrance → ramps / concourse
    E("entrance_main", "ramp_west",        15, path_type="normal")
    E("entrance_main", "ramp_east",        15, path_type="normal")
    E("entrance_main", "concourse_south",  12, path_type="normal")
    E("ramp_west",     "concourse_south",  10, path_type="ramp", accessible=True)
    E("ramp_east",     "concourse_south",  10, path_type="ramp", accessible=True)

    # Exits
    E("exit_west",     "ramp_west",        15, path_type="normal")
    E("exit_east",     "ramp_east",        15, path_type="normal")
    E("exit_east",     "auto_bus_stand",   10, path_type="normal")
    E("reserved_parking", "exit_west",      8, path_type="normal")

    # Concourse internal mesh
    E("concourse_south",  "concourse_center", 8, path_type="normal")
    E("concourse_center", "concourse_west",  20, path_type="normal")
    E("concourse_center", "concourse_east",  20, path_type="normal")
    E("concourse_center", "concourse_north", 8,  path_type="normal")

    # Concourse → station building
    E("concourse_north",  "station_building_center", 55, path_type="normal")

    # Station building → facilities
    E("station_building_center", "waiting_hall_north", 20, path_type="normal")
    E("station_building_center", "waiting_hall_south", 15, path_type="normal")
    E("station_building_center", "ticket_counters",     8, path_type="normal")
    E("station_building_center", "toilet_male",        28, path_type="normal")
    E("station_building_center", "toilet_female",      28, path_type="normal")
    E("station_building_center", "help_desk",          18, path_type="normal")
    E("station_building_center", "drinking_water",     22, path_type="normal")
    E("station_building_center", "parking_west",       50, path_type="normal")
    E("station_building_center", "auto_bus_stand_north", 40, path_type="normal")

    # Concourse → FOB entries / subway entry at concourse level
    E("concourse_west",  "fob1_concourse",        48, path_type="normal")
    E("concourse_east",  "fob2_concourse",        48, path_type="normal")
    E("concourse_center","subway_concourse_entry", 45, path_type="normal")

    # ─────────────────────────────────────────────────────────────────────
    #  EDGES — Platform walking (west ↔ FOB1 ↔ subway ↔ FOB2 ↔ east)
    # ─────────────────────────────────────────────────────────────────────
    for i in range(1, 7):
        # west end → fob1 stairs
        E(f"platform_{i}_west",   f"fob1_stairs_p{i}", 25, path_type="normal")
        # fob1 stairs → subway entry (center)
        E(f"fob1_stairs_p{i}",    f"platform_{i}_center", 20, path_type="normal")
        # also fob1 stairs → subway via center
        E(f"platform_{i}_center", f"subway_entry_p{i}",   0, path_type="normal")
        # subway entry → fob2 stairs
        E(f"platform_{i}_center", f"fob2_stairs_p{i}",  15, path_type="normal")
        # fob2 stairs → east end
        E(f"fob2_stairs_p{i}",    f"platform_{i}_east", 25, path_type="normal")

    # ─────────────────────────────────────────────────────────────────────
    #  EDGES — FOB-1 stairs (ground ↔ bridge, NOT accessible)
    # ─────────────────────────────────────────────────────────────────────
    for i in range(1, 7):
        E(f"fob1_stairs_p{i}", f"fob1_bridge_p{i}",
          8, path_type="stairs", accessible=False)

    E("fob1_concourse", "fob1_bridge_concourse",
      8, path_type="stairs", accessible=False)

    # FOB-1 bridge corridor (bridge level, connecting platform strips)
    prev = "fob1_bridge_concourse"
    for i in [6, 5, 4, 3, 2, 1]:
        E(prev, f"fob1_bridge_p{i}", 10, path_type="fob_bridge", accessible=False)
        prev = f"fob1_bridge_p{i}"

    # FOB-1 Lift (ground ↔ bridge, accessible)
    E("lift_fob1_ground", "lift_fob1_upper", 2, path_type="lift", accessible=True)
    # Connect lift to nearby platform & bridge nodes (between P4 & P5)
    E("lift_fob1_ground", "fob1_stairs_p4", 5, path_type="normal")
    E("lift_fob1_ground", "fob1_stairs_p5", 5, path_type="normal")
    E("lift_fob1_upper",  "fob1_bridge_p4", 3, path_type="normal")
    E("lift_fob1_upper",  "fob1_bridge_p5", 3, path_type="normal")

    # ─────────────────────────────────────────────────────────────────────
    #  EDGES — FOB-2 stairs (ground ↔ bridge, NOT accessible)
    # ─────────────────────────────────────────────────────────────────────
    for i in range(1, 7):
        E(f"fob2_stairs_p{i}", f"fob2_bridge_p{i}",
          8, path_type="stairs", accessible=False)

    E("fob2_concourse", "fob2_bridge_concourse",
      8, path_type="stairs", accessible=False)

    prev = "fob2_bridge_concourse"
    for i in [6, 5, 4, 3, 2, 1]:
        E(prev, f"fob2_bridge_p{i}", 10, path_type="fob_bridge", accessible=False)
        prev = f"fob2_bridge_p{i}"

    # ─────────────────────────────────────────────────────────────────────
    #  EDGES — Subway stairs (ground ↔ subway, stairs → NOT accessible
    #          but the subway corridor itself is accessible via lift)
    # ─────────────────────────────────────────────────────────────────────
    for i in range(1, 7):
        E(f"subway_entry_p{i}", f"subway_under_p{i}",
          6, path_type="stairs", accessible=False)

    E("subway_concourse_entry", "subway_under_concourse",
      6, path_type="stairs", accessible=False)

    # Subway underground corridor
    prev = "subway_under_concourse"
    for i in [6, 5, 4, 3, 2, 1]:
        E(prev, f"subway_under_p{i}", 10, path_type="subway")
        prev = f"subway_under_p{i}"

    # Subway Lift (ground ↔ subway, accessible)
    E("lift_subway_ground", "lift_subway_lower", 2, path_type="lift", accessible=True)
    E("lift_subway_ground", "fob2_stairs_p4",    5, path_type="normal")
    E("lift_subway_ground", "fob2_stairs_p5",    5, path_type="normal")
    E("lift_subway_lower",  "subway_under_p4",   3, path_type="normal")
    E("lift_subway_lower",  "subway_under_p5",   3, path_type="normal")

    return nodes, edges


# ── Helper: get adjacency list (respecting blocked edges & accessibility) ─

def build_adjacency(
    nodes: Dict[str, Node],
    edges: List[Edge],
    accessible_only: bool = False,
    blocked_edges: Optional[set] = None
) -> Dict[str, List[Tuple[str, float, Edge]]]:
    """
    Build an adjacency list.
    Returns { node_id: [(neighbour_id, cost, edge_obj), ...] }
    """
    adj: Dict[str, List[Tuple[str, float, Edge]]] = {nid: [] for nid in nodes}
    blocked = blocked_edges or set()

    for e in edges:
        if e.blocked or (e.from_node, e.to_node) in blocked:
            continue
        if accessible_only and not e.accessible:
            continue

        adj[e.from_node].append((e.to_node, e.distance, e))
        if e.bidirectional:
            if (e.to_node, e.from_node) not in blocked:
                adj[e.to_node].append((e.from_node, e.distance, e))

    return adj
