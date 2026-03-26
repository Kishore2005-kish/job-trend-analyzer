# ------------------ IMPORTS ------------------
from fastapi import FastAPI
from ml.preprocess import load_data
from ml.extract_skills import extract_skills
from ml.trend_analysis import get_trending

# ------------------ APP INIT ------------------
app = FastAPI()

# ------------------ ROOT ------------------
@app.get("/")
def home():
    return {"message": "Job Market Analyzer API running 🚀"}

# ------------------ TRENDING SKILLS ------------------
@app.get("/trending")
def trending():
    data = load_data()

    all_skills = []

    for text in data:
        skills = extract_skills(text)
        all_skills.extend(skills)

    trend = get_trending(all_skills)

    return {
        "trending_skills": trend
    }

# ------------------ SKILL GAP ANALYZER ------------------
@app.post("/skill-gap")
def skill_gap(data: dict):
    user_skills = [s.lower() for s in data["skills"]]

    dataset = load_data()

    all_skills = []

    for text in dataset:
        skills = extract_skills(text)
        all_skills.extend(skills)

    trending = [skill for skill, _ in get_trending(all_skills)]

    gap = list(set(trending) - set(user_skills))

    return {
        "your_skills": user_skills,
        "missing_skills": gap
    }

# ------------------ OPTIONAL: ANALYZE TEXT ------------------
@app.post("/analyze-text")
def analyze_text(data: dict):
    text = data["text"]
    skills = extract_skills(text)

    return {
        "detected_skills": skills
    }