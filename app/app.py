import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import joblib
import requests
import os

st.set_page_config(page_title="TaxiVision - Predicción de Demanda NYC", layout="wide")


# 1. Cargar assets

@st.cache_data(show_spinner=True)
def load_assets():
    demand_hourly = pd.read_csv("demand_hourly.csv")
    zone_lookup = pd.read_csv("taxi_zone_lookup.csv")
    df_points = pd.read_parquet("nyc_for_dashboard.parquet")
    model_rf = joblib.load("rf_demand_model.joblib")
    encoder = joblib.load("ordinal_encoder.joblib")
    # scaler/model TF optional
    return demand_hourly, zone_lookup, df_points, model_rf, encoder

demand_hourly, zone_lookup, df_points, model_rf, encoder = load_assets()

st.title("TaxiVision - Predicción de Demanda NYC")

# Top layout: selector zona
st.sidebar.header("Configuración")
boroughs = ["Todos"] + sorted(zone_lookup["Borough"].dropna().unique().tolist())
sel_borough = st.sidebar.selectbox("Filtrar Borough", boroughs)

if sel_borough != "Todos":
    zones_available = zone_lookup[zone_lookup["Borough"]==sel_borough]["Zone"].tolist()
else:
    zones_available = zone_lookup["Zone"].tolist()

zone_selected = st.selectbox("Seleccione Zona (por nombre):", zones_available, index=0)
zone_row = zone_lookup[zone_lookup["Zone"]==zone_selected].iloc[0]
zone_id = int(zone_row["LocationID"])

st.markdown(f"**Zona seleccionada:** {zone_selected} — LocationID: {zone_id} — Borough: {zone_row['Borough']}")


# 2. Heatmap por hora

st.header("Mapa de calor (pickups)")

hour_sel = st.slider("Selecciona la hora (pickup)", 0, 23, 12)
df_hour = df_points[df_points["pickup_hour"]==hour_sel].dropna(subset=["pickup_latitude","pickup_longitude"])
heat_data = df_hour[["pickup_latitude","pickup_longitude"]].values.tolist()

m = folium.Map(location=[40.75, -73.98], zoom_start=11)
if len(heat_data) > 0:
    HeatMap(heat_data, radius=8, blur=10, max_zoom=13).add_to(m)
st_folium(m, width=1000, height=550)


# 3. Predicción por hora para zona seleccionada

st.header("Demanda Esperada por Hora (Predicción)")

# Construir input para las 24 horas
hours = np.arange(0,24)
# Usar month & dow como mediana de la selección de fechas del conjunto de datos — fex: tomar el mes más común y dow
# Pero lo más sencillo: utilice month=6, dow=2 como marcadores de posición O calcule a partir de la distribución del conjunto de datos
common_month = int(demand_hourly.get('pickup_hour', pd.Series([1])).index[0]) if False else 6
# Construir tabla
input_df = pd.DataFrame({
    "PULocationID": [zone_id]*24,
    "pickup_hour": hours,
    "month": [6]*24,
    "dow": [2]*24
})
# Codificar y predecir con RF
# Copiar entrada
X_enc = input_df[["PULocationID"]].copy()

# Convertir todo a string, incluso NaN
X_enc["PULocationID"] = X_enc["PULocationID"].astype(str)

# Reemplazar valores inválidos por "-1" (string)
X_enc["PULocationID"] = X_enc["PULocationID"].replace(["nan", "None", ""], "-1")

# Transformar
X_enc["PULocationID_enc"] = encoder.transform(X_enc[["PULocationID"]])

X_enc = pd.DataFrame({
    "PULocationID_enc": X_enc["PULocationID_enc"],
    "pickup_hour": input_df["pickup_hour"],
    "month": input_df["month"],
    "dow": input_df["dow"]
})

preds = model_rf.predict(X_enc)
preds = np.clip(preds, a_min=0, a_max=None)

pred_df = pd.DataFrame({"pickup_hour": hours, "prediction": preds})
# Suavizado con media móvil para visualización
pred_df["prediction_smooth"] = pred_df["prediction"].rolling(3, center=True, min_periods=1).mean()

# Trama
st.line_chart(pred_df.set_index("pickup_hour")["prediction_smooth"])

# Mostrar tabla
st.dataframe(pred_df.style.format({"prediction":"{:.1f}", "prediction_smooth":"{:.1f}"}))


# 4. Comparar con histórico (demand_hourly)

st.header("Comparación con demanda histórica (media por hora)")

hist = demand_hourly[demand_hourly["PULocationID"]==zone_id].sort_values("pickup_hour")
if hist.empty:
    st.info("No hay datos históricos suficientes para esta zona en el sample.")
else:
    merged = pred_df.merge(hist[["pickup_hour","demand_mean"]], on="pickup_hour", how="left")
    st.line_chart(merged.set_index("pickup_hour")[["prediction_smooth","demand_mean"]])


# 5. Integración mínima de Clima

st.header("🌤 Clima (histórico) para la fecha seleccionada")

# Fecha selector basado en df_points
dates = sorted(df_points["pickup_date"].unique())
sel_date = st.selectbox("Selecciona fecha (para consultar clima):", dates, index=0)

use_openweather = os.environ.get("OPENWEATHER_API_KEY", "") != "" or False
OW_KEY = os.environ.get("OPENWEATHER_API_KEY","")

if OW_KEY:
    st.write("Usando OpenWeather (API key encontrada en variable de entorno).")
else:
    st.write("Usando Open-Meteo (no requiere key).")

def get_weather_openmete(date):
    # Usar Open-Meteo (latitude/longitude de NYC)
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=40.7128&longitude=-74.0060&hourly=temperature_2m,precipitation,"
        f"timezone=America%2FNew_York&start_date={date}&end_date={date}"
    )
    r = requests.get(url, timeout=10)
    return r.json()

def get_weather_openweather(date, key):
    # OpenWeather One Call (historical) requiere timestamp unix por hora y cuenta PRO para historico extendido.
    # Consulta de forecast para la fecha cercana (si no está disponible, fallback)
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat=40.7128&lon=-74.0060&exclude=minutely,daily,alerts&appid={key}&units=metric"
    r = requests.get(url, timeout=10)
    return r.json()

weather_json = None
if OW_KEY:
    try:
        weather_json = get_weather_openweather(sel_date, OW_KEY)
        # Extraer la temperatura por hora si está disponible
        if 'hourly' in weather_json:
            hrs = weather_json['hourly']
            wdf = pd.DataFrame(hrs)[['dt','temp','rain']] if 'rain' in pd.DataFrame(hrs).columns else pd.DataFrame(hrs)[['dt','temp']]
            # Convertir dt
            wdf['Hora'] = pd.to_datetime(wdf['dt'], unit='s').dt.strftime("%Y-%m-%dT%H:%M")
            wdf = wdf.rename(columns={'temp':'Temperatura (°C)'}).fillna(0)
        else:
            weather_json = get_weather_openmete(sel_date)
            hours = weather_json["hourly"]["time"]
            temps = weather_json["hourly"]["temperature_2m"]
            precip = weather_json["hourly"]["precipitation"]
            wdf = pd.DataFrame({"Hora":hours, "Temperatura (°C)":temps, "Precipitación (mm)":precip})
    except Exception as e:
        st.warning("OpenWeather falla: usando Open-Meteo como fallback. Error: "+str(e))
        weather_json = get_weather_openmete(sel_date)
        hours = weather_json["hourly"]["time"]
        temps = weather_json["hourly"]["temperature_2m"]
        precip = weather_json["hourly"]["precipitation"]
        wdf = pd.DataFrame({"Hora":hours, "Temperatura (°C)":temps, "Precipitación (mm)":precip})
else:
    try:
        weather_json = get_weather_openmete(sel_date)

        # Validación robusta de clave "hourly"
        if ("hourly" not in weather_json or
            "time" not in weather_json["hourly"] or
            "temperature_2m" not in weather_json["hourly"]):

            st.warning("Open-Meteo no devolvió datos horarios para esta fecha.")
            wdf = pd.DataFrame()

        else:
            hours = weather_json["hourly"]["time"]
            temps = weather_json["hourly"]["temperature_2m"]
            precip = weather_json["hourly"].get("precipitation", [0]*len(hours))

            wdf = pd.DataFrame({
                "Hora": hours,
                "Temperatura (°C)": temps,
                "Precipitación (mm)": precip
            })

    except Exception as e:
        st.error("Error consultando Open-Meteo: " + str(e))
        wdf = pd.DataFrame()

if not wdf.empty:
    st.subheader("Valores horarios del clima")
    st.dataframe(wdf)
    st.line_chart(wdf.set_index("Hora")["Temperatura (°C)"])

st.markdown("---")
st.caption("Dashboard generado con sample del dataset. Para producción, usar todos los datos y re-entrenar modelo con features extendidos (clima, eventos, holidays).")
