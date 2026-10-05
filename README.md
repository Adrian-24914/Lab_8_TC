# Laboratorio 8 - Teoría de la Computación

Proyecto en Python para implementar y medir experimentalmente los programas de los Problemas 1, 2 y 3. Cada ejecución genera una tabla en consola, un CSV con los datos obtenidos y una gráfica PNG independiente.

Las respuestas teóricas, incluyendo las correspondientes a los Problemas 4 y 5, no forman parte de este código. La carpeta `respuestas_teoricas/` está reservada para agregar posteriormente ese PDF.

## Estructura

```text
laboratorio8/
├── main.py
├── problema1.py
├── problema2.py
├── problema3.py
├── requirements.txt
├── README.md
├── resultados/
│   ├── problema1/
│   ├── problema2/
│   └── problema3/
└── respuestas_teoricas/
    └── respuestas.pdf  
```

## Requisitos

- Python 3.10 o superior recomendado.
- `pip`.
- Las dependencias listadas en `requirements.txt`.

## Instalación

Desde la carpeta del proyecto, cree y active un entorno virtual (opcional, pero recomendado):

```bash
python -m venv .venv
```

En Windows:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instale la dependencia:

```bash
pip install -r requirements.txt
```

## Ejecución

Para abrir el menú principal:

```bash
python main.py
```

Opciones del menú:

1. Ejecuta el profiling del Problema 1.
2. Ejecuta el profiling del Problema 2.
3. Ejecuta el profiling del Problema 3.
4. Ejecuta los tres perfiles, uno después de otro.
5. Cierra el programa.

Cada archivo también puede ejecutarse de forma individual:

```bash
python problema1.py
python problema2.py
python problema3.py
```

## Resultados y gráficas

Cada problema utiliza los valores de `n`: 1, 10, 100, 1000, 10000, 100000 y 1000000. Los resultados se muestran como tabla en la consola y se guardan como:

- `resultados/problema1/resultados_problema1.csv` y `grafica_problema1.png`
- `resultados/problema2/resultados_problema2.csv` y `grafica_problema2.png`
- `resultados/problema3/resultados_problema3.csv` y `grafica_problema3.png`

Las gráficas usan escala logarítmica en el eje X para hacer legibles los tamaños de entrada muy distintos. Cada gráfica se abre con `matplotlib` y queda guardada como PNG.

## Metodología de profiling

Se mide el tiempo con `time.perf_counter()`. Para una medición que dura menos de 0.02 segundos, el programa la ejecuta dos veces adicionales y guarda el promedio de las tres ejecuciones. Para los demás casos guarda el tiempo de una sola ejecución. El CSV indica la cantidad de repeticiones usada.

Los ciclos se ejecutan realmente: el programa no reemplaza el trabajo por fórmulas. En el Problema 1, `//` reproduce la división entera de los límites originales.

Los Problemas 2 y 3 ofrecen el parámetro `mostrar_secuencia`. Durante el profiling se mantiene en `False`, de modo que se conservan las iteraciones lógicas pero se evita que el costo de imprimir miles o millones de líneas sea lo que domine la medición. Para una demostración pequeña, puede usarse desde el intérprete de Python, por ejemplo:

```python
from problema2 import problema2
problema2(5, mostrar_secuencia=True)
```

El mismo patrón funciona con `problema3`.

## Límite de tiempo

Las mediciones tienen un límite cooperativo de 3 segundos por ejecución. Si un caso no termina antes de ese límite, se registra como `TIMEOUT` en la tabla y en el CSV, sin inventar un tiempo de ejecución. Los puntos con `TIMEOUT` no se dibujan en la gráfica. Puede cambiarse el valor de `LIMITE_TIEMPO_SEGUNDOS` en el archivo del problema si se desea realizar una corrida más larga.

Los resultados dependen del hardware, el sistema operativo, la versión de Python y la carga de la computadora durante la ejecución.

## Video de demostración


