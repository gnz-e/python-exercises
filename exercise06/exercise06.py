"""
Problema: Eslabón Fuerte Más Débil

¿Conoces la frase “una cadena es tan fuerte como su eslabón más débil”?

Imagina una cerca de eslabones representada como una matriz llamada `strength`.
Cada posición (i, j) contiene un número que indica qué tan fuerte es ese eslabón.
Entre más alto el número, más fuerte es. Todos los valores son únicos.

Definición:
El “Eslabón Fuerte Más Débil” es un número que cumple:

1. Es el valor más pequeño en su fila
2. Es el valor más grande en su columna

Objetivo:
Dada la matriz `strength`, devuelve ese número si existe.
Si no existe, devuelve -1.

Se garantiza que si existe, será único.

Ejemplo 1:
Entrada:
strength = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Salida: 7

Explicación:
- 7 es el menor en su fila [7, 8, 9] y el mayor en su columna [1, 4, 7]

Ejemplo 2:
Entrada:
strength = [
    [9, 8, 10],
    [6, 15, 4]
]

Salida: -1

Explicación:
Ningún número cumple ambas condiciones.
"""

def weakest_strong_link(strength):
    # obtener el numero de filas
    num_rows = len(strength)

    # recorrer cada fila
    for row in range(num_rows):
        # obtener el valor minimo de la fila actual
        min_value = min(strength[row])

        # encontrar la columna donde está ese valor minimo
        col_index = strength[row].index(min_value)

        # construir la columna completa usando esa posicion
        column = [strength[i][col_index] for i in range(num_rows)]

        # verificar si es el maximo de la columna
        if min_value == max(column):
            return min_value

    return -1

def weakest_strong_link_2(strength):
    num_rows = len(strength)

    for row in range(num_rows):
        min_value = min(strength[row])
        col_index = strength[row].index(min_value)

        is_max = True
        for i in range(num_rows):
            if strength[i][col_index] > min_value:
                is_max = False
                break

        if is_max:
            return min_value

    return -1

print(weakest_strong_link([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(weakest_strong_link([
    [9, 8, 10],
    [6, 15, 4]
]))

print(weakest_strong_link_2([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(weakest_strong_link_2([
    [9, 8, 10],
    [6, 15, 4]
]))