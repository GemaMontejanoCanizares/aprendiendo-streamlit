
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
@st.cache  # Esta línea ayuda a cachear los datos para que la app sea más rápida
def load_data():
    data = pd.read_csv('Peliculas.csv')
    return data

data = load_data()

# Título de la aplicación
st.title('Gráfica de Películas por Año')

# Agrupar por año y contar películas
movies_per_year = data.groupby('Year').size()

# Crear gráfica
fig, ax = plt.subplots()
movies_per_year.plot(kind='bar', color='skyblue', ax=ax)
plt.xlabel('Año')
plt.ylabel('Número de Películas')
plt.title('Número de Películas por Año')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar gráfica en Streamlit
st.pyplot(fig)
