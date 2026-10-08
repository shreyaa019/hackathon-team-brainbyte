"""
translations.py — Multilingual support for RailSaathi

Supports:  English (en), Kannada (kn), Hindi (hi)

Provides:
  • Static UI string translations
  • Facility type labels
  • Direction phrases
  • Error messages
  • API response wrappers for i18n
"""

from __future__ import annotations
from typing import Dict, Optional

SUPPORTED_LANGS = ["en", "kn", "hi"]

# ── Static UI strings ───────────────────────────────────────────────────

UI_STRINGS: Dict[str, Dict[str, str]] = {
    # App
    "app_name": {
        "en": "RailSaathi",
        "kn": "ರೈಲ್‌ಸಾಥಿ",
        "hi": "रेलसाथी",
    },
    "app_tagline": {
        "en": "Smart Navigation for Mysuru Junction",
        "kn": "ಮೈಸೂರು ಜಂಕ್ಷನ್‌ಗೆ ಸ್ಮಾರ್ಟ್ ನ್ಯಾವಿಗೇಶನ್",
        "hi": "मैसूरु जंक्शन के लिए स्मार्ट नेविगेशन",
    },

    # Navigation modes
    "mode_normal": {
        "en": "Normal Route",
        "kn": "ಸಾಮಾನ್ಯ ಮಾರ್ಗ",
        "hi": "सामान्य मार्ग",
    },
    "mode_accessible": {
        "en": "Accessible Route (Wheelchair / Disabled)",
        "kn": "ಪ್ರವೇಶಿಸಬಹುದಾದ ಮಾರ್ಗ (ಗಾಲಿಕುರ್ಚಿ / ಅಂಗವಿಕಲ)",
        "hi": "सुलभ मार्ग (व्हीलचेयर / विकलांग)",
    },
    "mode_elder": {
        "en": "Elder-Friendly Route",
        "kn": "ಹಿರಿಯರ-ಸ್ನೇಹಿ ಮಾರ್ಗ",
        "hi": "वरिष्ठ-अनुकूल मार्ग",
    },

    # Directions
    "turn_left": {
        "en": "Turn left",
        "kn": "ಎಡಕ್ಕೆ ತಿರುಗಿ",
        "hi": "बाएँ मुड़ें",
    },
    "turn_right": {
        "en": "Turn right",
        "kn": "ಬಲಕ್ಕೆ ತಿರುಗಿ",
        "hi": "दाएँ मुड़ें",
    },
    "go_straight": {
        "en": "Go straight",
        "kn": "ನೇರವಾಗಿ ಹೋಗಿ",
        "hi": "सीधे चलें",
    },
    "go_up": {
        "en": "Go up",
        "kn": "ಮೇಲೆ ಹೋಗಿ",
        "hi": "ऊपर जाएँ",
    },
    "go_down": {
        "en": "Go down",
        "kn": "ಕೆಳಗೆ ಹೋಗಿ",
        "hi": "नीचे जाएँ",
    },

    # Path types
    "path_stairs": {
        "en": "Stairs",
        "kn": "ಮೆಟ್ಟಿಲುಗಳು",
        "hi": "सीढ़ियाँ",
    },
    "path_lift": {
        "en": "Lift / Elevator",
        "kn": "ಲಿಫ್ಟ್",
        "hi": "लिफ्ट",
    },
    "path_ramp": {
        "en": "Ramp",
        "kn": "ರ‍್ಯಾಂಪ್",
        "hi": "रैंप",
    },
    "path_subway": {
        "en": "Subway (Underground)",
        "kn": "ಸಬ್‌ವೇ (ಭೂಗತ)",
        "hi": "सबवे (भूमिगत)",
    },
    "path_fob": {
        "en": "Foot Over Bridge",
        "kn": "ಕಾಲು ಸೇತುವೆ",
        "hi": "फुट ओवर ब्रिज",
    },
    "path_escalator": {
        "en": "Escalator",
        "kn": "ಎಸ್ಕಲೇಟರ್",
        "hi": "एस्केलेटर",
    },

    # Facilities
    "facility_toilet": {
        "en": "Toilet / Restroom",
        "kn": "ಶೌಚಾಲಯ",
        "hi": "शौचालय",
    },
    "facility_ticket_counter": {
        "en": "Ticket Counter",
        "kn": "ಟಿಕೆಟ್ ಕೌಂಟರ್",
        "hi": "टिकट काउंटर",
    },
    "facility_waiting_hall": {
        "en": "Waiting Hall",
        "kn": "ಕಾಯುವ ಸಭಾಂಗಣ",
        "hi": "प्रतीक्षालय",
    },
    "facility_help_desk": {
        "en": "Help Desk",
        "kn": "ಸಹಾಯ ಕೇಂದ್ರ",
        "hi": "सहायता केंद्र",
    },
    "facility_drinking_water": {
        "en": "Drinking Water",
        "kn": "ಕುಡಿಯುವ ನೀರು",
        "hi": "पीने का पानी",
    },
    "facility_lift": {
        "en": "Lift / Elevator",
        "kn": "ಲಿಫ್ಟ್",
        "hi": "लिफ्ट",
    },
    "facility_parking": {
        "en": "Parking",
        "kn": "ಪಾರ್ಕಿಂಗ್",
        "hi": "पार्किंग",
    },

    # Status messages
    "status_operational": {
        "en": "Operational",
        "kn": "ಕಾರ್ಯನಿರತ",
        "hi": "चालू",
    },
    "status_out_of_service": {
        "en": "Out of Service",
        "kn": "ಸೇವೆಯಲ್ಲಿಲ್ಲ",
        "hi": "सेवा बंद",
    },
    "status_blocked": {
        "en": "Path Blocked",
        "kn": "ಮಾರ್ಗ ನಿರ್ಬಂಧಿಸಲಾಗಿದೆ",
        "hi": "मार्ग अवरुद्ध",
    },

    # Errors
    "error_no_route": {
        "en": "No route found. Some paths may be blocked.",
        "kn": "ಮಾರ್ಗ ಕಂಡುಬಂದಿಲ್ಲ. ಕೆಲವು ಮಾರ್ಗಗಳು ನಿರ್ಬಂಧಿಸಲ್ಪಟ್ಟಿರಬಹುದು.",
        "hi": "कोई मार्ग नहीं मिला। कुछ मार्ग अवरुद्ध हो सकते हैं।",
    },
    "error_invalid_node": {
        "en": "Invalid location specified.",
        "kn": "ಅಮಾನ್ಯ ಸ್ಥಳ ನಿರ್ದಿಷ್ಟಪಡಿಸಲಾಗಿದೆ.",
        "hi": "अमान्य स्थान निर्दिष्ट किया गया।",
    },

    # Accessibility warnings
    "warning_stairs_on_route": {
        "en": "⚠ This route includes stairs.",
        "kn": "⚠ ಈ ಮಾರ್ಗದಲ್ಲಿ ಮೆಟ್ಟಿಲುಗಳಿವೆ.",
        "hi": "⚠ इस मार्ग में सीढ़ियाँ हैं।",
    },
    "warning_use_lift": {
        "en": "Consider using the lift for an accessible route.",
        "kn": "ಪ್ರವೇಶಿಸಬಹುದಾದ ಮಾರ್ಗಕ್ಕೆ ಲಿಫ್ಟ್ ಬಳಸುವುದನ್ನು ಪರಿಗಣಿಸಿ.",
        "hi": "सुलभ मार्ग के लिए लिफ्ट का उपयोग करें।",
    },

    # Voice
    "voice_start": {
        "en": "Starting voice navigation.",
        "kn": "ಧ್ವನಿ ನ್ಯಾವಿಗೇಶನ್ ಪ್ರಾರಂಭಿಸಲಾಗುತ್ತಿದೆ.",
        "hi": "वॉइस नेविगेशन शुरू हो रहा है।",
    },
    "voice_arrived": {
        "en": "You have arrived at your destination.",
        "kn": "ನೀವು ನಿಮ್ಮ ಗಮ್ಯಸ್ಥಾನವನ್ನು ತಲುಪಿದ್ದೀರಿ.",
        "hi": "आप अपने गंतव्य पर पहुँच गए हैं।",
    },
}


def t(key: str, lang: str = "en") -> str:
    """Look up a translated string. Falls back to English."""
    entry = UI_STRINGS.get(key, {})
    return entry.get(lang, entry.get("en", key))


def get_all_strings(lang: str = "en") -> Dict[str, str]:
    """Return all UI strings for a given language."""
    return {k: t(k, lang) for k in UI_STRINGS}
