# Simulador MLQ Scheduling

Este proyecto implementa un simulador estructurado del algoritmo **MLQ (Multilevel Queue) Scheduling** en Python, empleando Programación Orientada a Objetos (POO).

El código fue desarrollado para la asignatura de **Sistemas Operativos** en la **Universidad del Valle**. Lee procesos definidos en archivos de texto, calcula de forma exacta las métricas de planificación y escribe las salidas comparativas para dos esquemas de planificación diferentes.

---

## Esquemas de Planificación Soportados

El simulador ejecuta secuencialmente ambos esquemas para cada archivo de entrada procesado:

### Esquema 1:
*   **Cola 1 ($Q_1$ - Prioridad Máxima):** Round Robin (RR) con quántum = $1$.
*   **Cola 2 ($Q_2$ - Prioridad Media):** Round Robin (RR) con quántum = $3$.
*   **Cola 3 ($Q_3$ - Prioridad Mínima):** Shortest Job First (SJF) no expropiativo.

### Esquema 2:
*   **Cola 1 ($Q_1$ - Prioridad Máxima):** Round Robin (RR) con quántum = $3$.
*   **Cola 2 ($Q_2$ - Prioridad Media):** Round Robin (RR) con quántum = $5$.
*   **Cola 3 ($Q_3$ - Prioridad Mínima):** Prioridad no expropiativo.

---

## Estructura del Proyecto

```text
mlqq/
├── main.py                 # Punto de entrada y parser de I/O
├── proceso.py              # Clase Proceso y cálculo de métricas
├── cola_mlq.py             # Clase ColaMLQ con políticas RR, SJF y Priority
├── planificador_mlq.py     # Clase PlanificadorMLQ (orquestación jerárquica)
├── README.md               # Documentación general
├── .gitignore              # Exclusión de archivos de reporte e IDE
├── inputs/                 # Casos de prueba (.txt)
│   ├── mlq001.txt
│   ├── mlq002.txt
│   └── ...
└── outputs/                # Resultados de la simulación
    ├── esquema1/           # Salidas exclusivas del Esquema 1
    └── esquema2/           # Salidas exclusivas del Esquema 2
```

---

## Formato de Entrada

Cada proceso se ingresa en el archivo de texto con la siguiente estructura (uno por línea):

```text
etiqueta; BT; AT; Q; Prioridad
```

*   **etiqueta:** Nombre o identificador del proceso.
*   **BT (Burst Time):** Tiempo de CPU requerido.
*   **AT (Arrival Time):** Tiempo de llegada del proceso.
*   **Q (Queue):** Cola inicial donde se hospeda el proceso ($1, 2$ o $3$).
*   **Prioridad:** Jerarquía numérica (usada en la política Priority).

---

## Cómo Ejecutar

Para correr la simulación sobre todos los archivos de prueba en la carpeta `inputs/` y generar de forma organizada los reportes en `outputs/`:

```bash
python main.py
```

---

## Estructura de Salida

Se crean archivos de texto con el sufijo `_salida.txt` para cada esquema dentro de `outputs/esquema1/` y `outputs/esquema2/`. El archivo consolidado contiene:
1. Una tabla con el formato de columnas: `etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT`.
2. Las medias aritméticas de:
    - **WT (Waiting Time):** Tiempo de espera.
    - **CT (Completion Time):** Tiempo de finalización.
    - **RT (Response Time):** Tiempo de respuesta.
    - **TAT (Turnaround Time):** Tiempo de retorno.
3. El diagrama de Gantt textual con la línea de tiempo de ejecución detallada por proceso, cola e inicio-fin (`proceso[inicio-fin](cola)`).

---

## Autor

*   **William Hernández** - Código: `2228934`
*   *Asignatura de Sistemas Operativos*, Ingeniería de Sistemas, **Universidad del Valle**.
