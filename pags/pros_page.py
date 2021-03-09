import streamlit as st 

st.subheader("Procesos para determinar el estado del individuo")

st.write("""
    Tanto el dispositivo como el cuestionario tienen la capacidad de determinar si en efecto el usuario de este 
    está infectado de COVId-19, si es necesario que sea hospitalizado o que requiera la atención de un médico.
    Esto se determina mediante la conexión de las siguientes proposiciones:\n
    Fiebre: A \n
    Fatiga : B \n
    Tos: C \n
    Apetito: D \n
    Dificultad para respirar: E \n
    Olfato: F \n
    Garganta: G \n
    Oxigeno < 89%: H \n
    Cabeza: I \n
    Temperatura real > 38.5: J \n
""")
st.write("""
    COVID-19:\n
    ABCDE+DE+CE+CF+EB+BC+CFA+AB+GCF+GBF+GAF+AE \n
    Ley de absorción\n
    DE+CE+CF+CF+EB+BC+CFA+AB+GCF+GBF+GAF+AE\n
    Ley de absorción\n
    DE+CE+CF+EB+BC+AB+GCF+GBF+GAF+AE\n
    Ley de absorción → Máxima simplificación\n
    DE+CE+CF+EB+BC+AB+GBF+GAF+AE\n
    \n
    Hospitalización = 
    H + JE + E \n
    Ley de absorción → Máxima simplificación\n
    H+E\n
    \n
    No acudir con médico =\n
    !A !B !C !D !E !I !G !F +  !A !B !C !D !E !I !G F + !A !B !C !D !E I !G !F + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G !F + !A B !C !D !E !I !G F + !J \n
    Ley distributiva\n
    !A !B !C !D !E !I !G (!F + F) + !A !B !C !D !E I !G !F + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G !F + !A B !C !D !E !I !G F + !J \n
    Ley complementaria y de identidad\n
    !A !B !C !D !E !I !G + !A !B !C !D !E I !G !F + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G !F + !A B !C !D !E !I !G F + !J \n
    Ley distributiva\n
    !A !B !C !D !E !G (I !F + !I) + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G !F + !A B !C !D !E !I !G F + !J \n
    Ley de absorción\n
    !A !B !C !D !E !G (!F + !I) + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G !F + !A B !C !D !E !I !G F + !J \n
    Ley distributiva\n
    !A !B !C !D !E !G (!F + !I) + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G (!F + F) + !J \n
    Ley complementaria y de identidad\n
    !A !B !C !D !E !G (!F + !I) + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G + !J \n
    Distribucion\n
    !A !B !C !D !E !G !F + !A !B !C !D !E !G !I + !A !B !C D !E !I !G !F + !A B !C !D !E !I !G + !J\n
    Ley distributiva\n
    !A !B !C !D !E !G !F + !A !C !D !E !G !I (!B + B) + !A !B !C D !E !I !G !F + !J\n
    Ley complementaria y de identidad\n
    !A !B !C !D !E !G !F + !A !C !D !E !G !I + !A !B !C D !E !I !G !F + !J\n
    Ley distributiva\n
    !A !C !D !E !G !I + !A !B !C !E !G !F (D !I + !D) + !J\n
    Ley de absorción\n
    !A !C !D !E !G !I + !A !B !C !E !G !F (!I + !D) + !J\n
    Distribución → Máxima simplificación\n
    !A !C !D !E !G !I + !A !B !C !E !G !F !I +!A !B !C !E !G !F !D + !J\n
\n
""")