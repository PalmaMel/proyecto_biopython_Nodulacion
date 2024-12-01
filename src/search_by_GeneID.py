import pandas as pd

# Cargar la lista de GeneIDs desde un archivo de texto
with open("results/id_list.txt", "r") as file:
    gene_ids = [line.strip() for line in file if line.strip()]


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
output_file = "filtered_gene_data.csv"
filtered_data.to_csv(output_file, index=False)

print(f"Datos filtrados guardados en {output_file}")
