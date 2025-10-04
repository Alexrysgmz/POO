#Instanciar los objetos para posteriormente implementarlos
from coches import *

def borrarPantalla():
    import os
    os.system('cls')

def espereTecla():
    input("\t\t...Oprima ENTER para continuar...")

def datos_autos(tipo):
    print(f"\n\t...Ingresar los datos del vehiculo tipo {tipo}...")
    marca=input("Marca ").upper()
    color=input("Color ").upper()
    modelo=input("Modelo ").upper()
    velocidad=int(input("Velocidad "))
    caballaje=int(input("Caballaje "))
    plazas=int(input("Plazas "))
    return marca,color,modelo,velocidad,caballaje,plazas

def imprimir(marca,color,modelo,velocidad,caballaje,plazas):
    print(marca,color,modelo,velocidad,caballaje,plazas)

def autos():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("carro")
    coche=Coches(marca,color,modelo,velocidad,caballaje,plazas)
    imprimir(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    
def camiones():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("camion")
    eje=int(input("Ingrese el eje "))
    capacidad=int(input("Ingresa la capacidad de carga "))

    camion=Camiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidad)

    print(camion.marca,camion.color,camion.modelo,camion.velocidad,camion.caballaje,camion.plazas,camion.eje,camion.capacidadCarga)

def camionetas():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos("camioneta")
    traccion=input("Ingresa la traccion ").upper()
    cerrada=input("Ingresa si es cerrada o no ").upper()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False
    
    coche=Camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
    imprimir(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(coche.traccion,coche.cerrada)

borrarPantalla()
def main():
    opcion=True
    while opcion:
        borrarPantalla()
        opcion=input("\n\t\t...Menu principal...\n1.-Autos\n2.-Camionetas\n3.-Camiones\n4.-Salir\nElige una opcion: ").lower().strip()
        match opcion:
            case "1":
                borrarPantalla()
                print("Autos")
                autos()
                espereTecla()
            case "2":
                borrarPantalla()
                print("Camionetas")
                camionetas()
                espereTecla()
            case "3":
                borrarPantalla()
                print("Camiones")
                camiones()
                espereTecla()  
            case "4":
                borrarPantalla()
                print("Gracias por utilizar el software")
                opcion=False
            case _:
                borrarPantalla()
                print("Opcion no valida, vuelva a intentarlo")
                input("Oprima tecla para continuar")  
                opcion=True

if __name__=="__main__":
    main()

