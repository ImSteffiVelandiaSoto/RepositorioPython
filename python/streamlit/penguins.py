import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Penguins mínimo", page_icon="🐧", layout="wide")

st.title("🐧 Penguins - Mini Dashboard")
st.caption("Fuente: seaborn-data (GitHub)")

# 1) Cargar datos (SIN cachear)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)

# Tipos
num_cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
for c in num_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df["sex"] = df["sex"].astype("string")
df["species"] = df["species"].astype("string")

# 2) Filtro lateral: SOLO sexo
st.sidebar.header("Filtro")
sex_opts = sorted(df["sex"].dropna().unique().tolist())
sel_sex = st.sidebar.multiselect("Sexo", sex_opts, default=sex_opts)

# Aplicar filtro
df_f = df[df["sex"].isin(sel_sex)].copy()

st.sidebar.markdown(f"**Registros:** {len(df_f):,} / {len(df):,}")

# 3) Dos gráficas
if df_f.empty:
    st.info("No hay datos para el filtro seleccionado.")
else:
    col1, col2 = st.columns(2)

    # Gráfica 1: Dispersión (longitud vs profundidad del pico)
    with col1:
        st.subheader("Pico: longitud vs profundidad")
        fig_scatter = px.scatter(
            df_f,
            x="bill_length_mm",
            y="bill_depth_mm",
            color="species",
            hover_data=["island", "sex", "body_mass_g"],
            labels={
                "bill_length_mm": "Longitud del pico (mm)",
                "bill_depth_mm": "Profundidad del pico (mm)",
                "species": "Especie",
            }
        )
        fig_scatter.update_layout(height=440, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_scatter, use_container_width=True)

    # Gráfica 2: Boxplot de masa corporal por especie
    with col2:
        st.subheader("Masa corporal por especie")
        fig_box = px.box(
            df_f,
            x="species",
            y="body_mass_g",
            points="outliers",
            color="species",
            labels={
                "species": "Especie",
                "body_mass_g": "Masa corporal (g)",
            }
        )
        fig_box.update_layout(showlegend=False, height=440, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_box, use_container_width=True)
