import pandas as pd
import matplotlib.pyplot as plt

df_tropici = pd.read_excel("./data/Complete repository Nodulation.xlsx", sheet_name="Nod21NE", header=1) 
df_giardini = pd.read_excel("./data/Complete repository Nodulation.xlsx", sheet_name="Nod21NI", header=1)


print(df_giardini.columns)
print(df_tropici.columns)

nitrogen_genes = ['nifH', 'nodA', 'nodB']  
df_filtered_tropici = df_tropici[df_tropici['ID'].isin(nitrogen_genes)]
df_filtered_giardini = df_giardini[df_giardini['ID'].isin(nitrogen_genes)]

comparison = df_filtered_tropici.set_index('ID')[['log2FoldChange']].rename(columns={'log2FoldChange': 'Tropici'})
comparison['Giardini'] = df_filtered_giardini.set_index('ID')['log2FoldChange']
comparison['Difference'] = comparison['Tropici'] - comparison['Giardini']
print(comparison)
comparison[['Tropici', 'Giardini']].plot(kind='bar', figsize=(10, 6))
plt.title("Comparación de la expresión génica: R. tropici vs R. giardini")
plt.ylabel("log2FoldChange")
plt.show()
