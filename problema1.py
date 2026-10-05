"""Implementación y profiling del Problema 1."""

from __future__ import annotations

import csv
import time
from pathlib import Path
from typing import Callable

import matplotlib.pyplot as plt


VALORES_N = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
LIMITE_TIEMPO_SEGUNDOS = 3.0
DIRECTORIO_RESULTADOS = Path(__file__).resolve().parent / "resultados" / "problema1"


class TiempoAgotado(Exception):
    """Indica que una ejecución superó el límite configurado."""


def problema1(n: int, limite_tiempo: float | None = None) -> int:
    """Ejecuta literalmente los tres ciclos del programa del enunciado."""
    if n < 0:
        raise ValueError("n debe ser un entero no negativo.")

    limite = None if limite_tiempo is None else time.perf_counter() + limite_tiempo
    contador = 0
    comprobaciones = 0

    for _i in range(n // 2, n + 1):
        for _j in range(1, n - n // 2 + 1):
            k = 1
            while k <= n:
                contador += 1
                comprobaciones += 1
                if limite is not None and comprobaciones % 4096 == 0:
                    if time.perf_counter() >= limite:
                        raise TiempoAgotado
                k *= 2
    return contador


def medir_ejecucion(funcion: Callable[..., int], n: int) -> dict[str, object]:
    """Mide una ejecución; repite solo las mediciones extremadamente rápidas."""
    tiempos: list[float] = []
    try:
        inicio = time.perf_counter()
        resultado = funcion(n, LIMITE_TIEMPO_SEGUNDOS)
        tiempos.append(time.perf_counter() - inicio)

        if tiempos[0] < 0.02:
            for _ in range(2):
                inicio = time.perf_counter()
                resultado = funcion(n, LIMITE_TIEMPO_SEGUNDOS)
                tiempos.append(time.perf_counter() - inicio)

        return {
            "n": n,
            "tiempo_segundos": sum(tiempos) / len(tiempos),
            "estado": "COMPLETADO",
            "repeticiones": len(tiempos),
            "resultado": resultado,
        }
    except TiempoAgotado:
        return {
            "n": n,
            "tiempo_segundos": None,
            "estado": "TIMEOUT",
            "repeticiones": len(tiempos) + 1,
            "resultado": None,
        }


def imprimir_tabla(resultados: list[dict[str, object]]) -> None:
    print("\nProblema 1 - resultados de profiling")
    print(f"{'n':>10}  {'Tiempo (s)':>14}  {'Estado':>12}  {'Repeticiones':>12}")
    print("-" * 56)
    for fila in resultados:
        tiempo = "TIMEOUT" if fila["tiempo_segundos"] is None else f"{fila['tiempo_segundos']:.8f}"
        print(f"{fila['n']:>10}  {tiempo:>14}  {fila['estado']:>12}  {fila['repeticiones']:>12}")


def guardar_csv(resultados: list[dict[str, object]]) -> Path:
    DIRECTORIO_RESULTADOS.mkdir(parents=True, exist_ok=True)
    destino = DIRECTORIO_RESULTADOS / "resultados_problema1.csv"
    with destino.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(
            archivo,
            fieldnames=["n", "tiempo_segundos", "estado", "repeticiones", "resultado"],
        )
        escritor.writeheader()
        escritor.writerows(resultados)
    return destino


def guardar_grafica(resultados: list[dict[str, object]], mostrar: bool = True) -> Path:
    DIRECTORIO_RESULTADOS.mkdir(parents=True, exist_ok=True)
    destino = DIRECTORIO_RESULTADOS / "grafica_problema1.png"
    completos = [fila for fila in resultados if fila["tiempo_segundos"] is not None]

    figura, eje = plt.subplots()
    if completos:
        eje.plot(
            [fila["n"] for fila in completos],
            [fila["tiempo_segundos"] for fila in completos],
            marker="o",
        )
    eje.set_xscale("log")
    eje.set_title("Problema 1 - Tamaño de entrada vs. tiempo de ejecución")
    eje.set_xlabel("Tamaño de entrada (n)")
    eje.set_ylabel("Tiempo de ejecución (segundos)")
    eje.grid(True, which="both", linestyle="--", alpha=0.5)
    figura.tight_layout()
    figura.savefig(destino, dpi=150)
    if mostrar:
        plt.show()
    plt.close(figura)
    return destino


def ejecutar_profiling(mostrar_grafica: bool = True) -> list[dict[str, object]]:
    resultados = [medir_ejecucion(problema1, n) for n in VALORES_N]
    imprimir_tabla(resultados)
    csv_generado = guardar_csv(resultados)
    grafica_generada = guardar_grafica(resultados, mostrar_grafica)
    print(f"CSV guardado en: {csv_generado}")
    print(f"Gráfica guardada en: {grafica_generada}")
    return resultados


if __name__ == "__main__":
    ejecutar_profiling()
