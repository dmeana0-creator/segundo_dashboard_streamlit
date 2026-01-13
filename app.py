import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import time

st.set_page_config(page_title="Streaming Log Dashboard")

# Refrescar cada 2000 ms
st_autorefresh(interval=2000, key="refresh")

st.title("Dashboard en streaming desde un archivo CSV")

df = pd.read_csv("https://raw.githubusercontent.com/dmeana0-creator/segundo_dashboard_streamlit/refs/heads/main/log.csv")

st.line_chart(df["valor"])
st.dataframe(df.tail(5))