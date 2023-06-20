import streamlit as st
import pandas as pd

st.image('./img/dataBRIDGE_logo_black.png')
if st.checkbox('elegi algo'):
    st.write('holandia')

st.markdown('***')

st.markdown('### chamuyo')
st.write('gracias y bla bla bla bla blaaaaaaa') 

st.text('Fixed width text')
st.markdown('_Markdown_') # see *

st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')

st.subheader('My sub')
st.code('for i in range(8): foo()')

