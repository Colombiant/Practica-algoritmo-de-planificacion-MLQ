from collections import deque


class ColaMLQ:
    """Representa una cola del planificador MLQ."""

    def __init__(self, numero, politica, quantum=None):
        self.numero = numero
        self.politica = politica
        self.quantum = quantum
        self.procesos = deque()

    def agregar(self, proceso):
        self.procesos.append(proceso)

    def hay_procesos(self):
        return len(self.procesos) > 0

    def tomar(self):
        """Selecciona el siguiente proceso segun la politica de la cola."""
        if self.politica == "PRIORITY":
            mejor = max(
                self.procesos,
                key=lambda p: (p.prioridad, -p.at, -p.orden),
            )
            self.procesos.remove(mejor)
            return mejor

        if self.politica == "SJF":
            mejor = min(self.procesos, key=lambda p: (p.bt, p.at, p.orden))
            self.procesos.remove(mejor)
            return mejor

        return self.procesos.popleft()

    def tiempo_ejecucion(self, proceso):
        """Devuelve cuanto tiempo se ejecuta el proceso en este turno."""
        if self.politica == "RR":
            return min(self.quantum, proceso.restante)
        return proceso.restante
