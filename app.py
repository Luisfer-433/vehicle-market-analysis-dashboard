import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de anuncios de vehículos')

df = pd.read_csv('vehicles_us.csv')

show_hist = st.checkbox('Mostrar histograma del odómetro')
if show_hist:
    fig_hist = px.histogram(df, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

show_scatter = st.checkbox('Mostrar dispersión precio vs odómetro')
if show_scatter:
    fig_scatter = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
