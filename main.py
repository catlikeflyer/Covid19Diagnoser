import streamlit as st
import pags.diag_page
import pags.info_page
import pags.data_page
import pags.proto_page
import pags.viz_page

def main():
    st.title('DiaCoMoC')
    st.subheader("Diagnostico de COVID-19 y monitoreo constante")
    st.write('''
        Sebastián González, Gerardo Gutiérrez, Do Hyun Nam para
        TC1003.B.100
    ''')

    pages = {
        "Sobre el proyecto": pags.info_page,
        "Diagnóstico en linea": pags.diag_page,
        "Prototipo": pags.proto_page,
        "Monitoreo con datos ya generados": pags.data_page,
        "Monitoreo con reporte nuevo": pags.viz_page
    }

    st.sidebar.title('Ir a:')

    selection = st.sidebar.radio("", list(pages.keys()))

    page = pages[selection]
    page.load()

if __name__ == "__main__":
    main()