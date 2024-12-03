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
El siguiente script se encarga responder a la primera parte de la pregunta: 

¿Cuáles son los genes que como consecuencia de la infección por R. giardini cambian su expresión,
con respecto al control y R. tropici, y cuáles son las consecuencias de estos cambios en las vías 
dependientes de nitrógeno y el crecimiento?

Genera 4 gráficos interactivos por medio de la libreria de `plotly.express` para responder sobre los efectos
de la infección en la expresión génica. Al final, se crea un archivo con las IDs de los genes identificados.

Salida:
    Achivos:
        Id_list.txt: Archivo de Ids de genes en el directorio results.

Se asume la sig organizacion del directorio de trabajo:
```
|-- data
|   |-- Complete_repositorio_de_RNAseq.xlsx
|   |-- N5vsNE.xlsx
|   |-- NEvsNI.xlsx
|-- src 
    |-- differanaliza.py
|--results
```
usage:
    python differanaliza.py
'''
#==================CODE===================
# Definimos las rutas de los archivos
file_N5vsNE = './data/N5vsNE.xlsx'
file_NEvsNI= './data/NEvsNI.xlsx'
# Se leen los archivos excel con pandas 
N5vsNE = pd.read_excel(file_N5vsNE, sheet_name="O'Rourke_AddFile14_NEvN5")
NEvsNI = pd.read_excel(file_NEvsNI, sheet_name="O'Rourke_AddFile15_NEvNI")

# Se seleccionan las columnas de interes: 'GeneID', 'NE', 'N5' y 'FoldChange'
N5vsNE = N5vsNE[['GeneID', 'NE', 'N5', 'FoldChange']]
NEvsNI = NEvsNI[['GeneID', 'NE', 'NI', 'FoldChange']]

# ================Grafico_1====================
# =================N5_vs_NE===================
'''
Grafica de dispersion de los niveles de expresión de los genes dentro de N5 que corresponden a los Nódulos 
de pre-fijación (fix+) recogidos 5 DAI(days after inoculation) vs NE que corresponden a los nódulos fix+ recogidos
21 DAI(days after inoculation) a partir del dataframe N5vsNE
'''
# Se crea un gráfico de dispersion basado en el DataFrame
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

# ================Grafico_2====================
# =================NE_vs_NI===================
'''
Grafica de dispersion de los niveles de expresión de los genes dentro de NE que corresponden a los nódulos 
fix+ recogidos 21 DAI(days after inoculation) vs NI que corresponde a los nódulos fix- recogidos 21 DAI(days
after inoculation) a partir del dataframe NEvsNI
'''
figNEvsNI = px.scatter(NEvsNI,
                    x='GeneID', # Columna de identificadores de genes (eje X)
                    y= 'FoldChange', # Columna para el cambio de expresion (cambio de expresion)
                    title= 'Comparacion de Patrones de Expresion: NE vs NI', # Titulo
                    labels={ # Etiquetas para los ejes
                        'GeneID': 'ID del Gen', 'FoldChange': 'Log2Fold Change'})
# Mostrar la grafica interactiva en el navegador 
figNEvsNI.show() 

# ================Grafico_3====================
# ===============Interseccion_de_N5_vs_NE_y_NE_vs_NI====================
'''
Se combinan los dataframe anteriores y se genera una grafica de dispersión de la intersección
entre sus niveles de expresión.

Se busca encontrar los genes con expresion diferencial en ambas comparaciones: Busamos identificar patrones
comunes o únicos en los cambios de expresión.
'''
# Se combinan los DataFrames N5vsNE y NEvsNI 
# Se utilizan sufijos para lidiar con las columnas con mismo nombre 
combi = pd.merge(N5vsNE, NEvsNI, on= 'GeneID', suffixes=('_N5vsNE', '_NEvsNI')) 
# Para bsucar la exp diferencial solo ocupamos las columnas de ID y FoldChange`s
combi = combi[['GeneID', 'FoldChange_N5vsNE', 'FoldChange_NEvsNI']]
# Se calcula un Foldchange combiando
combi['FoldChange_N5vsNI'] = combi['FoldChange_N5vsNE'] + combi['FoldChange_NEvsNI']


N5vsNI = combi[['GeneID', 'FoldChange_N5vsNI']]

# Creacion del grafico
figN5vsNI = px.scatter(N5vsNI,
                    x='GeneID',
                    y= 'FoldChange_N5vsNI',
                    title= 'Log2Fold Change: N5 vs NI',
                    labels={
                        'GeneID': 'ID del Gen', 'FoldChange': 'Log2Fold Change'})
# Mostrar la grafica interactiva en el navegador 
figN5vsNI.show()

# ========================Grafico_4============================
# ==============Genes_Diferenciales_Destacados=================
'''
Se identifican genes con expresiones diferenciales específicas:
    - Categoría 1: Genes con menor expresión en NE y mayor en NI.
        + NE FoldChange_N5vsNE < 0
        + NI con un FoldChange_N5vsNI > 0

    - Categoría 2: Genes con mayor expresión en NE y menor en NI.
        + NI con un FoldChange_N5vsNI < 0
        + NE con un FoldChange_N5vsNE > 0
'''
# Filtrado por las categorias mencionadas 
diff1 = combi[(combi['FoldChange_N5vsNE'] < 0) & (combi['FoldChange_N5vsNI'] > 0)]
diff1['Categoría:'] = 'NE < 0, NI >0'
diff2 =  combi[(combi['FoldChange_N5vsNE'] > 0) & (combi['FoldChange_N5vsNI'] < 0)]
diff2['Categoría:'] = 'NE > 0, NI <0'

# Combinacion de Genes Filtrados
# Obtener un conjunto de genes diferenciales 
diferenciada = pd.concat([diff1,diff2])

# Creacion del grafico
fig_diff = px.scatter(diferenciada, 
                x='FoldChange_N5vsNE', # Columna de identificadores de genes (eje X)
                y='FoldChange_N5vsNI', # Columna para el cambio de expresion (cambio de expresion)
                title='Genes con expresión diferencial respecto a N5', # Titulo
                labels={ # Etiquetas para los ejes 
                    'GeneID': 'ID del Gen', 'FoldChange_N5vsNI': 'Nivel de Expresion', 'FoldChange_N5vsNE': 'Nivel de Expresión'},
                hover_data= ['GeneID'])

fig_diff.add_shape(type="line", x0=0, x1=0, y0=min(combi["FoldChange_N5vsNI"]), y1=max(combi["FoldChange_N5vsNI"]),
            line=dict(color="Black", dash="dash"))
fig_diff.add_shape(type="line", x0=min(combi["FoldChange_N5vsNE"]), x1=max(combi["FoldChange_N5vsNE"]), y0=0, y1=0,
            line=dict(color="Black", dash="dash"))
fig_diff.show()

# ======Archivo Final======
# Pasar a un archivo las IDS
diferenciada_copy = diferenciada.copy()
# Extraer la columna 'GeneID' como una lista
Id_list = diferenciada_copy['GeneID'].tolist()
# Guardar la lista de IDs en un archivo 
path = 'results/id_list.txt'
with open(path, 'w') as f:
    for id in Id_list:
        f.write(f"{id}\n")