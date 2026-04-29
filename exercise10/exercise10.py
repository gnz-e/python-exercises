"""
Problema: Triangular Sum

Se te da un arreglo de enteros nums, donde cada elemento es un solo dígito (0-9).

La suma triangular de nums es el valor del único elemento que queda en nums
después de que el siguiente proceso termina:

- Sea nums un arreglo con n elementos.
- Si n == 1, termina el proceso.
- De lo contrario, crea un nuevo arreglo newNums de longitud n - 1.
- Para cada índice i, asigna:
    newNums[i] = (nums[i] + nums[i+1]) % 10
  donde % representa el operador módulo.
- Reemplaza nums con newNums.
- Repite el proceso desde el inicio.

Devuelve la suma triangular de nums.

--------------------------------------------------

Ejemplo #1

Entrada:
nums = [1, 3, 5, 7]

Iteración #1:
newNums = [(1 + 3) % 10, (3 + 5) % 10, (5 + 7) % 10]
         = [4, 8, 2]

Iteración #2:
newNums = [(4 + 8) % 10, (8 + 2) % 10]
         = [2, 0]

Iteración #3:
newNums = [(2 + 0) % 10]
         = [2]

Salida:
2

--------------------------------------------------

Ejemplo #2

Entrada:
nums = [9, 7, 5, 3]

Iteración #1:
newNums = [(9 + 7) % 10, (7 + 5) % 10, (5 + 3) % 10]
         = [6, 2, 8]

Iteración #2:
newNums = [(6 + 2) % 10, (2 + 8) % 10]
         = [8, 0]

Iteración #3:
newNums = [(8 + 0) % 10]
         = [8]

Salida:
8
"""

def triangular_sum(nums):
    # si la lista ya tiene un solo elemento, ese es el resultado final
    if len(nums) == 1:
        return nums[0]

    while len(nums) > 1:
        # creamos una nueva lista donde guardaremos los resultados de la iteracion
        new_nums = []

        for i in range(len(nums) - 1):
            # sumamos dos elementos consecutivos y aplicamos modulo 10
            # esto asegura que el resultado siempre sea un digito (0-9)
            value = (nums[i] + nums[i + 1]) % 10

            # agregamos el resultado a la nueva lista
            new_nums.append(value)

        # reemplazamos la lista original con la nueva lista reducida
        nums = new_nums

    return nums[0]

print(triangular_sum([1, 3, 5, 7]))
print(triangular_sum([9, 7, 5, 3]))