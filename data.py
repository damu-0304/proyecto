import sqlite3
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Conectar a la base de datos
conn = sqlite3.connect('proyecto.db')

# Leer una tabla en un DataFrame (reemplaza 'nombre_tabla' con el nombre de la tabla que quieras consultar)
df = pd.read_sql_query("SELECT * FROM test_data", conn)

# Mostrar los datos
print(df["variable_1"])

# Crear el histograma
plt.hist(df["variable_1"], bins=200, color='aqua', edgecolor='blue', alpha=0.7)

# Añadir título y etiquetas
plt.title('Histograma de variable_1')
plt.xlabel('Valores de variable_1')
plt.ylabel('Frecuencia')

plt.savefig("Variable1")
# Mostrar el histograma
plt.show()

# Crear el histograma
plt.hist(df["variable_2"], bins=200, color='lime', edgecolor='limegreen', alpha=0.7)

# Añadir título y etiquetas
plt.title('Histograma de variable_2')
plt.xlabel('Valores de variable_2')
plt.ylabel('Frecuencia')

plt.savefig("Variable2")
# Mostrar el histograma
plt.show()

# Cerrar la conexión
conn.close()
