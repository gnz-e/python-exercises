"""
Problema: Factorial de un Número.

Dado un número n, escribe una fórmula que devuelva n! (factorial de n).

En caso de que no recuerdes la fórmula del factorial:

n! = n x (n-1) x (n-2) x .. x 2 x 1

Por ejemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120

Entonces, el resultado sería 120.

Se asume que "n" es un número entero no negativo.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

def factorial_iterative_desc(n):
    result = 1

    if n == 0 or n == 1:
        return 1

    # recorremos desde n hasta 1 (sin incluir el 0)
    for i in range(n, 0, -1):
        result *= i

    return result

def factorial_iterative_asc(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(5))

print(factorial_iterative_desc(2))
print(factorial_iterative_desc(5))

print(factorial_iterative_asc(2))
print(factorial_iterative_asc(5))