from pathlib import Path
import sys

from planificador_mlq import PlanificadorMLQ
from proceso import Proceso


def leer_procesos(ruta):
    """Lee un archivo separado por punto y coma y crea objetos Proceso."""
    procesos = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea or linea.startswith("#"):
                continue

            partes = [parte.strip() for parte in linea.split(";")]
            if len(partes) != 5:
                raise ValueError(f"Linea invalida en {ruta}: {linea}")

            etiqueta, bt, at, cola, prioridad = partes
            procesos.append(
                Proceso(
                    etiqueta=etiqueta,
                    bt=float(bt),
                    at=float(at),
                    cola=int(cola),
                    prioridad=int(prioridad),
                    orden=len(procesos),
                )
            )

    return procesos


def numero(valor):
    """Muestra enteros sin decimales y floats con dos decimales."""
    if abs(valor - int(valor)) < 0.00001:
        return str(int(valor))
    return f"{valor:.2f}"


def calcular_promedios(procesos):
    return {
        "WT": sum(p.wt for p in procesos) / len(procesos),
        "CT": sum(p.ct for p in procesos) / len(procesos),
        "RT": sum(p.rt for p in procesos) / len(procesos),
        "TAT": sum(p.tat for p in procesos) / len(procesos),
    }


def escribir_salida(ruta_entrada, ruta_salida, procesos, linea_tiempo, esquema):
    """Escribe el archivo de resultados pedido en el parcial."""
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    promedios = calcular_promedios(procesos)

    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(f"# archivo: {ruta_entrada.name}\n")
        if esquema == 1:
            archivo.write("# esquema: Q1=RR(1), Q2=RR(3), Q3=SJF no expropiativo\n")
        else:
            archivo.write("# esquema: Q1=RR(3), Q2=RR(5), Q3=Priority no expropiativo\n")
        archivo.write("# etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT\n")

        for p in procesos:
            archivo.write(
                f"{p.etiqueta};{numero(p.bt)};{numero(p.at)};{p.cola};"
                f"{p.prioridad};{numero(p.wt)};{numero(p.ct)};"
                f"{numero(p.rt)};{numero(p.tat)}\n"
            )

        archivo.write(
            "# "
            f"WT={numero(promedios['WT'])}; "
            f"CT={numero(promedios['CT'])}; "
            f"RT={numero(promedios['RT'])}; "
            f"TAT={numero(promedios['TAT'])};\n"
        )
        archivo.write("# linea de tiempo: proceso[inicio-fin](cola)\n")
        archivo.write("# ")
        archivo.write(
            " -> ".join(
                f"{etiqueta}[{numero(inicio)}-{numero(fin)}](Q{cola})"
                for etiqueta, inicio, fin, cola in linea_tiempo
            )
        )
        archivo.write("\n")


def ejecutar_archivo(ruta_entrada):
    # --- ESQUEMA 1 ---
    procesos1 = leer_procesos(ruta_entrada)
    planificador1 = PlanificadorMLQ(esquema=1)
    terminados1 = planificador1.ejecutar(procesos1)
    ruta_salida1 = Path("outputs") / "esquema1" / f"{ruta_entrada.stem}_salida.txt"
    escribir_salida(ruta_entrada, ruta_salida1, terminados1, planificador1.linea_tiempo, esquema=1)

    # --- ESQUEMA 2 ---
    procesos2 = leer_procesos(ruta_entrada)
    planificador2 = PlanificadorMLQ(esquema=2)
    terminados2 = planificador2.ejecutar(procesos2)
    
    # Salida organizada para Esquema 2
    ruta_salida2 = Path("outputs") / "esquema2" / f"{ruta_entrada.stem}_salida.txt"
    escribir_salida(ruta_entrada, ruta_salida2, terminados2, planificador2.linea_tiempo, esquema=2)
    
    # Salida por defecto en la raíz para compatibilidad
    ruta_salida_defecto = Path("outputs") / f"{ruta_entrada.stem}_salida.txt"
    escribir_salida(ruta_entrada, ruta_salida_defecto, terminados2, planificador2.linea_tiempo, esquema=2)
    
    return ruta_salida_defecto


def main():
    if len(sys.argv) > 1:
        entradas = [Path(nombre) for nombre in sys.argv[1:]]
    else:
        entradas = sorted(Path("inputs").glob("*.txt"))

    if not entradas:
        print("No se encontraron archivos de entrada.")
        print("Uso: python main.py inputs/mlq025.txt")
        return

    for ruta in entradas:
        salida = ejecutar_archivo(ruta)
        print(f"Procesado {ruta} -> {salida}")


if __name__ == "__main__":
    main()
