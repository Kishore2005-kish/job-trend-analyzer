import requests
import json
import os

# ------------------ CONFIG ------------------
API_KEY = "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"  # 🔥 paste your NEW key here

CACHE_FILE = "ml/role_cache.json"


# ------------------ CACHE ------------------
def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


# ------------------ AI FUNCTION ------------------
def get_ai_skills(role):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # 🔥 more reliable
        "messages": [
            {
                "role": "user",
                "content": f"List 5 important skills for a {role}. Only comma separated."
            }
        ]
    }

    try:
        res = requests.post(url, headers=headers, json=data, timeout=10)
        response = res.json()

        print("🔥 FULL RESPONSE:", response)

        if "choices" not in response:
            return []

        text = response["choices"][0]["message"]["content"]

        skills = [s.strip().lower() for s in text.split(",") if s.strip()]

        return skills[:5]

    except Exception as e:
        print("❌ API error:", e)
        return []


# ------------------ MAIN FUNCTION ------------------
def calculate_skill_gap(user_skills, role):
    user_skills = [s.lower().strip() for s in user_skills]
    role_key = role.lower().strip()

    cache = load_cache()

    # 🔥 CACHE FIRST
    if role_key in cache:
        print("⚡ USING CACHE")
        base_skills = cache[role_key]

    else:
        print("🚀 CALLING API")
        base_skills = get_ai_skills(role_key)

        # 🔥 FALLBACK (if API fails)
        if not base_skills:
            print("⚠️ FALLBACK USED")

            if "blockchain" in role_key:
                base_skills = ["web3", "ethereum", "smart contracts"]
            elif "cyber" in role_key or "security" in role_key:
                base_skills = ["penetration testing", "cryptography", "network security"]
            elif "devops" in role_key:
                base_skills = ["docker", "kubernetes", "ci/cd"]
            elif "frontend" in role_key:
                base_skills = ["html", "css", "javascript", "react"]
            elif "java" in role_key:
                base_skills = ["spring", "spring boot", "microservices", "rest api"]
            elif "data" in role_key:
                base_skills = ["machine learning", "sql", "data analysis", "aws"]
            else:
                base_skills = ["problem solving", "communication", "fundamentals"]

        # 🔥 STORE
        cache[role_key] = base_skills
        save_cache(cache)

    # 🔥 GAP
    gap = [s for s in base_skills if s not in user_skills][:5]

    return {
        "role": role,
        "your_skills": user_skills,
        "missing_skills": gap,
        "recommendation": f"Focus on learning {', '.join(gap[:2])}" if gap else "You are well aligned!"
    }