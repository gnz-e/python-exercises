"""
Problema: Rotate Image

Dada una matriz 2D de tamaño n x n que representa una imagen,
rota la imagen 90 grados en sentido horario.

Debes realizar la rotación en el mismo lugar (in-place),
lo que significa que debes modificar directamente la matriz de entrada.
NO debes crear otra matriz 2D para realizar la rotación.

Ejemplo 1:

Entrada:
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Salida:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Ejemplo 2:

Entrada:
matrix = [
  [5,1,9,11],
  [2,4,8,10],
  [13,3,6,7],
  [15,14,12,16]
]

Salida:
[
  [15,13,2,5],
  [14,3,4,1],
  [12,6,8,9],
  [16,7,10,11]
]
"""

def rotate_image(matrix):
    # Transpone la matriz usando zip()
    element = zip(*matrix)

    # Recorre cada fila transpuesta
    for idx, row in enumerate(element):

        # Invierte la fila y la guarda en la matriz original
        matrix[idx] = list(row[::-1])

    # Retorna la matriz rotada
    return matrix

print(rotate_image([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))

print(rotate_image([
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]))

def rotate_image2(matrix):
    # Obtiene el tamaño de la matriz
    n = len(matrix)

    # Transponer la matriz
    for i in range(n):
        for j in range(i, n):
            # Intercambia filas por columnas (transposicion)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Invertir cada fila
    for row in matrix:
        row.reverse()

    # Retorna la matriz rotada
    return matrix

print(rotate_image2([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))

print(rotate_image2([
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]))

def rotate_image3(matrix):
    # Transponer y luego invertir filas
    matrix[:] = [list(row[::-1]) for row in zip(*matrix)]

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

rotate_image3(matrix1)
rotate_image3(matrix2)

print(matrix1)
print(matrix2)