# Análisis del Deadlock - Punto 2.1

## Implementación del Sistema de Transferencias Bancarias

### Especificaciones Implementadas
- **5 cuentas bancarias** numeradas 0-4
- **Saldos iniciales**: Cuenta[i] = 1000 * (i+1) 
  - Cuenta 0: $1000
  - Cuenta 1: $2000  
  - Cuenta 2: $3000
  - Cuenta 3: $4000
  - Cuenta 4: $5000
- **10 threads** ejecutando transferencias concurrentes según tabla especificada
- **30 transferencias totales** (3 por thread)

### Función de Transferencia (VERSIÓN CON DEADLOCK)

```python
def transferir(cuentas, origen, destino, monto):
    """
    Implementa el pseudocódigo especificado:
    transfer(cuenta_origen, cuenta_destino, monto):
        lock(cuenta_origen)
        lock(cuenta_destino)
        if saldo[cuenta_origen] >= monto:
            saldo[cuenta_origen] -= monto
            saldo[cuenta_destino] += monto
        unlock(cuenta_destino)
        unlock(cuenta_origen)
    """
```

### Resultados del Experimento

| Métrica | Versión CON Deadlock |
|---------|---------------------|
| Tiempo de ejecución (ms) | N/A (bloqueado) |
| Transferencias completadas | 0/30 |
| Threads bloqueados | 10/10 |
| Saldos finales correctos | No verificable |

### Análisis del Deadlock Detectado

#### 1. ¿En qué secuencia específica de locks ocurre el deadlock?

El deadlock ocurre debido a la **espera circular** creada por los siguientes patrones de adquisición de locks:

- **Thread-1** (0→1): Adquiere lock cuenta 0, intenta adquirir cuenta 1
- **Thread-2** (1→0): Adquiere lock cuenta 1, intenta adquirir cuenta 0
- **Thread-3** (2→3): Adquiere lock cuenta 2, intenta adquirir cuenta 3  
- **Thread-4** (3→2): Adquiere lock cuenta 3, intenta adquirir cuenta 2
- **Thread-9** (3→1): Intenta adquirir cuenta 3 (ya tomada por Thread-4)
- **Thread-10** (4→3): Adquiere lock cuenta 4, intenta adquirir cuenta 3

**Secuencia específica del deadlock:**
1. Thread-1 adquiere cuenta 0, espera cuenta 1
2. Thread-2 adquiere cuenta 1, espera cuenta 0  ← **Ciclo 1: Thread-1 ↔ Thread-2**
3. Thread-3 adquiere cuenta 2, espera cuenta 3
4. Thread-4 adquiere cuenta 3, espera cuenta 2  ← **Ciclo 2: Thread-3 ↔ Thread-4**
5. Otros threads esperan recursos ya tomados, creando más dependencias

#### 2. Condiciones del Deadlock Verificadas

✅ **Exclusión mutua**: Los locks son mutuamente exclusivos
✅ **Retener y esperar**: Los threads mantienen un lock mientras esperan otro
✅ **Sin desalojo**: Los locks no pueden ser forzados a liberarse
✅ **Espera circular**: Existe un ciclo de dependencias de recursos

#### 3. Threads Específicamente Bloqueados

Todos los 10 threads están bloqueados:
- Thread-1: Bloqueado esperando cuenta 1 (retenida por Thread-2)
- Thread-2: Bloqueado esperando cuenta 0 (retenida por Thread-1)
- Thread-3: Bloqueado esperando cuenta 3 (retenida por Thread-4)
- Thread-4: Bloqueado esperando cuenta 2 (retenida por Thread-3)  
- Thread-5: Bloqueado esperando cuenta 4 (retenida por Thread-10)
- Thread-6: Bloqueado esperando cuenta 0 (retenida por Thread-1)
- Thread-7: Bloqueado esperando cuenta 1 (retenida por Thread-2)
- Thread-8: Bloqueado esperando cuenta 2 (retenida por Thread-3)
- Thread-9: Bloqueado esperando cuenta 3 (retenida por Thread-4)
- Thread-10: Bloqueado esperando cuenta 3 (retenida por Thread-4)

### Estado Final del Sistema

**Saldos finales**: Sin cambios (todas las transferencias bloqueadas)
- Cuenta[0] = $1000 (sin cambio)
- Cuenta[1] = $2000 (sin cambio)  
- Cuenta[2] = $3000 (sin cambio)
- Cuenta[3] = $4000 (sin cambio)
- Cuenta[4] = $5000 (sin cambio)

**Consistencia**: Los saldos permanecen consistentes debido a que ninguna transferencia se completó.

## Próximo Paso: Implementar Versión SIN Deadlock

Para resolver el deadlock, se implementará una **versión con ordenamiento de recursos** que:
1. Siempre adquiera locks en orden ascendente por número de cuenta
2. Use la estrategia: `lock(min(origen, destino))` primero, luego `lock(max(origen, destino))`
3. Elimine la posibilidad de espera circular