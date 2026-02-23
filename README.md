# 📊 Dropshipping Data Analyzer

## 📝 Descripción del Proyecto
Este proyecto es un motor de análisis de datos construido en Python. Su objetivo es procesar métricas comerciales de productos (como costos, volumen de ventas y gasto publicitario) para identificar automáticamente "Productos Ganadores" en el modelo de dropshipping, eliminando la toma de decisiones basada en la intuición.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías:** Pandas (Manipulación y análisis de datos), Random (Generación de datos sintéticos).
* **Control de Versiones:** Git y GitHub.
* **Arquitectura:** Estructura modular separando extracción de datos (`main.py`) y lógica de negocio (`src/processing.py`).

## ⚙️ Cómo ejecutar el proyecto
1. Clona este repositorio en tu máquina local.
2. Crea y activa un entorno virtual (`python -m venv venv`).
3. Instala las dependencias necesarias: `pip install pandas`.
4. Ejecuta el script principal: `python main.py`.

## 📈 Lógica del "Score Ganador"
El algoritmo evalúa cada producto basándose en 4 pilares matemáticos:
1. **Volumen de Ventas (40%):** Demanda actual del mercado.
2. **ROAS Estimado (30%):** Retorno de Inversión Publicitaria.
3. **Calificación del Cliente (20%):** Calidad percibida.
4. **Tendencia de Búsqueda (10%):** Interés a lo largo del tiempo

## 📁 Estructura del Proyecto
```text
dropshipping_data_analyzer/
├── data/
│   └── productos_analizados.csv  # Resultados procesados
├── src/
│   └── processing.py             # Motor lógico y matemático
├── main.py                       # Script principal de ejecución
├── .gitignore                    # Archivos excluidos de control de versiones
└── README.md                     # Documentación del proyecto
