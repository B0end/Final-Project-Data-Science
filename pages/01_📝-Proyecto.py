import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.image('./img/dataBRIDGE_logo_black.png')

st.markdown('***')

st.title('DESCRIPCIÓN :memo:')
st.write('Nuestro proyecto consiste en recopilar, depurar y analizar datos de reseñas de Yelp y Google Maps, utilizando técnicas de análisis de sentimientos y machine learning para determinar las ubicaciones más adecuadas para establecer nuevos locales comerciales y descubrir oportunidades de inversión investigando aspectos como el crecimiento del mercado, la demanda de servicios de belleza, la competencia existente y las tendencias emergentes. Con base en el análisis realizado, generaremos recomendaciones claras y fundamentadas para el inversor. Estas recomendaciones mostrarán las oportunidades de inversión más atractivas en el rubro de belleza, destacando los aspectos clave que respaldan la viabilidad y el potencial de crecimiento de cada oportunidad.')

st.image('./img/giphy_science.gif', width=700)


st.markdown('***')

st.markdown('### ALCANCE :earth_americas:')
st.write('La opinión de los usuarios se ha convertido en un dato invaluable en la planificación de estrategias comerciales. Plataformas de reseñas como Yelp y Google Maps proporcionan una gran cantidad de información sobre la percepción de los usuarios respecto a diversos negocios, incluyendo restaurantes, hoteles, estéticas y otros servicios relacionados. Esta retroalimentación es esencial para las empresas, ya que les permite evaluar su desempeño, identificar áreas de mejora y comprender cómo son percibidas por los usuarios. Como parte de una consultora de data, se nos ha contratado para realizar un análisis detallado de la opinión de los usuarios en Yelp y Google Maps sobre negocios relacionados con el cuidado personal y la estética en el mercado estadounidense.')
df = pd.read_csv('./data/reviews_google_count_MAL.csv')
conteo_resenas = df.groupby('year')['rating'].count()
st.line_chart(conteo_resenas)

st.subheader('OBJETIVO :sparkles:')
st.write('El objetivo principal del proyecto es brindar a nuestro cliente: inversor de la industria estetica latinoamericana una vision general del mercado estadounidensecon el fin de que tome las decisiones mas informadas e inteligentespara incorporarse como competidor en dicho mercado. Gracias a un análisisexhaustivo de la opinión de los usuarios en Yelp y Google Maps podremosidentificar tendencias, predecir el crecimiento o decaimiento de rubroscomerciales y tomar decisiones estratégicas informadas para mejorardecisiones de gestion e inversion de negocios.')
st.text('grafica interactiva cantidad de negocios por estado')
st.image('./img/Screenshot 2023-06-14 at 21.03.05.png')

st.markdown('***')

st.subheader('KPIS :chart_with_upwards_trend:')

st.write('Los indicadores clave de rendimiento (KPIs) son métricas utilizadas para evaluar el desempeño y el progreso hacia los objetivos de una organización. Son importantes porque proporcionan información objetiva para tomar decisiones informadas. En nuestro proyecto, consideramos que la cantidad de reviews positivas influye positivamente en las ventas, la popularidad y la satisfacción del cliente. Medir este KPI nos permite evaluar la satisfacción del cliente y su impacto en el éxito del negocio. Es crucial establecer métricas y realizar un seguimiento constante de este KPI para comprender la evolución y tomar decisiones estratégicas.')

# Datos de ejemplo en forma de pandas DataFrame
kpis = {
    "KPI": ["Volumen de reviews (popularidad)", "Proporción positiva de reviews (baja negatividad)", "Satisfacción del cliente (mejora del servicio", "Aumento de catidad de locales por estado (aumento de demanda)", "Rubro belleza vs rubro restaurant (competencia)"],
    "Descripción": [f"aumentar en un 5% lacantidad de reviews respecto al mes anterior", "La de reviews positivas debe mantenerse en 5:1 sobre las negativas. Considerando Review positiva > 4", f"Aumentar a 3% el promedio de calificaciones", f"Aumentar en un 2% la cantidad de negocios por Estado", "Comparar el promedio de calificaciones del rubro belleza contra el rubro restaurant"],
    "Frecuencia": ["Mensual", "Mensual", "Mensual", "Mensual", "Mensual"]
}
df = pd.DataFrame(kpis)

st.table(df)

st.markdown('***')

st.subheader('STACK TECNOLÓGICO :partly_sunny: ')
st.image('./img/stackfinal_.png')
st.write('El flujo de trabajo completo involucra la configuración de la API de Drive, la extracción de datos desde Google Drive, la carga de datos en Google Cloud Store, el procesamiento de datos con Dataflow y la carga de datos en BigQuery. Esto nos permite tener datos limpios y ordenados en nuestro data warehouse de BigQuery.')

st.markdown('***')

st.title("MACHINE LEARNING :alien:")
st.subheader('ANÁLISIS DE SENTIMIENTO :bar_chart:')
st.write('Aplicación de técnicas de procesamiento de lenguaje natural (NLP) para analizar el sentimiento de las reseñas y clasificarlas en positivas, negativas o neutrales. Haciendo uso de la libreria SentimentIntensityAnalyzer del conjunto nltk.sentiment. La cual genera una nueva columna donde se clasifica cada reseña, reemplazando/traduciendo así la reseña misma a su categoría representante. Es así como podemos ordenar y filtrar para dar a conocer cuales Estados se encuentran más contentos con el servicio y cuales no.')


code = '''# Modelo de Machine Learning el cual detecta la polaridad del sentimiento con respecto a las reviews.
    def get_sentiment(text):
    try:
        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = analyzer.polarity_scores(text)
        compound_score = sentiment_scores['compound']
        
        if compound_score > 0:
            return 'Positivo'
        elif compound_score < 0:
            return 'Negativo'
        else:
            return 'Neutral'
    except:
        return 'Error'

# Aplicar el análisis de sentimiento a la columna 'text' y crear la nueva columna 'sentiment'
gmap_ML_mood['sentiment'] = gmap_ML_mood['text'].apply(get_sentiment)'''
st.code(code, language='python')

st.caption('ejemplo: resultado del modelo entrenado')
st.image('./img/mL_sentiment.png')

st.subheader('RECOMENDACIÓN POR ZONA 🗺️')
st.write('A través de un modelo de clustering en tres dimensiones (latitud, longitud y promedio de rating) se investigan y se agrupan los negocios. Esto orientado a sus ubicaciones geográficas específicas (Estado y Condado/County) junto a sus tendencias de rating. Complementando así con la vigente competencia en cada locación; ordenado desde el elemento con mas rating hacia el menor. En el mismo se utilizó la librería sklearn donde se extrajo las sublibrerias StandardScaler para estandarizar los datos, KMeans para el proceso de clsutering y por ultimo una segunda libreria llamada geodesic del conjunto de geopy para identificar los condados y Estados de las ubicaciones investigadas.')
code2 = '''# Escalar las variables de entrada
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar el algoritmo de clustering K-means
kmeans = KMeans(n_clusters=50, random_state=42)
kmeans.fit(X_scaled)

# Obtener el centroide (zona central) de cada cluster y calcular el radio espacial del cluster
centers = scaler.inverse_transform(kmeans.cluster_centers_)

avg_ratios = []
densities = []
proximities = []
competitors = []

for i, center in enumerate(centers):
    cluster_points = data_area.loc[kmeans.labels_ == i, ['latitude', 'longitude']]
    distances = cluster_points.apply(lambda point: geodesic((center[0], center[1]), (point['latitude'], point['longitude'])).kilometers, axis=1)

    cluster_avg_ratings = data_area['avg_rating'][kmeans.labels_ == i]
    avg_ratio = np.mean(cluster_avg_ratings)
    avg_ratios.append(avg_ratio)

    density = len(cluster_points)
    densities.append(density)

    proximity = distances.mean()
    proximities.append(proximity)

    competitor_count = len(data_area[(kmeans.labels_ == i) & (data_area['avg_rating'] > avg_ratio)])
    competitors.append(competitor_count)'''
st.code(code2, language='python')

st.text('ejemplo: resultado del modelo entrenado')
st.image('./img/m_zona1.png')


