# Guión de Video Explicativo (Máximo 5 Minutos)

Este guión está estructurado para cumplir con el checklist de la entrega y el límite estricto de **5 minutos**. Está organizado por secciones con estimación de tiempo.

---

## ⏱️ Minuto 0:00 - 0:45 | Introducción y Estructura del Proyecto
*   **Visual en pantalla:** Mostrar el explorador de archivos con la estructura del proyecto (`main.py`, `proceso.py`, `cola_mlq.py`, `planificador_mlq.py`, `informe.typ`, `outputs/informe.pdf`).
*   **Qué decir:**
    > *"Hola a todos. En este video voy a explicar mi implementación del algoritmo de planificación de colas multinivel (MLQ) en Python utilizando Programación Orientada a Objetos. 
    > Nuestro simulador ha sido ampliado para soportar y comparar dos esquemas académicos diferentes:
    > El Esquema 1, que implementa Round Robin 1, Round Robin 3 y Shortest Job First no expropiativo en la Cola 3.
    > Y el Esquema 2, que implementa Round Robin 3, Round Robin 5 y prioridad jerárquica no expropiativa en la Cola 3.
    > Analizaremos la arquitectura del código y el impacto de rendimiento en ambos esquemas."*

---

## ⏱️ Minuto 0:45 - 2:00 | Estructuras de Datos y Lógica de Colas
*   **Visual en pantalla:** Código en `proceso.py` y `cola_mlq.py`.
*   **Qué decir:**
    > *"En `Proceso`, modelamos los campos estándar y calculamos mediante `@property` los tiempos de ejecución de CPU: Waiting Time, Completion Time, Response Time y Turnaround Time.
    > En `cola_mlq.py`, manejamos dinámicamente las políticas. La Cola Round Robin utiliza un deque de colecciones con extracción FIFO mediante `popleft()`.
    > Para Shortest Job First (Cola 3 de Esquema 1), seleccionamos el trabajo con menor burst time utilizando `min`.
    > Para Prioridad (Cola 3 de Esquema 2), elegimos con `max` ordenando de mayor a menor jerarquía. En ambas políticas implementamos una lógica robusta de desempate secundaria que considera el tiempo de llegada y el orden original de inserción."*

---

## ⏱️ Minuto 2:00 - 3:00 | Planificador Dinámico e Inicialización
*   **Visual en pantalla:** Código en `planificador_mlq.py` y `main.py`.
*   **Qué decir:**
    > *"La clase `PlanificadorMLQ` recibe en su constructor el parámetro `esquema` (1 o 2). Esto nos permite inicializar de forma dinámica los quántums y las políticas de las colas.
    > El método de despacho en `planificador_mlq.py` siempre otorga la CPU a la cola de mayor prioridad disponible de arriba hacia abajo. En `main.py`, el simulador carga los archivos, ejecuta ambos esquemas para cada entrada plano y escribe los reportes separados en archivos sufijo `*_salida_esquema1.txt` y `*_salida_esquema2.txt`."*

---

## ⏱️ Minuto 3:00 - 4:30 | Comparativa de Resultados y Discrepancias
*   **Visual en pantalla:** Mostrar el PDF del informe compilado en las páginas 2 o 3 con las tablas y líneas Gantt comparativas lado a lado.
*   **Qué decir:**
    > *"En nuestro informe compilado en Typst, comparamos detalladamente los esquemas lado a lado. 
    > Por ejemplo, para `mlq001.txt`, el Esquema 2 promedia un Waiting Time de 18.8 ms contra 20 ms del Esquema 1. Esto se debe a que quántums iniciales más grandes reducen la alternancia redundante entre tareas activas.
    > También quiero destacar que en la guía del parcial y el caso `mlq001` de ejemplo, se halló una discrepancia: los promedios listados corresponden a dividir el tiempo total por 4 en lugar del total real de 5 procesos. El simulador realiza el cálculo matemáticamente correcto dividiendo por 5."*

---

## ⏱️ Minuto 4:30 - 5:00 | Conclusión y Cierre
*   **Visual en pantalla:** Mostrar la diapositiva final o enlace de GitHub.
*   **Qué decir:**
    > *"En conclusión, el simulador demuestra cómo pequeños cambios en los quántums de Round Robin y la política de prioridad de la cola base alteran sustancialmente los tiempos globales de respuesta y espera. Los entregables incluyen el código fuente en GitHub, los archivos planos de métricas y el PDF del informe final. Muchas gracias por su atención."*
