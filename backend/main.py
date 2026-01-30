from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = []


@app.post("/add")
def add_mood(data: dict):
    mood_entry = {
        "id": len(db) + 1,
        "mood": data.get("mood", "unknown"),
        "note": data.get("note", ""),
        "timestamp": datetime.now().isoformat(),
        "date_formatted": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "day_of_week": datetime.now().strftime("%A"),
        "is_weekend": datetime.now().weekday() >= 5,
    }
    db.append(mood_entry)
    return {"status": "added", "entry": mood_entry}


@app.get("/list")
def list_moods():
    sorted_db = sorted(db, key=lambda x: x["timestamp"], reverse=True)
    for item in sorted_db:
        item["age_in_seconds"] = (
            datetime.now() - datetime.fromisoformat(item["timestamp"])
        ).total_seconds()
    return {"moods": sorted_db, "count": len(sorted_db)}
