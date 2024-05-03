import numpy as np
import pandas as pd

# Pr
df = pd.read_csv('archivo.csv')


df.columns = df.columns.str.strip().str.replace('\n', '', regex=True).str.replace('  ', ' ', regex=True)

poblacion = df.shape[0]

n = 20

# Obtener la cantidad de personas por género
counts = df['GENERO'].value_counts()

sample_sizes = (counts / poblacion * n).round().astype(int)

# si la suma no es igual a la deseada
if sample_sizes.sum() != n:
    diff = n - sample_sizes.sum()
    sample_sizes[sample_sizes.idxmax()] += diff

# Realizar el muestreo estratificado
stratified_sample = pd.DataFrame()
for gender, size in sample_sizes.items():
    sample = df[df['GENERO'] == gender].sample(n=size, random_state=1)  # random_state para reproducibilidad
    stratified_sample = pd.concat([stratified_sample, sample], ignore_index=True)

# Mostrar la muestra estratificada
# print(stratified_sample)
############################################################################################################
# CONGLOMERADO
# Identificar todos los posibles conglomerados
conglomerates = df['EDAD'].unique()

# Seleccionar 3 conglomerados al azar
selected_conglomerates = np.random.choice(conglomerates, size=3, replace=False)

# Filtrar el DataFrame para incluir solo los miembros de los conglomerados seleccionados
cluster_sample = df[df['EDAD'].isin(selected_conglomerates)]

# print(cluster_sample)


############################################################################################################
#SISTEMATICO
step = df.shape[0] // n

# Creamos una lista de índices de fila para seleccionar los elementos
indices = np.arange(0, df.shape[0], step)

# Seleccionamos las filas correspondientes a los índices calculados
systematic_sample = df.iloc[indices]

print(systematic_sample)