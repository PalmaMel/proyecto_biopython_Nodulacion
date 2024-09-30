# Nodulacion en *Phaseolus vulgaris*

Nombre: <!-- Daniel Bautista (<danielzb@lcg.unam.mx>)  
Nombre: <!-- Palma Melissa (<melissap@lcg.unam.mx>) 

Fecha:  10/09/2024

## Introducción

El frijol común (*Phaseolus vulgaris*) es una de las leguminosas más importantes a nivel mundial, representando 
alrededor del 50% del consumo global de leguminosas de grano. Su importancia es particularmente notable en América
Latina y África, donde constituye un componente esencial de las dietas tradicionales. Además de ser una fuente valiosa
de proteínas dietéticas, con un contenido que oscila entre el 20% y el 25%, el frijol común también es rico en 
micronutrientes y calorías, lo que lo convierte en un alimento fundamental para millones de personas. 

Adicionalmete las legumbres son contribuyentes importantes al nitrógeno biológico (N), un nutriente critico  
para la produccion y crecimiento, este nutriente a pesar de su abundacia atmosferica las plantas solo pueden 
utilizar formas reducidas de este elemento, como el amonio (NH₄⁺) o los nitratos (NO₃⁻). La fijación de nitrógeno
atmosférico es posible gracias a la acción de bacterias específicas, algunas de las que fijan nitrógeno de manera 
simbiótica, asociándose con plantas huéspedes, como las legumbres, que les suministran azúcares provenientes de la
fotosíntesis como fuente de energía, mientras que los microorganismos proporcionan nitrógeno fijado para el crecimiento
de la planta.

En el caso de legumbres como *P.vulgaris* estas bacterias colonizan el sistema de raíces de la planta huésped y 
hacen que las raíces formen nódulos (anaeróbicos) para albergar a las bacterias que empezaron a fijar nitrógeno que la
planta aprovechara para producir semillas ricas en nitrógeno. Siendo las legumbres no noduladas bajas en nitrógeno y con 
una producción baja de semillas.

La fijación e nitrógeno desempeña un papel fundamental en el mantenimiento de la salud de los ecosistemas tanto acuáticos como 
terrestres en todo el planeta, es el estudio de los mecanismos que subyacen a las relaciones simbióticas, la formación de nódulos
y la fijación de nitrógeno de gran importancia, por ejemplo como una posible alternativa natural para suministrar este nutriente 
esencial a las plantas en contraste fertilizantes sintéticos cuyo uso excesivo ha generado serios problemas ecológicos a nivel 
global, como la creación de zonas muertas en áreas costeras. 

## Planteamiento del problema

<!-- Describir la problemática que se presenta, la situación que motiva la realización del proyecto/análisis y que está causando posibles inconvenientes. -->

**aqui van las preguntas**

## Metodología

Se descargaron los datos del repositorio *Phaseolus vulgaris* gene expression atlas (PvGEA) disponible en: (<https://www.zhaolab.org/PvGEA/>)
y publicado en el articulo: `An RNA-Seq based gene expression atlas of the common bean`

Los datos de entrada consisten los patrones de expresión génica de 24 muestras únicas recogidas de siete tejidos distintos de *Phaseolus vulgaris* cv. negro jamapa; 
raíces, nódulos, hojas, tallos, flores, semillas y vainas. El archivo con los datos se encuentra en formato xlsx.


### A. Datos de Entrada 

Los datos de entrada fueron descargados desde (<https://www.zhaolab.org/PvGEA/>) y se encuentran en `proyecto_biopython/data`

```
|-- data
|   |-- Complete_repositorio_de_RNAseq.xlsx
```


#### Metadatos de la carpeta de datos


> Versión/Identificador del genoma: Única (1.0) 

> Fecha de descarga: 08/09/2024

>| Archivo | Descripción  | Tipo | 
|:--      |:--           |:--  |
| Complete repository Nodulation.xlsx  | Conjunto de datos transcriptomicos de P. vulgaris en distintas condiciones  | Formato xlsx |


#### Formato de los archivos



- `Complete repository Nodulation.xlsx` : formato xlsx




Tabla 1																	
ID	baseMean | log2FoldChange | lfcSE | stat | pvalue | padj | Nod1_CE3_1 | Nod1_CE3_2 | Nod7_ControlNod_1 | Nod7_ControlNod_2	Nod7_ControlNod_3 | Nod1_CE3_1_normalized | Nod1_CE3_2_normalized | Nod7_ControlNod_1_normalized	Nod7_ControlNod_2_normalized | Nod7_ControlNod_3_normalized | Expression
Phvul.005G176566.1 | 44782.3494466328 | 11.87766212 | 0.317104344 | 37.45663639 | 4.68390446134868E-307 | 9.7429896700514E-303 | 75 | 26 | 77938 | 24632 | 42324 | 19.29591336 | 20.62183748 | 78073.3064579329 | 53420.7090675681 | 92377.8139568296 | Down_Nod1_CE3_Up_Nod7_ControlNod
Phvul.005G050500.1 | 14403.3290991897 | 11.53764934 | 0.350822334 | 32.88744251 | 3.32318903771128E-237 | 3.45628275867162E-233	38 | 6 | 25497 | 8869 | 12474 | 9.776596101	| 4.758885572 | 25541.264784289	| 19234.6650178736	| 27226.1802121135 |  Down_Nod1_CE3_Up_Nod7_ControlNod
Phvul.005G176475.1 | 18825.8705758968 | 9.891831227	| 0.307022284 | 32.21860998	| 9.68608390179848E-228	| 6.71600770804367E-224	125	| 43 | 32632 | 10152 | 18032 | 32.15985559	| 34.1053466 | 32688.6517018048	| 22017.1743445092	| 39357.2616309789 | Down_Nod1_CE3_Up_Nod7_ControlNod



Formato: 

> a. Posee un conjunto de hojas de calculo que estan estructuradas de la siguiente forma:

> b. Un encabezado que la nombra como Tabla 1

> c. Después viene una fila que describe las columnas
    ID: Identificador del gen, en este caso nombres como Phvul.005G176566.1 (posiblemente genes del frijol común).
    baseMean: La media de las lecturas normalizadas para este gen a través de todas las muestras.
    log2FoldChange: El cambio en la expresión del gen entre las condiciones comparadas, expresado como un cambio logarítmico en base 2. Valores positivos indican una mayor expresión en la condición experimental, y negativos indican menor expresión.
    lfcSE: El error estándar del valor de log2FoldChange, que indica la precisión de esta estimación.
    stat: Estadístico usado en la prueba de hipótesis para la diferencia en la expresión del gen.
    pvalue: Valor p de la prueba de hipótesis, que indica la significancia estadística del cambio en la expresión.
    padj: Valor p ajustado, que corrige los valores p originales para múltiples comparaciones (control de la tasa de falsos positivos).
    Columnas de muestra (como "Nod1_CE3_1", "Nod7_ControlNod_1"): Datos de expresión cruda para cada muestra.
    Columnas "normalized": Expresión de los genes, pero normalizada para facilitar la comparación entre muestras.
    Expression: Descripción del patrón de expresión del gen, en este caso "Down_Nod1_CE3_Up_Nod7_ControlNod", lo que indica que el gen se expresa menos en una condición y más en otra.

> d. Los valores



-
## Resultados
 

### X. Pregunta 

Archivo(s):     

Algoritmo: 

Gráfico

1. 

Solución: Describir paso a paso la solución, incluyendo los comandos correspondientes

```bash

```




## Análisis y Conclusiones

 <!-- Describir todo lo que descubriste en este análisis --> 


## Referencias
 [1] O’Rourke, J.A., Iniguez, L.P., Fu, F. et al. An RNA-Seq based gene expression atlas of the common bean. BMC Genomics 15, 866 (2014). https://doi.org/10.1186/1471-2164-15-866
 [2] Wagner, S. C.. (2011) Biological Nitrogen Fixation. Nature Education Knowledge 3(10):15
 [3]