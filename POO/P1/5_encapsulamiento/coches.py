# Instanciar los objetos para posteriormente implementarlos

from coches import Coches

import os
os.system('cls')

num_coches=int(input("Cuantos coches quiere?: "))

for i in range(0,num_coches):
    print(f"\n\t...Datos del Coche...{i+1}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("Plazas: "))

    # Crear Objetos o instanciar la clase

    coche1=Coches()
    print(f"\t\tDatos del Vehiculo: \nMarca: {coche1.marca}, \nColor: {coche1.getColor()}, \nModelo: {coche1.getModelo()}, \
        \nVelocidad: {coche1.getVelocidad()}, \nPotencia: {coche1.getPotencia()}, \Plazas: {coche1.getPlazas()}")

