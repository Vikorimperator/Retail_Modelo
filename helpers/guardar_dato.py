import os


def guardar_dataframe(dataframe, base_dir, nombre_archivo):
    """
    Guarda un DataFrame en la carpeta 'data/procesados' en formato CSV.

    Args:
        dataframe (pd.DataFrame): El DataFrame limpio que deseas guardar.
        base_dir (str): La ruta base del proyecto.
        nombre_archivo (str): Nombre del archivo CSV a guardar, e.g., 'Base_Ventas_Procesada.csv'.

    Returns:
        str: Ruta completa donde se guardó el archivo.
    """
    # Definir la carpeta donde se guardará el archivo
    procesados_dir = os.path.join(base_dir, "data", "procesados")

    # Crear la carpeta si no existe
    os.makedirs(procesados_dir, exist_ok=True)

    # Ruta completa del archivo
    file_output = os.path.join(procesados_dir, nombre_archivo)

    # Guardar el DataFrame en formato CSV
    dataframe.to_csv(file_output, index=False)

    # Imprimir mensaje de éxito
    print(f"Archivo limpio guardado en: {file_output}")

    # Retornar la ruta completa del archivo
    return file_output
