import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Administración del Restaurante")

# Cargar los datos
try:
    df = pd.read_csv('../static/datasets/Restaurante.csv')
except FileNotFoundError:
    st.error("El archivo de datos no se encontró. Asegúrate de que el archivo esté en la ruta correcta.")
    st.stop()

# Convertir la columna 'Fecha' a datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')

# Obtener las opciones únicas de cada filtro
productosU = sorted(df['Producto'].unique())
fechasU = sorted(df['Fecha'].dt.date.unique())

# Configurar las columnas y selectores
col1, col2 = st.columns(2)

with col1:
    fechasU.insert(0, "Todas")
    optionFecha = st.selectbox('Fecha', (fechasU))

with col2:
    productosU.insert(0, "Todos")
    optionProducto = st.selectbox('Producto', (productosU))

# Filtrar los datos según las opciones seleccionadas
filtered_data = df
if optionFecha != "Todas":
    filtered_data = filtered_data[filtered_data['Fecha'].dt.date == optionFecha]

if optionProducto != "Todos":
    filtered_data = filtered_data[filtered_data['Producto'] == optionProducto]

# Crear un gráfico de barras para el total de ventas por producto
ventas_por_producto = filtered_data.groupby('Producto')['Total'].sum().reset_index()
fig_bar = px.bar(ventas_por_producto, x='Producto', y='Total', title='Total de Ventas por Producto')

# Crear un gráfico de líneas para la evolución de ventas en el tiempo
ventas_por_fecha = filtered_data.groupby('Fecha')['Total'].sum().reset_index()
fig_line = px.line(ventas_por_fecha, x='Fecha', y='Total', title='Evolución de Ventas a lo Largo del Tiempo')

# Mostrar los gráficos
st.plotly_chart(fig_bar, use_container_width=True)
st.plotly_chart(fig_line, use_container_width=True)

# Mostrar la tabla filtrada
st.write("Datos filtrados", filtered_data)
