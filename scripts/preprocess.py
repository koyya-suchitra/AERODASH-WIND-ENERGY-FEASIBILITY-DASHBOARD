# scripts/preprocess.py
import pandas as pd
import numpy as np

def clean_df(df):
    df.rename(columns={"time": "DATE"}, inplace=True)
    df['DATE'] = pd.to_datetime(df['DATE']).dt.normalize()
    df.dropna(axis=1, thresh=0.7*len(df), inplace=True)
    df['AVG WIND SPEED'].fillna(df['AVG WIND SPEED'].median(), inplace=True)
    # Remove outliers
    Q1, Q3 = df['AVG WIND SPEED'].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    df = df[df['AVG WIND SPEED'].between(Q1 - 1.5*IQR, Q3 + 1.5*IQR)]
    return df
