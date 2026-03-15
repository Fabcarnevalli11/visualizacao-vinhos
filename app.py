import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Interativo - Qualidade do Vinho")

st.write("Análise exploratória do dataset Wine Quality")

df = pd.read_csv("winequality-red.csv", sep=";")

st.subheader("Amostra do Dataset")
st.dataframe(df.head())

st.subheader("Distribuição da Qualidade dos Vinhos")

fig1 = px.histogram(df, x="quality")
st.plotly_chart(fig1)

st.subheader("Relação entre Teor Alcoólico e Qualidade")

fig2 = px.scatter(df, x="alcohol", y="quality")
st.plotly_chart(fig2)

st.subheader("Correlação entre Variáveis")

corr = df.corr()
fig3 = px.imshow(corr)
st.plotly_chart(fig3)