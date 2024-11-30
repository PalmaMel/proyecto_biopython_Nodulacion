#=============DATA================
# AUTHOR: Bautista Daniel Zaid & Palma Luna Melissa
# MAIL: danielzb@lcg.unam.mx or melissap@lcg.unam.mx, 
# TITLE: differanaliza.py
# DATE: OCT 2024
#=================================
#=============IMPORTS=============
import pandas as pd
# Libreria Plotly Express para graficar de manera interactiva
import plotly.express as px 
#=================================
'''
Description:
El siguiente script se encarga de generar una grafica de dispersion interactiva de los niveles de expresión de
los genes dentro de N5 que corresponden a los Nódulos de pre-fijación (fix+) recogidos 5 DAI(days after inoculation)
vs NI que corresponde a los nódulos fix+ recogidos 21 DAI(days after inoculation)

Se asume la sig organizacion del directorio de trabajo:
```
|-- data
|   |-- Complete_repositorio_de_RNAseq.xlsx
|   |-- N5vsNE.xlsx
|   |-- NEvsNI.xlsx
|-- src 
    |-- differanaliza.py
```
usage:
    python differanaliza.py
'''
#==================CODE===================
# Definimos las rutas de los archivos
file_N5vsNE = './data/N5vsNE.xlsx'
# Se leen los archivos excel con pandas 
N5vsNE = pd.read_excel(file_N5vsNE, sheet_name="O'Rourke_AddFile14_NEvN5")
# Se seleccionan las columnas de interes: 'GeneID', 'NE', 'N5' y 'FoldChange'
N5vsNE = N5vsNE[['GeneID', 'NE', 'N5', 'FoldChange']]

# ===Creacion de Grafico===

# Se crea unu gráfico de dispersion basado en el DataFrame
# Utilizamos 'GeneID' como eje X y 'FoldChange' como eje Y.
fig = px.scatter(N5vsNE, 
                x='GeneID', # Columna de identificadores de genes (eje X)
                y='FoldChange', # Columna para el cambio de expresion (cambio de expresion)
                title='Comparacion de Patrones de Expresion: N5 vs NE', # Titulo
                labels={ # Etiquetas para los ejes
                    'GeneID': 'ID del Gen', 'FoldChange': 'Nivel de Expresion'})
fig.update_traces(marker=dict(size=5, color='purple')) # Aspectos graficos: size de los puntos y color

# Mostrar la grafica interactiva en el navegador 
fig.show()