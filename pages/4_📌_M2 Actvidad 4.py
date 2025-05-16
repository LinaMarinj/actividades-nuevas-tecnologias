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
Desarrollar una aplicación web interactiva utilizando Streamlit que permita a los usuarios explorar y manipular un DataFrame de Pandas,
haciendo uso intensivo de los métodos .loc y .iloc"""
)

st.header("Objetivos de aprendizaje")

st.markdown(
    """
- Manejo selecciones
- Uso de filtros y modificaciones de datos.
"""
)

st.markdown('<h2 style="color:#0063F7;">Solución</h2>', unsafe_allow_html=True)


st.markdown(
    """
<h1 style='font-size: 2.2em'>
🌏 Explora el mundo con y sin visa: Destinos para 
<span style='color:#FFD700;'>Col</span><span style='color:#0033A0;'>ombia</span><span style='color:#CE1126;'>nos</span> ✈️
</h1>
""",
    unsafe_allow_html=True,
)


df = pd.read_csv("pages/static/dataset/destinos_para_colombianos.csv")


opcion = st.selectbox(
    "Que destinos deseas ver:",
    (
        "Destinos que sí requieren visa",
        "Destinos que no requieren visa",
        "Destinos donde puedo quedarme hasta 90 días",
        "Destinos donde puedo quedarme hasta 180 días",
        "Todos los destinos",
        "Modifica un destino a visitar",
        "Primero 5 paises de la lista",
        "Top 3 paises más visitados",
    ),
)

if opcion == "Destinos que sí requieren visa":
    st.subheader("▪️  Destinos que sí requieren visa: ")
    si_visa = df.loc[df["Requiere Visa"] == "Sí", "País"]
    st.dataframe(si_visa)

if opcion == "Destinos que no requieren visa":
    st.subheader("▪️ Destinos que no requieren visa: ")
    no_visa = df.loc[df["Requiere Visa"] == "No Aplica", "País"]
    st.dataframe(no_visa)


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
    st.dataframe(edited_df)


if opcion == "Primero 5 paises de la lista":
    st.subheader("▪️Primero 5 paises de la lista: ")
    primeros_cinco = df.iloc[0:5]
    st.dataframe(primeros_cinco)

if opcion == "Top 3 paises más visitados":
    st.subheader("▪️Primero 5 paises de la lista ⭐:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("México")
        st.image("assets/mexico.jpg")
    with col2:
        st.subheader("Perú")
        st.image("assets/peru.jpg")
    with col3:
        st.subheader("Chile")
        st.image("assets/chile.jpg")

    df_mas_visitados = df.iloc[[17, 13, 7]]
    st.dataframe(df_mas_visitados)
    