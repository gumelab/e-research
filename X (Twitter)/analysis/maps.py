import time
from selenium import webdriver
import pandas as pd
from geopy.geocoders import Nominatim
import folium

# Carregar os dados do CSV
df = pd.read_csv('seuarquivo.csv')

# Criar um objeto geolocalizador
geolocator = Nominatim(user_agent="my_geocoder")

# Função para obter as coordenadas de uma cidade
def get_coordinates(city):
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Adicionar colunas de latitude e longitude ao DataFrame
df['Latitude'], df['Longitude'] = zip(*df['place'].apply(get_coordinates))

# Remover linhas com coordenadas ausentes
df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# Criar o mapa
map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=5)

# Adicionar marcadores para cada cidade no mapa
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['place']).add_to(map)

# Salvar o mapa como um arquivo HTML temporário
map.save('mapa.html')

# Configurar o navegador para capturar uma captura de tela da página HTML
browser = webdriver.Chrome()  # Você pode precisar baixar o webdriver adequado para seu navegador
browser.get('file://' + 'mapa.html')  # Abra o arquivo HTML no navegador
time.sleep(5)  # Espere um pouco para garantir que o mapa seja carregado completamente

# Capturar uma captura de tela do mapa
browser.save_screenshot('mapa.png')

# Fechar o navegador
browser.quit()
