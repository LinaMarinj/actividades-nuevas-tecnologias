import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Momento 2 - Actividad 1")

st.header("Creación de DataFrames en Pandas con Streamlit")
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


biblioteca = {
    "Titulo": [
        "orgullo y perjuicio",
        "orgullo y perjuicio",
        "orgullo y perjuicio",
        "orgullo y perjuicio",
    ],
    "Autor": ["juanita", "juanita", "juanita", "juanita"],
    "Año de publicación": ["1998", "1998", "1998", "1998"],
    "Genero": ["Romance", "Romance", "Romance", "Romance"],
}

df_bibioteca = pd.DataFrame(biblioteca)


st.subheader("DataFrame de libros")
st.write(
    """1. Crea un diccionario en tu script con al menos cuatro claves: "título", "autor", año de publicación" y "género". Para cada clave asigna una lista con datos de ejemplo sobre libros (por ejemplo, 3 o 4 libros distintos)."""
)
st.code(biblioteca)
st.dataframe(df_bibioteca)

lista_biblioteca = [
    {
        "Titulo": "orgullo y perjuicio",
        "Autor": "juanita",
        "Año de publicación": "1998",
        "Genero": "Romance",
    },
    {
        "Titulo": "orgullo y perjuicio",
        "Autor": "juanita",
        "Año de publicación": "1998",
        "Genero": "Romance",
    },
    {
        "Titulo": "orgullo y perjuicio",
        "Autor": "juanita",
        "Año de publicación": "1998",
        "Genero": "Romance",
    },
    {
        "Titulo": "orgullo y perjuicio",
        "Autor": "juanita",
        "Año de publicación": "1998",
        "Genero": "Romance",
    },
]

df_lista_biblioteca = pd.DataFrame(lista_biblioteca)


st.write("DataFrame de libros")
st.code(biblioteca)
st.dataframe(df_lista_biblioteca)


# listas de listas

productos = [
    ["Pantalón", 100.000, 15],
    ["Vestido", 55.000, 50],
    ["Zapatos", 120.00, 80],
    ["Camisa", 80.000, 30],
]

columnas = ["Producto", "Precio", "Cantidad en Stock"]
df_productos = pd.DataFrame(productos, columns=columnas)

st.dataframe(df_productos)
