# 🧠 Model Card: Predictor de Demanda v1.0

## 1. Descripción del modelo
- **Algoritmo:** Random Forest Regressor  
- **Framework:** Scikit-learn  
- **Fecha de entrenamiento:** 15/nov/2025  

Este modelo estima la **demanda esperada de taxis por zona y hora** en la ciudad de Nueva York, utilizando patrones históricos y variables contextuales.

---

## 2. Datos de entrenamiento
- **Registros:** 300,000 viajes procesados (muestra considerada)  
- **Periodo analizado:** 2015  
- **Número de features:** 18 variables (ver `data_dictionary.md`, sección “Variables derivadas”)  

Las fuentes incluyen:
- NYC Taxi Trips Dataset (TLC)
- Datos climáticos (OpenWeather API)
- Enriquecimiento geoespacial (boroughs y zonas)

---

## 3. Performance del modelo
Evaluado sobre un conjunto de test equivalente al 20% de los datos:

- **RMSE (Test):** 6.029  
- **MAE (Test):** 3.271 

Estos valores indican un buen desempeño para escenarios operativos de redistribución de taxis y estimación de demanda por hora.

---

## 4. Limitaciones conocidas
- El modelo disminuye su precisión en **eventos atípicos** como tormentas fuertes o feriados grandes (New Year’s Eve, maratón de NYC).  
- La precisión baja en **zonas con escasos registros** (baja densidad).  
- No considera factores externos como tráfico en tiempo real o incidentes urbanos.  
- No está optimizado para **predicción minuto a minuto** (funciona por hora).  
- Requiere al menos **6–12 meses de historial** para que una zona tenga buen desempeño.  

---

## 5. Uso recomendado
- Predicción **por hora** de demanda de taxis a nivel de zona.  
- Redistribución operativa para flotas y movilidad urbana.  
- Priorización de zonas de alta demanda con fines logísticos.  
- Visualización en dashboards interactivos basados en mapas.  
- Escenarios donde se necesita entender patrones históricos y estacionales.

> No recomendado para predicciones en tiempo real sin un pipeline adicional (streaming + actualización continua).

---
