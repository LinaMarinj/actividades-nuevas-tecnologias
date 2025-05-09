import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_icon="📌", layout="wide")

st.title("Momento 2 - Actividad 1")

st.header("Creación de DataFrames en Pandas con Streamlit")
st.markdown(
    """
Esta actividad consiste en construir una aplicación web básica con Streamlit que permita visualizar distintos DataFrames creados con la biblioteca Pandas.
Se trabajan diversas fuentes de datos, como diccionarios, listas, etc; 
con el objetivo de familiarizarse con la manipulación y visualización de datos en entornos interactivos.
"""
)

st.header("Objetivos de aprendizaje")

st.markdown(
    """
- Familiarizarse con la creación de DataFrames en Pandas y mostrarlos usando Streamlit.
"""
)

st.markdown('<h1 style="color:#0063F7;">Solución</h1>', unsafe_allow_html=True)

st.subheader("**1. Diccionario:**")

st.write(
    """Crea un diccionario en tu script con al menos cuatro claves: título, autor, año de publicación y género.
    Para cada clave, asigna una lista con datos de ejemplo sobre libros (por ejemplo, 3 o 4 libros distintos)."""
)

# 1. Diccionario
biblioteca = {
    "Titulo": [
        "Orgullo y prejuicio",
        "El Señor de los Anillos",
        "Harry Potter",
        " Bajo la misma estrella",
    ],
    "Autor": ["Jane Austen", "	J. R. R. Tolkien", "J. K. Rowling", "John Green"],
    "Año de publicación": ["1813", "1954", "1997", "2012"],
    "Genero": [
        "Novela romántica / Clásico",
        "Fantasía épica",
        "Fantasía / Aventura",
        "	Novela juvenil / Drama romántico",
    ],
}
st.subheader("DataFrame de libros")
df_bibioteca = pd.DataFrame(biblioteca)
st.dataframe(df_bibioteca)


if st.button("Ver código #1"):
    mostrar_codigo_uno = """biblioteca = {
    "Titulo": [
        "Orgullo y prejuicio",
        "El Señor de los Anillos",
        "Harry Potter",
        " Bajo la misma estrella",
    ],
    "Autor": ["Jane Austen", "	J. R. R. Tolkien", "J. K. Rowling", "John Green"],
    "Año de publicación": ["1813", "1954", "1997", "2012"],
    "Genero": [
        "Novela romántica / Clásico",
        "Fantasía épica",
        "Fantasía / Aventura",
        "Novela juvenil / Drama romántico",
    ],
}
df_bibioteca = pd.DataFrame(biblioteca)
st.dataframe(df_bibioteca)
"""

    st.code(mostrar_codigo_uno, language="python")


# 2. Lista de diccionarios

lista_ciudades = [
    {
        "nombre": "Medellín",
        "Población": "2,500,000",
        "País": "Colombia",
    },
    {
        "nombre": "Bogotá",
        "Población": "8,000,000 ",
        "País": "Colombia",
    },
    {
        "nombre": "Nueva York",
        "Población": "8,500,000",
        "País": "Estados Unidos",
    },
    {
        "nombre": "Los Ángeles ",
        "Población": "4,000,000",
        "País": "Estados Unidos",
    },
]

df_lista_ciudades = pd.DataFrame(lista_ciudades)
st.subheader("**2. Lista de diccionarios:**")

st.write(
    """**Una lista de diccionarios es como una colección de filas, donde cada diccionario representa una fila con sus columnas etiquetadas.**
    Crea una lista que contenga varios diccionarios (por ejemplo, 3 o 4). Cada diccionario debe tener las claves "nombre", "población" y "país", 
    con valores correspondientes a ciudades diferentes."""
)

st.subheader("Información de Ciudades")
st.dataframe(df_lista_ciudades)


if st.button("Ver código #2"):
    mostrar_codigo_dos = """lista_ciudades = [
    {
        "nombre": "Medellín",
        "Población": "2,500,000",
        "País": "Colombia",
    },
    {
        "nombre": "Bogotá",
        "Población": "8,000,000 ",
        "País": "Colombia",
    },
    {
        "nombre": "Nueva York",
        "Población": "8,500,000",
        "País": "Estados Unidos",
    },
    {
        "nombre": "Los Ángeles ",
        "Población": "4,000,000",
        "País": "Estados Unidos",
    },
]
df_lista_ciudades = pd.DataFrame(lista_ciudades)
st.dataframe(df_lista_ciudades)
"""
    st.code(mostrar_codigo_dos, language="python")


# 3. listas de listas

productos = [
    ["Pantalónes", "$100.000", 15],
    ["Vestidos", "$80.000", 50],
    ["Zapatos", "$150.000", 80],
    ["Camisas", "$50.000", 30],
]

columnas = ["Producto", "Precio", "Cantidad en Stock"]
df_productos = pd.DataFrame(productos, columns=columnas)


st.subheader("**3. Lista de listas:**")

st.write(
    """**Una lista de listas representa datos en forma de tabla, donde cada sublista es una fila, pero necesitas definir los nombres de las columnas por separado.**
    Crea una lista que contenga sublistas (por ejemplo, 3 o 4 filas). Cada sublista debe tener tres elementos: nombre del producto, precio y cantidad en stock
    (usa datos inventados)."""
)

st.subheader("Productos en Inventario")
st.dataframe(df_productos)

if st.button("Ver código #3"):
    mostrar_codigo_tres = """productos = [
    ["Pantalónes", "$100.000", 15],
    ["Vestidos", "$80.000", 50],
    ["Zapatos", "$150.000", 80],
    ["Camisas", "$50.000", 30],
]

columnas = ["Producto", "Precio", "Cantidad en Stock"]
]
df_productos = pd.DataFrame(productos, columns=columnas)
st.dataframe(df_productos)
"""
    st.code(mostrar_codigo_tres, language="python")


# 4. series

st.subheader("**4. Series:**")

st.write(
    """**Las Series son como columnas individuales en Pandas, y puedes combinarlas para formar un DataFrame.**
   Crea tres Series separadas: una con nombres de personas, otra con sus edades y otra con sus ciudades 
   (asegúrate de que tengan la misma cantidad de elementos, por ejemplo, 4 personas)."""
)

nombres = pd.Series(
    [
        "Lucas",
        "Mario",
        "Sara",
        "Carolina",
        "John",
    ]
)
edades = pd.Series([18, 20, 23, 30, 40])
ciudades = pd.Series(["Medellín", "Bogotá", "Cali", "Armenia", "Manizales"])


series_combinadas = {
    "Nombres": nombres,
    "edades": edades,
    "ciudades": ciudades,
}
df_datos_personas = pd.DataFrame(series_combinadas)
st.subheader("Datos de Personas")
st.dataframe(df_datos_personas)


if st.button("Ver código #4"):
    mostrar_codigo_series = """nombres = pd.Series(
    [
        "Lucas",
        "Mario",
        "Sara",
        "Carolina",
        "John",
    ]
)
edades = pd.Series([18, 20, 23, 30, 40])
ciudades = pd.Series(["Medellín", "Bogotá", "Cali", "Armenia", "Manizales"])


series_combinadas = {
    "Nombres": nombres,
    "edades": edades,
    "ciudades": ciudades,
}
df_datos_personas = pd.DataFrame(series_combinadas)
st.dataframe(df_datos_personas)"""
    st.code(mostrar_codigo_series, language="python")


# 5. 
