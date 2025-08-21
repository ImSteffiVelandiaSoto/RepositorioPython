import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset de seaborn
df = sns.load_dataset("tips")

# Título
st.title("Ejemplo con Streamlit y Seaborn - Dataset Tips")

# Mostrar primeras filas
st.subheader("Vista previa de los datos")
st.write(df.head())

# Filtro por día
dias = df["day"].unique()
dia_seleccionado = st.selectbox("Selecciona un día:", dias)
df_filtrado = df[df["day"] == dia_seleccionado]

st.subheader(f"Datos filtrados por {dia_seleccionado}")
st.write(df_filtrado)

# Gráfico de dispersión
st.subheader("Relación entre total_bill y tip")
fig, ax = plt.subplots()
sns.scatterplot(data=df_filtrado, x="total_bill", y="tip", hue="sex", ax=ax)
st.pyplot(fig)

# Gráfico de barras
st.subheader("Promedio de propinas por sexo")
fig2, ax2 = plt.subplots()
sns.barplot(data=df_filtrado, x="sex", y="tip", ax=ax2, estimator="mean", errorbar=None)
st.pyplot(fig2)
