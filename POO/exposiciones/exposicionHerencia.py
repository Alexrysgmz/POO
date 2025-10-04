"""
Programacion Orientada a Objetos

Que es la Herencia en la POO?? 👌👌

"""

import os 
os.system('cls')

# Clase Padre
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def hacer_sonido(self):
        print(f"{self.nombre} esta haciendo sonidos")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Clases Hijas
class Perro(Animal):
    def dormir(self):
        print(f"{self.nombre} está durmiendo")
    def hacer_sonido(self):
        print(f"{self.nombre} está ladrando")
    def mover_cola(self):
        print(f"{self.nombre} está moviendo su colita")

class Gato(Animal):
    def dormir(self):
        print(f"{self.nombre} está durmiendo")
    def hacer_sonido(self):
        print(f"{self.nombre} está Maullando")
    def ronronear(self):
        print(f"{self.nombre} está ronroneando")

# Crear Objetos
perro=Perro("Fido")
gato=Gato("Logan")

# Metodos heredados
perro.dormir()
gato.dormir()
print()

# Metodos Sobreescritos
perro.hacer_sonido()
gato.hacer_sonido()
print()

# Metodos Especificos

perro.mover_cola()
gato.ronronear()
print()

