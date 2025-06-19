# scripts/data_fetch.py
from meteostat import Point, Daily
from datetime import datetime

def fetch_meteo_data(lat, lon, start, end):
    loc = Point(lat, lon)
    df = Daily(loc, start, end).fetch()
    if "wspd" not in df.columns:
        raise Exception("Wind speed column missing")
    df.rename(columns={"wspd": "AVG WIND SPEED", "wdir": "WIND DIRECTION",
                       "wpgt": "WIND PEAK GUST"}, inplace=True)
    df.reset_index(inplace=True)
    return df[["time","AVG WIND SPEED","WIND DIRECTION","WIND PEAK GUST"]]
