"""
Problema: Is Anagram?

Dadas dos cadenas de caracteres, `s` y `t`, devuelve
`True` si son anagramas entre sí; de lo contrario, devuelve `False`.

Un anagrama es una palabra o frase formada al reorganizar las
letras de otra palabra o frase, utilizando todas las letras originales
exactamente una vez.

Puedes asumir que ambas cadenas contendrán caracteres en minúscula.

Ejemplo n.° 1
Entrada: `s = "listen", t = "silent"

Salida: True

Ejemplo n.° 2
Entrada: `s = "astronomer", t = "moonstarer"

Salida: True

Ejemplo n.° 3
Entrada: `s = "lemur", t = "lemer"

Salida: False
"""

def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram("listen", "silent"))
print(is_anagram("astronomer", "moonstarer"))
print(is_anagram("lemur", "lemer"))