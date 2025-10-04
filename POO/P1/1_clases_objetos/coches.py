import os
os.system('cls')

class Coches():
    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    # Valores iniciales (es posible declarar al principio de una clase)
    marca=''
    color=''
    modelo=0
    velocidad=0
    caballaje=0
    plazas=0

    # Metodos o acciones o funciones que hace el objeto}

    def acelerar(self):
        pass
        
    def frenar(self):
        pass
# Fin definir clase

# Crear un objeto o instancia la clase

coche1=Coches()
coche1.marca='VW'
coche1.color='Blanco'
coche1.modelo=2022
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5

print(f"\t\tDatos del vehiculo 1: \nmarca: {coche1.marca} \ncolor: {coche1.color} \nmodelo: {coche1.modelo} \
      \nvelocidad: {coche1.velocidad} \ncaballaje: {coche1.caballaje} \nplazas: {coche1.plazas}")

coche2=Coches()
coche2.marca='Nissan'
coche2.color='Azul'
coche2.modelo=2020
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6

print(f"\n\t\tDatos del vehiculo 2: \nmarca: {coche2.marca} \ncolor: {coche2.color} \nmodelo: {coche2.modelo} \
      \nvelocidad: {coche2.velocidad} \ncaballaje: {coche2.caballaje} \nplazas: {coche2.plazas}")

