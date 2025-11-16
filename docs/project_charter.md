# 📘 Project Charter: TaxiVision NYC

## 1. Objetivo de Negocio
El proyecto busca optimizar la disponibilidad de taxis en la ciudad de Nueva York mediante la predicción anticipada de la demanda en diferentes zonas y horarios. El objetivo es reducir tiempos de espera, mejorar la eficiencia operativa y apoyar decisiones estratégicas de movilidad basadas en datos.

---

## 2. Objetivo de Data Science
**Pregunta técnica a responder:**  
¿Podemos predecir la demanda futura de taxis por zona y hora utilizando datos históricos y variables contextuales?

**Qué se va a predecir:**  
- La **cantidad estimada de solicitudes/demanda de taxis** en una ubicación (lat/long o zona) y una hora específica.

**Tipo de problema:**  
- Predicción numérica → **Modelo de regresión** (p. ej. Random Forest, LSTM).

---

## 3. Alcance

### ✔️ Incluye
- Recolección y procesamiento del dataset de NYC Taxi.  
- Análisis exploratorio de datos (EDA).  
- Construcción de un modelo predictivo de demanda.  
- Visualización geoespacial mediante mapas de calor.  
- Desarrollo de una aplicación en Streamlit para consulta interactiva.  
- Generación de dashboards con predicciones por zona y hora.  
- Documentación completa del proceso y despliegue local.

### ❌ No incluye (Out of Scope)
- Sistema de predicción en tiempo real.  
- Integración con plataformas externas (Uber, Lyft, NY Taxi API).  
- Sistema de alertas automáticas.  
- App móvil nativa.  
- Infraestructura cloud para producción.

---

## 4. Stakeholders
- **Product Owner:** Natalia Martínez  
- **Data Scientists:** Equipo TaxiVision (1–2 integrantes según evolución).  
- **Usuarios finales:**  
  - Conductores de taxis o flotillas.  
  - Empresas de movilidad urbana.  
  - Analistas de transporte y logística.  
  - Público general interesado en planificación de movilidad.

---

## 5. Métricas de Éxito

### ✔️ Métrica técnica (ML)
- Error de predicción (RMSE) dentro de rangos aceptables.  
- **R² ≥ 0.85** o equivalente para validar precisión del modelo.  
- Comparación con baseline que muestre mejora significativa.

### ✔️ Métrica de negocio
- Reducción estimada de tiempos de espera en zonas críticas.  
- Mejora proyectada de la eficiencia operativa en **≥ 20%**.  
- Identificación clara de hotspots que permitan redistribución efectiva.

---

## 6. Timeline
- **Inicio:** 15 de noviembre de 2025  
- **Entrega MVP:** 15 de diciembre de 2025  
- **Entrega final:** 15 de enero de 2026  

---

