# scripts/main.py
import pandas as pd
from datetime import datetime
from scripts.data_fetch import fetch_meteo_data
from scripts.preprocess import clean_df
from scripts.model_pipeline import process_city


cities = {
    "Kakinada": (16.93, 82.22),
    "Visakhapatnam": (17.69, 83.21),
    "Jaisalmer": (26.91, 70.91),
    "Nellore": (14.45, 79.99),
    "Kurnool": (15.83, 78.04),
}

start = datetime(2024,1,1)
end = datetime(2025,5,31)

all_results = pd.DataFrame()
for city, (lat, lon) in cities.items():
    df = fetch_meteo_data(lat, lon, start, end)
    df_clean = clean_df(df)
    city_results = process_city(df_clean, city)
    all_results = pd.concat([all_results, city_results], ignore_index=True)

all_results.to_csv("C:/Users/suchi/Desktop/aerodash/data/wind_forecasts.csv", index=False)
print("✅ CSV ready for Tableau")