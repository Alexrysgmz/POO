from conexionBD import *

class Operaciones:

    @staticmethod
    def crear(numero1, numero2, signo, resultado):
        try:
            cursor.execute(
            "insert into bd_operaciones values(null,NOW(),%s,%s,%s,%s)",
            (numero1,numero2,signo,resultado)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def mostrar():
        try:
            cursor.execute(
            "select * from bd_operaciones",
            )
            return cursor.fetchall()
        except:    
            return []

    @staticmethod
    def actualizar(numero1, numero2, signo, resultado, idn):
        try:
            cursor.execute(
                "update bd_operaciones set numero1=%s, numero2=%s, signo=%s, resultado=%s where id=%s",
                (numero1,numero2,signo,resultado,idn)
            )
            conexion.commit()
            return True
        except: 
            return False

    @staticmethod
    def eliminar(id):
            try:
                cursor.execute(
                    "delete from bd_operaciones where id=%s",
                    (id,)
                ) 
                conexion.commit() 
                return True  
            except:    
                return False
    
    @staticmethod
    def mostrarID(idb):
        try:
            cursor.execute(
            "select id from bd_operaciones",
            )
            return True
        except:    
            return False