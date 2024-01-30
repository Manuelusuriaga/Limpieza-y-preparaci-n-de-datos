import pandas  as pandas
import numpy as numpy

df = pandas.read_csv("archivo.csv")

# 1.Verificar que no existan valores faltantes   
print(df.isna())

# 2.Verificar que no existan filas repetidas
print(df.duplicated())

# 3.Verificar si existen valores atípicos y eliminarlos
# Calcular el rango intercuartil (IQR)
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
# Definir los límites para detectar valores atípicos
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# Filtrar los valores atípicos
df_cleaned = df[(df >= lower_bound) & (df <= upper_bound)]

# Resultado
print(df_cleaned)

# 4. Crear una columna que categorice por edades 0-12: Niño, 13-19: Adolescente, 20-39: Jóvenes adulto, 40-59: Adulto60-...: Adulto mayor

bins = [0, 12, 19, 39, 59, float('inf')]
labels = ['Niño', 'Adolescente', 'Joven Adulto', 'Adulto', 'Adulto Mayor']

df['Categoria_Edad'] = pandas.cut(df['age'], bins=bins, labels=labels, right=False)

# 5.Guardar el resultado como un archivo CSV
df.to_csv('resultado_categorizacion.csv', index=False)

print(df)