"""
Ejercicio Practico #2 "Modelar y Diagramar en POO

"""

import os
os.system('cls')

# Clase de Coches
class Coches:
    # Metodo constructor que inicializa los valores cuando se instancia un obejto de la clase
    def __init__(self,color,marca,velocidad):
         # Atributos del objeto:
         self.__color=color
         self.__marca=marca
         self.__velocidad=velocidad

    # Metodos del objeto:
    def acelerar(self,incremento):
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad
    
    def frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    
    def tocar_claxon(self):
        print("Piiiiii")

#  Instanciar o crear objeto de la clase Coches
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)

print(coche1.acelerar(50))
print(coche2.frenar(100))
print(coche1.tocar_claxon())
# print(f"Los valores del objeto 1 son: {coche1.__marca}, {coche1.__color}, {coche1.__velocidad}")
# print(f"El coche 1 aceleró de: {coche1.__velocidad} a {coche1.acelerar(50)}")
# print(f"Los valores del objeto 2 son: {coche2.__marca}, {coche2.__color}, {coche2.__velocidad}")
# print(f"El coche 2 frenó de {coche2.__velocidad} a {coche2.frenar(100)}")


