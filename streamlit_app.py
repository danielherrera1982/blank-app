import streamlit as st
import pandas as pd
import plotly.express as ptl
import seaborn as sns
import requests
import matplotlib.pyplot as plt

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

# grafico

filtered_df = data[data['sensor_uq'] == 'A228DE51-023B-43B0-B652']
# Asegurarse de que la columna add_date sea de tipo datetime
#filtered_df['add_date'] = pd.to_datetime(filtered_df['add_date'], errors='coerce')
# Configurar el índice del DataFrame para usar add_date
filtered_df = filtered_df.sort_values('add_date')  # Ordenar por fecha
#filtered_df.set_index('add_date', inplace=True)

st.write(f"Análisis con data filtrada")
st.dataframe(filtered_df, hide_index=True, use_container_width=True)

ciudad_desercion = ptl.line(filtered_df ,x='add_date', y='measure', title='Deserción por ciudad')
st.plotly_chart(ciudad_desercion)

#plot = plt.plot(filtered_df.index, filtered_df['measure'], label='Temperatura', marker='o', linestyle='-', color='blue')
#st.plotly_chart(plot)
