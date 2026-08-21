
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="TechStore Analytics Dashboard", layout="wide")

st.title("🚀 TechStore: Sistema de Analytics Predictivo")
st.markdown("Dashboard interactivo para la optimización de ventas, marketing y segmentación de clientes.")

# Sidebar de navegación
st.sidebar.header("Panel de Control")
seccion = st.sidebar.selectbox("Seleccione Módulo", ["Resumen Ejecutivo", "Segmentación RFM", "Simulador de Precios"])

if seccion == "Resumen Ejecutivo":
    st.header("KPIs Principales de Negocio")
    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Totales Proyectados", "$1,450,000", "+12%")
    col2.metric("Clientes Activos", "2,000", "0%")
    col3.metric("ROI de Marketing", "3.4x", "+0.5x")
    
    st.info("Utilice el menú lateral para explorar los modelos de segmentación y simulación de precios.")

elif seccion == "Segmentación RFM":
    st.header("Análisis de Segmentos de Clientes (K-Means)")
    st.write("Visualización de clústeres basados en Recencia, Frecuencia y Monetario.")
    # Aquí puedes integrar tu gráfico o tabla resumen de clústeres

elif seccion == "Simulador de Precios":
    st.header("Simulador de Elasticidad Precio-Demanda")
    precio_base = st.slider("Precio Base del Producto ($)", 50, 500, 100)
    variacion = st.slider("Variación de Precio (%)", -30, 30, 0)
    st.success(f"Precio simulado: ${precio_base * (1 + variacion/100):.2f}")
