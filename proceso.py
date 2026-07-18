from dataclasses import dataclass, field


@dataclass
class Proceso:
    """Guarda la informacion y los tiempos calculados de un proceso."""

    etiqueta: str
    bt: float
    at: float
    cola: int
    prioridad: int
    orden: int
    restante: float = field(init=False)
    inicio: float | None = None
    fin: float | None = None

    def __post_init__(self):
        # Al inicio, el proceso todavia necesita ejecutar todo su BT.
        self.restante = self.bt

    @property
    def wt(self):
        """Waiting Time: tiempo total esperando en cola."""
        return self.tat - self.bt

    @property
    def ct(self):
        """Completion Time: instante en el que termina."""
        return self.fin

    @property
    def rt(self):
        """Response Time: primera entrada a CPU menos llegada."""
        return self.inicio - self.at

    @property
    def tat(self):
        """Turnaround Time: tiempo desde llegada hasta finalizacion."""
        return self.fin - self.at
