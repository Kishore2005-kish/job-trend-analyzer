from preprocess import load_data
from extract_skills import extract_skills
from trend_analysis import get_trending

data = load_data()

all_skills = []

for text in data:
    skills = extract_skills(text)
    all_skills.extend(skills)

trend = get_trending(all_skills)

print("🔥 Trending Skills:")
print(trend)