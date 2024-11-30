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
El siguiente script se encarga de generar una grafica de dispersion interactiva de 

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
file_NEvsNI = './data/NEvsNI.xlsx'
# Se leen los archivos excel con pandas 
N5vsNE = pd.read_excel(file_N5vsNE, sheet_name="O'Rourke_AddFile14_NEvN5")
NEvsNI = pd.read_excel(file_NEvsNI, sheet_name="O'Rourke_AddFile15_NEvNI")

# Se seleccionan las columnas de interes: 'GeneID', 'NE', 'N5' y 'FoldChange'
N5vsNE = N5vsNE[['GeneID', 'NE', 'N5', 'FoldChange']]
NEvsNI = NEvsNI[['GeneID', 'NE', 'NI', 'FoldChange']]

# ===Creacion de Grafico===

# Se crea unu gráfico de dispersion basado en el DataFrame
# Utilizamos 'GeneID' como eje X y 'FoldChange' como eje Y.
figN5vsNE = px.scatter(N5vsNE, 
                x='GeneID', # Columna de identificadores de genes (eje X)
                y='FoldChange', # Columna para el cambio de expresion (cambio de expresion)
                title='Comparacion de Patrones de Expresion: N5 vs NE', # Titulo
                labels={ # Etiquetas para los ejes 
                    'GeneID': 'ID del Gen', 'FoldChange': 'Nivel de Expresion'})
figN5vsNE.update_traces(marker=dict(size=5, color='purple')) # Aspectos graficos: size de los puntos y color

# Mostrar la grafica interactiva en el navegador 
figN5vsNE.show()

figNEvsNI = px.scatter(NEvsNI,
                       x='GeneID',
                       y= 'FoldChange',
                       title= 'Log2Fold Change: NE vs NI',
                       labels={
                           'GeneID': 'ID del Gen', 'FoldChange': 'Log2Fold Change'})
figNEvsNI.show()

combi = pd.merge(N5vsNE, NEvsNI, on= 'GeneID', suffixes=('_N5vsNE', '_NEvsNI'))
combi = combi[['GeneID', 'FoldChange_N5vsNE', 'FoldChange_NEvsNI']]
combi['FoldChange_N5vsNI'] = combi['FoldChange_N5vsNE'] + combi['FoldChange_NEvsNI']

N5vsNI = combi[['GeneID', 'FoldChange_N5vsNI']]

figN5vsNI = px.scatter(N5vsNI,
                       x='GeneID',
                       y= 'FoldChange_N5vsNI',
                       title= 'Log2Fold Change: N5 vs NI',
                       labels={
                           'GeneID': 'ID del Gen', 'FoldChange': 'Log2Fold Change'})
figN5vsNI.show()
