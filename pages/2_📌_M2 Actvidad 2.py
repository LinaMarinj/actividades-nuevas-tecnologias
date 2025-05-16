import pandas as pd
import streamlit as st
import io


# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Momento 2 - Actividad 2")

st.header("Estudiantes en Colombia")
st.markdown(
    """
En esta actividad, se trabajará con un archivo CSV que contiene información de 50 estudiantes en Colombia,
 incluyendo datos como su nombre, edad, ciudad, promedio académico y asistencia. 
"""
)

st.header("Objetivo de aprendizaje")

st.markdown(
    """
    El objetivo principal es desarrollar una aplicación interactiva con Streamlit que permita explorar 
    y visualizar fácilmente la informacion información del archivo CSV.

"""
)

st.markdown('<h2 style="color:#0063F7;">Solución</h2>', unsafe_allow_html=True)


st.title("🧑‍🎓 Bienvenido al explorador de Estudiantes")

st.subheader("¿Qué deseas hacer hoy con los registros?")

opcion = st.selectbox(
    "Elige una opción:",
    (
        "Ver primeras y últimas 5 filas",
        "Resumen del dataset .info() y .describe()",
        "Seleccionar columnas específicas",
        "Filtrar por promedio",
    ),
)


archivo = pd.read_csv("pages/static/dataset/estudiantes_colombia.csv")

# Opción 1
if opcion == "Ver primeras y últimas 5 filas":
    # primeras 5  filas

    st.subheader("▪️ Primeras 5 filas")
    st.dataframe(archivo.head())

    # ultimas  5 filas
    st.subheader("▪️ Últimas 5 filas")
    st.dataframe(archivo.tail())


# Opción 2
elif opcion == "Resumen del dataset .info() y .describe()":
    st.subheader("Resumen general del dataset")

    buffer = io.StringIO()
    archivo.info(buf=buffer)
    info = buffer.getvalue()
    st.text(info)

    st.subheader("Estadísticas descriptivas")
    st.write(archivo.describe())


# Opción 3
elif opcion == "Seleccionar columnas específicas":
    st.subheader("Que columnas quieres ver")
    columnas = st.multiselect(
        "Selecciona una o más columnas:",
        archivo.columns.tolist(),
        default=["id", "nombre", "edad", "ciudad", "promedio", "asistencia"],
    )
    st.dataframe(archivo[columnas])


# Opción 4
elif opcion == "Filtrar por promedio":
    st.title("Filtrar estudiantes por promedio")

    filtrar_promedio = st.slider(
        "Selecciona el promedio mínimo",
        min_value=0.0,
        max_value=5.0,
        value=3.0,
        step=0.1,
    )

    filtrados = archivo[archivo["promedio"] > filtrar_promedio]

    st.write(f"Estudiantes con promedio mayor a {filtrar_promedio}:")
    st.write(filtrados)
