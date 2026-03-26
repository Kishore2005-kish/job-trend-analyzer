def skill_gap(user_skills, trending_skills):
    return list(set(trending_skills) - set(user_skills))