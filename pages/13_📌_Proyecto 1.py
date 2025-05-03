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

st.markdown("**Datos suministrados por: Hospital General de Medellín**")
st.text(
    "Descripción de datos de las defunciones ocurridas en el Hospital General de Medellín que se publican de manera trimestral"
)
st.text("Última Actualización: 1 de abril de 2024")
