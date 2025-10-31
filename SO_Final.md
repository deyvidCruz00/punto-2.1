**Taller No 2  Sistemas Operativos** 

**Universidad Pedagógica y Tecnológica de Colombia** 

**Aplicaciones de Sistemas Operativos** 

Este taller consta de cuatro puntos los cuales están relacionados con el contenido de la segunda unidad. 

Cada  ejercicio  necesita  de  la  toma  de  uno  o  más  pantallazos.  Para  ejecutar  este procedimiento debe pulsar la tecla print screen y pegar el resultado de la operación en algún editor gráfico. La otra sería tomar fotos… de muy buena resolución…… 

Requerimientos previos: Documentos de las unidades y contenido de las clases 

1. **Presentación del Informe (Valor:  0.5)** 



|**Presentación del informe**  ||
| - | :- |
|El  informe  se  encuentra  en  formato  PDF.  Cuenta  con  citas  de  pie  de  página  y referencias bibliográficas según norma establecida. Incluye portadas, contraportadas, índices y tablas de contenido según norma académica. Cuenta con numeración para tablas, ilustraciones, páginas y demás elementos componentes del trabajo. Incluye conclusiones  y  resultados  claramente  visibles  con  relación  directa  a  los  puntos resueltos, demostrando análisis crítico de los resultados obtenidos. |Total Punto |
|**Valor: 0.5**  |**0.5**  |

2. **Problemas de Concurrencia y Sincronización (1.0 punto)** 

**Contexto Técnico** 

Implementar y analizar tres escenarios de sincronización que demuestren problemas clásicos de concurrencia: deadlock, starvation y race conditions. Cada escenario debe implementarse en DOS versiones: una que exhiba el problema y otra que lo resuelva mediante mecanismos de sincronización apropiados. 

1. **Escenario de Deadlock: Sistema de Transferencias Bancarias (0.35 puntos) Especificación técnica:** 

   Simular un sistema bancario con las siguientes características: 

- **5 cuentas bancarias** numeradas 0-4 
- Saldo inicial: Cuenta[i] = 1000 \* (i+1) (Cuenta 0: $1000, Cuenta 1: $2000, etc.) 
- **10 threads** ejecutando transferencias concurrentes 
- Cada thread intenta realizar transferencias entre pares de cuentas aleatorias 

**Operación de transferencia:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.001.jpeg)

**Tabla de transferencias a ejecutar:** 



|Thread  |` `Transferencia 1 (Origen→Destino, Monto)  |` `Transferencia 2  |` `Transferencia 3 |
| - | :- | - | - |
|1  |` `0→1, $200  |` `1→2, $300  |` `2→0, $150 |
|2  |` `1→0, $250  |` `0→2, $100  |` `2→1, $200 |
|3  |` `2→3, $300  |` `3→4, $400  |` `4→2, $250 |
|4  |` `3→2, $350  |` `2→4, $200  |` `4→3, $300 |
|5  |` `4→0, $400  |` `0→3, $250  |` `3→4, $150 |
|6  |` `0→4, $300  |` `4→1, $350  |` `1→0, $200 |
|7  |` `1→3, $250  |` `3→0, $300  |` `0→1, $150 |
|8  |` `2→1, $200  |` `1→4, $250  |` `4→2, $300 |
|9  |` `3→1, $300  |` `1→2, $200  |` `2→3, $250 |
|10  |` `4→3, $350  |` `3→2, $250  |` `2→4, $200 |

**Implementaciones requeridas:** 

1) **Versión CON deadlock:** 
- Implementar locks sin ordenamiento 
- Documentar con screenshot el momento exacto del deadlock 
- Identificar qué threads están bloqueados esperando qué recursos 
2) **Versión SIN deadlock:** 
- Implementar solución mediante ordenamiento de recursos u otro mecanismo 
- Justificar la estrategia elegida 
- Demostrar que todas las transferencias se completan exitosamente 

**Entregables específicos:** 

**Tabla comparativa de ejecución:** 



|Métrica |Versión CON Deadlock |Versión SIN Deadlock |
| - | - | - |
|Tiempo de ejecución (ms) |N/A (bloqueado) |[Medir] |
|Transferencias completadas |X/30 |30/30 |
|Threads bloqueados |[Identificar cuáles] |0 |
|Saldos finales correctos |No verificable ||
|Screenshot con timestamp |||
**Análisis de resultados:** 

- ¿En qué secuencia específica de locks ocurre el deadlock en su implementación? 
- ¿Por qué la solución implementada previene el deadlock? Justificar con el algoritmo de Banker o grafos de asignación de recursos. 
- ¿Qué trade-offs introduce la solución en términos de rendimiento? 
2. **Escenario de Starvation: Sistema de Prioridades de Tareas (0.35 puntos) Especificación técnica:** 

   Simular un sistema de procesamiento de tareas con las siguientes características: 

- **Cola compartida** con capacidad máxima de 20 tareas 
- **3 tipos de tareas:** Alta prioridad (A), Media prioridad (M), Baja prioridad (B) 
- **5 threads productores:** Generan tareas con distribución: 60% B, 30% M, 10% A 
- **3 threads consumidores:** Procesan tareas de la cola 
- Tiempo de procesamiento: A=50ms, M=100ms, B=150ms 

**Secuencia de producción específica (primeras 30 tareas):** 



|Orden  |` `1-10  |` `11-20  |` `21-30 |
| - | - | - | - |
|Tareas  |` `B,B,M,B,B,B,A,M,B,B  |` `M,B,B,B,A,B,M,B,B,B  |` `B,B,B,M,A,B,B,M,B,B |

**Implementaciones requeridas:** 

1) **Versión CON starvation:** 
- Implementar política en donde siempre se prioricen las tareas tipo A y M 
- Documentar cuántas tareas tipo B quedan sin procesar después de 10 segundos 
- Mostrar el estado de la cola en diferentes momentos 
2) **Versión SIN starvation:** 
- Implementar mecanismo de aging u otra estrategia que garantice progreso de todas las tareas 
- Demostrar que todas las tareas eventualmente se procesan 

**Tabla de monitoreo temporal:** 



|Tiempo (seg) |Tareas A Procesadas |Tareas M Procesadas |Tareas B Procesadas |Tareas B en Espera |Screenshot |
| - | :- | :- | :- | :- | - |
|2 ||||||
|4 ||||||
|6 ||||||
|8 ||||||
|10 ||||||
**Análisis de resultados:** 

- ¿Cuál es el tiempo de espera máximo observado para una tarea tipo B en la versión CON starvation? 
- ¿Cómo funciona exactamente el mecanismo anti-starvation implementado? Describir el algoritmo con pseudocódigo. 
- ¿Qué overhead introduce la solución en términos de tiempo de procesamiento total? 
3. **Escenario de Race Condition: Gestor de Inventario Concurrente (0.30 puntos) Especificación técnica:** 

   Simular un sistema de inventario con: 

- **10 productos** (ID: 0-9) 
- Stock inicial: Producto[i] = 100 unidades 
- **20 threads** ejecutando operaciones concurrentes 
- Operaciones: *vender(producto\_id, cantidad)* y *reabastecer(producto\_id, cantidad)* 

**Secuencia de operaciones específica***:* 



|Thread |Operación 1 |Operación 2 |Operación 3 |Operación 4 |Operación 5 |
| - | - | - | - | - | - |
|1-5 |Vender(0, 10) |Vender(1, 15) |Vender(2, 20) |Vender(3, 5) |Vender(4, 25) |
|6-10 |Reabastecer(0, 30) |Reabastecer(1, 20) |Reabastecer(2, 40) |Reabastecer(3, 10) |Reabastecer(4, 35) |
|11-15 |Vender(5, 15) |Vender(6, 20) |Vender(7, 10) |Vender(8, 25) |Vender(9, 15) |
|16-20 |Reabastecer(5, 25) |Reabastecer(6, 30) |Reabastecer(7, 15) |Reabastecer(8, 40) |Reabastecer(9, 20) |

**Implementaciones requeridas:** 

1) **Versión CON race condition:** 
- Implementar sin sincronización 
- Ejecutar 10 veces y documentar inconsistencias en el stock final 
- Identificar operaciones específicas donde ocurren las race conditions 
2) **Versión SIN race condition:** 
- Implementar con mutex, semáforos o variables atómicas 
- Verificar consistencia del stock final en 10 ejecuciones 

**Tabla de resultados (10 ejecuciones):** 



|Ejecución |Stock Final Prod 0 (Esperado: 120) |Stock Final Prod 5 (Esperado: 110) |¿Todos Correctos? |Screenshot |
| - | :-: | :-: | :- | - |
|CON RC #1 |||||
|CON RC #2 |||||
|... |||||
|SIN RC #1 |120 |110 |||
|SIN RC #2 |120 |110 |||
|... |||||
**Análisis de Resultados:** 

- ¿Cuál es el rango de valores incorrectos observados en las 10 ejecuciones CON race condition? 
- ¿En qué líneas específicas del código ocurre la sección crítica? 
- Comparar  el  overhead  de  las  diferentes  técnicas  de  sincronización  (mutex  vs semáforos) en términos de tiempo de ejecución. 

**Entregables Generales del Punto 2 Cuadro de información técnica:** 



|Aspecto  |` `Detalle |
| - | - |
|Lenguaje  |` `C++ (recomendado) / Otro justificado |
|Compilador  |` `GCC/G++ versión X.X / MSVC / Clang |
|SO Desarrollo  |` `Windows/Linux/macOS |
|Librería de Threads  |` `std::thread (C++11) / pthreads / WinAPI |
|Hardware  |` `CPU, RAM, Núcleos |

**Estructura de archivos:** 

apellido1\_apellido2\_concurrencia/ 

├── deadlock\_con\_problema.cpp ├── deadlock\_solucion.cpp 

├── starvation\_con\_problema.cpp ├── starvation\_solucion.cpp 

├── race\_condition\_con\_problema.cpp ├── race\_condition\_solucion.cpp 

├── README\_compilacion.txt 

└── resultados\_comparativos.xlsx 



|**Problemas de Concurrencia (Valor: 1.0)** ||
| - | :- |
|**Deadlock (0.35 pts):** Se implementan ambas versiones (con y sin deadlock) del sistema de transferencias bancarias ejecutando las 30 transferencias especificadas en  la  tabla.  La  versión  CON  deadlock  demuestra  el  bloqueo  con  screenshot timestampeado identificando threads y recursos bloqueados. La versión SIN deadlock completa  todas  las  transferencias  exitosamente  con  saldos  finales  correctos verificables. La tabla comparativa está completa con todas las métricas solicitadas. El análisis responde las tres preguntas identificando la secuencia específica de locks que causa deadlock, justificando la solución con teoría (Banker/grafos) y discutiendo trade-offs de rendimiento con datos numéricos. |Total Punto |
|**Starvation (0.35 pts):** Se implementan ambas versiones del sistema de prioridades procesando  las  30  tareas  especificadas.  La  versión  CON  starvation  documenta cuántas tareas tipo B quedan sin procesar después de 10 segundos. La versión SIN starvation demuestra que todas las tareas se procesan eventualmente. La tabla de monitoreo temporal está completa con screenshots en los 5 momentos solicitados (2, 4, 6, 8, 10 seg). El análisis identifica el tiempo de espera máximo de tareas B, describe el  algoritmo  anti-starvation  con  pseudocódigo  detallado  y  cuantifica  el  overhead introducido. ||
|**Race Condition (0.30 pts):** Se implementan ambas versiones del gestor de inventario ejecutando las operaciones especificadas para los 20 threads. La versión CON race condition  se  ejecuta  10  veces  documentando  inconsistencias  en  stock  final  e identificando operaciones específicas donde ocurren. La versión SIN race condition demuestra consistencia en 10 ejecuciones con stocks finales correctos verificables (Prod 0=120, Prod 5=110). La tabla de resultados de 10 ejecuciones está completa. El análisis cuantifica el rango de valores incorrectos, identifica líneas de código de secciones  críticas  y  compara  overhead  de  diferentes  técnicas  de  sincronización (mutex, semáforos, atómicas) con mediciones de tiempo. ||
|**Valor: 0.35 + 0.35 + 0.30** |**1.0** |

3. **Simulación de Sistema de Archivos Ext (1.5 puntos)** 

**Especificación Técnica del Sistema:** 

Implementar una simulación del sistema de archivos Ext con la siguiente estructura de datos obligatoria: 

**Parámetros del sistema:** 

- Tamaño de bloque: 1 KB (1024 bytes) 
- Número de inodos: 32 
- Número de bloques de datos: 128 
- Bloques por inodo (punteros directos): 12 
- Puntero indirecto simple: 1 (apuntando a bloque con 256 punteros adicionales) 

**Estructuras de datos requeridas:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.002.jpeg)

1. **Implementación de Operaciones Básicas (0.6 puntos) Funciones obligatorias:** 
1) **Función crear\_archivo:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.003.jpeg)

2) **Función eliminar\_archivo:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.004.jpeg)

3) **Función listar\_archivos:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.005.jpeg)

4) **Función calcular\_fragmentacion:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.006.jpeg)

**d) Función mostrar\_estado\_disco:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.007.jpeg)

2. **Prueba de Estrés Específica (0.6 puntos)** 

Ejecutar la siguiente secuencia de 100 operaciones y documentar el estado del sistema en momentos clave: 

**Tabla de operaciones:** 



|Op#  |` `Operación  |` `Nombre  |` `Tamaño (KB)  |` `Acción |
| - | - | - | - | - |
|1-10  |` `Crear  |` `archivo\_01 a archivo\_10  |` `5 KB c/u  |` `Crear |
|11-20  |` `Crear  |` `archivo\_11 a archivo\_20  |` `10 KB c/u  |` `Crear |
|21-25  |` `Eliminar  |` `archivo\_02, 05, 08, 12, 15  |-  |` `Eliminar |
|26-35  |` `Crear  |` `archivo\_21 a archivo\_30  |` `3 KB c/u  |` `Crear |
|36-40  |` `Eliminar  |` `archivo\_03, 07, 11, 18, 22  |-  |` `Eliminar |
|41-50  |` `Crear  |` `archivo\_31 a archivo\_40  |` `8 KB c/u  |` `Crear |
|51-55  |` `Eliminar  |` `archivo\_01, 06, 13, 25, 32  |-  |` `Eliminar |
|56-70  |` `Crear  |` `archivo\_41 a archivo\_55  |` `2 KB c/u  |` `Crear |
|71-80  |` `Eliminar  |` `10 archivos aleatorios  |-  |` `Eliminar |
|81-100  |` `Crear  |` `archivo\_56 a archivo\_75  |` `Tamaños variables 1-15 KB  |` `Crear |

**Capturas del estado del sistema:** 



|Momento  |` `Operación #  |` `Screenshot Debe Mostrar |
| - | - | - |
|Snapshot 1  |` `Después de op 20  |` `Lista archivos + Estado disco + Fragmentación% |
|Snapshot 2  |` `Después de op 40  |` `Lista archivos + Estado disco + Fragmentación% |
|Snapshot 3  |` `Después de op 60  |` `Lista archivos + Estado disco + Fragmentación% |
|Snapshot 4  |` `Después de op 80  |` `Lista archivos + Estado disco + Fragmentación% |
|Snapshot 5  |` `Después de op 100  |` `Lista archivos + Estado disco + Fragmentación% |

**Tabla de evolución del sistema:** 



|Snapshot |Op# |Archivos Activos |Bloques Ocupados |Fragmentación % |Inodos Libres |Bloques Libres |
| - | - | :-: | :- | :-: | - | :-: |
|1 |20 ||||||
|2 |40 ||||||
|3 |60 ||||||
|4 |80 ||||||
|5 |100 ||||||
3. **Análisis de Limitaciones (0.3 puntos) Análisis de resultados:** 
1) **Fragmentación externa:** 
- Graficar la evolución de la fragmentación en los 5 snapshots 
- Identificar en qué momento alcanza el pico máximo 
- Explicar por qué ocurre fragmentación en la secuencia de operaciones específica 
2) **Eficiencia de búsqueda:** 
- Medir tiempo promedio de búsqueda de bloques libres en cada snapshot 
- Comparar con un esquema ideal de bloques contiguos 
- Proponer una mejora al algoritmo de búsqueda 
3) **Limitaciones del esquema de punteros:** 
- Calcular el tamaño máximo de archivo soportado con 12 punteros directos + 1 indirecto 
- ¿Qué porcentaje de archivos creados en la prueba requirieron puntero indirecto? 
- ¿Qué pasaría si se intentara crear un archivo de 1 MB? 
4) **Comparación con Ext moderno:** 
- Identificar 3 diferencias principales entre esta simulación y Ext4 real 
- ¿Qué optimizaciones tiene Ext4 que no están en esta simulación? 

**Entregables del Punto 3** 

**Código fuente:** 

Nomenclatura: apellido1\_apellido2\_ext.cpp **Debe incluir:** 

- Todas las estructuras de datos definidas 
- Las 5 funciones obligatorias completamente comentadas 
- Función main() que ejecute la prueba de estrés completa 
- Makefile o instrucciones de compilación 

**Archivo de resultados:** 

- resultados\_ext.xlsx: Tabla de evolución + gráficos de fragmentación 



|**Sistema de Archivos Ext (Valor: 1.5)** ||
| - | :- |
|**Implementación de Operaciones (0.6 pts):** Se implementan correctamente las cinco funciones  obligatorias  (crear\_archivo,  eliminar\_archivo,  listar\_archivos, calcular\_fragmentacion,  mostrar\_estado\_disco)  siguiendo  las  especificaciones técnicas. El código utiliza las estructuras de datos definidas (Superbloque, Inodo con 32 entradas, Bloque con 128 unidades de 1KB) y está exhaustivamente comentado explicando la lógica de cada función. La función crear\_archivo calcula correctamente bloques  necesarios,  asigna  punteros  directos  e  indirectos  según  corresponda,  y actualiza bitmaps. La función eliminar\_archivo libera correctamente todos los bloques asignados  incluyendo  indirectos.  La  función  calcular\_fragmentacion  implementa correctamente la fórmula especificada. El código compila sin errores y es ejecutable según instrucciones proporcionadas. |Total Punto |



|**Sistema de Archivos Ext (Valor: 1.5) - Continuación** ||
| - | :- |
|**Prueba de Estrés (0.6 pts):** Se ejecuta la secuencia completa de 100 operaciones especificadas  en  la  tabla  (creaciones  con  tamaños  específicos  y  eliminaciones indicadas). Se capturan y presentan los 5 snapshots obligatorios (operaciones 20, 40, 60, 80, 100) con screenshots timestampeados mostrando lista de archivos, estado visual del disco y porcentaje de fragmentación en cada momento. La tabla de evolución del sistema está completa con todas las métricas solicitadas (archivos activos, bloques ocupados, fragmentación%, inodos libres, bloques libres) para los 5 snapshots. Los datos son consistentes y verificables con las capturas. El video muestra la ejecución completa de la prueba con transiciones claras entre snapshots. ||
|**Análisis  de  Limitaciones  (0.3  pts):**  Se  presenta  gráfico  de  evolución  de fragmentación identificando el pico máximo y explicando causas específicas de la secuencia de operaciones. Se miden y comparan tiempos de búsqueda de bloques libres en cada snapshot con propuesta concreta de mejora al algoritmo. Se calcula correctamente el tamaño máximo de archivo soportado (12 punteros directos × 1KB + 1 indirecto × 256 punteros × 1KB = 268 KB) y se documenta cuántos archivos de la prueba requirieron puntero indirecto. Se analizan limitaciones ante un archivo de 1 MB. Se  identifican  3  diferencias  principales  con  Ext4  real  explicando  optimizaciones ausentes en la simulación. ||
|**Valor: 0.6 + 0.6 + 0.3** |**1.5** |

4. **Memoria Virtual y MMU (2.0 puntos)** 
1. **Simulación de Traducción de Direcciones con MMU (1.0 punto) Especificación Técnica del Sistema** 

   **Parámetros obligatorios:** 

- Espacio de direcciones lógicas: **16 bits** (0x0000 - 0xFFFF = 64 KB) 
- Tamaño de página: **4 KB** (4096 bytes) 
- Número de páginas lógicas: 64 KB / 4 KB = **16 páginas** (0-15) 
- Memoria física: **32 KB** (8 marcos de página numerados 0-7) 
- Bits para offset: 12 bits (log₂ 4096) 
- Bits para número de página: 4 bits (log₂ 16) 

**Estructura de la tabla de páginas:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.008.jpeg)

**Estado inicial obligatorio de la tabla de páginas:** 



|Página Lógica |Marco Físico |Presente |Modificada |Referenciada |
| - | - | - | - | - |
|0 |3 |true |false |false |
|1 |-1 |false |false |false |
|2 |5 |true |false |false |
|3 |1 |true |true |false |
|4 |-1 |false |false |false |
|5 |7 |true |false |false |
|6 |-1 |false |false |false |
|7 |2 |true |false |false |
|8 |-1 |false |false |false |
|9 |4 |true |false |false |
|10 |-1 |false |false |false |
|11 |6 |true |false |false |
|12-15 |-1 |false |false |false |

**Implementación Requerida** 

**Función de traducción de direcciones:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.009.jpeg)

**Casos de Prueba Obligatorios (10 traducciones) Tabla de traducciones a ejecutar y documentar:** 



|# |Dir. Lógica (Hex) |Página |Offset (Hex) |¿Presente? |Marco |Dir. Física (Hex) |Resultado |Screenshot |
| - | :- | - | - | - | - | :- | - | - |
|1 |0x0000 |0 |0x000 |Sí |3 |0x3000 |Hit ||
|2 |0x0FFF |0 |0xFFF |Sí |3 |0x3FFF |Hit ||
|3 |0x1234 |1 |0x234 |No |- |- |Page Fault ||
|4 |0x2ABC |2 |0xABC |Sí |5 |0x5ABC |Hit ||
|5 |0x3500 |3 |0x500 |Sí |1 |0x1500 |Hit ||
**Tabla de traducciones a ejecutar y documentar:** 



|# |Dir. Lógica (Hex) |Página |Offset (Hex) |¿Presente? |Marco |Dir. Física (Hex) |Resultado |Screenshot |
| - | :- | - | - | - | - | :- | - | - |
|6 |0x4000 |4 |0x000 |No |- |- |Page Fault ||
|7 |0x5800 |5 |0x800 |Sí |7 |0x7800 |Hit ||
|8 |0x7FFF |7 |0xFFF |Sí |2 |0x2FFF |Hit ||
|9 |0x9200 |9 |0x200 |Sí |4 |0x4200 |Hit ||
|10 |0xB500 |11 |0x500 |Sí |6 |0x6500 |Hit ||
**Análisis de la traducción:** 

- **Tasa de aciertos:** Calcular Hit Rate = (Hits / Total accesos) × 100 
- **Cálculo manual:** Para las traducciones #1, #4 y #7, mostrar el cálculo manual paso a paso:  
- Conversión binaria de la dirección lógica 
- Extracción de bits de página y offset 
- Consulta a tabla de páginas 
- Construcción de dirección física 
- **Optimización:**  ¿Qué  estructura  de  datos  adicional  mejoraría  el  rendimiento  de búsqueda en la tabla de páginas? 

**Entregables Punto 4.1** 

Código: apellido1\_apellido2\_mmu.cpp 

- Estructuras de datos definidas 
- Función traducir\_direccion() implementada 
- Función main() que ejecute las 10 traducciones 
- Tabla de resultados completa con timestamps 
2. **Simulación de Paginación y Reemplazo (1.0 punto) Especificación Técnica** 

   **Parámetros del sistema:** 

- Memoria física: **4 marcos de página** (reducido para observar reemplazos) 
- Espacio de intercambio (swap): Capacidad ilimitada simulada 
- Algoritmos de reemplazo a implementar: **FIFO** y **LRU** 

**Secuencia de Referencias Obligatoria (20 accesos)** 

**Secuencia de páginas referenciadas:** 

**2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2, 7, 3, 4, 5, 6, 7, 2, 4 Implementación de Algoritmos** 

**Estructura de control:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.010.jpeg)

**Funciones requeridas:** 

![](Aspose.Words.515a6cde-5f08-4146-a73b-0b7728fe7a14.011.jpeg)

**Tabla de Simulación FIFO** 



|Acceso |Página |Estado Memoria (Marcos 0-3) |¿Fallo? |Víctima |Screenshot |
| - | - | :-: | - | - | - |
|1 |2 |[2,\_,\_,\_] |✓ |- |✓ |
|2 |3 |[2,3,\_,\_] |✓ |- ||
|3 |2 |[2,3,\_,\_] |✗ |- ||
|4 |1 |[2,3,1,\_] |✓ |- ||
|5 |5 |[2,3,1,5] |✓ |- ||
|6 |2 |[2,3,1,5] |✗ |- ||
|7 |4 |[4,3,1,5] |✓ |Pág 2 (marco 0) |✓ |
|8 |5 |[4,3,1,5] |✗ |- ||
|9 |3 |[4,3,1,5] |✗ |- ||
|10 |2 |[4,2,1,5] |✓ |Pág 3 (marco 1) |✓ |
|11 |5 |[4,2,1,5] |✗ |- ||
|12 |2 |[4,2,1,5] |✗ |- ||
|13 |7 |[4,2,7,5] |✓ |Pág 1 (marco 2) |✓ |
|14 |3 |[4,2,7,3] |✓ |Pág 5 (marco 3) ||
|15 |4 |[4,2,7,3] |✗ |- ||
|16 |5 |[5,2,7,3] |✓ |Pág 4 (marco 0) ||
|17 |6 |[5,6,7,3] |✓ |Pág 2 (marco 1) ||
|18 |7 |[5,6,7,3] |✗ |- ||
|19 |2 |[5,6,2,3] |✓ |Pág 7 (marco 2) |✓ |
|20 |4 |[5,6,2,4] |✓ |Pág 3 (marco 3) |✓ |

**Tabla de Simulación LRU:** 



|Acceso |Página |Estado Memoria (Marcos 0-3) |¿Fallo? |Víctima |LRU (menos reciente) |Screenshot |
| - | - | :-: | - | - | :-: | - |
|1 |2 |[2,\_,\_,\_] |✓ |- |- |✓ |
|2 |3 |[2,3,\_,\_] |✓ |- |- ||
|3 |2 |[2,3,\_,\_] |✗ |- |Pág 3 ||
|4 |1 |[2,3,1,\_] |✓ |- |- ||
|5 |5 |[2,3,1,5] |✓ |- |- ||
|6 |2 |[2,3,1,5] |✗ |- |Pág 3 ||
|7 |4 |[2,4,1,5] |✓ |Pág 3 (marco 1) |Pág 1 |✓ |
|8 |5 |[2,4,1,5] |✗ |- |Pág 1 ||
|9 |3 |[2,4,3,5] |✓ |Pág 1 (marco 2) |Pág 2 ||
|10 |2 |[2,4,3,5] |✗ |- |Pág 4 ||
|11 |5 |[2,4,3,5] |✗ |- |Pág 4 ||
|12 |2 |[2,4,3,5] |✗ |- |Pág 4 ||
|13 |7 |[2,7,3,5] |✓ |Pág 4 (marco 1) |Pág 3 |✓ |
|14 |3 |[2,7,3,5] |✗ |- |Pág 2 ||
|15 |4 |[4,7,3,5] |✓ |Pág 2 (marco 0) |||
|16 |5 |[4,7,3,5] |✗ |- |Pág 4 ||
|17 |6 |[6,7,3,5] |✓ |Pág 4 (marco 0) |||
|18 |7 |[6,7,3,5] |✗ |- |Pág 6 ||
|19 |2 |[6,2,3,5] |✓ |Pág 7 (marco 1) |✓ ||
|20 |4 |[6,2,4,5] |✓ |Pág 3 (marco 2) |✓ ||
**Análisis Comparativo Obligatorio Tabla de métricas finales:** 



|Métrica |FIFO |LRU |Diferencia |
| - | - | - | - |
|Fallos de página totales |/20 |/20 ||
|Tasa de fallos (%) |% |% ||
|Reemplazos realizados ||||
|Páginas más reemplazadas |[Listar] |[Listar] ||
|Mejor algoritmo para esta secuencia ||||
**Análisis de resultados:** 

- **Anomalía  de  Belady:**  ¿Se  observaría  si  aumentáramos  a  5  marcos  con  FIFO? Justificar. 
- **Patrón de acceso:** ¿Qué características de la secuencia favorecen a LRU sobre FIFO? 
- **Overhead:** Estimar el costo computacional adicional de LRU vs FIFO (operaciones por acceso). 
- **Hiperpaginación:** Si esta secuencia se repitiera continuamente con solo 2 marcos, ¿qué tasa de fallos esperaría? ¿Se consideraría hiperpaginación? 

**Entregables Punto 4.2:** 

Código: apellido1\_apellido2\_paginacion.cpp 

- Implementación de FIFO completa 
- Implementación de LRU completa 
- Función main() que ejecute la secuencia de 20 accesos 
- Ambas tablas completas con screenshots en momentos clave 

**Cuadro de información técnica:** 



|Aspecto  |` `Detalle |
| - | - |
|Lenguaje  |` `C++ (recomendado) / Otro justificado |
|Compilador  |` `GCC/G++ versión / MSVC / Clang |
|SO Desarrollo  |` `Windows/Linux/macOS |
|Hardware  |` `CPU, RAM |

**Estructura de archivos:** 

apellido1\_apellido2\_memoria/ 

├── apellido1\_apellido2\_mmu.cpp 

├── apellido1\_apellido2\_paginacion.cpp ├── README\_compilacion.txt 

├── resultados\_mmu.xlsx 

└── resultados\_paginacion.xlsx 



|` `**Memoria Virtual y MMU (Valor: 2.0)** ||
| - | :- |
|**MMU y Traducción (1.0 pt):** Se implementa correctamente la simulación de MMU con los parámetros especificados (16 bits dirección lógica, 4KB página, 8 marcos físicos).  Las  estructuras  de  datos  (EntradaTablaPaginas  con  marco\_fisico, presente,  modificada,  referenciada)  están  correctamente  definidas.  La  tabla  de páginas  se  inicializa  con  el  estado  obligatorio  especificado.  La  función traducir\_direccion() implementa correctamente la extracción de número de página (bits 15-12) y offset (bits 11-0), consulta la tabla, calcula dirección física como (marco << 12) | offset y detecta page faults. Se ejecutan y documentan las 10 traducciones  obligatorias  con  tabla  completa  mostrando  dirección  lógica  hex, página,  offset  hex,  presente,  marco,  dirección  física  y  resultado.  Screenshots timestampeados  muestran  la  ejecución  de  cada  traducción.  Se  calcula correctamente el Hit Rate. Se muestran cálculos manuales paso a paso (binario, extracción bits, consulta tabla, construcción dirección física) para las traducciones #1, #4 y #7. Se propone optimización válida de estructura de datos con justificación. |Total Punto |
|**Paginación  y  Reemplazo  (1.0  pt):**  Se  implementan  correctamente  ambos algoritmos (FIFO y LRU) con las estructuras de datos especificadas (MarcoMemoria con pagina, timestamp\_carga, ultimo\_acceso). Se ejecuta la secuencia obligatoria de 20 referencias (2,3,2,1,5,2,4,5,3,2,5,2,7,3,4,5,6,7,2,4) para ambos algoritmos con 4 marcos de memoria. Las tablas de simulación están completas mostrando estado de memoria en cada acceso, indicador de fallo, página víctima reemplazada y para LRU la página menos recientemente usada. Screenshots timestampeados documentan momentos clave (accesos 1, 7, 10, 13, 19, 20). La tabla de métricas finales compara fallos totales, tasa de fallos, reemplazos realizados e identifica el mejor algoritmo para esta secuencia. El análisis responde las 4 preguntas: explica anomalía  de  Belady  con  justificación  teórica,  identifica  características  de  la secuencia  que  favorecen  a  LRU  (localidad  temporal),  estima  overhead computacional de LRU vs FIFO cuantificando operaciones, y calcula tasa de fallos esperada con 2 marcos evaluando si constituye hiperpaginación. ||
|**Valor: 1.0 + 1.0** |**2.0** |



|**Información general** |||||
| - | :- | :- | :- | :- |
|Tiempo de desarrollo |Casi 7 semanas ||||
|Forma de trabajo |Igual que en la cohorte pasada ||||
|**Totales** |||||
|Punto 1 |Punto 2 |Punto 3 |Punto 4 |Total |
|Valor: 0.5 |Valor: 1.0 |Valor: 1.5 |Valor: 2.0 |5\.0 |

**POLÍTICAS DE ENTREGA** 

**Puntualidad:** Entregas fuera de plazo = 0.0 **Plataforma única:** Solo Moodle. Otros medios = 0.0 

**Completitud:**  Solo  se  evalúan  trabajos  100%  completos.  Incompletos  =  máx  0.5  (solo presentación) 

**Código ejecutable:** Código que no compile o ejecute = 0.0 en ese punto **Evidencia con timestamp:** Screenshots sin timestamps o usuario = -0.2 por punto **Originalidad: Similitud de código >70% entre grupos =** 0.0 para ambos  

**¡Que se diviertan! Att,**  

**Alex :)** 
