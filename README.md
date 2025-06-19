# ⚡ Wind Energy Feasibility Dashboard – Team AeroDash
> ✅ *A final project submitted for the* **1M1B Green Internship 2025**

> Want to look at it?
https://public.tableau.com/app/profile/suchitra.koyya/viz/AERODASH-WINDENERGYFEASIBILITYDASHBOARD/Dashboard2

> A powerful, interactive dashboard built using **Tableau**, backed by **SARIMA modeling** and **Meteostat** weather data, to forecast wind energy potential and assess feasibility of windmill installations across key Indian cities.

---

## 🚀 Overview

This project evaluates the **wind energy generation feasibility** across multiple cities in India using:

- 🌪️ **Wind speed forecasting (30 days ahead)**
- 📈 **Power generation estimation**
- ✅ **Feasibility classification**
- 📍 **Location-wise comparison via interactive dashboard**

---

## 🧠 What We Built

- 📦 **Python Pipeline** for:
  - Fetching historical weather data using `Meteostat`
  - Cleaning & preprocessing
  - Forecasting wind speed using **SARIMA** model
  - Estimating daily power output (kWh) using turbine formula
  - Classifying **feasibility** based on average power threshold

- 📊 **Tableau Dashboard** for:
  - Dynamic city selection
  - Wind forecast line chart
  - Bar chart for power output
  - Feasibility visualized via heatmaps and shapes
  - Geographical location map
  - KPI cards for average wind speed and power

---

## 📁 Project Structure

aerodash/
│
├── scripts/
│ ├── data_fetch.py # Fetches Meteostat daily data
│ ├── preprocess.py # Cleans, formats, removes outliers
│ └── model_pipeline.py # SARIMA modeling + power estimation
│
├── data/
│ └── wind_forecasts.csv # Final output file with forecasts and feasibility
│
├── tableau/
│ └── dashboard.twbx # Final Tableau dashboard (can export to PDF/image)
│
├── screenshots/
│ └── dashboard_preview.png # Image of final dashboard
│
└── README.md # This file


---

## 🧪 Methodology

### ✅ Data Collection
- **Source:** Meteostat API
- **Cities:** Jaisalmer, Kakinada, Visakhapatnam, Nellore, Kurnool
- **Duration:** Jan 2024 to May 2025

### 🔧 Forecasting & Modeling
- SARIMA `(1,1,1)(1,1,1,12)` model fitted for each city
- Forecasted 30 days ahead daily wind speed
- Converted km/h → m/s
- Estimated power output:
  
  \[
  P = 0.5 × ρ × A × v^3 × η × 24 / 1000
  \]

  where:
  - ρ = air density (1.225 kg/m³)
  - A = π × radius² (20m radius used)
  - η = turbine efficiency (35%)

### ⚡ Feasibility Logic

> **Feasible** if average daily power ≥ **2000 kWh** (assuming 15 turbines)

---

## 📊 Tableau Dashboard Features

| Component                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 📈 Wind Speed Forecast     | Line chart showing 30-day trend, colored by city, with ideal threshold line |
| ⚡ Power Forecast          | Bar chart showing daily forecasted kWh output per city                      |
| ✅ Feasibility Map         | Shape-based chart showing “Feasible” or “Not This Time!” status             |
| 📍 Geographic Map          | Interactive city-level map using coordinates                                |
| 🧮 KPI Cards               | Displays average wind speed and average power for selected city             |
| 🎛️ Filters                | City selector with dynamic interactivity across charts                      |

---

## 🎨 Design Theme

- **Dark mode** aesthetic (Black + Electric Blue)
- Neon-style fonts and glowing highlights
- Custom shapes (✅ / ❌), city-wise color schemes
- Informative tooltips, responsive layout

---

## 🧠 Insights & Use-Cases

- Identify **wind-rich locations** for future windmill setups
- Provide **evidence-based planning tool** to energy agencies
- Show **seasonal & city-wise patterns** using historical modeling
- Easily extensible to other regions / energy sources

---

## 📌 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/koyya-suchitra/AERODASH-WIND-ENERGY-FEASIBILITY-DASHBOARD.git
   cd aerodash


👨‍💻 Team AeroDash
Suchitra Koyya https://www.linkedin.com/in/suchitra-koyya-605a242b5
Rohith Kumar Jogi https://www.linkedin.com/in/rohith-kumar-jogi-747a782b8

📢 Let's Connect
Have suggestions or want to use this for your region?
Connect on LinkedIn or drop a ⭐️ if this helped!

