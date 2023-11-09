from flask import Flask
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def plotly_chart():
    # Crear un DataFrame de pandas.
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

    # Convertir el DataFrame a HTML y almacenarlo en una variable.
    df_html = df.to_html()

    # Crear una figura con Plotly.
    fig = px.bar(df, x=df.index, y=['A', 'B', 'C'], barmode='group', title="Sample Bar Chart")

    # Convertir la figura a HTML y desactivar la inclusión de Plotly.js
    # ya que lo incluiremos por separado en el HTML final.
    fig_html = pio.to_html(fig, full_html=False, include_plotlyjs=False)

    # Construir la respuesta HTML final, incluyendo Plotly.js solo una vez.
    return f"""
    <html>
        <head>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
            {df_html} <!-- Coloca la tabla por encima de la gráfica -->
            <hr> <!-- Una línea horizontal como separador -->
            {fig_html} <!-- La gráfica de barras viene después de la tabla -->
        </body>
    </html>
    """

# Aquí iría el código para ejecutar con waitress si lo necesitas.
# Por ejemplo:
# from waitress import serve
# serve(app, host='0.0.0.0', port=8080)
