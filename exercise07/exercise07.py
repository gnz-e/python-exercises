"""
Problema: fizz_buzz_sum

Escribe una función fizz_buzz_sum para encontrar la suma de todos los
múltiplos de 3 o 5 por debajo de un valor objetivo.

Por ejemplo, si el valor objetivo es 10, los múltiplos de 3 o 5
menores que 10 son: 3, 5, 6 y 9.

Como:
3 + 5 + 6 + 9 = 23 -> entonces la función debería devolver 23.
"""

def fizz_buzz_sum(num):
    # inicializamos la variable que acumulara la suma
    sum_numbers = 0

    # recorre todos los numeros desde 0 hasta num-1
    for i in range(num):
        # verifica si el numero es multiplo de 3 o de 5
        if i % 3 == 0 or i % 5 == 0:
            sum_numbers += i

    # retornar la suma total
    return sum_numbers

def fizz_buzz_sum_(num):
    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)

print(fizz_buzz_sum(10))
print(fizz_buzz_sum(16))
print(fizz_buzz_sum(100))

print(fizz_buzz_sum_(10))
print(fizz_buzz_sum_(16))