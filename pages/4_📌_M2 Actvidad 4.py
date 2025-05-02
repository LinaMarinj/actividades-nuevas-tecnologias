import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Momento 2 - Actividad 4")

st.header(
    "Creación de una aplicación interactiva con Streamlit utilizando .loc y .iloc"
)
st.markdown(
    """
Desarrollar una aplicación web interactiva utilizando Streamlit que permita a los usuarios explorar y manipular un DataFrame de Pandas, haciendo uso intensivo de los métodos .loc y .iloc para realizar selecciones, filtros y modificaciones de datos. La temática y el diseño de la aplicación son libres, permitiendo expresar su creatividad.
"""
)

st.header("Objetivos de aprendizaje")

st.markdown(
    """
- Comprender los métodos .loc y .iloc para realizar selecciones.
- Aprender a utilizar los métodos .loc y .iloc.
- Aplicar estos conocimientos en una actividad práctica
"""
)

st.header("Solución")


st.markdown(
    """
<h1 style='font-size: 2.2em'>
🌏 Explora el mundo con y sin visa: Destinos para 
<span style='color:#FFD700;'>Col</span><span style='color:#0033A0;'>ombia</span><span style='color:#CE1126;'>nos</span> ✈️
</h1>
""",
    unsafe_allow_html=True,
)


df = pd.read_csv("destinos_para_colombianos.csv")


opcion = st.selectbox(
    "Que destinos deseas ver:",
    (
        "Destinos que sí requieren visa",
        "Destinos que no requieren visa",
        "Destinos donde puedo quedarme hasta 30 días",
        "Destinos donde puedo quedarme hasta 90 días",
        "Destinos donde puedo quedarme hasta 180 días",
        "Todos los destinos",
        "Modifica un destino a visitar",
    ),
)

if opcion == "Destinos que sí requieren visa":
    st.subheader("▪️ Destinos que sí requieren visa: ")
    si_visa = df.loc[df["Requiere Visa"] == "Sí", "País"]
    st.dataframe(si_visa)

if opcion == "Destinos que no requieren visa":
    st.subheader("▪️ Destinos que no requieren visa: ")
    no_visa = df.loc[df["Requiere Visa"] == "No Aplica", "País"]
    st.dataframe(no_visa)


if opcion == "Destinos donde puedo quedarme hasta 30 días":
    st.subheader("▪️Destinos donde puedo quedarme hasta 30 días: ")
    dias_treinta = df.loc[df["Días Máximos de Estadía"] == "30 días"]
    st.dataframe(dias_treinta)


if opcion == "Destinos donde puedo quedarme hasta 90 días":
    st.subheader("▪️Destinos donde puedo quedarme hasta 90 días: ")
    dias_noventa = df.loc[df["Días Máximos de Estadía"] == "90 días"]
    st.dataframe(dias_noventa)

if opcion == "Destinos donde puedo quedarme hasta 180 días":
    st.subheader("▪️Destinos donde puedo quedarme hasta 180 días: ")
    dias_maximos = df.loc[df["Días Máximos de Estadía"] == "180 días"]
    st.dataframe(dias_maximos)


if opcion == "Todos los destinos":
    st.subheader("▪️ Todos los destinos: ")
    todos_los_destinos = df.iloc[0:40]
    st.dataframe(todos_los_destinos)

if opcion == "Modifica un destino a visitar":
    edited_df = st.data_editor(df, use_container_width=True)
