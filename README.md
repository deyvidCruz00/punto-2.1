================================================================================
INSTRUCCIONES DE COMPILACIÓN Y EJECUCIÓN
Problemas de Concurrencia y Sincronización
================================================================================

REQUISITOS DEL SISTEMA
--------------------------------------------------------------------------------
Lenguaje: Python 3.8 o superior
Sistema Operativo: Windows 10/11, Linux, macOS
Librerías requeridas: threading (estándar de Python)

VERIFICACIÓN DE PYTHON
--------------------------------------------------------------------------------
Abrir terminal y ejecutar:
    python --version

Debe mostrar: Python 3.x.x (donde x >= 8)

================================================================================
PUNTO 2.1: DEADLOCK - SISTEMA DE TRANSFERENCIAS BANCARIAS
================================================================================

VERSIÓN CON DEADLOCK
--------------------------------------------------------------------------------
Archivo: deadlock_con_problema.py

Ejecución:
    python deadlock_con_problema.py

Resultado esperado:
    - Sistema se bloquea (deadlock)
    - Threads quedan esperando indefinidamente
    - Presionar Ctrl+C para terminar


VERSIÓN SIN DEADLOCK
--------------------------------------------------------------------------------
Archivo: deadlock_solucion.py

Ejecución:
    python deadlock_solucion.py

Resultado esperado:
    - 30 transferencias completadas exitosamente
    - Saldos finales correctos
    - Sin bloqueos


================================================================================
PUNTO 2.2: STARVATION - SISTEMA DE PRIORIDADES DE TAREAS
================================================================================

VERSIÓN CON STARVATION
--------------------------------------------------------------------------------
Archivo: starvation_con_problema.py

Ejecución:
    python starvation_con_problema.py

Duración: 10 segundos
Resultado esperado:
    - Tareas tipo B no se procesan
    - 15-20 tareas B quedan sin procesar
    - Screenshots automáticos a los 2, 4, 6, 8, 10 segundos


VERSIÓN SIN STARVATION
--------------------------------------------------------------------------------
Archivo: starvation_solucion.py

Ejecución:
    python starvation_solucion.py

Duración: 10 segundos
Resultado esperado:
    - Todas las tareas se procesan eventualmente
    - Mecanismo de aging visible
    - Tareas B progresan gradualmente


================================================================================
PUNTO 2.3: RACE CONDITION - GESTOR DE INVENTARIO CONCURRENTE
================================================================================

VERSIÓN CON RACE CONDITION
--------------------------------------------------------------------------------
Archivo: race_condition_con_problema.py

Ejecución:
    python race_condition_con_problema.py

Resultado esperado:
    - Stock final inconsistente (varía en cada ejecución)
    - Valores incorrectos para Producto 0 y Producto 5
    - Ejecutar 10 veces para documentar variaciones


VERSIÓN SIN RACE CONDITION
--------------------------------------------------------------------------------
Archivo: race_condition_solucion.py

Ejecución:
    python race_condition_solucion.py

Resultado esperado:
    - Stock final consistente (siempre igual)
    - Producto 0: 120 unidades
    - Producto 5: 110 unidades
    - Resultados idénticos en 10 ejecuciones


================================================================================
EJECUCIÓN DE PRUEBAS AUTOMATIZADAS
================================================================================

SCRIPT DE PRUEBAS RACE CONDITION
--------------------------------------------------------------------------------
Archivo: ejecutar_pruebas_race_condition.py

Ejecución:
    python ejecutar_pruebas_race_condition.py

Descripción:
    Ejecuta automáticamente 10 veces cada versión (con y sin race condition)
    y genera tabla comparativa de resultados.


================================================================================
CAPTURA DE SCREENSHOTS
================================================================================

MOMENTOS CLAVE PARA SCREENSHOTS:

Deadlock:
    - Momento del bloqueo (versión con problema)
    - Finalización exitosa (versión solución)

Starvation:
    - t=0s, 2s, 4s, 6s, 8s, 10s (ambas versiones)
    - Estado final mostrando tareas procesadas

Race Condition:
    - Resultado final de cada una de las 10 ejecuciones (ambas versiones)


================================================================================
SOLUCIÓN DE PROBLEMAS
================================================================================

ERROR: "python no se reconoce como comando"
--------------------------------------------------------------------------------
Solución Windows:
    1. Usar: py --version
    2. Ejecutar programas con: py nombre_archivo.py

Solución Linux/macOS:
    1. Usar: python3 --version
    2. Ejecutar programas con: python3 nombre_archivo.py


ERROR: "ModuleNotFoundError: No module named 'threading'"
--------------------------------------------------------------------------------
Solución:
    threading es módulo estándar de Python.
    Verificar versión de Python (debe ser >= 3.8)


PROGRAMA NO TERMINA (Deadlock intencional)
--------------------------------------------------------------------------------
Solución:
    Presionar Ctrl+C para terminar forzosamente.
    Esto es comportamiento esperado en deadlock_con_problema.py


================================================================================
NOTAS IMPORTANTES
================================================================================

1. Los programas generan salida verbose en consola para demostrar el 
   funcionamiento interno. Esto es intencional para propósitos académicos.

2. Los tiempos de ejecución son aproximados y pueden variar según el hardware.

3. Para deadlock_con_problema.py, el bloqueo puede ocurrir en diferentes 
   puntos en cada ejecución debido a la naturaleza no determinística de 
   los threads.

4. Todos los programas incluyen timestamps para facilitar la documentación
   y análisis de resultados.

5. Los screenshots deben capturarse cuando el programa indica:
   "MOMENTO PARA SCREENSHOT" o "CAPTURAR SCREENSHOT AQUI"


================================================================================
ESTRUCTURA DE ARCHIVOS
================================================================================

punto-2.1/
├── deadlock_con_problema.py
├── deadlock_solucion.py
├── starvation_con_problema.py
├── starvation_solucion.py
├── race_condition_con_problema.py
├── race_condition_solucion.py
├── ejecutar_pruebas_race_condition.py
├── README_compilacion.txt
├── README_deadlock.md
├── README_starvation.md
└── README_race_condition.txt


================================================================================
FIN DEL DOCUMENTO
================================================================================
