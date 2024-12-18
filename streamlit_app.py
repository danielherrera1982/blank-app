import streamlit as st
import pandas as pd
import plotly.express as ptl
import seaborn as sns
import requests

# URL del web service
url = "https://api.latam-ia.com/api/Measures" 

@st.cache_data
def load_sensors(rows=500):
  try:
    # Hacer la solicitud GET
    response = requests.get(url)
    
    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta JSON a un DataFrame
        json = response.json()
        data = pd.DataFrame(json)
    return data
  except Exception as e:
    print(f"Ocurrió un error: {e}")

data = load_sensors()

st.title("Dashboard IoT")
st.sidebar.title("Filtros")
mostrar = st.sidebar.checkbox("Mostrar análisis completo")

st.write(f"Análisis con data completa")
st.dataframe(data, hide_index=True, use_container_width=True)

#Histograma
histograma = ptl.histogram(data, x='measure', title='Histograma de edades', nbins=10)
st.plotly_chart(histograma)
