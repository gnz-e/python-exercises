"""
Problema: Contains Duplicate

Dada una lista de enteros llamada input, devuelve True si algún valor aparece
al menos dos veces en la lista. Devuelve False si todos los elementos son distintos.

Ejemplo 1:
Entrada:
input = [1, 3, 5, 7, 1]

Salida:
True

Explicación:
El número 1 aparece dos veces.

--------------------------------------------------

Ejemplo 2:
Entrada:
input = [1, 3, 5, 7]

Salida:
False

Explicación:
Todos los elementos son distintos, no hay duplicados.
"""

def contains_duplicate_count(nums)-> bool:
    duplicate = [i for i in nums if nums.count(i) > 1]
    if duplicate:
        return True

    return False

print(contains_duplicate_count([1, 3, 5, 7, 1]))
print(contains_duplicate_count([1, 3, 5, 7]))

def contains_duplicate_set(nums)-> bool:
    return len(nums) != len(set(nums))

print(contains_duplicate_set([1, 3, 5, 7, 1]))
print(contains_duplicate_set([1, 3, 5, 7]))

def contains_duplicate_seen(nums) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

print(contains_duplicate_seen([1, 3, 5, 7, 1]))
print(contains_duplicate_seen([1, 3, 5, 7]))