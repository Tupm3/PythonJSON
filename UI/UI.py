import os,time
from Controllers.LoginController import LoginController
class UI(object):
    '''# Clase UI\n
    Clase que contiene todas las pantallas y entradas que requieran interacción con el Usuario.\n
    Notas:\n
    - Clase Estática
        - No se necesita instanciar un objeto para iniciar los métodos'''
    @staticmethod
    def menuVendedor(user):
        finished = False
        while not finished:
            print("|"+"Bienvenido Vendedor".center(28," "),user["Nombre"]+"|")
    
    @staticmethod
    def menuSysAdmin(user):
        finished = False
        while not finished:
            print("|"+"Bienvenido SysAdmin".center(28," "),user["Nombre"]+"|")

    @staticmethod
    def menuSupervisor(user):
        finished = False
        while not finished:
            print("|"+"Bienvenido Supervisor".center(28," "),user["Nombre"]+"|")

    @staticmethod
    def menu(rol,user):
        if rol == "Vendedor": UI.menuVendedor(user)
        elif rol == "Supervisor": UI.menuSupervisor(user)
        elif rol == "Sys_Admin": UI.menuSysAdmin(user)
        else: print("Error desconocido. Contactar con Sys_Admin")

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
