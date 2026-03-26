skills_list = [
    "python", "java", "sql", "aws",
    "machine learning", "data analysis",
    "power bi", "tableau",
    "react", "node", "docker",
    "kubernetes", "spark", "hadoop",
    "spring", "hibernate", "microservices",
    "spring boot", "rest api", "oop",
    "linux", "git", "agile",
    "tensorflow", "pytorch",
    "html", "css", "javascript"
]

# 🔥 normalize aliases
skill_alias = {
    "js": "javascript",
    "ml": "machine learning"
}

# 🔥 remove useless skills
ignore_skills = [
    "excel", "communication", "teamwork",
    "oop", "agile", "linux", "git"
]

def normalize(skill):
    return skill_alias.get(skill, skill)


def extract_skills(text):
    text = text.lower()
    found = []

    for skill in skills_list:
        if skill in text:
            found.append(normalize(skill))

    # remove noise + duplicates
    found = [s for s in found if s not in ignore_skills]

    return list(set(found))