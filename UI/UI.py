import os,time
from Controllers.LoginController import LoginController
class UI(object):
    '''# Clase UI\n
    Clase que contiene todas las pantallas y entradas que requieran interacción con el Usuario.\n
    Notas:\n
    - Clase Estática
        - No se necesita instanciar un objeto para iniciar los métodos'''
    @staticmethod
    def menuVendedor():
        pass
    
    @staticmethod
    def menuSysAdmin():
        pass

    @staticmethod
    def menuSupervisor():
        pass

    @staticmethod
    def login():
        '''# Login\n Funcion inicial del Programa'''
        lc = LoginController()
        verified = False
        while not verified:
            os.system("cls")
            usr = input("Ingresa tu usuario:    ")
            psw = input("Ingresa tu contraseña: ")
            if (lc.verificarUsuario(usr,psw)): 
                rol = lc.getRol(usr)
                verified = True
        os.system("Cls")
        print("Usuario Verificado...")
        print("Cargando UI.",end ="")
        for c in range(0,5):
            time.sleep(0.5)
            print(".",end ="")
        



        


