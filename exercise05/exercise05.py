"""
Problema: Devolver arreglo de dígitos y sumarle uno más.

Estamos intentando crear un clon digital de DJ Khaled. No se necesita inteligencia
artificial avanzada ni algoritmos complicados.

Solo debes tomar un número y sumarle uno más.

Más específicamente, se te da un arreglo de enteros digits, donde cada digits[i]
representa el i-ésimo dígito de un número entero positivo. Los dígitos están
ordenados desde el más significativo hasta el menos significativo.

Debes devolver un arreglo de dígitos que represente el número después de sumarle uno.

Ejemplo #1
Entrada: digits = [1, 2, 3]
Salida: [1, 2, 4]

Ejemplo #2
Entrada: digits = [6, 9]
Salida: [7, 0]
"""

def another_one(digits):
    num_lista = int(''.join(map(str, digits))) + 1
    return [int(i) for i in str(num_lista)]

def another_one_2(digits):
    # recorremos la lista desde el ultimo digito (menos significativo)
    # hasta el primero (más significativo)
    for i in range(len(digits) - 1, -1, -1):
        # si el digito actual es menor que 9
        # podemos simplemente sumarle 1 y terminar
        if digits[i] < 9:
            digits[i] += 1
            return digits # ya no hay acarreo, terminamos

        # si el digito es 9, al sumarle 1 se convierte en 0
        # y generamos un acarreo al siguiente digito
        digits[i] = 0

    # si todos los digitos eran 9 (ejemplo: [9,9,9])
    # entonces todos se volvieron 0 y necesitamos agregar un 1 al inicio
    return [1] + digits

print(another_one([1, 2, 3]))
print(another_one([7, 9]))
print(another_one([6, 9]))
print(another_one([9, 9]))
print(another_one([1, 9, 9, 9, 9]))

print(another_one_2([6, 9]))
print(another_one_2([9, 9]))
print(another_one_2([1, 9, 9, 9, 9]))