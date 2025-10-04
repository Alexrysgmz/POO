import os
os.system('cls')

class Coches():

    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    # Valores iniciales (es posible declarar al principio de una clase)
    __marca=''
    __color=''
    __modelo=0
    __velocidad=0
    __caballaje=0
    __plazas=0

    """
        Crear lo metodos setters y getters , estos metodos son importantes y necesarios en todas las clases para que el 
    programador interactue con los valores de los atributos a travez de estos metodos...digamos quye es la manera mas
    adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar o cambiar un valor (set) a un 
    atributo en particular de la clase a traves de un objeto.

        En teoría, se debería de crear un metodo Getters y Setters por cada atributo que contenga la clase.

        Los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves del return.

        Por otro lado, el metodo Set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en
    cuestión.
    """

    #Atributo o propiedad en cuestión

    #1er forma de crear Set y Get
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca=marca

    #2da forma de crear Set y Get
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self,marca):
        self.__marca=marca
    

    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color=color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,modelo):
        self.__modelo=modelo

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad

    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self,plazas):
        self.__plazas=plazas


    #Metodos o acciones o funciones que hace el objeto}
    def acelerar(self):
        pass    
    def frenar(self):
        pass

# Fin definir clase

#Crear un objeto o instancia la clase

coche1=Coches()

coche1.marca="VW"
coche1.setColor=("Blanco")
coche1.setModelo=("2022")
coche1.setVelocidad=(220)
coche1.setCaballaje=(150)
coche1.setPlazas=(5)

print(f"\t\tDatos del vehiculo 1: \n-Marca: {coche1.marca} \n-Color: {coche1.getColor()} \n-Modelo: {coche1.getModelo()} \
      \n-Velocidad: {coche1.getVelocidad()} \n-Caballaje: {coche1.getCaballaje()} \n-Plazas: {coche1.getPlazas()}")

coche2=Coches()

coche2.setMarca=('Nissan')
coche2.setColor=('Azul')
coche2.setModelo=('2020')
coche2.setVelocidad=(100)
coche2.setCaballaje=(150)
coche2.setPlazas=(6)

print(f"\t\tDatos del vehiculo 2: \n-Marca: {coche2.getMarca()} \n-Color: {coche2.getColor()} \n-Modelo: {coche2.getModelo()} \
      \n-Velocidad: {coche2.getVelocidad()} \n-Caballaje: {coche2.getCaballaje()} \n-Plazas: {coche2.getPlazas()}")
