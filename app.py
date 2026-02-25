import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

# -----------------------
# CONFIGURACIÓN
# -----------------------
st.set_page_config(
    page_title="Descarga de Prueba",
    layout="centered"
)

REGISTRO = Path("registros.csv")
ADMIN_PASSWORD = "Tik@#1978"
PRUEBAS = {
    "Alfredo": "pruebas/Python_version_1_Lu.zip",
    # "Xavier": "pruebas/Python_version_2_Xavier.zip"
}

st.markdown("""
<style>
/* Empujar contenido admin muy abajo */
.admin-space {
    height: 1200px;
}

/* Hacer invisible el expander */
.streamlit-expanderHeader {
    display: none;
}

/* Quitar bordes y sombras */
[data-testid="stExpander"] {
    border: none;
    box-shadow: none;
}
</style>
""", unsafe_allow_html=True)


# -----------------------
# FUNCIÓN REGISTRO
# -----------------------
def guardar_registro(nombre, profesor):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fila = pd.DataFrame([[nombre, profesor, ahora]],
                         columns=["nombre", "profesor", "fecha_hora"])

    if REGISTRO.exists():
        fila.to_csv(REGISTRO, mode="a", header=False, index=False)
    else:
        fila.to_csv(REGISTRO, index=False)

# -----------------------
# INTERFAZ ESTUDIANTES
# -----------------------
st.title("Acceso a la prueba")

nombre = st.text_input("Nombre y apellidos")
profesor = st.selectbox(
    "Selecciona tu profesor",
    list(PRUEBAS.keys())
)

st.markdown("---")

if nombre and profesor:
    with open(PRUEBAS[profesor], "rb") as f:
        if st.download_button(
            label="Descargar prueba",
            data=f,
            file_name=Path(PRUEBAS[profesor]).name,
            mime="application/zip"
        ):
            guardar_registro(nombre, profesor)
            st.success("Descarga registrada correctamente.")
else:
    st.info("Completa tu nombre y selecciona una opción.")


st.markdown("### Las pruebas las envían por un discord al respectivo profesor")
st.markdown('<div class="admin-space"></div>', unsafe_allow_html=True)


# -----------------------
# SECCIÓN ADMIN OCULTA
# -----------------------
with st.expander(""):
    password = st.text_input(
        "",
        type="password",
        label_visibility="collapsed",
        placeholder=""
    )

    if password == ADMIN_PASSWORD:

        if REGISTRO.exists():
            with open(REGISTRO, "rb") as f:
                st.download_button(
                    "",
                    data=f,
                    file_name="registros_final.csv",
                    mime="text/csv"
                )

        if st.button(""):
            st.session_state.prueba_cerrada = True
            st.success("")

# en streamlit cloud:
# https://pruebasfundamentos-19-12-2025.streamlit.app/