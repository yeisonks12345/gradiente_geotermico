# App que permite estimar el gradiente geotérmico por departamento en Colombia
A partir de la investigación realizada por; Juan C. Mejía Fragoso,  Manuel A. Flórez, Rocío Bernal Olaya en el paper Predicting the geothermal gradient in Colombia: A machine learning approach, se usan 3306 registros, las varaibles para usadas para estimar el gradiente geotermico son: produndidad de moho, anomalia magnenita, curie depth entre otros, para estimar el potencial geotermico se prueba una red neuronal FCNN (Fully connected neural network), es un tipo de red neuronal artificial donde cada neurona en una capa está conectada a cada neurona en la siguiente capa. Adicionalmente se concatenan los departamentos en Colombia para poder segmentar las zonas de interes de una manera mas intuitiva, para el despliegue se usa la libreria streamlit de python.