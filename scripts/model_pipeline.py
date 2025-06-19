# scripts/model_pipeline.py
import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def estimate_power(v_ms, radius=20, efficiency=0.35, air_density=1.225):
    area = np.pi * radius**2
    return 0.5 * air_density * area * (v_ms**3) * efficiency * 24 / 1000

def process_city(df, city, threshold_kwh=2000):  # changed threshold
    NUM_TURBINES = 15  # average wind farm size
    
    df.set_index(pd.to_datetime(df['DATE']), inplace=True)
    df = df.asfreq('D').fillna(method='ffill')
    series = df['AVG WIND SPEED']
    
    model = SARIMAX(series, order=(1,1,1), seasonal_order=(1,1,1,12))
    fit = model.fit(disp=False)
    
    forecast_kmh = fit.forecast(steps=30)
    forecast_ms = forecast_kmh / 3.6
    
    # Multiply power per turbine by number of turbines
    power = forecast_ms.apply(lambda v: estimate_power(v) * NUM_TURBINES)
    avg_power = power.mean()
    
    feasibility = "Feasible" if avg_power >= threshold_kwh else "Not Feasible"
    
    result = pd.DataFrame({
        "City": city,
        "Date": pd.date_range(df.index[-1] + pd.Timedelta(days=1), periods=30),
        "Wind Forecast (km/h)": forecast_kmh.values,
        "Power (kWh/day)": power.values,
        "Feasibility": feasibility
    })
    return result
