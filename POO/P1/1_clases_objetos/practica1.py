"""
Practica #1 
Implementar paradigma estructurado orientado a objetos

-Crear un programa que obtenga el area de un rectangulo

"""

import os
os.system('cls')

#1 Estructurado
def areaRectangulo(base,altura):
    area=base*altura
    return area

base=6
altura=5
print(f"El area del rectangulo es: {areaRectangulo(5,6)}")


#2 POO
class AreaRectangulo:
    def areaRectangulo(self,base,altura):
        area=base*altura
        return area
        
rectangulo=AreaRectangulo() #Instanciar un objeto de la clase "AreaRectangulo"
print(f"El area del rectangulo es: {areaRectangulo(5,6)}")



class AreaRectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def areaRectangulo(self):
        area=base*altura
        return area
        
rectangulo=AreaRectangulo(5,6) #Instanciar un objeto de la clase "AreaRectangulo"
print(f"El area del rectangulo es: {areaRectangulo(5,6)}")

