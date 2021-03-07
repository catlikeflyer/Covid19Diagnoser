import streamlit as st  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_linreg(file, concept: str):
    x_day = file['Tiempo (dias)']

    if concept == 'temp':
        fignum = 1
        ylim = [0, 50]
        text = 'Temperatura en Celsius'
        val = "Temperatura"
    if concept == 'oxi':
        fignum = 2
        ylim = [50, 100]
        text = 'Saturación de Oxígeno'
        val = "Oxigenación"

    y_con = file[val]

    c = len(x_day)

    X = np.matrix([np.ones(c), x_day], dtype=float).T
    Y = np.matrix(y_con, dtype=float).T

    p_mat = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)

    if p_mat[1] > 0: 
        tend = f"Tendencia creciente, tu {text} está aumentando {p_mat[1][0]} por día"
    elif p_mat[1] < 0: 
        tend = f"Tendencia decreciente, tu {text} está disminuyendo {p_mat[1][0]} por día"
    else:
        tend = "Tendencia plana"

    x = np.linspace(0, c+1)
    y = np.array(p_mat[1]*x + p_mat[0])

    
    fig = plt.figure(fignum)
    plt.style.use('fast')
    plt.plot(x, y.T, color='b')
    plt.grid()
    plt.scatter(np.array(x_day), np.array(y_con), color='c')
    plt.ylim(ylim)
    plt.xlabel("Días transcurridos")
    plt.ylabel(text)
    plt.show()

    return fig, x_day, y_con, tend

def create_df(days, oxi, temp):
    arr = np.array([oxi, temp]).transpose()

    return pd.DataFrame(arr, index=days, columns=['Oxígeno','Temperatura'])

def load():
    st.title("Oxigenación y temperatura")
    st.write("Utilize reportes en el formato arrojado por el prototipo en arduino")
    st.write("""
        Procura que la columna para los días se llame [Tiempo (dias)], 
        para la temperatura [Temperatura] y para el oxígeno [Oxígeno]. Respeta 
        las mayúsculas, los espacios y acentos tal cual se mencionan en este párrafo.
    """)

    filename = st.file_uploader("Suba reporte en formato .csv", type="csv")

    if filename is not None:
        df = pd.read_csv(filename)

        oxi_fig, oxi_day, oxi_y, oxi_tend = plot_linreg(df, "oxi")
        temp_fig, temp_day, temp_y, temp_tend = plot_linreg(df, "temp")

        st.dataframe(create_df(oxi_day, oxi_y, temp_y))
        col1, col2 = st.beta_columns(2)

        with col1:
            st.header("Niveles de oxigenación")
            st.pyplot(oxi_fig)
            st.write(oxi_tend)

        with col2:
            st.header("Temperaturas")
            st.pyplot(temp_fig)
            st.write(temp_tend)



