import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./data/reviews_google_count_MAL.csv')

st.dataframe(df)

# Agrupar por año y contar las reseñas por año
conteo_resenas = df.groupby('year')['rating'].count()
# Crear el gráfico de barras
fig, ax = plt.subplots()
conteo_resenas.plot(kind='bar', xlabel='Año', ylabel='Cantidad de Reseñas', title='Cantidad de Reseñas por Año', ax=ax)
# Mostrar el gráfico en Streamlit
st.pyplot(fig)

st.line_chart(conteo_resenas, xlabel='Año', ylabel='Cantidad de Reseñas', title='Cantidad de Reseñas por Año')