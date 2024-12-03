#=============DATA================
# AUTHOR: Bautista Daniel Zaid & Palma Luna Melissa
# MAIL: danielzb@lcg.unam.mx or melissap@lcg.unam.mx, 
# TITLE: senescencia.py
# DATE: NOV 2024
#=================================
#=============IMPORTS=============
import pandas as pd
# Libreria Plotly Express para graficar de manera interactiva
import plotly.express as px 
#=================================
'''
El siguiente script se encarga responder la pregunta: 

¿Cómo afecta el envejecimiento prematuro a los tejidos infectados por R. giardini y qué relación 
tiene con la expresión de genes asociados a la senescencia celular? ¿Qué relación hay entre la 
infeccion por R. giardini tiene con la expresión de genes asociados a la senescencia celular? 

Por lo que: 
El script realiza filtra genes asociados a "Senescencia" en base a su descripción funcional, posteriormente 
exporta los resultados y los guarda en en un archivo CSV, y crea un gráfico de dispersión que muestra la relación
entre el ID del gen y la expresión diferencial.

```
|-- data
|   |-- Complete_repositorio_de_RNAseq.xlsx
|   |-- N5vsNE.xlsx
|   |-- NEvsNI.xlsx
|-- src 
    |-- differanaliza.py
    |-- filtered_gene_data.csv
```

Datos de entrada: 
    Archivos:
    - NEvsNI.xlsx
Salida: 
    filtered_sensc-assocd_data.csv

usage:
    python senescencia.py
'''
# Cargar el archivo Excel
file_NEvsNI= './data/NEvsNI.xlsx'
# Se leen los archivos excel con pandas 
NEvsNI = pd.read_excel(file_NEvsNI, sheet_name="O'Rourke_AddFile15_NEvNI")

# Filtrar filas donde 'Pfam_Description' contenga "senescence" (insensible a mayúsculas/minúsculas)
NEvsNI = NEvsNI[NEvsNI['Pfam_Description'].str.contains("senescence", case=False, na=False)]

# Guardar los resultados en un archivo CSV
output_file = "results/filtered_sensc-assocd_data.csv"
NEvsNI.to_csv(output_file, index=False)

print(f"Datos filtrados guardados en {output_file}")

# Generar Grafics de Dispersion 
figNEvsNI = px.scatter(NEvsNI,
                    x='GeneID', # IDs de los genes
                    y= 'FoldChange', # Cambio de expresion
                    title= 'Log2Fold Change: NE vs NI',
                    labels={
                        'GeneID': 'ID del Gen', 'FoldChange': 'Log2Fold Change'})
figNEvsNI.show()