import pandas as pd

def load_data():
    df = pd.read_csv("data/postings.csv", nrows=2000, encoding="latin1")
    return df["description"].dropna().tolist()