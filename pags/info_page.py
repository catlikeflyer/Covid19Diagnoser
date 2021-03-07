import streamlit as st 
import os
from PIL import Image

def load():
    st.write(""" 
    En el momento actual en el que se está viviendo la pandemia de Covid-19 es esencial 
    hacer lo posible para detectar algún contagio de manera rápida y eficiente con el 
    fin de cuidar la salud y evitar la propagación del virus. \n
    Y es por lo anterior que es de suma importancia detectar si se presentan síntomas y 
    realizar un diagnóstico donde se pueda determinar los pasos a seguir dependiendo del 
    malestar de cualquier individuo. \n
    Con el fin de hacer un dispositivo preciso, se utilizan 9 parámetros,  los cuales 
    determinarán las acciones a seguir dependiendo de si existen síntomas graves o no. 
    Los síntomas tomados en cuenta para el diagnóstico son aquellos reconocidos como los 
    más comunes por la Organización Mundial de la Salud. Además, el dispositivo debe ser 
    eficiente, por lo que la mayoría de los síntomas se tomarán como valores booleanos,
    y los únicos valores donde se consideran rangos son la temperatura y la oxigenación 
    ya que pueden ser media con instrumentos de precisión.
    """)
    image = Image.open(os.path.join('img', 'covid.png'))
    st.image(image, caption=None, use_column_width=True, clamp=False, channels='RGB', output_format='auto')