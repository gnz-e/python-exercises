"""
Problema: Compound Interest

Para esta empresa Fintech, necesitas construir una calculadora de interés compuesto
utilizando las cuatro variables siguientes como entrada:

Principal: Es la cantidad inicial que depositas en la cuenta. Es el monto base que
comenzará a generar intereses de inmediato.

Tasa de interés: Es el porcentaje de tu saldo actual que el banco añade a tu cuenta
como interés cada año. Por ejemplo, una tasa de interés del 5% significa que el banco
agregará el 5% de tu saldo a tu cuenta cada año.

Aporte anual: Es una cantidad fija que agregas a tu inversión al final de cada año,
como un depósito regular que decides hacer. Cada vez que realizas este aporte, aumenta
tu saldo, lo que a su vez incrementa el interés que ganarás el
siguiente año (ya que el interés se calcula sobre un saldo mayor).

Años de inversión: Es el tiempo durante el cual tu dinero permanece en la cuenta,
generando interés compuesto anualmente. Cuanto más tiempo inviertas, más crecerá
tu saldo, no solo por los intereses, sino también por los aportes adicionales.

Usando estos cuatro valores, calcula el monto final que tendrás después del número
de años especificado, con capitalización anual. Es decir, al final de cada año, ganarás
intereses sobre tu saldo actual y luego harás un aporte adicional.

Devuelve el resultado redondeado a dos decimales.

Ejemplo #1

Entrada:
principal = 500
tasa = 10
aporte = 50
años = 3

Salida:
831.00

Explicación:

Año 1: Inicias con 500, crece un 10% (interés = 50), total 550. Sumando 50 de aporte → 600.
Año 2: 600 crece un 10% (interés = 60), total 660. Sumando 50 → 710.
Año 3: 710 crece un 10% (interés = 71), total 781. Sumando 50 → 831.

Ejemplo #2

Entrada:
principal = 1000
tasa = 20
aporte = 100
años = 10

Salida:
8787.60

P.D.: Como reto matemático, intenta implementar esto sin usar iteraciones (sin for ni while), en tiempo O(1).
"""

def compound_interest(principal, rate, contribution, years):
    for _ in range(years):
        interest  = (rate / 100) * principal
        principal = principal + interest + contribution

    return round(principal, 2)

print(compound_interest(500, 10, 50, 3))
print(compound_interest(1000, 20, 100, 10))

def compound_interest_o1(principal, rate, contribution, years):
    r = rate / 100
    total = principal * (1 + r) ** years + contribution * (((1 + r) ** years - 1) / r)
    return round(total, 2)

print(compound_interest_o1(500, 10, 50, 3))
print(compound_interest_o1(1000, 20, 100, 10))