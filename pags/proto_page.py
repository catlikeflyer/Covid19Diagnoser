import streamlit as st 
import os
from PIL import Image

def load():
    st.subheader("""
    Prototipo del dispositivo realizado en una simulación de arduino mediante Tinkercad.
    Se utilizaron varios medios de entrada y salida como:
    """)
    st.markdown("""
    - Sensor de temperatura
    - Placa de teclas
    - Pantalla LCD 2x16
    """)
    image = Image.open(os.path.join("img", "cad.png"))
    st.image(image, use_column_width=True)
    st.markdown('[Link a simulacion](https://www.tinkercad.com/things/cPxAzSaZ0Y0-dazzling-maimu-wolt/editel?sharecode=M9-cPAjPjf3NwASxy7KPZNyBXYWOb8MoUrl8uTKui9M)')
    st.markdown('[Link a video](https://drive.google.com/drive/folders/185kL27CYBdKBynTVJ3fK7Xng_iWLSaYp?usp=sharing)')