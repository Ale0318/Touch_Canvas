import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("DRAAW ☀️")
st.markdown("""
<style>

/* Fondo degradado morado pastel */
.stApp {
    background: linear-gradient(
        135deg,
        #E9D5FF,
        #D8B4FE,
        #F3E8FF
    );
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #C084FC;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Propiedades del tablero")
  
    st.subheader("Tamaño del tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
  
    drawing_mode = st.selectbox(
      "Trazos",
      ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
  
    stroke_width = st.slider ("Selecciona el tamaño de tu Trazo", 1, 30, 15)
  
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
  
    bg_color = st.color_picker("Color del fondo", "#000000")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
  
