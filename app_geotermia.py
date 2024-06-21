import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import streamlit as st

st.set_page_config(page_title="App gradiente geotérmico",
                   layout="centered",
                   initial_sidebar_state="auto")

st.title("App que permite estimar el gradiente geotérmico por departamento en Colombia")

datos_geotermicos = pd.read_csv('Datos_departamento.csv',sep=';')
lista_deptos= datos_geotermicos['DEPART'].unique().tolist()
lista_deptos.insert(0,'Todos')

st.sidebar.header('Escoja el departamento de interés: ')

departamentos = st.sidebar.selectbox('',lista_deptos)
def datos():
    datos_geotermicos_d = pd.read_csv('Datos_departamento.csv',sep=';')
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

