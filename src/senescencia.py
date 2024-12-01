import pandas as pd
import plotly.express as px

# Cargar el archivo Excel
file_NEvsNI= './data/NEvsNI.xlsx'
# Se leen los archivos excel con pandas 
NEvsNI = pd.read_excel(file_NEvsNI, sheet_name="O'Rourke_AddFile15_NEvNI")

# Filtrar filas donde 'PANTHER_DESCRIPTION' contenga "leghemoglobin" (insensible a mayúsculas/minúsculas)
NEvsNI = NEvsNI[NEvsNI['Pfam_Description'].str.contains("senescence", case=False, na=False)]

# Guardar los resultados en un archivo CSV
output_file = "filtered_sensc-assocd_data.csv"
NEvsNI.to_csv(output_file, index=False)

print(f"Datos filtrados guardados en {output_file}")

figNEvsNI = px.scatter(NEvsNI,
                    x='GeneID',
                    y= 'FoldChange',
                    title= 'Log2Fold Change: NE vs NI',
                    labels={
                        'GeneID': 'ID del Gen', 'FoldChange': 'Log2Fold Change'})
figNEvsNI.show()