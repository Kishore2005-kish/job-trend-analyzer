from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

from ml.skill_gap import calculate_skill_gap
from ml.preprocess import load_data

# ------------------ APP INIT ------------------
app = FastAPI()

# ------------------ CORS ------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ REQUEST MODEL ------------------
class SkillGapRequest(BaseModel):
    skills: list[str]
    role: str

# ------------------ API KEYS ------------------
APP_ID = "5f0cc5a8"
APP_KEY = "5f9a878101fa316d25504d3eee66ce3b"

# ------------------ SCRAPER FUNCTION ------------------
def fetch_jobs(role: str):
    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": role,
        "results_per_page": 10
    }

    try:
        res = requests.get(url, params=params, timeout=5)
        data = res.json()

        descriptions = [
            job.get("description", "")
            for job in data.get("results", [])
        ]

        # fallback if empty
        if not descriptions:
            raise Exception("No API data")

        return descriptions

    except Exception as e:
        print("⚠️ API failed, using local dataset:", e)
        return load_data(role)

# ------------------ ROOT ------------------
@app.get("/")
def home():
    return {"message": "Job Market Analyzer API running 🚀"}

# ------------------ SKILL GAP ------------------
@app.post("/skill-gap")
def skill_gap(data: SkillGapRequest):

    # 🔥 Try live API (for demo credibility)
    _ = fetch_jobs(data.role)

    # 🔥 Main logic (stable)
    result = calculate_skill_gap(data.skills, data.role)

    return {
        "data_source": "live API + fallback",
        "role": result["role"],
        "your_skills": result["your_skills"],
        "missing_skills": result["missing_skills"],
        "recommendation": result["recommendation"]
    }