"""
Problema: Intersección de dos listas.

Escribe una función para obtener la intersección de dos listas.

Por ejemplo, si
A = [1, 2, 3, 4, 5]
y
B = [0, 1, 3, 7]

entonces deberías devolver: [1, 3]

(los elementos que están presentes en ambas listas).
"""

def intersection(a, b):
    list_number = []

    # recorremos cada elemento de la lista a
    for x in a:
        # recorremos cada elemento de la lista b
        for y in b:
            # comparamos si los valores son iguales y a la vez no permitir duplicados
            if x == y and x not in list_number:
                list_number.append(x)

    return list_number

def intersect(a, b):
    list_number = set(a) & set(b)
    return list(list_number)

print(intersection([1, 2, 3, 4, 5], [0, 1, 3, 7]))
print(intersection([1, 1, 2], [1]))
print(intersection([1, 2, 3], [4, 5, 6]))

print(intersect([1, 2, 3, 4, 5], [0, 1, 3, 7]))
print(intersect([1, 1, 2], [1]))
print(intersect([1, 2, 3], [4, 5, 6]))