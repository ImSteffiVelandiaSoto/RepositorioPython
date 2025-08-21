# dashboard_titanic.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------
# Configuración básica de la app
# -----------------------------
st.set_page_config(
    page_title="Dashboard Titanic",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚢 Dashboard Titanic")
st.caption("Fuente: seaborn-data (GitHub)")

# -----------------------------
# Carga de datos (cacheada)
# -----------------------------
@st.cache_data(show_spinner=True)
def load_data():
    # CSV oficial del repo de seaborn
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
    df = pd.read_csv(url)
    # Limpiezas y enriquecimientos útiles
    # Consistencia de tipos
    numeric_cols = ["age", "fare", "parch", "sibsp", "survived", "pclass"]
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # Mapeos legibles
    df["survived_label"] = df["survived"].map({0: "No", 1: "Sí"})
    df["class"] = df["class"].astype(str)  # por si llega categorical
    # Buckets de edad
    bins = [-0.1, 12, 18, 30, 45, 60, np.inf]
    labels = ["0-12", "13-18", "19-30", "31-45", "46-60", "61+"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
    return df

df = load_data()

# -----------------------------
# Barra lateral (filtros)
# -----------------------------
st.sidebar.header("Filtros")

# Filtros por categoría
pclass_opts = sorted(df["pclass"].dropna().unique().tolist())
sex_opts = sorted(df["sex"].dropna().unique().tolist())
embark_opts = sorted(df["embark_town"].dropna().unique().tolist())
alone_opts = sorted(df["alone"].dropna().unique().tolist())

sel_pclass = st.sidebar.multiselect("Clase (pclass)", pclass_opts, default=pclass_opts)
sel_sex = st.sidebar.multiselect("Sexo", sex_opts, default=sex_opts)
sel_embark = st.sidebar.multiselect("Puerto embarque", embark_opts, default=embark_opts)
sel_alone = st.sidebar.multiselect("¿Viajaba solo/a?", alone_opts, default=alone_opts)

# Rango de edad y tarifa (fare)
age_min, age_max = int(np.nanmin(df["age"])), int(np.nanmax(df["age"]))
fare_min, fare_max = float(np.nanmin(df["fare"])), float(np.nanmax(df["fare"]))

sel_age = st.sidebar.slider("Rango de edad", min_value=age_min, max_value=age_max, value=(age_min, age_max))
sel_fare = st.sidebar.slider("Rango de tarifa (fare)", min_value=float(fare_min), max_value=float(fare_max), value=(float(fare_min), float(fare_max)))

# Aplicar filtros
mask = (
    df["pclass"].isin(sel_pclass) &
    df["sex"].isin(sel_sex) &
    df["embark_town"].isin(sel_embark) &
    df["alone"].isin(sel_alone) &
    df["age"].between(sel_age[0], sel_age[1], inclusive="both") &
    df["fare"].between(sel_fare[0], sel_fare[1], inclusive="both")
)
df_f = df[mask].copy()

st.sidebar.markdown(f"**Registros filtrados:** {len(df_f):,} / {len(df):,}")

# -----------------------------
# KPIs
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

survival_rate = df_f["survived"].mean() * 100 if len(df_f) else 0
avg_age = df_f["age"].mean() if len(df_f) else np.nan
avg_fare = df_f["fare"].mean() if len(df_f) else np.nan
passengers = len(df_f)

col1.metric("🚹🧍 Pasajeros", f"{passengers:,}")
col2.metric("💙 Tasa de supervivencia", f"{survival_rate:,.1f}%")
col3.metric("🎂 Edad promedio", f"{avg_age:,.1f}" if not np.isnan(avg_age) else "—")
col4.metric("💵 Tarifa promedio", f"{avg_fare:,.2f}" if not np.isnan(avg_fare) else "—")

st.divider()

# -----------------------------
# Tabs / Pestañas
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Supervivencia",
    "🧒 Edades",
    "🧭 Embarque",
    "📈 Variables",
    "📄 Datos"
])

# ---- Tab 1: Supervivencia
with tab1:
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("Supervivencia por sexo y clase")
        if len(df_f):
            fig = px.bar(
                df_f,
                x="sex",
                color="survived_label",
                barmode="group",
                facet_col="pclass",
                category_orders={"survived_label": ["No", "Sí"], "sex": ["male", "female"]},
                title=None
            )
            fig.update_layout(height=450, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No hay datos para los filtros seleccionados.")

    with c2:
        st.subheader("Distribución (pie)")
        if len(df_f):
            pie = px.pie(
                df_f,
                names="survived_label",
                title="Supervivencia total (filtrada)"
            )
            pie.update_layout(height=450, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(pie, use_container_width=True)
        else:
            st.info("No hay datos para los filtros seleccionados.")

# ---- Tab 2: Edades
with tab2:
    st.subheader("Distribución de edades por supervivencia")
    if len(df_f):
        # Histograma
        hist = px.histogram(
            df_f,
            x="age",
            color="survived_label",
            nbins=30,
            marginal="box",
            opacity=0.85
        )
        hist.update_layout(height=420, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(hist, use_container_width=True)

        # Tasa de supervivencia por grupo de edad y clase
        st.markdown("**Tasa de supervivencia por grupo de edad y clase**")
        rate = (
            df_f.dropna(subset=["age_group"])
            .groupby(["age_group", "pclass"])["survived"]
            .mean()
            .reset_index()
        )
        rate["survival_rate"] = rate["survived"] * 100
        line = px.line(
            rate,
            x="age_group",
            y="survival_rate",
            color="pclass",
            markers=True
        )
        line.update_layout(yaxis_title="Tasa (%)", height=420, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(line, use_container_width=True)
    else:
        st.info("No hay datos para los filtros seleccionados.")

# ---- Tab 3: Embarque
with tab3:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Conteo por puerto de embarque")
        if len(df_f):
            bar = px.bar(
                df_f.dropna(subset=["embark_town"]),
                x="embark_town",
                color="survived_label",
            )
            bar.update_layout(height=420, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(bar, use_container_width=True)
        else:
            st.info("No hay datos para los filtros seleccionados.")
    with c2:
        st.subheader("Tasa de supervivencia por puerto de embarque")
        if len(df_f):
            surv_port = (
                df_f.dropna(subset=["embark_town"])
                .groupby("embark_town")["survived"]
                .mean()
                .reset_index()
            )
            surv_port["survival_rate"] = surv_port["survived"] * 100
            bar2 = px.bar(surv_port, x="embark_town", y="survival_rate")
            bar2.update_layout(yaxis_title="Tasa (%)", height=420, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(bar2, use_container_width=True)
        else:
            st.info("No hay datos para los filtros seleccionados.")

# ---- Tab 4: Variables (correlaciones/relaciones)
with tab4:
    st.subheader("Relaciones entre variables numéricas")
    if len(df_f):
        numeric = df_f[["age", "fare", "sibsp", "parch", "survived", "pclass"]].dropna()
        if len(numeric):
            # Mapa de calor (usando plotly imshow)
            corr = numeric.corr(numeric_only=True)
            heat = px.imshow(
                corr,
                text_auto=True,
                aspect="auto",
                title="Matriz de correlación"
            )
            heat.update_layout(height=520, margin=dict(l=10, r=10, t=40, b=10))
            st.plotly_chart(heat, use_container_width=True)

            st.markdown("**Relación Fare vs Age (color = supervivencia)**")
            sc = px.scatter(
                df_f, x="age", y="fare",
                color="survived_label",
                hover_data=["pclass", "sex", "embark_town"]
            )
            sc.update_layout(height=420, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(sc, use_container_width=True)
        else:
            st.info("No hay suficientes observaciones numéricas tras los filtros.")
    else:
        st.info("No hay datos para los filtros seleccionados.")

# ---- Tab 5: Datos + descarga
with tab5:
    st.subheader("Tabla de datos (filtrados)")
    st.dataframe(df_f, use_container_width=True, height=420)
    csv = df_f.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Descargar CSV filtrado",
        data=csv,
        file_name="titanic_filtrado.csv",
        mime="text/csv"
    )

# -----------------------------
# Nota de ayuda
# -----------------------------
with st.expander("ℹ️ Ayuda rápida"):
    st.markdown(
        """
        - Usa la **barra lateral** para aplicar filtros por clase, sexo, puerto, edad, tarifa y si viajaba solo/a.
        - Los **KPIs** de arriba cambian dinámicamente según tus filtros.
        - Explora las **pestañas** para ver diferentes perspectivas: supervivencia, edades, embarque, correlaciones y la tabla de datos.
        - Puedes **descargar** el subconjunto filtrado desde la pestaña **Datos**.
        """
    )
