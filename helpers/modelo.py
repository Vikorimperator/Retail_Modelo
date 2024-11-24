import numpy as np
import torch.nn as nn
import torch


def comprobar_dispositivo():
    """
    Comprueba si CUDA está disponible y configura el dispositivo para PyTorch.
    
    Returns:
        device (torch.device): Dispositivo configurado (CPU o GPU).
    """
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA está disponible. Los modelos pueden ser entrenados en GPU.")
        print("Cantidad de GPUs disponibles:", torch.cuda.device_count())
        print("Nombre de la GPU:", torch.cuda.get_device_name(0))
    else:
        device = torch.device("cpu")
        print("CUDA no está disponible. Los modelos serán entrenados en CPU.")
    return device



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


class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, device):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.device = device
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        # Inicializar h0 y c0 en el dispositivo correcto
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(self.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(self.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out
