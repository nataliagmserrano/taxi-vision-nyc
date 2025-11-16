# 🚖 TaxiVision NYC — Predicción Inteligente de Demanda de Taxis

**Predicción de demanda de taxis en Nueva York mediante Machine Learning, visualización geoespacial y enfoque Design Thinking.**  
Un proyecto que une datos reales, UX y analítica avanzada para mejorar la eficiencia en la movilidad urbana.

---

## 🏷️ Badges
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ❗ 1. Problema que resuelve

La ciudad de Nueva York enfrenta constantes fluctuaciones en la demanda de taxis, generando:
- 🚕 **Disponibilidad irregular**: taxis saturados en horas pico y zonas sin cobertura.  
- ⏳ **Largos tiempos de espera** para usuarios en zonas de alta demanda.  
- 💸 **Pérdidas económicas para conductores** por posicionamiento ineficiente.  
- 📉 **Toma de decisiones sin datos** por parte de operadores de movilidad.  

El impacto afecta a miles de usuarios, conductores y empresas de transporte.  
Resolverlo permite **optimizar recursos, mejorar la experiencia de viaje y reducir congestión urbana**.

---

## 💡 2. Solución propuesta

TaxiVision es una **aplicación interactiva con modelos Predictivos** que:
- Estima la **demanda futura de taxis por zona y hora** usando Machine Learning.  
- Muestra la información en un **dashboard geoespacial** intuitivo (calor, mapas interactivos).  
- Permite analizar tendencias, horarios críticos y patrones de movilidad.  
- Implementa un proceso basado en **Design Thinking** para garantizar utilidad real.  

**Tecnologías usadas:**  
LSTM / Random Forest / regresión, Pandas, Numpy, Folium, Streamlit, análisis temporal, mapas interactivos, Heatmaps.

**Outputs generados:**
- Predicción de demanda por cuadrante/lat-long.  
- Visualizaciones interactivas.  
- Mapas de calor históricos y futuros.  
- Insights accionables para toma de decisiones.

---

## ⭐ 3. Características principales (Features)

- 🔮 **Predicción de demanda de taxis por hora** (modelo ML).  
- 🗺️ **Mapas de calor interactivos** con Folium + datos reales de NYC.  
- 📊 **Dashboard web en Streamlit** con visualizaciones dinámicas.  
- 📈 **Análisis de tendencias históricas** y patrones temporales.  
- ⚠️ **Identificación de zonas críticas** de alta o baja demanda.  
- 🧠 **Pipeline de datos completo**: limpieza → modelo → predicción → visualización.  
- 📱 **Interfaz simple basada en principios de Design Thinking**.  

---

## 🛠️ 4. Tecnologías utilizadas (Tech Stack)

### **Backend & Data Processing**
- Python 3.9+  
- Pandas, NumPy  
- PySpark (opcional para big data)

### **Machine Learning**
- Scikit-learn  
- TensorFlow/Keras (opcional LSTM)  
- XGBoost  
- Joblib (para exportar modelos)

### **Visualización**
- Folium  
- Streamlit  
- Matplotlib / Plotly

### **APIs y Datos**
- NYC Taxi Dataset  
- OpenWeather API (opcional para enriquecer predicción)

### **DevOps**
- Git & GitHub  
- Docker (futuro)

---

## 📂 5. Estructura del proyecto

```
📦 taxi-vision-nyc
│
├── 📁 data/                  # Datos crudos y procesados
│   ├── raw/
│   └── processed/
│
├── 📁 notebooks/             # Exploración y prototipos (EDA, pruebas ML)
│
├── 📁 src/
│   ├── data_prep.py         # Limpieza y preparación de datos
│   ├── train_model.py       # Entrenamiento del modelo
│   ├── predict.py           # Script de predicción
│   ├── utils.py             # Funciones auxiliares
│   └── config.py            # Gestión de parámetros/paths
│
├── 📁 app/
│   └── streamlit_app.py     # Aplicación web
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

## 🚀 6. Instalación y uso
🔧 **Prerequisitos**
- Python 3.9+
- pip
- Git

📥 **a. Clonar el repositorio**
```bash
git clone https://github.com/tu_usuario/taxi-vision-nyc.git
cd taxi-vision-nyc
```
🧪 **b. Crear entorno virtual**
```bash
python -m venv venv
source venv/Scripts/activate      # Windows
```
📦 **c. Instalar dependencias**
```bash
pip install -r requirements.txt
```
🔐 **d. Configurar variables de entorno**
```bash
cp .env.example .env
**Editar .env con tu API_KEY de OpenWeather u otras credenciales**
```
▶️ **e. Ejecutar el proyecto**
```bash
streamlit run app/streamlit_app.py
```
🧰 **Uso básico (ejemplo)**
```bash
from src.predict import predict_demand
pred = predict_demand(latitude=40.75, longitude=-73.98, hour=15)
print(pred)
```

## 📊 7. Resultados (Métricas y visuales)
Incluye:
- Capturas del dashboard Streamlit.
- Mapas de calor históricos y futuros.

## 🗺️ 8. Roadmap
**- Versión actual (v1.0)**
       ```
        - Modelo inicial de predicción (Random Forest / LSTM).
        - Dashboard Streamlit funcional.
        - Mapas de calor con Folium.
        - Pipeline completo de datos.
        ```
**- Próximas versiones**
        ```
        - Predicción en tiempo real vía API REST.
        - Integración con OpenWeather para mejorar la precisión.
        - Implementación de auto-ML.
        - Dockerización completa.
        - App móvil.
        - Soporte multi-idioma.
        ```

## 🤝 9. Contribución

¡Las contribuciones son bienvenidas!

Para contribuir:
**a. Hacer fork del proyecto**
**b. Crear una rama:**
        ```
        git checkout -b feature/NuevaCaracteristica
        ```
**c. Hacer commit:**
        ```
        git commit -m "Add: nueva característica"
        ```
**d. Subir cambios:**
        ```
        git push origin feature/NuevaCaracteristica
        ```
**e. Abrir un Pull Request**


## 👥 10. Equipo y contacto
**Desarrollado por:** Natalia Martínez

**📧 Contacto:** email@gmail.com

**📄 Licencia:** Este proyecto está bajo la licencia MIT.

