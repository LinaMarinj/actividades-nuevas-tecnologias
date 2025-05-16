import streamlit as st

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Momento 2 - Actividad 3")

st.header("Practica de filtrado con Pandas y filtros dinámicos en Streamlit")
st.markdown(
    """
    En esta actividad se aplicarán distintas técnicas de filtrado de datos con Pandas, tanto en **Google Colab** (plataforma gratuita en línea que permite escribir y ejecutar código Python directamente desde el navegador) 
    como en una aplicación interactiva con **Streamlit.** Se utilizarán operadores, funciones y métodos específicos para filtrar información relevante de un DataFrame.
"""
)

st.header("Objetivos de aprendizaje")

st.markdown(
    """
- Filtrado básico y avanzado de datos en Pandas.
- Uso de operadores y funciones para manipulación de DataFrames.
- Implementación de filtros interactivos en aplicaciones con Streamlit.
- Ejecución y visualización de código Python en Google Colab.
"""
)

st.markdown('<h2 style="color:#0063F7;">Solución</h2>', unsafe_allow_html=True)

st.subheader("Actividad 1: Practica de filtrado en Pandas-Google Colab")

st.markdown(
    "<p style='color:blue;'>Haz clic en el siguiente enlace o cópialo:</p>",
    unsafe_allow_html=True,
)
st.code(
    "https://colab.research.google.com/drive/17m49EDOf7mnTSlpjbRzWb6OTJwN87Way?usp=sharing",
    language="text",
)


st.subheader(
    "Actividad 2: Desarrollar una aplicación de filtros dinámicos en Streamlit"
)
