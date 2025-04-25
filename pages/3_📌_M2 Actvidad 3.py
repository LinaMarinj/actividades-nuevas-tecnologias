import streamlit as st

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Momento 2 - Actividad 3")

st.header("Filtrado de datos en Pandas con todas las formas y operadores")
st.markdown(
    """
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
"""
)

st.header("Objetivos de aprendizaje")

st.markdown(
    """
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
"""
)

st.header("Solución")

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
