import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_aproximadas_colombia.csv')
st.set_page_config(
    page_title="Dashboard Ventas de Regalos", #Título de la página
    page_icon="📊", # Ícono
    layout="wide", # Forma de layout ancho o compacto
    initial_sidebar_state="expanded" # Definimos si el sidebar aparece expandido o colapsado
)
 # Agrupar datos
ventas_por_producto = df.groupby("Producto")["Ventas (unidades)"].sum()
ventas_por_temporada = df.groupby("Temporada")["Ventas (unidades)"].sum()
ventas_totales = df["Ventas (unidades)"].sum()

st.title("Tablero de Analisis de Ventas de Regalos")

with st.container():
 # Dividir pantalla en dos columnas
  col1, col2, col3 = st.columns(3)
  with col1:
    st.metric("Total de Ventas (unidades)", ventas_totales)
  with col2:
    st.write("### Ventas por Producto")
    st.bar_chart(ventas_por_producto)
  with col3:
   st.write("### Ventas por Temporada")
   fig, ax = plt.subplots()
   ax.pie(
    ventas_por_temporada, 
    labels=ventas_por_temporada.index, 
    autopct="%1.1f%%", 
    startangle=90, 
    colors=plt.cm.Set3.colors
   )
   ax.set_title("Distribución de Ventas por Temporada")
   st.pyplot(fig)
with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.write("### Ranking de Productos Más Vendidos")
        productos_mas_vendidos = ventas_por_producto.sort_values(ascending=True)
        fig, ax = plt.subplots()
        productos_mas_vendidos.plot(kind="barh", ax=ax, color="orange")
        ax.set_title("Ranking de Productos Más Vendidos")
        st.pyplot(fig)
    with col5:
        #st.write("### Datos Resumidos")
        #st.dataframe(df.head(10))
        comparacion = df.pivot_table(
            index="Producto", 
            columns="Temporada", 
            values="Ventas (unidades)", 
            aggfunc="sum"
        )
        st.write("### Ventas por Producto y Temporada")
        fig, ax = plt.subplots(figsize=(10, 6))
        comparacion.plot(kind="bar", stacked=True, ax=ax)
        ax.set_title("Ventas por Producto y Temporada")
        ax.set_xlabel("Producto")
        ax.set_ylabel("Ventas (unidades)")
        ax.legend(title="Temporada")
        st.pyplot(fig)
    with col6:
       st.write("### Análisis de Ventas de Regalos Personalizados")
       st.text("Este tablero presenta un análisis detallado de las ventas de regalos personalizados a lo largo de diferentes temporadas. "
            "Se ha segmentado la información por productos, temporadas y rankings de los productos más vendidos. "
            "Los gráficos permiten visualizar las tendencias de ventas, comparaciones entre productos y una distribución de las ventas por temporada, "
            "permitiendo así una comprensión más profunda del comportamiento del mercado y la estacionalidad en las compras.")
       st.write("Este análisis es clave para tomar decisiones informadas sobre estrategias de ventas, promociones y planificación de inventarios, "
             "permitiendo a los negocios de regalos personalizados optimizar sus esfuerzos en función de los patrones de consumo observados.")
       st.markdown("**Autor: Selena Rivera Quiroga**")
       st.markdown("**Linkedin:/in/selenariveraq**")