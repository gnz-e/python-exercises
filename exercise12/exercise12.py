"""
Problema: Roman to Integer

Se te da un número romano válido y debes convertirlo a un número entero.

Por si no piensas mucho en el Imperio Romano, aquí tienes una tabla rápida
de equivalencias:

Símbolo    Valor
I          1
V          5
X          10
L          50
C          100
D          500
M          1000

Regla general:
Los números romanos se escriben de mayor a menor de izquierda a derecha.

Ejemplo:
XI = 10 + 1 = 11

XXX = 10 + 10 + 10 = 30

--------------------------------------------------

Ejemplo 1:

Entrada:
s = "XI"

Salida:
11

Explicación:
X = 10, I = 1 -> 10 + 1 = 11

--------------------------------------------------

Regla especial (resta):

En algunos casos, un número menor aparece antes de uno mayor para indicar resta.

Ejemplos:
IV = 5 - 1 = 4
IX = 10 - 1 = 9

Esta regla aplica en los siguientes casos:

I antes de V (5) o X (10) -> 4 y 9
X antes de L (50) o C (100) -> 40 y 90
C antes de D (500) o M (1000) -> 400 y 900

--------------------------------------------------

Ejemplo 2:

Entrada:
s = "LXIX"

Salida:
69

Explicación:
L = 50
X = 10
IX = 9

Total: 50 + 10 + 9 = 69
"""

def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):
        value = roman_values[s[i]]

        if i + 1 < len(s) and value < roman_values[s[i + 1]]:
            total -= value
        else:
            total += value

    return total

print(roman_to_int("XI"))
print(roman_to_int("IV"))
print(roman_to_int("CDXX"))
print(roman_to_int("LXIX"))