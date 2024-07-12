import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import streamlit as st

st.set_page_config(page_title="App gradiente geotérmico",
                   layout="centered",
                   initial_sidebar_state="auto")

st.title("App que permite estimar el gradiente geotérmico por departamento en Colombia")
st.write("A partir de la investigación realizada por; Juan C. Mejía Fragoso,  Manuel A. Flórez, Rocío Bernal Olaya en el paper Predicting the geothermal gradient in Colombia: A machine learning approach, se usan 3306 registros cque contienen datos como: la longitud, latitud ,produndidad de moho, anomalia magnenita, curie depth entre otros. A partir de estos datos se estima el gradiente geotermico en Colombia usando una red neuronal FCNN (Fully connected neural network), la cual es un tipo de red neuronal artificial donde cada neurona en una capa está conectada a cada neurona en la siguiente capa. Como métricas del modelo se obtiene un R2 de 0.31 y un MAE de 3.13.")
st.title("Desarrollo de la aplicación")
st.write('Para desarrollar la aplicación, se usa el archivo "data_pre_norm.csv" insumo de la investigación de Mejía et al, (2024), como novedad se concatenan los departamentos en Colombia para poder segmentar las zonas de interes de una manera mas intuitiva. Para el despliegue se usa la libreria streamlit de python que permite desarrollar aplicaciones web a partir de modelos de inteligencia artificial de forma ágil.')
st.title('Indicaciones para usar la app')
st.write("En el menú de la izquierda encontrará una lista desplegable por departamento, seleccione el de su interés y la aplicación mostrara una nube de puntos que estiman el gradiente geotermico en la zona seleccionada, de igual forma es posible descargar un listado con las coordenadas y el valor númerico del gradiente geotermico.")
datos_geotermicos = pd.read_csv('Datos_departamento1.csv',)
lista_deptos= datos_geotermicos['DEPART'].unique().tolist()
lista_deptos.insert(0,'Todos')

st.sidebar.header('Escoja el departamento de interés: ')

departamentos = st.sidebar.selectbox('',lista_deptos)
def datos():
    datos_geotermicos_d = pd.read_csv('Datos_departamento1.csv')
    if departamentos == 'Todos':
        return datos_geotermicos_d
    else:
        return datos_geotermicos_d[datos_geotermicos_d['DEPART']==departamentos]
datos_filtro_dpto = datos()
cmap = plt.cm.jet
predicted_gdf = gpd.GeoDataFrame(datos_filtro_dpto, geometry=gpd.points_from_xy(datos_filtro_dpto['Longitude'], datos_filtro_dpto['Latitude']))

# Determine the color range
vmin = predicted_gdf['Predicted Geothermal Gradient (C/Km)'].min()
vmax = predicted_gdf['Predicted Geothermal Gradient (C/Km)'].max()

# Create a subplot
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the predicted values
predicted_plot = predicted_gdf.plot(column='Predicted Geothermal Gradient (C/Km)', cmap=cmap, markersize=5, legend=True, ax=ax)
ax.set_title('Predicted Values Map')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Calculate grid positions based on your data's latitude and longitude
min_lon, max_lon = -78, -66
min_lat, max_lat = -4, 12
lon_grid = list(range(int(min_lon), int(max_lon) + 1, 2))
lat_grid = list(range(int(min_lat), int(max_lat) + 1, 2))

# Add gridlines for latitude and longitude
ax.set_xticks(lon_grid)
ax.set_yticks(lat_grid)
ax.grid()

# Load world country geometries
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Subset the world dataset to only include countries within your area of interest
world = world.cx[-74:-73, 4:5]

# Plot country borders within your area of interest
world.boundary.plot(ax=ax, linewidth=0.5, color='black')

# Show the plot
st.write(fig)


st.sidebar.header('Listado por rangos de gradiente, permite imprimir un listado con latitud y longitud: ')
rangos = st.sidebar.selectbox('',['15-24 °c/km','25-34°c/km','mayor a 35 °c/km'])

if rangos == '15-24 °c/km':

    st.write(datos_filtro_dpto[datos_filtro_dpto['Predicted Geothermal Gradient (C/Km)']<=24].reset_index())
elif rangos == '25-34°c/km':
    st.write(datos_filtro_dpto[(datos_filtro_dpto['Predicted Geothermal Gradient (C/Km)'] >= 25) & (datos_filtro_dpto['Predicted Geothermal Gradient (C/Km)']<=34)].reset_index())
elif rangos == 'mayor a 35 °c/km':
 st.write(datos_filtro_dpto[datos_filtro_dpto['Predicted Geothermal Gradient (C/Km)']>34].reset_index())

