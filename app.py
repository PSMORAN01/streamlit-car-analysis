import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('https://github.com/PSMORAN01/streamlit-car-analysis/vehicles_us.csv') # leer los datos

# Título de la aplicación
st.title('Informe de Vehículos')

# Subtítulo
nombre = st.text_input('Ingresa tu nombre')

# Mostrar mensaje de bienvenida cuando el usuario ingrese su nombre
if nombre:
    st.write(f'Bienvenido {nombre}, aquí podrás visualizar un breve resumen sobre los vehículos en este año')

# Botón para mostrar/ocultar gráfico de vehículos por modelo
if 'show_model' not in st.session_state:
    st.session_state.show_model = False

if st.button('Mostrar/Ocultar Cantidad de Vehículos por Modelo'):
    st.session_state.show_model = not st.session_state.show_model

if st.session_state.show_model:
    fig1 = px.bar(car_data, x="model", title="Cantidad de Vehículos por Modelo", labels={"model": "Modelo", "count": "Cantidad de Vehículos"}, color="model")
    st.plotly_chart(fig1)

# Botón para mostrar/ocultar gráfico de relación entre precio y kilometraje
if 'show_price_mileage' not in st.session_state:
    st.session_state.show_price_mileage = False

if st.button('Mostrar/Ocultar Relación entre Precio y Kilometraje'):
    st.session_state.show_price_mileage = not st.session_state.show_price_mileage

if st.session_state.show_price_mileage:
    fig2 = px.scatter(car_data, x="odometer", y="price", color="fuel", title="Relación entre Precio y Kilometraje", labels={"odometer": "Kilometraje", "price": "Precio"})
    st.plotly_chart(fig2)

# Botón para mostrar/ocultar gráfico de kilometraje y año del vehículo
if 'show_mileage_year' not in st.session_state:
    st.session_state.show_mileage_year = False

if st.button('Mostrar/Ocultar Relación entre Kilometraje y Año del Vehículo'):
    st.session_state.show_mileage_year = not st.session_state.show_mileage_year

if st.session_state.show_mileage_year:
    fig3 = px.scatter(car_data, x="model_year", y="odometer", color="fuel", title="Relación entre Kilometraje y Año del Vehículo", labels={"model_year": "Año del Vehículo", "odometer": "Kilometraje"})
    st.plotly_chart(fig3)
