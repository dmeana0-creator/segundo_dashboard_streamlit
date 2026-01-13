import streamlit as st
import pandas as pd
import time

st.title("Dashboard en streaming desde un log CSV")

# Refrescar cada 2 segundos
st_autorefresh = st.experimental_rerun

# Leer el archivo CSV
df = pd.read_csv("https://raw.githubusercontent.com/dmeana0-creator/segundo_dashboard_streamlit/refs/heads/main/log.csv")

# Mostrar datos
st.subheader("Últimos datos")
st.dataframe(df.tail(10))

# Mostrar métricas
st.metric("Último valor", df["valor"].iloc[-1])

# Gráfico en tiempo real
st.line_chart(df["valor"])

# Esperar y refrescar
time.sleep(2)
st.experimental_rerun()