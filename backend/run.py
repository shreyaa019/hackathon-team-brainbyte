"""
run.py — Entry point to start the RailSaathi API server.

Usage:
    python run.py
"""

import uvicorn
from config import HOST, PORT, DEBUG

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG,
    )
