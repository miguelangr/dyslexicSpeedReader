import plotly.express as px

# Definir los datos, incluyendo nombres, padres, y valores
data = {
    'names': [
        "Padre", 
        "Hijo1 High", "Hijo2 High", "Hijo3 High", 
        "Hijo4 Medium", "Hijo5 Medium", "Hijo6 Medium", 
        "Hijo7 Low", "Hijo8 Low", "Hijo9 Low"
    ],
    'parents': [
        "", 
        "Padre", "Padre", "Padre",
        "Padre", "Padre", "Padre",
        "Padre", "Padre", "Padre"
    ],
    'values': [100] + [10]*9,  # Valor del padre y luego los valores de los hijos
    # Colores en formato HEX representando High, Medium, Low intensities para amarillo, rojo, verde
    'colors': [
        "#000000",  # Padre
        "#FFD700", "#FF4500", "#32CD32",  # High Intensity
        "#FFDAA5", "#FFA07A", "#90EE90",  # Medium Intensity
        "#FFFFE0", "#F08080", "#8FBC8F"   # Low Intensity
    ]
}

# Crear el gráfico Sunburst
fig = px.sunburst(
    data_frame=data,
    names='names',
    parents='parents',
    values='values',
    color='colors',
    color_discrete_sequence=data['colors'],  # Usar los colores proporcionados
)

# Mostrar el gráfico
fig.show()
