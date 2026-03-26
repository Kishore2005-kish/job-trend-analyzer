import requests

APP_ID = "5f0cc5a8"
APP_KEY = "5f9a878101fa316d25504d3eee66ce3b"

def fetch_jobs(role="data scientist"):
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": role,
        "results_per_page": 10
    }

    res = requests.get(url, params=params)
    data = res.json()

    descriptions = []

    for job in data.get("results", []):
        descriptions.append(job.get("description", ""))

    return descriptions