import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('.\\vehicles_us.csv')  # leer los datos

st.header('Análisis de datos de anuncios de venta de coches')  # título
build_histogram = st.checkbox(
    'Construir un histograma')  # casilla de verificación
# casilla de verificación
build_disp = st.checkbox('Construir un grafico de dispersión')

if build_disp:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    # título del gráfico
    st.title('Gráfico de dispersión de odómetro y precio')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    st.title('Histograma de odómetro de coches')  # título del gráfico
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
