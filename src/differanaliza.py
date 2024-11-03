#=============DATA================
# AUTHOR: Bautista Daniel Zaid & Palma Luna Melissa
# MAIL: danielzb@lcg.unam.mx or melissap@lcg.unam.mx, 
# TITLE: differanaliza.py
# DATE: OCT 2024
#=================================
#=============IMPORTS=============
import pandas as pd
import matplotlib.pyplot as plt
#=================================
'''
Description:

Se asume que hay una carpeta llamada data
usage:
    python differanaliza.py
'''
#==================CODE===================
# Definimos las rutas de los archivos
file_N5vsNE = './data/N5vsNE.xlsx'
file_NEvsNI = './data/NEvsNI.xlsx'
# Se leen los archivos excel con pandas 
N5vsNE = pd.read_excel(file_N5vsNE, sheet_name="O'Rourke_AddFile14_NEvN5")
# Se seleccionan las columnas de interes: 'GeneID', 'NE', 'N5' y 'FoldChange'
N5vsNE = N5vsNE[['GeneID', 'NE', 'N5', 'FoldChange']]
# Se establecen dimensiones para el grafico
plt.figure(figsize=(12,6))
# se crea el grafico de lineas
plt.plot(N5vsNE['GeneID'], N5vsNE['FoldChange'], label='FoldChange', marker='o', color='purple')

# Titulos y etiquetas
plt.title('Comparacion de Patrones de Expresion: N5 vs NE')
plt.ylabel('Nivel de Expresion')
plt.xticks(rotation=90)  # Rotar etiquetas de genes para mejor visualizacion
plt.legend()

# Mostrar la grafica
plt.tight_layout()
plt.show()