import streamlit as st  
import numpy as np
import os 
import matplotlib.pyplot as plt
import csv
import pandas as pd

def file_selector(folder_path:str='./reportes'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)

    return os.path.join(folder_path, selected_filename)

def plot_linreg(file: str, concept: str):
    x_day = []
    y_con = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        if concept == 'temp':
            rownum = 11
            fignum = 1
            ylim = [0, 50]
            text = 'Temperatura en Celsius'
        if concept == 'oxi':
            rownum = 12
            fignum = 2
            ylim = [50, 100]
            text = 'Saturación de Oxígeno'

        for row in csv_reader:
            x_day.append(float(row[0]))
            y_con.append(float(row[rownum]))

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

    return pd.DataFrame(arr, index=days, columns=['Oxigeno','Temperatura'])

def load():
    st.title("Oxigenacion y temperatura")
    st.subheader("Inserta tu archivo en la carpeta de reportes (.txt o .csv)")    
    st.write('''
        Selecciona tu archivo de datos para recibir reporte de monitoreo:
    ''')

    filename = file_selector()
    st.write('Seleccionaste `%s`' % filename)

    oxi_fig, oxi_day, oxi_y, oxi_tend = plot_linreg(filename, "oxi")
    temp_fig, temp_day, temp_y, temp_tend = plot_linreg(filename, "temp")

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

