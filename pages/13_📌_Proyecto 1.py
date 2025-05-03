import streamlit as st
import pandas as pd


# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Proyecto Grupal")


st.header("Solución")


st.subheader("🏥Defunciones ocurridas en en el Hospital General de Medellín")


df = pd.read_csv(
    "Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv"
)

st.markdown(
    """
### Introducción

Este proyecto tiene como objetivo explorar, analizar y visualizar los datos de defunciones ocurridas en el Hospital General de Medellín entre los años 2022 y 2023. 

La base de datos utilizada es de acceso gratuito y contiene información detallada sobre cada caso de fallecimiento, incluyendo variables como:

- Año de defunción
- Sitio y tipo de defunción
- Fecha, sexo y edad del fallecido
- Estado civil, nivel educativo y ocupación
- municipio de residencia
- Muerte y causas

A través del uso de Python, la librería **pandas** para el análisis de datos y **Streamlit** para la construcción de una interfaz interactiva, este proyecto busca ofrecer una herramienta sencilla pero poderosa para examinar datos.

Este análisis puede ser útil para investigadores y profesionales de la salud pública interesados en comprender mejor la dinámica de mortalidad en esta institución.

"""
)

st.markdown("**Datos suministrados por:**")
st.code(
    "https://www.datos.gov.co/Salud-y-Protecci-n-Social/Defunciones-ocurridas-en-en-el-Hospital-General-de/hwwv-mhse/about_data",
    language="text",
)

