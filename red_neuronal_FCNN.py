import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
# r2 de 0.3161, MAE 3.1345
# lectura de datos
data = pd.read_csv('input_y_dpto.csv',sep=';')

# separar los datos en features y target
features = data.iloc[:, 1:-1].values
target = data.iloc[:, -1].values

# Escalado de las variables con minmax

scaler = MinMaxScaler()
features=  scaler.fit_transform(features)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Construcción del modelo de red neuronal completamente conectada
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

# Compilamos el modelo
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

# Entrenamiento del modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluación del modelo
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f'Mean Absolute Error on test set: {test_mae}')

# Predicción sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Cálculo del R² y MAE
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f'R² on test set: {r2}')
print(f'Mean Absolute Error on test set: {mae}')


# generar predicción con FCNN a todos los datos
data['Predicted Geothermal Gradient (C/Km)'] = model.predict(features)
datos = data[['Longitude','Latitude','DEPART','Predicted Geothermal Gradient (C/Km)']]

datos.to_csv('Datos_departamento1.csv')
#data['prediccionfcnngg'] = model.predict(features)
#data.to_csv('datosconfcnn.csv')


