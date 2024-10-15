import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos para R. tropici y R. giardini
df_tropici = pd.read_excel("./data/Complete repository Nodulation.xlsx", sheet_name="Nod21NE", header=1) 
df_giardini = pd.read_excel("./data/Complete repository Nodulation.xlsx", sheet_name="Nod21NI", header=1)

# Imprimir las columnas para verificar que se cargaron correctamente
print(df_giardini.columns)
print(df_tropici.columns)

# Filtrar genes de interés basados en la columna 'Expression'
# Esto agrupa los datos según las categorías de la columna 'Expression'
expression_counts = df_tropici['Expression'].value_counts()

# Mostrar el conteo de las categorías en la columna 'Expression'
print(expression_counts)

# Graficar la distribución de las categorías de expresión
expression_counts.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange'])
plt.title("Distribución de expresión génica: R. tropici vs R. giardini")
plt.ylabel("Número de genes")
plt.xlabel("Categoría de expresión")
plt.xticks(rotation=45)
plt.show()
