#=============DATA================
# AUTHOR: Palma Luna Melissa 
# MAIL: danielzb@lcg.unam.mx or melissap@lcg.unam.mx
# TITLE: search_by_GeneID.py 
# DATE: NOV 2024
#=================================
#=============IMPORTS=============
from Bio import Entrez
#=================================
def main ():
    #==========PRIMERA_PARTE========== 
    """
    Hacer una búsqueda con esearch (en este caso contamos con los nombres de los organismos), 
    la búsqueda nos dará su ID.

    ORGANISMOS: Notoryctes typhlops y Chrysochloris asiatica
    """
    # Favor de insertar su email 
    Entrez.email = "@lcg.unam.mx" 
    
    # Buscar ID para "Notoryctes typhlops"
    handle = Entrez.esearch(db='taxonomy', term="Notoryctes typhlops", retmode="xml")
    record = Entrez.read(handle)
    handle.close()  # Cerrar el handle manualmente
    Notoryctes_typhlops = record['IdList']
    # print (f" El ID de Notoryctes typhlops es: {Notoryctes_typhlops"})

    # Buscar ID para "Chrysochloris asiatica"
    handle2 = Entrez.esearch(db='taxonomy', term="Chrysochloris asiatica", retmode="xml")
    record2 = Entrez.read(handle2)
    handle2.close()
    Chrysochloris_asiatica = record2['IdList']
    # print (f" el ID de Chrysochloris asiatica es: {Chrysochloris_asiatica}")
    
    #=================================
    """
    Usar el ID para obtener archivo con el linale de cada topo. 
    Contesta la pregunta:  En que punto divergen sus linajes.
    """
    # Obtener detalles usando efetch
    if Notoryctes_typhlops:
        handle = Entrez.efetch(db="taxonomy", id=Notoryctes_typhlops, retmode="xml")
        record = Entrez.read(handle)
        handle.close()
        # Se imprime linaje completo de Notoryctes typhlops:
        # print("Linaje de Notoryctes typhlops:")
        linaje_Not= record[0]["Lineage"]
        print (f"\n{linaje_Not}")

    if Chrysochloris_asiatica:
        handle2 = Entrez.efetch(db="taxonomy", id=Chrysochloris_asiatica, retmode="xml")
        record2 = Entrez.read(handle2)
        handle2.close()
        # Se imprime linaje completo de Chrysochloris asiatica
        # print(f"\Linaje de Chrysochloris asiatica:")
        linaje_chry=record2[0]["Lineage"]
        # print(linaje_chry)
        linaje_Not_list = linaje_Not.split('; ')
    
        # Convertir el linaje de Chrysochloris asiatica a lista
        linaje_chry_list = linaje_chry.split('; ')
        
        # compararamos linajes usando lista del linaje de Chrysochloris asiatica
        common=[] 
        for ancestor in linaje_chry_list:
            if ancestor in linaje_Not_list:
                common.append(ancestor)
        print(f" Lo comunes entre ambos organismos son:\n{common}")
        
        # Obtenemos ultimo ancestro comun
        ultimo_comun = None
        for ancestor in reversed(linaje_chry_list):
            if ancestor in linaje_Not_list:
                ultimo_comun = ancestor
                break
        print(f"\nDivergen a partir de: {ultimo_comun}")
        

main()