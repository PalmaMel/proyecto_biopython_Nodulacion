#=============DATA================
# AUTHOR: Bautista Daniel Zaid & Palma Luna Melissa
# MAIL: danielzb@lcg.unam.mx or melissap@lcg.unam.mx, 
# TITLE: search_by_GeneID.py
# DATE: NOV 2024
#=================================
#=============IMPORTS=============
import pandas as pd
#=================================

'''
Description:
El siguiente script se encarga de generar filtrar los datos y generar el archivo 'filtered_gene_data.csva' que responden a 
la segunda parte parte de la pregunta: 

¿Cuáles son los genes que como consecuencia de la infección por R. giardini cambian su expresión,
con respecto al control y R. tropici, y cuáles son las consecuencias de estos cambios en las vías 
dependientes de nitrógeno y el crecimiento?

El script obtiene informacion de los genes obtenidos por el script de differanaliza.py.

Se asume la sig organizacion del directorio de trabajo:
```
|-- data
|   |-- Complete_repositorio_de_RNAseq.xlsx
|   |-- N5vsNE.xlsx
|   |-- NEvsNI.xlsx
|-- src 
    |-- differanaliza.py
|--results
|   |--id_list.txt
```
Datos de entrada: 
    id_list.txt: Archivo con los Ids con expresion diferencial
Salida: 
    filtered_gene_data.csv: Archivo con los datos filtrados de los genes relevantes, como:
        - descripciones funcionales
        - anotaciones asociadas.
usage:
    python search_by_GeneID.py
'''

# Cargar la lista de GeneIDs desde un archivo de texto
with open("results/id_list.txt", "r") as file:
    gene_ids = [line.strip() for line in file if line.strip()] # Se eliminan lineas vacias

# Se define ruta del archivo
file_NEvsNI= './data/NEvsNI.xlsx'

# Se leen los archivos excel con pandas 
NEvsNI = pd.read_excel(file_NEvsNI, sheet_name="O'Rourke_AddFile15_NEvNI")

# Filtrar las filas que contienen los GeneIDs
filtered_data = NEvsNI[NEvsNI['GeneID'].isin(gene_ids)]

# Seleccionar las columnas relevantes
columns_to_save = [
    'GeneID', 'PfamID', 'Pfam_Description', 'PANTHER_ID', 'Panther_Description ',
    'KOG_ID', 'KOG_Description ', 'EC_ID', 'EC_Description', 'GO_Description ',
    'Transcription Factor Family'
]
filtered_data = filtered_data[columns_to_save]

# Guardar los resultados en un archivo CSV 
output_file = "results/filtered_gene_data.csv"
filtered_data.to_csv(output_file, index=False)

print(f"Datos filtrados guardados en {output_file}")
