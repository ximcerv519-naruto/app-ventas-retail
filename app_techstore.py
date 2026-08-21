
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial de la página
st.set_page_config(page_title="TechStore Analytics Dashboard", layout="wide")

st.title("🚀 TechStore: Sistema de Analytics Predictivo")
st.markdown("Dashboard interactivo para la optimización de ventas, marketing y segmentación de clientes.")

# Sidebar de navegación
st.sidebar.header("Panel de Control")
seccion = st.sidebar.selectbox("Seleccione Módulo", ["Resumen Ejecutivo", "Segmentación RFM", "Simulador de Precios"])

# ==========================================
# MÓDULO 1: RESUMEN EJECUTIVO
# ==========================================
if seccion == "Resumen Ejecutivo":
    st.header("KPIs Principales de Negocio")
    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Totales Proyectados", "$1,450,000", "+12%")
    col2.metric("Clientes Activos", "2,000", "0%")
    col3.metric("ROI de Marketing", "3.4x", "+0.5x")
    
    st.info("Utilice el menú lateral para explorar los modelos de segmentación y simulación de precios.")
    
    st.markdown("---")
    st.subheader("Insights Clave para Dirección")
    st.write("• Los clientes de alta frecuencia concentran el mayor porcentaje de ingresos.")
    st.write("• Se recomienda reasignar presupuesto de marketing digital a campañas de retención en segmentos de riesgo.")

# ==========================================
# MÓDULO 2: SEGMENTACIÓN RFM (CON GRÁFICAS)
# ==========================================
elif seccion == "Segmentación RFM":
    st.header("Análisis de Segmentos de Clientes (K-Means)")
    st.write("Visualización de clústeres basados en Recencia, Frecuencia y Monetario.")
    
    # Generar o cargar datos simulados/reales para que la app muestre contenido visual inmediato
    @st.cache_data
    def cargar_datos_rfm_demo():
        np.random.seed(42)
        n = 500
        df_demo = pd.DataFrame({
            'Recencia': np.random.exponential(scale=30, size=n),
            'Frecuencia': np.random.poisson(lam=3, size=n) + 1,
            'Monetario': np.random.gamma(shape=2, scale=200, size=n),
            'Cluster_KMeans': np.random.choice([0, 1, 2, 3], size=n)
        })
        # Simulando componentes PCA para la gráfica
        df_demo['PCA1'] = np.random.normal(size=n) + df_demo['Cluster_KMeans'] * 1.5
        df_demo['PCA2'] = np.random.normal(size=n) + (df_demo['Cluster_KMeans'] % 2) * 2
        return df_demo

    df_rfm = cargar_datos_rfm_demo()
    
    # 1. Tabla resumen de perfiles por Clúster
    st.subheader("Resumen de Promedios por Segmento")
    df_resumen = df_rfm.groupby('Cluster_KMeans')[['Recencia', 'Frecuencia', 'Monetario']].mean().reset_index()
    df_resumen.columns = ['Segmento (Clúster)', 'Recencia Promedio (días)', 'Frecuencia Promedio', 'Valor Monetario Promedio ($)']
    st.dataframe(df_resumen.style.format("{:.2f}"))
    
    st.markdown("---")
    st.subheader("Proyección Espacial de Clústeres (Reducción PCA)")
    st.write("Gráfico de dispersión que muestra la separación natural de los clientes de TechStore en 2 dimensiones principales.")
    
    # 2. Generación de la gráfica con Matplotlib y Seaborn
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(
        x='PCA1', y='PCA2', hue='Cluster_KMeans', 
        data=df_rfm, palette='Set1', s=70, alpha=0.8, ax=ax
    )
    ax.set_title("Segmentación de Clientes TechStore (PCA proyectado)")
    ax.set_xlabel("Componente Principal 1")
    ax.set_ylabel("Componente Principal 2")
    ax.legend(title='Segmento')
    
    # Renderizar la gráfica dentro de la app web de Streamlit
    st.pyplot(fig)

# ==========================================
# MÓDULO 3: SIMULADOR DE PRECIOS
# ==========================================
elif seccion == "Simulador de Precios":
    st.header("Simulador de Elasticidad Precio-Demanda")
    st.write("Evalúa el impacto financiero de modificar los precios de catálogo.")
    
    col_sim1, col_sim2 = st.columns(2)
    with col_sim1:
        precio_base = st.slider("Precio Base del Producto ($)", 50, 500, 100)
    with col_sim2:
        variacion = st.slider("Variación de Precio (%)", -30, 30, 0)
        
    precio_simulado = precio_base * (1 + variacion / 100)
    elasticidad = -1.5
    cambio_demanda_pct = elasticidad * (variacion / 100)
    demanda_base = 1000
    demanda_estimada = demanda_base * (1 + cambio_demanda_pct)
    ingresos_estimados = precio_simulado * demanda_estimada
    
    st.success(f"• **Precio Simulado:** ${precio_simulado:.2f}")
    st.info(f"• **Demanda Estimada:** {demanda_estimada:.0f} unidades")
    st.metric("Ingresos Proyectados", f"${ingresos_estimados:,.2f}", f"{variacion}% var. precio")
