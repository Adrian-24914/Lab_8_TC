"""Punto de entrada interactivo para el Laboratorio 8."""

from problema1 import ejecutar_profiling as ejecutar_problema1
from problema2 import ejecutar_profiling as ejecutar_problema2
from problema3 import ejecutar_profiling as ejecutar_problema3


def mostrar_menu() -> None:
    print("\n=================================")
    print("LABORATORIO 8")
    print("Teoría de la Computación")
    print("=================================")
    print("1. Ejecutar Problema 1")
    print("2. Ejecutar Problema 2")
    print("3. Ejecutar Problema 3")
    print("4. Ejecutar todos")
    print("5. Salir")


def main() -> None:
    acciones = {
        "1": ejecutar_problema1,
        "2": ejecutar_problema2,
        "3": ejecutar_problema3,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion in acciones:
            acciones[opcion]()
        elif opcion == "4":
            for ejecutar in acciones.values():
                ejecutar()
        elif opcion == "5":
            print("Hasta luego.")
            return
        else:
            print("Opción inválida. Ingrese un número del 1 al 5.")


if __name__ == "__main__":
    main()
