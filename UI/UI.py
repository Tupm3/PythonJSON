from Models.Context import Context
from Controllers.Controllers import LoginController
import os
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
    def menuSysAdmin(parameter_list):
        pass

    @staticmethod
    def menuSupervisor(parameter_list):
        pass

    @staticmethod
    def login():
        '''# Login\n Funcion inicial del Programa'''
        lc = LoginController()
        usr = input("Ingresa tu usuario:    ")
        psw = input("Ingresa tu contraseña: ")
        exists,rol = lc.verificarUsuario()


        


