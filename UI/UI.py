import os,time
from Controllers.LoginController import LoginController
from Controllers.Sys_AdminController import Sys_AdminController
class UI(object):
    '''# Clase UI\n
    Clase que contiene todas las pantallas y entradas que requieran interacción con el Usuario.\n
    Notas:\n
    - Clase Estática
        - No se necesita instanciar un objeto para iniciar los métodos'''
    @staticmethod
    def menuVendedor(user):
        finished = False
        while not finished: pass
    
    @staticmethod
    def menuSysAdmin(user):
        op = 0
        finished = False
        while not finished:
            print("Menu:")
            print("1) Crear  Personal")
            print("2) Editar Personal")
            print("3) Salir")
            while op<=0 or op>3:
                op = input("Selecciona una opción: ")
            
        login()

    def reset(msg):
        print(msg)
        p = input("Presiona cualquier tecla")

    @staticmethod
    def menuSupervisor(user):
        finished = False
        while not finished: pass


    @staticmethod
    def menu(rol,user):
        msg = " Bienvenido {} ".format(rol)
        print("|"+msg.center(28,"*")+"|")
        if rol == "Vendedor": UI.menuVendedor(user)
        elif rol == "Supervisor": UI.menuSupervisor(user)
        elif rol == "Sys_Admin": UI.menuSysAdmin(user)
        else: print("Error desconocido. Contactar con Sys_Admin")

    @staticmethod
    def login():
        '''# Login\n Funcion inicial del Programa'''
        lc = LoginController()
        verified = False
        os.system("cls")
        while not verified:
            usr = input("Ingresa tu usuario:    ")
            psw = input("Ingresa tu contraseña: ")
            if (lc.verificarUsuario(usr,psw)): 
                rol = lc.getRol(usr)
                verified = True
            if not verified:
                os.system('cls')
                print("Ingresa un usuario válido ")
        os.system("Cls")
        print("Usuario Verificado...")
        print("Cargando Interfaz.",end ="")
        for c in range(0,5):
            time.sleep(0.3)
            print(".",end ="")
        user = lc.getUser(usr+psw)
        os.system('cls')
        return rol,user
    
    def startLogin():
        rol,user = UI.login()
        UI.menu(rol,user)
