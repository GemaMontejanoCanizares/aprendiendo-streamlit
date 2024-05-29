import streamlit as st
import pandas as pd

# Cargar datos
@st.cache  # Esta línea ayuda a cachear los datos para que la app sea más rápida
def load_data():
    data = pd.read_csv('./devcontainer/Peliculas.csv')
    return data

data = load_data()

# Título de la aplicación
st.title('Gráfica de Películas por Año')

# Agrupar por año y contar películas
movies_per_year = data['Year'].value_counts().sort_index()

# Crear gráfica usando Streamlit
st.bar_chart(movies_per_year)
