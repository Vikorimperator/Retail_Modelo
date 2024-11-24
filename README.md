# MODELO
## Descripción del proyecto
Este proyecto tiene como objetivo desarrollar un flujo de trabajo para la extracción, visualización y modelado de datos, utilizando un enfoque modular y organizado. La estructura del proyecto está diseñada para ser clara y extensible, facilitando la colaboración y la comprensión del código.

## Estructura del proyecto
La organización del proyecto es la siguiente:
```bash
MODELO/
│
├── .venv/                        # Entorno virtual del proyecto
├── data/                         # Carpeta que contiene los datos
│   ├── procesados/               # Datos procesados
│   └── raw/                      # Datos crudos
│
├── helpers/                      # Funciones auxiliares
│   ├── __init__.py               # Archivo de inicialización del módulo
│   ├── guardar_dato.py           # Función para guardar datos
│   ├── importar_data.py          # Función para importar datos
│   ├── modelo.py                 # Funciones relacionadas con el modelo
│   └── visualizaciones.py        # Funciones para visualización de datos
│
├── models/                       # Modelos entrenados y sus configuraciones
│
├── 1.extraccion.ipynb                # Extracción y preparación de datos
├── 2.visualizacion_beneficios.ipynb  # Visualización de datos y análisis de beneficios
├── 3.modelo_ML.ipynb                 # Creación y evaluación de modelos de ML
│
├── requirements.txt              # Dependencias del proyecto
└── .gitignore                    # Archivos y carpetas ignorados por Git
```
## Uso
Coloca tus datos crudos en la carpeta data/raw.

Utiliza los notebooks para extraer, procesar y modelar los datos:
 * 1.extraccion.ipynb: Procesa y limpia los datos crudos.
 * 2.visualizacion_beneficios.ipynb: Genera visualizaciones y análisis exploratorios.
 * 3.modelo_ML.ipynb: Entrena y evalúa modelos de Machine Learning.

Los resultados procesados se guardarán en la carpeta data/procesados.
