import streamlit as st 


def load():
    st.subheader('Marque los recuadros que considere ciertos: ')
    A = st.checkbox("¿Tiene fiebre?")
    B = st.checkbox("¿Tiene fátiga?")
    C = st.checkbox("¿Tiene tos?")
    D = st.checkbox("¿Tiene pérdida de apetito?")
    E = st.checkbox("¿Tiene dificultad al respirar?")
    F = st.checkbox("¿Tiene dolor de cabeza?")
    G = st.checkbox("¿Tiene dolor de garganta?")
    H = st.checkbox("¿Tiene pérdida del olfato?")
    I = st.number_input('Inserte nivel de saturación de oxígeno:  ', 1, 100, step=0.1) < 89
    J = st.number_input('Inserte su temperatura corporal: ', 30, 45, step=0.1) > 37.5

    covid = (D and E) or (C and E) or (C and H) or (B and E) or (B and C) or (A and B) or (B and G and H) or (A and G and H) or (A and E)
    hospital = I or J
    doctor = ((A and C and D and E and G and F) or (A and B and C and E and G and H and F) or (A and B and C and E and G and H and D) or J)

    if covid:
        st.write("""
            Es altamente probable que esté contagiado de COVID-19,
            tome sus medidas de seguridad para proteger a la comunidad.
        """)
    else:
        st.write("""
            No es probable que esté contagiado, sin embargo, tome sus medidas de precaución.
        """)

    if hospital:
        st.write("""
            Acuda al hospital inmediatamente, su salud está en riesgo.
        """)
    else:
        st.write("""
            No es necesario que acuda al hospital.
        """)

    if doctor:
        st.write("""
            Busque la atención de un médico inmediatamente.    
        """)
    else:
        st.write("""
            Su estado de salud no requiere atención medica inmediata. 
        """)