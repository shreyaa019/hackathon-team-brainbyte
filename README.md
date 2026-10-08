# RailSaathi 🚂

**Smart Indoor Navigation API for Mysuru Junction Railway Station**

> Built by **Team BrainByte** — Hackathon Project

---

## Overview

RailSaathi is a backend API that provides real-time indoor navigation for Mysuru Junction railway station. It supports accessible routing (wheelchair, elderly), multilingual voice directions (English, Kannada, Hindi), and live station status simulation.

## Features

- **Shortest-path routing** between any two station locations (Dijkstra)
- **Accessible mode** — avoids stairs, uses lifts & ramps only
- **Elder-friendly mode** — penalises stairs, prefers lifts & ramps
- **Turn-by-turn directions** with landmark references
- **Voice navigation** — SSML + plain text in EN / KN / HI
- **Station status** — blocked paths, facility outages, crowd levels
- **Facility finder** — nearest toilet, lift, ticket counter, etc.
- **Disruption simulation** for demo/testing

## Tech Stack

| Layer    | Technology           |
|----------|---------------------|
| API      | FastAPI (Python)    |
| Server   | Uvicorn             |
| Graph    | Custom Dijkstra     |
| i18n     | English, Kannada, Hindi |

## Project Structure

```
hackathon-team-brainbyte/
├── backend/
│   ├── __init__.py          # package marker
│   ├── config.py            # centralised settings (env vars)
│   ├── main.py              # FastAPI app & all endpoints
│   ├── pathfinding.py       # Dijkstra routing & direction gen
│   ├── station_graph.py     # Mysuru Junction graph (nodes/edges)
│   ├── station_status.py    # live status, blocked paths, simulation
│   ├── translations.py      # multilingual UI strings
│   ├── voice_directions.py  # SSML & narrated voice output
│   ├── requirements.txt     # Python dependencies
│   └── run.py               # server entry point
├── .gitignore
└── README.md
```

## Quick Start

```bash
# 1. Create & activate a virtual environment
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python run.py
```

The API will be available at **http://localhost:8000**.  
Interactive docs at **http://localhost:8000/docs**.

## Key API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/route` | Find navigation route |
| `POST` | `/api/route/voice` | Route with voice/visual directions |
| `GET`  | `/api/facilities` | List all facilities |
| `GET`  | `/api/facilities/nearest/{type}` | Find nearest facility |
| `GET`  | `/api/station/status` | Full station status snapshot |
| `POST` | `/api/station/simulate` | Trigger random disruption |
| `GET`  | `/api/nodes` | List all navigable nodes |
| `GET`  | `/api/translations?lang=kn` | UI strings in a language |
| `GET`  | `/api/languages` | Supported languages |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `RAILSAATHI_HOST` | `0.0.0.0` | Server bind address |
| `RAILSAATHI_PORT` | `8000` | Server port |
| `RAILSAATHI_DEBUG` | `false` | Enable auto-reload |
| `RAILSAATHI_CORS_ORIGINS` | `*` | Comma-separated allowed origins |

## License

Hackathon project — Team BrainByte.