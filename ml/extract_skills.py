skills_list = [
    "python", "java", "sql", "aws", "excel",
    "machine learning", "data analysis",
    "power bi", "tableau",
    "react", "node", "docker",
    "kubernetes", "spark", "hadoop"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in skills_list if skill in text]