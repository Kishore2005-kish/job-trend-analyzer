from collections import Counter

def get_trending(skills):
    return Counter(skills).most_common(15)