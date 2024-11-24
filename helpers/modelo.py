import numpy as np

def preparar_datos_lstm(data, target_col, lag=7):
    """
    Prepara los datos en formato de secuencias para LSTM.

    Args:
        data (pd.DataFrame): DataFrame con las características.
        target_col (str): Nombre de la columna objetivo.
        lag (int): Número de pasos rezagados (ventana deslizante).

    Returns:
        tuple: X (características), y (objetivo).
    """
    X, y = [], []
    for i in range(lag, len(data)):
        # Seleccionar ventana deslizante para las características
        X.append(data.iloc[i-lag:i].values)
        # Seleccionar solo la columna objetivo (target_col) para y
        y.append(data.iloc[i][target_col])
    return np.array(X), np.array(y)