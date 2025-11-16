# 📄 Diccionario de Datos

## Tabla: nyc_taxi_demand

A continuación se describen los campos originales utilizados para el análisis y modelado de demanda de taxis en NYC.

| Campo           | Tipo    | Descripción                                                        | Ejemplo            | Restricciones            |
|-----------------|---------|--------------------------------------------------------------------|--------------------|---------------------------|
| pickup_datetime | datetime| Fecha y hora de la recogida del taxi                               | 2024-01-15 14:00   | Not null                 |
| pickup_latitude | float   | Latitud de la ubicación de recogida                               | 40.752             | -90 a 90, Not null       |
| pickup_longitude| float   | Longitud de la ubicación de recogida                              | -73.973            | -180 a 180, Not null     |
| passenger_count | int     | Número de pasajeros                                                | 2                  | >=1                      |
| trip_distance   | float   | Distancia del viaje en millas                                     | 3.1                | >=0                      |
| fare_amount     | float   | Tarifa cobrada (USD)                                               | 12.50              | >=0                      |
| weather_temp    | float   | Temperatura en °C (enriquecida con API)                           | 18.5               | Opcional                 |
| weather_desc    | string  | Descripción del clima (nubes, lluvia, etc.)                       | "cloudy"           | Opcional                 |
| borough         | string  | Borough asignado por lat/long (Manhattan, Bronx…)                 | "Manhattan"        | Opcional                 |
| zone_id         | int     | Zona de taxi según TLC shape file                                  | 132                | >=0, Opcional            |
| demand_bucket   | int     | Número de viajes en zona/hora (label agregado para agregaciones) | 57                 | >=0                      |

---

## 📊 Variables derivadas (features)

Las siguientes variables se generan durante el procesamiento para alimentar al modelo.

| Feature         | Fórmula / Origen                          | Descripción                                                       |
|-----------------|--------------------------------------------|-------------------------------------------------------------------|
| hour            | `pickup_datetime.hour`                     | Hora del día (0–23)                                               |
| day_of_week     | `pickup_datetime.weekday()`                | Día de la semana (0=lunes, 6=domingo)                            |
| month           | `pickup_datetime.month`                    | Mes del año (1–12)                                                |
| is_weekend      | `day_of_week in {5,6}`                     | Indica si es fin de semana                                       |
| demand_count    | `count(pickups grouped by zone_id, hour)`  | Cantidad de viajes en la zona y hora (target)                    |
| temp_bucket     | `bucket(weather_temp)`                     | Rango de temperatura categorizado                                |
| rush_hour       | `1 si hour in [7-9, 16-19] else 0`         | Indica si es hora pico                                            |
| distance_log    | `log(trip_distance + 1)`                   | Transformación logarítmica para estabilizar valores              |
| fare_log        | `log(fare_amount + 1)`                     | Transformación logarítmica del precio                            |
| lat_bin         | `binning(pickup_latitude)`                 | Agrupación espacial por latitud                                  |
| lon_bin         | `binning(pickup_longitude)`                | Agrupación espacial por longitud                                 |
| weather_encoded | `one_hot(weather_desc)`                    | Clima convertido a variables dummy                                |

---

## 🧩 Variable objetivo (Target)
**`demand_count`**  
Número de viajes registrados en una zona y hora específica.  
Tipo: **regresión** (variable continua).

---
