"""
Problema: Verificar Franjas Diagonales.

Se te da una matriz de tamaño m x n. Tu tarea es determinar si la matriz tiene franjas diagonales
donde todos los elementos en cada diagonal que va de arriba-izquierda a abajo-derecha son iguales entre sí.

En este contexto, cada franja diagonal recorre la matriz desde la esquina superior izquierda hasta
la esquina inferior derecha. Debes verificar si cada diagonal está compuesta únicamente por un mismo número.

Devuelve True si todas las franjas diagonales cumplen esta condición; de lo contrario, devuelve False.

Ejemplo 1

Entrada:

matrix = [[42, 7, 13, 99],
          [6, 42, 7, 13],
          [1, 6, 42, 7]]

Salida: True

Explicación:

Las diagonales son:

[1]
[6, 6]
[42, 42, 42]
[7, 7, 7]
[13, 13]
[99]

Todos los elementos en cada diagonal son iguales, por lo tanto la respuesta es True.

Ejemplo 2

Entrada:

matrix = [[8, 23],
          [69, 1]]

Salida: False

Explicación:

La diagonal [8, 1] contiene valores diferentes, por lo que no cumple la condición.
"""

def check_diagonal_stripes(matrix):
    # obtener número de filas
    num_rows = len(matrix)

    # obtener número de columnas
    num_cols = len(matrix[0])

    # recorremos desde la fila 1 y columna 1
    # porque vamos a comparar con el elemento anterior (arriba-izquierda)
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            # comparamos el elemento actual con el de la diagonal superior izquierda
            # si son diferentes, la matriz no cumple la condición
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False

    # si todas las comparaciones fueron correctas
    return True

print(check_diagonal_stripes(
    [[42, 7, 13, 99],
     [6, 42, 7, 13],
     [1, 6, 42, 7]]
))

print(check_diagonal_stripes(
    [[48, 23],
     [69, 1]]
))