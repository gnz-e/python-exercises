"""
Problema: Longest Substring Without Repeating Characters.

Dada una cadena s, encuentra la longitud de la subcadena 
más larga sin caracteres duplicados.

Ejemplo 1:

Entrada: s = "abcabcbb"
Salida: 3
Explicación: La respuesta es "abc", con una longitud de 3. 
Observa que "bca" y "cab" también son respuestas correctas.

Ejemplo 2:

Entrada: s = "bbbbb"
Salida: 1
Explicación: La respuesta es "b", con una longitud de 1.

Ejemplo 3:

Entrada: s = "pwwkew"
Salida: 3
Explicación: La respuesta es "wke", con una longitud de 3.
Observa que la respuesta debe ser una subcadena; "pwke" es
una subsecuencia, no una subcadena.
"""

def length_of_longest_substring(s: str) -> int:
    # Longitud maxima
    max_length = 0

    # Recorre desde cada posicion
    # i -> inicio de la subcadena
    for i in range(len(s)):
        current = ""

        # Construye subcadenas
        # j -> expansion de la subcadena
        for j in range(i, len(s)):

            # Si el caracter ya existe, detener
            if s[j] in current:
                break

            # Agregar caracter
            current += s[j]

            # Compara y guarda la longitud mayor
            max_length = max(max_length, len(current))

    return max_length

print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))