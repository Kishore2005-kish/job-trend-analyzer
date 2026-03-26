import pandas as pd

def load_data(role=None):
    df = pd.read_csv("data/jobs.csv", nrows=3000)

    # clean required columns
    df = df.dropna(subset=["Job Description", "Job Title"])

    if role:
        role = role.lower()

        df = df[df["Job Title"].str.lower().str.contains(role)]

        # fallback if empty
        if df.empty:
            df = pd.read_csv("data/jobs.csv", nrows=2000)

    return df["Job Description"].tolist()