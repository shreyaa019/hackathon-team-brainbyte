from fastapi import FastAPI

app = FastAPI(title="RailSaathi API")


@app.get("/")
def home():
    return {
        "app": "RailSaathi",
        "message": "RailSaathi backend is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }