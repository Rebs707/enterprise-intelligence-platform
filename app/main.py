from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def health():
    return {
        "platform": "Enterprise Intelligence Platform",
        "status": "running"
    }
