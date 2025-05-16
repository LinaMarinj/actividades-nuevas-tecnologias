import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import random

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

st.markdown(
    """
    Desarrollar una aplicación de filtros dinámicos en Streamlit.
    Cada filtro debe ser configurable desde la barra lateral (st.sidebar) y aplicarse solo si el usuario lo activa.
"""
)


# Configurar Faker para Colombia
fake = Faker("es_CO")

# Establecer semilla para reproducibilidad
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# Crear datos
n = 50
data = {
    "id": range(1, n + 1),
    "nombre_completo": [fake.name() for _ in range(n)],
    "edad": np.random.randint(15, 76, n),
    "region": random.choices(
        ["Caribe", "Andina", "Pacífica", "Orinoquía", "Amazonía"],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n,
    ),
    "municipio": random.choices(
        [
            "Barranquilla",
            "Santa Marta",
            "Cartagena",  # Caribe
            "Bogotá",
            "Medellín",
            "Tunja",
            "Manizales",  # Andina
            "Cali",
            "Quibdó",
            "Buenaventura",  # Pacífica
            "Villavicencio",
            "Yopal",  # Orinoquía
            "Leticia",
            "Puerto Inírida",  # Amazonía
        ],
        k=n,
    ),
    "ingreso_mensual": np.random.randint(800000, 12000001, n),
    "ocupacion": random.choices(
        [
            "Estudiante",
            "Docente",
            "Comerciante",
            "Agricultor",
            "Ingeniero",
            "Médico",
            "Desempleado",
            "Pensionado",
            "Emprendedor",
            "Obrero",
        ],
        k=n,
    ),
    "tipo_vivienda": random.choices(["Propia", "Arrendada", "Familiar"], k=n),
    "fecha_nacimiento": [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    "acceso_internet": random.choices([True, False], weights=[0.7, 0.3], k=n),
}

# Crear DataFrame
df_nuevo = pd.DataFrame(data)

# Introducir algunos valores nulos
df_nuevo.loc[3:5, "ingreso_mensual"] = np.nan
df_nuevo.loc[15:17, "ocupacion"] = np.nan

# Convertir fecha_nacimiento a datetime
df_nuevo["fecha_nacimiento"] = pd.to_datetime(df_nuevo["fecha_nacimiento"])


st.markdown('<h4 style="color:#0063F7;">DataFrame</h4>', unsafe_allow_html=True)

st.sidebar.title("Filtros")
st.markdown(
    """
Bienvenido a los filtros 😊. Usa la barra de navegación que está a la izquierda de tu pantalla
para elegir el filtro que quieras aplicar  👈 
"""
)

st.dataframe(data)

st.markdown('<h4 style="color:#0063F7;">Filtros Aplicados</h4>', unsafe_allow_html=True)


# Filtro 1: por rango de edad
filtro_edad = st.sidebar.checkbox("Filtrar por rango de edad")

if filtro_edad:
    min_edad, max_edad = st.sidebar.slider(
        "Seleccione el rango de edad", min_value=15, max_value=75, value=(20, 40)
    )
    df = df_nuevo[df_nuevo["edad"].between(min_edad, max_edad)]
    st.markdown("**Filtro por rango de edad**")
    st.dataframe(df)


# Filtro 2: por municipios específicos

filtro_municipios = st.sidebar.checkbox("Filtrar por municipios específicos")

if filtro_municipios:
    municipios_seleccionados = st.sidebar.multiselect(
        "Seleccione los municipios:",
        options=[
            "Barranquilla",
            "Santa Marta",
            "Cartagena",
            "Bogotá",
            "Medellín",
            "Tunja",
            "Manizales",
            "Cali",
            "Quibdó",
            "Buenaventura",
            "Villavicencio",
            "Yopal",
            "Leticia",
            "Puerto Inírida",
        ],
    )

    if municipios_seleccionados:
        df = df_nuevo[df_nuevo["municipio"].isin(municipios_seleccionados)]
        st.markdown("**Filtro por municipios específicos**")
        st.dataframe(df)


# Filtro 3: por ingreso mensual mínimo

filtro_ingreso_minimo = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo")


# Filtro 4: por ocupación

filtro_ocupacion = st.sidebar.checkbox("Filtrar por ocupación")

if filtro_ocupacion:
    ocupacion_seleccionada = st.sidebar.multiselect(
        "Seleccione los municipios:",
        options=[
            "Estudiante",
            "Docente",
            "Comerciante",
            "Agricultor",
            "Ingeniero",
            "Médico",
            "Desempleado",
            "Pensionado",
            "Emprendedor",
            "Obrero",
        ],
    )

    if ocupacion_seleccionada:
        df = df_nuevo[df_nuevo["ocupacion"].isin(ocupacion_seleccionada)]
        st.markdown("**Filtro por ocupación**")
        st.dataframe(df)


# Filtro 5: por municipios específicos

filtro_vivienda_no_propia = st.sidebar.checkbox(
    " Filtrar por tipo de vivienda no propia"
)

# Filtro 6: por municipios específicos

filtro_nombres_cadena = st.sidebar.checkbox(
    "Filtrar por nombres que contienen una cadena"
)

# Filtro 7: por municipios específicos

filtro_ano_nacimiento = st.sidebar.checkbox("Filtrar por año de nacimiento específico")

# Filtro 8: por municipios específicos

filtro_acceso_internet = st.sidebar.checkbox("Filtrar por acceso a internet")

# Filtro 9: por municipios específicos

filtro_ingresos_nulos = st.sidebar.checkbox("Filtrar por ingresos nulos ")

# Filtro 10: por municipios específicos

filtro_rango_fechas = st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento")
