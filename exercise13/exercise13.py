"""
Problema: Two Sum

Dado un arreglo de enteros nums y un entero target,
devuelve los índices de los dos números que suman exactamente target.

Condiciones:
- Puedes asumir que siempre existe exactamente una solución.
- No puedes usar el mismo elemento dos veces.
- Puedes devolver la respuesta en cualquier orden.

Ejemplo 1:
Entrada: nums = [2, 7, 11, 15], target = 9
Salida: [0, 1]
Explicación: nums[0] + nums[1] = 2 + 7 = 9

Ejemplo 2:
Entrada: nums = [3, 2, 4], target = 6
Salida: [1, 2]
Explicación: nums[1] + nums[2] = 2 + 4 = 6

Ejemplo 3:
Entrada: nums = [3, 3], target = 6
Salida: [0, 1]
Explicación: nums[0] + nums[1] = 3 + 3 = 6
"""

def two_sum(nums, target):
    num_to_index = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], index]

        num_to_index[num] = index

    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))