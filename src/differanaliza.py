import pandas as pd
import matplotlib.pyplot as plt

file_N5vsNE = './data/N5vsNE.xlsx'
file_NEvsNI = './data/NEvsNI.xlsx'

N5vsNE = pd.read_excel(file_N5vsNE, sheet_name="O'Rourke_AddFile14_NEvN5")
N5vsNE = N5vsNE[['GeneID', 'NE', 'N5', 'FoldChange']]

plt.figure(figsize=(12,6))

plt.plot(N5vsNE['GeneID'], N5vsNE['FoldChange'], label='FoldChange', marker='o', color='purple')

# Añadir títulos y etiquetas
plt.title('Comparación de Patrones de Expresión: N5 vs NE')
plt.ylabel('Nivel de Expresión')
plt.xticks(rotation=90)  # Rotar etiquetas de genes para mejor visualización
plt.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()