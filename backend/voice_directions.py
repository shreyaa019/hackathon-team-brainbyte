"""
voice_directions.py — Voice and visual direction support for RailSaathi

Generates:
  • SSML-annotated text for text-to-speech engines
  • Plain-text directions in 3 languages (EN, KN, HI)
  • Visual direction cues (arrow directions, icons)
  • Audio narration script segmented by step
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from pathfinding import RouteStep


SUPPORTED_LANGUAGES = {
    "en": {"name": "English",  "bcp47": "en-IN", "voice": "en-IN-Standard-A"},
    "kn": {"name": "ಕನ್ನಡ",    "bcp47": "kn-IN", "voice": "kn-IN-Standard-A"},
    "hi": {"name": "हिन्दी",    "bcp47": "hi-IN", "voice": "hi-IN-Standard-A"},
}

# Arrow / icon mapping for visual assistance
DIRECTION_ICON = {
    "straight": "⬆️",
    "left":     "⬅️",
    "right":    "➡️",
    "up":       "🔼",
    "down":     "🔽",
}

PATH_TYPE_ICON = {
    "normal":     "🚶",
    "stairs":     "🪜",
    "ramp":       "♿",
    "lift":       "🛗",
    "subway":     "🚇",
    "escalator":  "⬆️",
    "fob_bridge": "🌉",
}


@dataclass
class VoiceStep:
    """One step of narration for voice/visual guidance."""
    step_number: int
    text: str                          # plain text in requested language
    ssml: str                          # SSML for TTS
    direction_icon: str = "⬆️"
    path_icon: str = "🚶"
    distance_m: float = 0.0
    landmark: str = ""
    accessibility_warning: str = ""


@dataclass
class VoiceRoute:
    """Full narrated route."""
    language: str
    language_name: str
    bcp47_code: str
    intro_text: str
    intro_ssml: str
    steps: List[VoiceStep] = field(default_factory=list)
    summary_text: str = ""
    summary_ssml: str = ""
    total_distance_m: float = 0.0
    estimated_time_display: str = ""


def _format_time(seconds: float) -> dict:
    """Return time formatted in EN, KN, HI."""
    mins = int(seconds // 60)
    if mins < 1:
        return {
            "en": "less than a minute",
            "kn": "ಒಂದು ನಿಮಿಷಕ್ಕಿಂತ ಕಡಿಮೆ",
            "hi": "एक मिनट से कम",
        }
    return {
        "en": f"about {mins} minute{'s' if mins != 1 else ''}",
        "kn": f"ಸುಮಾರು {mins} ನಿಮಿಷ",
        "hi": f"लगभग {mins} मिनट",
    }


def _step_text(step: RouteStep, lang: str) -> str:
    """Get the instruction text in the requested language."""
    if lang == "kn":
        return step.instruction_kn or step.instruction
    elif lang == "hi":
        return step.instruction_hi or step.instruction
    return step.instruction


def _build_ssml(text: str, pause_ms: int = 500) -> str:
    """Wrap text in simple SSML with a trailing pause."""
    # Escape XML special chars
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<speak><p>{safe}</p><break time="{pause_ms}ms"/></speak>'


def generate_voice_route(
    steps: List[RouteStep],
    total_distance: float,
    estimated_seconds: float,
    origin_name: str,
    destination_name: str,
    lang: str = "en",
) -> VoiceRoute:
    """
    Generate a complete voice-narration package for a route.

    Parameters
    ----------
    steps : route steps from pathfinding
    total_distance : total route distance in metres
    estimated_seconds : estimated walking time
    origin_name, destination_name : human labels
    lang : "en" | "kn" | "hi"
    """
    lang_info = SUPPORTED_LANGUAGES.get(lang, SUPPORTED_LANGUAGES["en"])
    time_strs = _format_time(estimated_seconds)

    # ── Intro ──
    if lang == "kn":
        intro = (f"ನಮಸ್ಕಾರ! {origin_name} ಇಂದ {destination_name} ಗೆ "
                 f"ಒಟ್ಟು {total_distance:.0f} ಮೀಟರ್ ದೂರ. "
                 f"ಅಂದಾಜು ಸಮಯ {time_strs['kn']}. ಪ್ರಾರಂಭಿಸೋಣ.")
    elif lang == "hi":
        intro = (f"नमस्ते! {origin_name} से {destination_name} तक "
                 f"कुल {total_distance:.0f} मीटर दूरी है। "
                 f"अनुमानित समय {time_strs['hi']}। चलिए शुरू करते हैं।")
    else:
        intro = (f"Hello! Navigating from {origin_name} to {destination_name}. "
                 f"Total distance is {total_distance:.0f} metres. "
                 f"Estimated time is {time_strs['en']}. Let's begin.")

    voice_steps: List[VoiceStep] = []
    for i, s in enumerate(steps, 1):
        text = _step_text(s, lang)
        voice_steps.append(VoiceStep(
            step_number=i,
            text=text,
            ssml=_build_ssml(text),
            direction_icon=DIRECTION_ICON.get(s.direction, "⬆️"),
            path_icon=PATH_TYPE_ICON.get(s.path_type, "🚶"),
            distance_m=s.distance,
            landmark=s.landmark,
            accessibility_warning=s.accessibility_note,
        ))

    # ── Summary ──
    if lang == "kn":
        summary = f"ನೀವು {destination_name} ತಲುಪಿದ್ದೀರಿ. ಒಳ್ಳೆಯ ಪ್ರಯಾಣ ಹಾರೈಸುತ್ತೇವೆ!"
    elif lang == "hi":
        summary = f"आप {destination_name} पहुँच गए हैं। शुभ यात्रा!"
    else:
        summary = f"You have arrived at {destination_name}. Have a safe journey!"

    return VoiceRoute(
        language=lang,
        language_name=lang_info["name"],
        bcp47_code=lang_info["bcp47"],
        intro_text=intro,
        intro_ssml=_build_ssml(intro, pause_ms=800),
        steps=voice_steps,
        summary_text=summary,
        summary_ssml=_build_ssml(summary, pause_ms=1000),
        total_distance_m=total_distance,
        estimated_time_display=time_strs.get(lang, time_strs["en"]),
    )


# ── Convenience: full narration script as a single string ───────────────

def narration_script(voice_route: VoiceRoute) -> str:
    """Concatenate all narration into a single plain-text script."""
    parts = [voice_route.intro_text, ""]
    for vs in voice_route.steps:
        prefix = f"Step {vs.step_number}: {vs.direction_icon} {vs.path_icon} "
        parts.append(prefix + vs.text)
        if vs.accessibility_warning:
            parts.append(f"   {vs.accessibility_warning}")
    parts.append("")
    parts.append(voice_route.summary_text)
    return "\n".join(parts)


def ssml_full_script(voice_route: VoiceRoute) -> str:
    """Concatenate all SSML into a single <speak> document."""
    body_parts = []
    # Strip outer <speak> tags from individual SSMLs and concatenate
    import re
    def inner(ssml: str) -> str:
        m = re.search(r"<speak>(.*)</speak>", ssml, re.DOTALL)
        return m.group(1) if m else ssml

    body_parts.append(inner(voice_route.intro_ssml))
    for vs in voice_route.steps:
        body_parts.append(inner(vs.ssml))
    body_parts.append(inner(voice_route.summary_ssml))

    return f'<speak>{"".join(body_parts)}</speak>'
