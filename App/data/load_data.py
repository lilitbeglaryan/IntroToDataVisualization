# data/load_data.py

import pandas as pd

def load_data():
    """
    Loads the Credit Scoring dataset from a GitHub URL.
    Performs basic preprocessing and returns the DataFrame.
    """
    url = "https://raw.githubusercontent.com/Metricam/Public_data/master/FINANCE_Credit_Scoring.csv"
    df = pd.read_csv(url)

    # # Optional: convert column names to lowercase and strip whitespace
    # df.columns = df.columns.str.lower().str.strip()

    # Make sure 'default' column is treated as categorical (0 = no, 1 = yes)
    df['default'] = df['default'].astype(int)

    # Clean up 'age' in case of weird values
    df = df[df['age'] > 0]

    # Optional: map target to readable labels (for graphs)
    df['default_label'] = df['default'].map({0: "No Default", 1: "Default"})

    return df
