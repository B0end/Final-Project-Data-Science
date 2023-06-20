import streamlit as st
import pandas as pd

st.image('./img/dataBRIDGE_logo_black.png')

st.title("MACHINE LEARNING :alien:")
st.subheader('ANÁLISIS DE SENTIMIENTO :bar_chart:')

if st.checkbox('Mostrar ejemplo de resultado'):
    pass
    st.dataframe()

if st.button('Usar Google Maps'):
        st.write('mapa mapa mapa')
        pass
if st.button('Usar Yelp!'):
        st.write('yekpa mapa mapa')
        pass

dim= st.radio('Elegit que mostrar:', ('Algo', "Otra cosa"), horizontal=True)

if dim == 'Algo':
       st.write('Elegiste algo, bien')
else: 
       st.write('elegiste otra cosa y esta bien tambien')

estados = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'DC': 'District_of_Columbia',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New_Hampshire',
    'NJ': 'New_Jersey',
    'NM': 'New_Mexico',
    'NY': 'New_York',
    'NC': 'North_Carolina',
    'ND': 'North_Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode_Island',
    'SC': 'South_Carolina',
    'SD': 'South_Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West_Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}

rubros_list = ('Shaving Ice', 'Weight Loss Centers', 'Eyelash salon', 'Barbershop', 'Nail salon', 'Tanning', 'Reflexology', 'Massage', 'Massage Therapy', 'Spray Tanning', 'Beauty', 'Cosmetology Schools', 'Eyebrow Services', 'Hair Extensions', 'Skin care clinic', 'Nail Technicians', 'Beauty school', 'Day spa', 'Cosmetics store', 'Hair Stylists', 'Permanent Makeup', 'Tanning salon', 'Threading Services', 'Beauty product supplier', 'Beauty & Spas', 'Medical Spas', 'Beauty salon', 'Makeup artist', 'Body Contouring', 'Saunas', 'Hair removal service', 'Hair salon', 'Tattoo and piercing shop', 'Electrolysis hair removal service', 'Massage studio', 'Naturopathic/Holistic', 'Orthodontist', 'Spa', 'Clothing store', 'Makeup Artists', 'Tattoo', 'Skin Care', 'Halotherapy', 'Facial spa', 'Hair Removal', 'Eyelash Service', 'Hair Salons', 'Permanent make-up clinic', 'Eyelash service', 'Piercing', 'Cosmetic dentist', 'Wig shop', 'Nail Salons', 'Waxing')
rubros = st.multiselect('Selecciona uno o mas rubros', rubros_list, default= ('Nail salon', 'Barbershop', 'Eyelash service'))
estados = st.selectbox('Seleccionar Estado:', estados)
filtro_anio = st.slider('Filtrar por años', 1990, 2023, 1990)

st.markdown('<h3 style="text-align: justify;color: white">ANALISIS DE SENTIMIENTO encontrados:</h3>', unsafe_allow_html=True)
#df_filtrado = df[filtro_anio, estados, rubros, nombre, sentimiento]


st.sidebar.text('mmmm')


#st.markdown('<h3 style="text-align: justify;color: white">Top 5 de alojamientos recomendados</h3>', unsafe_allow_html=True)
#st.dataframe(data=recomen[['name_hotel',"avg_rating",'cat_name','state_name','sentimiento','url']])