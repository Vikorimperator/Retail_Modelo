import os
import pandas as pd


def cargar_datos_excel(base_dir, file_name="Prueba_Python.xlsx", sheets=None):
    """
    Carga las hojas de un archivo Excel en DataFrames de pandas.

    Args:
        base_dir (str): Directorio base donde se encuentra el archivo.
        file_name (str): Nombre del archivo Excel (por defecto: "Prueba_Python.xlsx").
        sheets (list): Lista de nombres de hojas a cargar. Si es None, carga todas las hojas.

    Returns:
        dict: Diccionario donde las claves son los nombres de las hojas y los valores son DataFrames.
    """
    # Construir la ruta completa al archivo
    file_path = os.path.join(base_dir, "data", "raw", file_name)

    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo no se encuentra en: {file_path}")

    # Cargar las hojas especificadas o todas si sheets es None
    try:
        if sheets:
            # Cargar solo las hojas indicadas
            data = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheets}
        else:
            # Cargar todas las hojas
            data = pd.read_excel(file_path, sheet_name=None)
        return data
    except Exception as e:
        raise ValueError(f"Error al cargar el archivo Excel: {e}")