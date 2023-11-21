
from flask import Flask, render_template
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

    # Convertir el DataFrame a HTML.
    df_html = df.to_html()

    # Crear una figura con Plotly.
    fig = px.bar(df, x=df.index, y=['A', 'B', 'C'], barmode='group', title="Sample Bar Chart")

    # Convertir la figura a HTML y desactivar la inclusión de Plotly.js
    fig_html = pio.to_html(fig, full_html=False, include_plotlyjs=False)

    # Render the template with DataFrame and Plotly chart HTML
    return render_template('index.html', df_html=df_html, fig_html=fig_html)

# Aquí iría el código para ejecutar con waitress si lo necesitas.
# from waitress import serve
# serve(app, host='0.0.0.0', port=8080)
