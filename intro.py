import streamlit as st
import pandas as pd

st.set_page_config(page_title = 'DataBrick APP', initial_sidebar_state='expanded')


st.image('./img/dataBRIDGE_logo_black.png')

st.markdown('***')

def main():
    # Crear tres columnas utilizando st.columns
    col1, col2, col3 = st.columns(3)

    # Agregar contenido a cada columna
    with col1:
        st.markdown("<h1 style='text-align: center; '><a href='/Proyecto' style='color: white;'>PROYECTO</h1></a></h1>", unsafe_allow_html=True)
        st.image("./img/giphy_proyecto.gif")

    with col2:
        st.markdown("<h1 style='text-align: center;'><a href='/Analytics' style='color: white;'>ANALYTICS</h1></a></h1>", unsafe_allow_html=True)
        st.image("./img/giphy_db.gif")

    with col3:
        st.markdown("<h1 style='text-align: center;'><a href='/ML' style='color: white;'>ML</h1>", unsafe_allow_html=True)
        st.image("./img/giphy_ml.gif")
        
if __name__ == '__main__':
    main()


st.markdown("<h1 style='text-align: center;'><a href='/Equipo' style='color: white;'>NOSOTROS</h1></a></h1>", unsafe_allow_html=True)
st.image("./img/gitHub.png")


st.markdown('_realizado por alumnos para el bootcamp de SoyHenry_') # see *
st.image("./img/Copy of HENRY - Fondo virtual 2.png")

st.markdown('***')
st.caption('Disclaimer: Este material se proporciona únicamente con fines educativos. No se pretende ni se debe interpretar como asesoramiento legal, financiero o profesional de ningún tipo. La información contenida en este material es precisa y completa en la medida de nuestro conocimiento, pero no garantizamos su exactitud, integridad o actualidad.')

st.markdown('***')

st.write("GitHub [link](https://github.com/BenJokek/Final-Project-Data-Science)")
st.write("PowerBi [link](https://github.com/BenJokek/Final-Project-Data-Science)")


