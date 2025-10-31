# Sistema de Transferencias Bancarias - Deadlock vs Sin Deadlock

## Descripción del Proyecto

Implementación del **Punto 2.1** del documento de Sistemas Operativos que demuestra:
- **Versión CON deadlock:** Sistema propenso a interbloqueo
- **Versión SIN deadlock:** Sistema con prevención de deadlock por ordenamiento de recursos

## Estructura de Archivos

```
punto-2.1/
├── deadlock_con_problema.py      # Implementación CON deadlock
├── deadlock_solucion.py          # Implementación SIN deadlock  
├── analisis_deadlock.md          # Análisis de la versión con deadlock
├── analisis_comparativo.md       # Comparación entre ambas versiones
├── SO_Final.md                   # Especificaciones del ejercicio
└── README_compilacion.txt        # Este archivo
```

## Especificaciones Técnicas

### Sistema Simulado:
- **5 cuentas bancarias** (IDs 0-4)
- **Saldos iniciales:** Cuenta[i] = $1000 × (i+1)
- **10 threads concurrentes**
- **30 transferencias totales** según tabla especificada

### Tecnologías:
- **Lenguaje:** Python 3.x
- **Librerías:** `threading`, `time` (estándar de Python)
- **SO Desarrollo:** Windows/Linux/macOS
- **Hardware:** CPU multi-core recomendado

## Instrucciones de Ejecución

### Prerrequisitos:
```bash
# Verificar Python instalado
python --version
# Debe mostrar Python 3.x
```

### Versión CON Deadlock:
```bash
# Ejecutar simulación con deadlock
python deadlock_con_problema.py

# Resultado esperado: 10/10 threads bloqueados
```

### Versión SIN Deadlock:
```bash
# Ejecutar simulación sin deadlock
python deadlock_solucion.py

# Resultado esperado: 10/10 threads completados exitosamente
```

## Resultados Esperados

### Versión CON Deadlock:
- ❌ **10/10 threads bloqueados**
- ❌ **0/30 transferencias completadas**
- ❌ **Tiempo infinito (timeout después de 5 segundos)**
- ❌ **Saldos sin cambios**

### Versión SIN Deadlock:
- ✅ **10/10 threads completados**
- ✅ **30/30 transferencias exitosas**
- ✅ **Tiempo: ~915ms**
- ✅ **Conservación de dinero verificada**

## Técnicas Implementadas

### Deadlock (Versión CON Problema):
- **Sin ordenamiento de locks**
- **Adquisición:** lock(origen) → lock(destino)
- **Resultado:** Espera circular → Deadlock

### Prevención (Versión SIN Problema):
- **Ordenamiento de recursos**
- **Adquisición:** lock(min(origen,destino)) → lock(max(origen,destino))
- **Resultado:** Eliminación de espera circular

## Análisis de Performance

| Métrica | CON Deadlock | SIN Deadlock |
|---------|--------------|--------------|
| Tiempo | ∞ (bloqueado) | ~915ms |
| Throughput | 0 ops/seg | ~32.8 ops/seg |
| Threads completados | 0/10 | 10/10 |
| Conservación dinero | No verificable | ✅ Verificado |

## Documentos de Análisis

1. **`analisis_deadlock.md`:**
   - Secuencia específica del deadlock
   - Threads bloqueados identificados
   - Condiciones del deadlock verificadas

2. **`analisis_comparativo.md`:**
   - Tabla comparativa completa
   - Justificación teórica de la solución
   - Trade-offs de performance
   - Estados finales de cuentas

## Troubleshooting

### Problema: Python no encontrado
```bash
# Windows: Instalar desde python.org
# Linux: sudo apt install python3
# macOS: brew install python3
```

### Problema: Deadlock no se produce
- **Causa:** Hardware muy rápido
- **Solución:** Aumentar `time.sleep()` en `transferir()`

### Problema: Resultados inconsistentes
- **Causa:** Condiciones de carrera
- **Solución:** Ejecutar múltiples veces para observar patrón

## Contacto y Soporte

- **Curso:** Sistemas Operativos - Universidad Pedagógica y Tecnológica de Colombia
- **Punto:** 2.1 - Problemas de Concurrencia y Sincronización
- **Implementación:** Deadlock Prevention mediante Lock Ordering

## Notas Adicionales

- Los screenshots deben capturarse durante la ejecución
- El timestamp es importante para la documentación
- Los saldos finales deben sumar exactamente $15000
- Todas las 30 transferencias están especificadas en el documento original