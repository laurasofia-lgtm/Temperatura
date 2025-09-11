import streamlit as st

# ---- Configuración de la página ----
st.set_page_config(
    page_title="Celsius ↔ Fahrenheit",
    page_icon="🌡️",
    layout="centered",
)

# ---- Funciones ----
def c_to_f(celsius: float) -> float:
    """Convierte Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit: float) -> float:
    """Convierte Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

# ---- UI ----
st.title("🌡️ Convertidor de Temperaturas")
st.caption("Convierte grados entre **Celsius (°C)** y **Fahrenheit (°F)** en tiempo real.")

# Tabs para organizar mejor
tab1, tab2 = st.tabs(["Celsius → Fahrenheit", "Fahrenheit → Celsius"])

with tab1:
    celsius = st.number_input("Temperatura en °C", value=0.0, step=0.5)
    decimales = st.slider("Decimales", 0, 4, 2)
    st.success(f"{celsius:.{decimales}f} °C = {c_to_f(celsius):.{decimales}f} °F")

with tab2:
    fahrenheit = st.number_input("Temperatura en °F", value=32.0, step=0.5)
    decimales = st.slider("Decimales", 0, 4, 2, key="f2c")
    st.success(f"{fahrenheit:.{decimales}f} °F = {f_to_c(fahrenheit):.{decimales}f} °C")

st.divider()
st.caption("⚡ Fórmulas usadas:  °F = (°C × 9/5) + 32   |   °C = (°F − 32) × 5/9")
