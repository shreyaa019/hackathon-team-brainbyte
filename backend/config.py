"""
config.py — Centralised configuration for RailSaathi backend

Loads settings from environment variables with sensible defaults.
"""

from __future__ import annotations

import os


# ── Server ──────────────────────────────────────────────────────────────

HOST: str = os.getenv("RAILSAATHI_HOST", "0.0.0.0")
PORT: int = int(os.getenv("RAILSAATHI_PORT", "8000"))
DEBUG: bool = os.getenv("RAILSAATHI_DEBUG", "false").lower() in ("1", "true", "yes")

# ── CORS ────────────────────────────────────────────────────────────────
# Comma-separated list of allowed origins.  "*" = allow all (dev only).
CORS_ORIGINS: list[str] = os.getenv("RAILSAATHI_CORS_ORIGINS", "*").split(",")

# ── App metadata ────────────────────────────────────────────────────────

APP_TITLE: str = "RailSaathi API"
APP_DESCRIPTION: str = (
    "Smart indoor navigation API for Mysuru Junction Railway Station. "
    "Supports accessible routing, voice directions, multilingual output, "
    "and real-time station status simulation."
)
APP_VERSION: str = "1.0.0"
STATION_NAME: str = "Mysuru Junction (MYS)"
