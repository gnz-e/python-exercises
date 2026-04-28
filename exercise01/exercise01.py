"""
Problema: Representación en cadena base 13.

Dado un número entero num, devuelve su representación en cadena en base 13.

En caso de que no uses mucho la base 13 (¿quién lo hace, verdad?), aquí tienes una explicación rápida:
así como la base 10 usa dígitos del 0 al 9, la base 13 usa esos mismos dígitos,
pero también utiliza las letras A, B y C para representar 10, 11 y 12 respectivamente.

Por ejemplo:

9 en base 13 es "9"
10 en base 13 es "A"
11 en base 13 es "B"
12 en base 13 es "C"
13 en base 13 es "10"
14 en base 13 es "11"
49 en base 13 es "3A" (ya que 3 * 13 + 10 = 49)
69 en base 13 es "54" (ya que 5 * 13 + 4 = 69)
"""

def convert_base13(num):
    # cadena que contiene los digitos posibles en base 13
    base13_digits = "0123456789ABC"

    def convert_positive(num_positive):
        # caso base: si el número es menor que 13
        # simplemente devolvemos su representacion directa
        if num_positive < 13:
            return base13_digits[num_positive]
        else:
            # division entera → reduce el numero
            # modulo → obtiene el residuo (ultimo digito en base 13)
            return convert_positive(num_positive // 13) + base13_digits[num_positive % 13]

    # si el numero es negativo
    if num < 0:
        # convertimos el valor absoluto y agregamos el signo "-"
        return "-" + convert_positive(abs(num))
    else:
        return convert_positive(num)

print(convert_base13(13))
print(convert_base13(49))
print(convert_base13(69))
print(convert_base13(-1845))