import os
os.system ('cls')

# Clases
class Alumnos: 
    # Constructor Alumnos
    def __init__(self,nombre,edad,matricula):
        self._nombre=nombre
        self._edad=edad
        self._matricula=matricula
    
    # Metodos de la clase Alumnos
    def inscribirse(self):
        pass

    def estudiar(self):
        pass
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad=edad

    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self,matricula):
        self._matricula=matricula

alumno1=Alumnos("Alex",19,"1234")
alumno2=Alumnos("Cris",20,"5678")

class Profesores:
    # Constructor Profesores
    def __init__(self,nombre,experiencia,num_profesor):
        self._nombre=nombre
        self._experiencia=experiencia
        self._num_profesor=num_profesor

    # Metodos de la clase Profesores
    def impartir():
        pass

    def evaluar():
        pass
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    
    @property
    def experiencia(self):
        return self._experiencia
    @experiencia.setter
    def experiencia(self,experiencia):
        self._experiencia=experiencia

    @property
    def num(self):
        return self._num_profesor
    @num.setter
    def num(self,num):
        self._num_profesor=num

profe1=Profesores("Dagoberto",14,12345678)
profe2=Profesores("Juan Pablo",3,87654321)

class Cursos():
    # Constructor Cursos
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    # Metodos de la clase Cursos
    def asignar():
        pass

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def edad(self,cod):
        self.__codigo=cod

    @property
    def creditos(self):
        return self.__creditos
    @creditos.setter
    def creditos(self,creditos):
        self.__creditos=creditos

curso1=Cursos("POO","67wxdd",10)
curso2=Cursos("Sistemas Operativos","693pv",10)

# Objetos
print("\n\n\t\t.::ALUMNOS::.")
print(f".::Alumno 1::. \nNombre: {alumno1.nombre} \nEdad: {alumno1.edad} \nMatricula: {alumno1.matricula}")
print(f"\n.::Alumno 2::. \nNombre: {alumno2.nombre} \nEdad: {alumno2.edad} \nMatricula: {alumno2.matricula}")

print("\n\n\t\t.::PROFESORES::.")
print(f".::Profesor 1::. \nNombre: {profe1.nombre} \nExperiencia: {profe1.experiencia} \nNumero de Profesor: {profe1.num}")
print(f"\n.::Profesor 2::. \nNombre: {profe2.nombre} \nExperiencia: {profe2.experiencia} \nNumero de Profesor: {profe2.num}")

print("\n\n\t\t.::CURSOS::.")
print(f".::Curso 1::. \nNombre: {curso1.nombre} \nCodigo: {curso1.codigo} \nCreditos: {curso1.creditos}")
print(f"\n.::Curso 2::. \nNombre: {curso2.nombre} \nCodigo: {curso2.codigo} \nCreditos: {curso2.creditos}")

