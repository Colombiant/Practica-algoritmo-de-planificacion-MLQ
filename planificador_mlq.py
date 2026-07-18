from collections import deque

from cola_mlq import ColaMLQ


class PlanificadorMLQ:
    """Simula el algoritmo MLQ con tres colas de prioridad fija."""

    def __init__(self, esquema=2):
        self.esquema = esquema
        if esquema == 1:
            self.colas = {
                1: ColaMLQ(1, "RR", quantum=1),
                2: ColaMLQ(2, "RR", quantum=3),
                3: ColaMLQ(3, "SJF"),
            }
        else:
            self.colas = {
                1: ColaMLQ(1, "RR", quantum=3),
                2: ColaMLQ(2, "RR", quantum=5),
                3: ColaMLQ(3, "PRIORITY"),
            }
        self.linea_tiempo = []

    def ejecutar(self, procesos):
        """Ejecuta todos los procesos y devuelve la lista terminada."""
        procesos = sorted(procesos, key=lambda p: (p.at, p.orden))
        pendientes = deque(procesos)
        tiempo = 0
        terminados = []

        while pendientes or self._hay_listos():
            self._pasar_a_listos(pendientes, tiempo)

            if not self._hay_listos():
                tiempo = pendientes[0].at
                self._pasar_a_listos(pendientes, tiempo)

            cola = self._siguiente_cola()
            proceso = cola.tomar()

            if proceso.inicio is None:
                proceso.inicio = tiempo

            duracion = cola.tiempo_ejecucion(proceso)
            inicio = tiempo
            tiempo += duracion
            proceso.restante -= duracion

            self.linea_tiempo.append((proceso.etiqueta, inicio, tiempo, cola.numero))
            self._pasar_a_listos(pendientes, tiempo)

            if proceso.restante > 0:
                cola.agregar(proceso)
            else:
                proceso.fin = tiempo
                terminados.append(proceso)

        return sorted(terminados, key=lambda p: p.orden)

    def _pasar_a_listos(self, pendientes, tiempo):
        """Mueve a su cola los procesos cuyo AT ya llego."""
        while pendientes and pendientes[0].at <= tiempo:
            proceso = pendientes.popleft()
            self.colas[proceso.cola].agregar(proceso)

    def _hay_listos(self):
        return any(cola.hay_procesos() for cola in self.colas.values())

    def _siguiente_cola(self):
        """Escoge la cola lista con mayor prioridad."""
        for numero in sorted(self.colas):
            if self.colas[numero].hay_procesos():
                return self.colas[numero]
        return None
