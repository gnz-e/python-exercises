"""
Una casa de venta de vehículos desea crear una aplicación para gestionar
los autos que tiene disponibles.

Para cada auto se cuenta con la siguiente información:
- Marca
- Modelo
- Precio

Actualmente, la concesionaria dispone de los siguientes vehículos:

Marca        Modelo     Precio
--------------------------------
Volkswagen   Amarok     25000
Volkswagen   Taos       32000
Chevrolet    Onix       22000
Chevrolet    Tracker    30000
Fiat         Cronos     21000
Fiat         Pulse      24000
Toyota       Corolla    28000
Toyota       Yaris      23000
Renault      Stepway    20000
Renault      Duster     27000
Nissan       Versa      25000

Objetivos del ejercicio:

1. Ordenar la lista de vehículos por precio de menor a mayor
   e imprimir el resultado en pantalla.

2. Ordenar la lista de vehículos por marca y luego por precio
   (ambos criterios) e imprimir el resultado.

3. Obtener una lista de todos los vehículos cuyo precio no supere los 23000.

4. Filtrar únicamente los vehículos de las marcas:
   - Chevrolet
   - Volkswagen

5. Mostrar todos los autos cuyo modelo contenga al menos
   una letra "a".
"""

class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Precio: {self.precio}"

cars = [
    Auto("Volkswagen", "Amarok", 25000),
    Auto("Volkswagen", "Taos", 32000),
    Auto("Chevrolet", "Onix", 22000),
    Auto("Chevrolet", "Tracker", 30000),
    Auto("Fiat", "Cronos", 21000),
    Auto("Fiat", "Pulse", 24000),
    Auto("Toyota", "Corolla", 28000),
    Auto("Toyota", "Yaris", 23000),
    Auto("Renault", "Stepway", 20000),
    Auto("Renault", "Duster", 27000),
    Auto("Nissan", "Versa", 25000)
]

# 1. ordenar por precio de menor a mayor
order_price = sorted(cars, key=lambda car: car.precio)

print("VEHICULOS POR PRECIO DE MENOR A MAYOR")
for auto in order_price:
    print(auto)

# 2. ordenar por marca y luego por precio
order_marca_price = sorted(cars, key=lambda car: (car.marca, car.precio)) # cars.sort(key=lambda car: (car.marca, car.precio))

print("\nVEHICULOS POR MARCA Y PRECIO DE MENOR A MAYOR")
for auto in order_marca_price:
    print(auto)

# 3. autos cuyo precio no supere los 23000
cars_under_23000 = [car for car in cars if car.precio <= 23000]

print("\nVEHICULOS CUYO PRECIO ES MENOR O IGUAL A 23000")
for auto in cars_under_23000:
    print(auto)

# 4. autos de marca chevrolet o volkswagen
cars_marcas = [car for car in cars if car.marca == 'Chevrolet' or car.marca == 'Volkswagen']

print("\nVEHICULOS POR MARCA CHEVROLET Y VOLKSWAGEN")
for auto in cars_marcas:
    print(auto)

# 5. autos cuyo modelo contiene al menos una "a"
cars_modelos = [car for car in cars if 'a' in car.modelo.lower()]

print("\nVEHICULOS CUYO MODELO CONTIENE AL MENOS UNA 'a'")
for auto in cars_modelos:
    print(auto)