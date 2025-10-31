import threading
import time

class Cuenta:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo
        self.lock = threading.Lock()

    def __str__(self):
        return f"Cuenta[{self.id}] = ${self.saldo}"

def transferir_sin_deadlock(cuentas, origen, destino, monto):
    """
    VERSIÓN SIN DEADLOCK - Prevención mediante Ordenamiento de Recursos
    
    TÉCNICA IMPLEMENTADA: Prevención de Espera Circular
    - Asigna un orden total a todos los recursos (cuentas)
    - Siempre adquiere locks en orden ascendente por ID de cuenta
    - Evita la espera circular que causa deadlock
    
    Estrategia: lock(min(origen, destino)) primero, luego lock(max(origen, destino))
    """
    cta_origen = cuentas[origen]
    cta_destino = cuentas[destino]
    
    # PREVENCIÓN DE DEADLOCK: Ordenamiento de recursos
    # Determinar el orden de adquisición de locks basado en ID de cuenta
    if origen < destino:
        primera_cuenta = cta_origen
        segunda_cuenta = cta_destino
        primer_id = origen
        segundo_id = destino
    else:
        primera_cuenta = cta_destino
        segunda_cuenta = cta_origen
        primer_id = destino
        segundo_id = origen

    print(f"[{threading.current_thread().name}] Iniciando transferencia ${monto}: Cuenta {origen} → Cuenta {destino}")
    print(f"[{threading.current_thread().name}] Orden de locks: Cuenta {primer_id} → Cuenta {segundo_id}")
    
    # PASO 1: Adquirir lock de la cuenta con menor ID primero
    print(f"[{threading.current_thread().name}] Adquiriendo lock de cuenta {primer_id}...")
    primera_cuenta.lock.acquire()
    print(f"[{threading.current_thread().name}] ✓ Lock adquirido para cuenta {primer_id}")
    
    try:
        # Simular procesamiento (menor tiempo que en versión con deadlock)
        time.sleep(0.05)
        
        # PASO 2: Adquirir lock de la cuenta con mayor ID
        print(f"[{threading.current_thread().name}] Adquiriendo lock de cuenta {segundo_id}...")
        segunda_cuenta.lock.acquire()
        print(f"[{threading.current_thread().name}] ✓ Lock adquirido para cuenta {segundo_id}")
        
        try:
            # PASO 3: Realizar la transferencia
            if cta_origen.saldo >= monto:
                cta_origen.saldo -= monto
                cta_destino.saldo += monto
                print(f"[{threading.current_thread().name}] ✅ ÉXITO: Transferencia ${monto} de Cuenta {origen} → Cuenta {destino}")
                print(f"[{threading.current_thread().name}] Saldos actuales: Cuenta {origen}=${cta_origen.saldo}, Cuenta {destino}=${cta_destino.saldo}")
            else:
                print(f"[{threading.current_thread().name}] ❌ FALLO: Saldo insuficiente en cuenta {origen} (saldo: ${cta_origen.saldo}, necesario: ${monto})")
        finally:
            # PASO 4: Liberar locks en orden inverso
            segunda_cuenta.lock.release()
            print(f"[{threading.current_thread().name}] ✓ Lock liberado para cuenta {segundo_id}")
    finally:
        primera_cuenta.lock.release()
        print(f"[{threading.current_thread().name}] ✓ Lock liberado para cuenta {primer_id}")
    
    print(f"[{threading.current_thread().name}] Transferencia completada sin deadlock.")

def ejecutar_transferencias_sin_deadlock(cuentas, transferencias):
    """Ejecuta una secuencia de transferencias para un thread específico - VERSIÓN SIN DEADLOCK"""
    thread_name = threading.current_thread().name
    print(f"\n{thread_name} iniciado - Ejecutando {len(transferencias)} transferencias (SIN DEADLOCK)")
    
    transferencias_exitosas = 0
    for i, (origen, destino, monto) in enumerate(transferencias, 1):
        print(f"\n{thread_name} - Operación {i}/{len(transferencias)}")
        try:
            transferir_sin_deadlock(cuentas, origen, destino, monto)
            transferencias_exitosas += 1
        except Exception as e:
            print(f"{thread_name} - ERROR en operación {i}: {e}")
        
        # Pequeña pausa entre transferencias del mismo thread
        time.sleep(0.02)
    
    print(f"\n{thread_name} FINALIZADO - {transferencias_exitosas}/{len(transferencias)} transferencias exitosas")
    return transferencias_exitosas

def main():
    # Crear 5 cuentas bancarias con saldos iniciales según especificación
    cuentas = [Cuenta(i, 1000*(i+1)) for i in range(5)]
    
    print("=== SIMULACIÓN SIN DEADLOCK - PREVENCIÓN POR ORDENAMIENTO DE RECURSOS ===")
    print("TÉCNICA: Prevención de Espera Circular")
    print("ESTRATEGIA: Adquisición de locks en orden ascendente por ID de cuenta")
    print()
    
    print("Estado inicial de cuentas:")
    for c in cuentas:
        print(f"  {c}")
    print()
    
    # Tabla de transferencias según especificación del documento (punto 2.1)
    operaciones = [
        [(0,1,200), (1,2,300), (2,0,150)],    # Thread 1
        [(1,0,250), (0,2,100), (2,1,200)],    # Thread 2
        [(2,3,300), (3,4,400), (4,2,250)],    # Thread 3
        [(3,2,350), (2,4,200), (4,3,300)],    # Thread 4
        [(4,0,400), (0,3,250), (3,4,150)],    # Thread 5
        [(0,4,300), (4,1,350), (1,0,200)],    # Thread 6
        [(1,3,250), (3,0,300), (0,1,150)],    # Thread 7
        [(2,1,200), (1,4,250), (4,2,300)],    # Thread 8
        [(3,1,300), (1,2,200), (2,3,250)],    # Thread 9
        [(4,3,350), (3,2,250), (2,4,200)],    # Thread 10
    ]

    print("Iniciando 10 threads con transferencias concurrentes...")
    print("VERSIÓN SIN DEADLOCK: Prevención por ordenamiento de recursos")
    print("-" * 70)
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.time()
    
    threads = []
    for i in range(10):
        t = threading.Thread(target=ejecutar_transferencias_sin_deadlock, 
                           args=(cuentas, operaciones[i]), name=f"Thread-{i+1}")
        threads.append(t)
        t.start()

    # Esperar por todos los threads (sin timeout, deberían completarse)
    print("Esperando finalización de threads...")
    threads_completados = 0
    transferencias_totales_exitosas = 0
    
    for t in threads:
        t.join()  # Sin timeout - deberían completarse
        if not t.is_alive():
            threads_completados += 1
    
    tiempo_fin = time.time()
    tiempo_ejecucion = (tiempo_fin - tiempo_inicio) * 1000  # En milisegundos
    
    print(f"\n=== RESULTADOS DEL EXPERIMENTO (SIN DEADLOCK) ===")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.2f} ms")
    print(f"Threads completados: {threads_completados}/10")
    print(f"Threads bloqueados: {10 - threads_completados}/10")
    
    if threads_completados == 10:
        print("\n✅ ÉXITO: Todas las transferencias completadas sin deadlock")
        print("✅ PREVENCIÓN EXITOSA: Espera circular eliminada")
    else:
        print(f"\n❌ PROBLEMA: {10 - threads_completados} threads no completaron")
    
    print("\n=== Estado final de cuentas ===")
    saldo_total_inicial = sum(1000*(i+1) for i in range(5))
    saldo_total_final = sum(c.saldo for c in cuentas)
    
    for c in cuentas:
        print(f"  {c}")
    
    print(f"\n=== Verificación de Consistencia ===")
    print(f"Saldo total inicial: ${saldo_total_inicial}")
    print(f"Saldo total final: ${saldo_total_final}")
    print(f"Conservación de dinero: {'✅ CORRECTO' if saldo_total_inicial == saldo_total_final else '❌ ERROR'}")
    
    print(f"\nTransferencias especificadas: 30 total")
    print(f"Técnica de prevención: Ordenamiento de recursos (lock ordering)")

if __name__ == "__main__":
    main()