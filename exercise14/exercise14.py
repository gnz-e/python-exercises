"""
Problema: Sumar dos números (Add Two Numbers)

Se te dan dos listas enlazadas no vacías que representan dos números enteros no negativos.
Los dígitos están almacenados en orden inverso, y cada nodo contiene un solo dígito.

Suma los dos números y devuelve el resultado como una lista enlazada.

Puedes asumir que los dos números no contienen ceros a la izquierda,
excepto el número 0 en sí.

Ejemplo 1:
Entrada: l1 = [2,4,3], l2 = [5,6,4]
Salida: [7,0,8]
Explicación: 342 + 465 = 807

Ejemplo 2:
Entrada: l1 = [0], l2 = [0]
Salida: [0]

Ejemplo 3:
Entrada: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Salida: [8,9,9,9,0,0,0,1]

Restricciones:
- El número de nodos en cada lista enlazada está en el rango [1, 100].
- 0 <= Node.val <= 9
- Se garantiza que la lista no tiene ceros a la izquierda.
"""

def add_two_numbers(l1, l2):
    l1 = int(''.join(map(str, l1[::-1])))
    l2 = int(''.join(map(str, l2[::-1])))
    sum_list = l1 + l2
    return [int(i) for i in str(sum_list)][::-1]

print(add_two_numbers([2, 4, 3], [5, 6, 4]))
print(add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
print(add_two_numbers([0], [0]))