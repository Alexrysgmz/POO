# # Se crea la clase
# class Calculadora: 
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2

#     # Crear Metodos
#     def suma():
#         n1+n2
#     def resta():
#         n1-n2
#     def multi():
#         n1*n2
#     def divi():
#         n1/n2

# # Crear objeto
# calculadora=Calculadora()
# n1=int(input("Ingrese N1: "))
# n2=int(input("Ingrese N2: "))
# print(f"\t\tResultados: \nSuma: {calculadora.suma}, \nResta: {calculadora.resta}, \multiplicacion: {calculadora.multi}\
#       \nDivision: {calculadora.divi}")


# Borrar Pantalla
import os
os.system('cls')

# Crear Clase
class Calculadora:
    def __init__(self):
        self._n1=int(input("Ingrese numero 1: "))
        self._n2=int(input("Ingrese numero 2: "))

    @property
    def n1(self):
        return self._n1
    
    @n1.setter
    def n1(self,n1):
        self._n1=n1

    @property
    def n2(self):
        return self._n2
    
    @n2.setter
    def n2(self,n2):
        self._n2=n2


    # Crear Metodos
    def sumar(self):
        return self._n1+self._n2
        
    def restar(self):
        return self._n1-self._n2
        
    def multiplicar(self):
        return self._n1*self._n2
        
    def dividir(self):
        return self._n1/self._n2

# Crear Objeto  
operacion=Calculadora()
print(f"{operacion.n1}+{operacion.n2}={operacion.sumar()}")
print(f"{operacion.n1}-{operacion.n2}={operacion.restar()}")
print(f"{operacion.n1}*{operacion.n2}={operacion.multiplicar()}")
print(f"{operacion.n1}/{operacion.n2}={operacion.dividir()}")

