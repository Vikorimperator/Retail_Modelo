import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def crear_heatmap_beneficio(df, index, columns, values, aggfunc="sum", cmap="Blues", titulo="Heatmap de Beneficio"):
    """
    Crea un heatmap para visualizar el beneficio agrupado por combinaciones de índices y columnas.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        index (str): Columna a usar como índice (ej. 'ciudad').
        columns (str): Columna a usar como columnas (ej. 'categoria').
        values (str): Columna cuyos valores se quieren analizar (ej. 'Beneficio').
        aggfunc (str): Función de agregación para los datos (por defecto: 'sum').
        cmap (str): Paleta de colores para el heatmap (por defecto: 'Blues').
        titulo (str): Título del gráfico.

    Returns:
        None: Muestra un heatmap utilizando Seaborn.
    """
    # Crear la tabla dinámica
    tabla_pivot = df.pivot_table(
        values=values, index=index, columns=columns, aggfunc=aggfunc, fill_value=0
    )
    
    # Configurar el gráfico
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        tabla_pivot, 
        annot=True, 
        fmt=".0f", 
        cmap=cmap, 
        linewidths=0.5
    )
    plt.title(titulo)
    plt.xlabel(columns.capitalize())
    plt.ylabel(index.capitalize())
    plt.show()


def graficar_distribucion(df, columna, titulo="Distribución de la Columna", bins=20, color="blue", alpha=0.7):
    """
    Grafica la distribución de una columna del DataFrame con un histograma y una curva de densidad (KDE).

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        columna (str): Nombre de la columna cuya distribución se desea graficar.
        titulo (str): Título del gráfico (por defecto: "Distribución de la Columna").
        bins (int): Número de bins para el histograma (por defecto: 20).
        color (str): Color de las barras del histograma (por defecto: "blue").
        alpha (float): Transparencia de las barras (por defecto: 0.7).

    Returns:
        None: Muestra el gráfico.
    """
    # Verificar que la columna exista en el DataFrame
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")
    
    # Configurar el gráfico
    plt.figure(figsize=(8, 6))
    sns.histplot(df[columna], bins=bins, kde=True, color=color, alpha=alpha)
    plt.title(titulo)
    plt.xlabel(f"{columna.capitalize()} ($)")
    plt.ylabel("Frecuencia")
    plt.show()


def visualizar_beneficios_interactivo(df, agrupador, titulo="Beneficios por Categoría"):
    """
    Visualiza los beneficios agrupados según la columna especificada con interactividad.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        agrupador (str): Columna por la que se desea agrupar los beneficios (ej. 'ciudad', 'categoria').
        titulo (str): Título de la gráfica.

    Returns:
        None: Muestra un gráfico interactivo de Plotly.
    """
    # Verificar que la columna exista en el DataFrame
    if agrupador not in df.columns:
        raise ValueError(f"La columna '{agrupador}' no existe en el DataFrame.")
    
    # Agrupar por la columna seleccionada y calcular la suma de beneficios
    beneficios_agrupados = df.groupby(agrupador)["Beneficio"].sum().reset_index()
    beneficios_agrupados = beneficios_agrupados.sort_values(by="Beneficio", ascending=False)
    
    # Crear el gráfico interactivo
    fig = px.bar(
        beneficios_agrupados,
        x=agrupador,
        y="Beneficio",
        color=agrupador,  # Asignar colores únicos a cada categoría
        title=titulo,
        labels={agrupador: agrupador.capitalize(), "Beneficio": "Beneficio ($)"},
        text="Beneficio",  # Mostrar el valor del beneficio en cada barra
        template="plotly_white",
    )
    
    # Personalizar la apariencia
    fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
    fig.update_layout(
        xaxis_title=agrupador.capitalize(),
        yaxis_title="Beneficio ($)",
        xaxis=dict(tickangle=45),  # Rotar etiquetas del eje x si es necesario
        height=600,  # Altura del gráfico
        showlegend=True,  # Mostrar leyenda para activar/desactivar categorías
    )
    
    # Mostrar el gráfico
    fig.show()
    
    
def graficar_tendencia_interactiva(df, fecha_columna, valor_columna, titulo="Tendencia en el Tiempo"):
    """
    Crea un gráfico de línea interactivo con Plotly para visualizar tendencias temporales,
    agrupando los datos por fecha.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        fecha_columna (str): Columna que contiene las fechas.
        valor_columna (str): Columna cuyos valores se desean graficar.
        titulo (str): Título del gráfico (por defecto: "Tendencia en el Tiempo").

    Returns:
        None: Muestra el gráfico interactivo de Plotly.
    """
    # Verificar que las columnas existan en el DataFrame
    if fecha_columna not in df.columns or valor_columna not in df.columns:
        raise ValueError(f"Las columnas '{fecha_columna}' o '{valor_columna}' no existen en el DataFrame.")
    
    # Asegurarse de que la columna de fechas esté en formato datetime
    df[fecha_columna] = pd.to_datetime(df[fecha_columna])
    
    # Agrupar los datos por fecha
    datos_agrupados = df.groupby(fecha_columna)[valor_columna].sum().reset_index()
    
    # Crear el gráfico interactivo
    fig = px.line(
        datos_agrupados,
        x=fecha_columna,
        y=valor_columna,
        title=titulo,
        labels={fecha_columna: "Fecha", valor_columna: valor_columna.capitalize()},
        template="plotly_white",
    )
    
    # Agregar un deslizador de rango en el eje X
    fig.update_xaxes(rangeslider_visible=True)
    
    # Mostrar el gráfico
    fig.show()