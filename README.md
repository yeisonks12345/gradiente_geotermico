# App que permite estimar el gradiente geotérmico por departamento en Colombia
A partir de la investigación realizada por; Juan C. Mejía Fragoso,  Manuel A. Flórez, Rocío Bernal Olaya en el paper Predicting the geothermal gradient in Colombia: A machine learning approach, se usan 3306 registros que contienen datos como: la longitud, latitud ,produndidad de moho, anomalía magnénita, curie depth entre otros. A partir de estos datos se estima el gradiente geotérmico en Colombia usando una red neuronal FCNN (Fully connected neural network), la cual es un tipo de red neuronal artificial donde cada neurona en una capa está conectada a cada neurona en la siguiente capa. Como métricas del modelo se obtiene un R2 de 0.31 y un MAE de 3.13.
# Desarrollo de la aplicación
Para desarrollar la aplicación, se usa el archivo "data_pre_norm.csv" insumo de la investigación de Mejía et al, (2024), como novedad se concatenan los departamentos en Colombia para poder segmentar las zonas de interés de una manera mas intuitiva. Para el despliegue se usa la libreria streamlit de python que permite desarrollar aplicaciones web a partir de modelos de inteligencia artificial de forma ágil.
# Indicaciones para usar la app
En el menú de la izquierda encontrará una lista desplegable por departamento, seleccione el de su interés y la aplicación mostrara una nube de puntos que estiman el gradiente geotérmico en la zona seleccionada, de igual forma es posible descargar un listado con las coordenadas y el valor númerico del gradiente geotérmico.

# Despliegue en local de la app
Para desplegar la aplicación, clone el repositorio, posteriormente instale las siguientes librerias que encuentra en el archivo requierements.txt:
1. pandas
2. streamlit
3. geopandas
4. matplotlib



