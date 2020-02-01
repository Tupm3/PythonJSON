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
        '''# Menu Vendedor\n
        Pantalla de control de Vendedor\n
        - Opciones:\n
            - 1) Iniciar Venta\n
            - 2) Salir'''
        finished = False
        while not finished: pass
    
    @staticmethod
    def menuSysAdmin(user):
        '''# Menu Sys_Admin\n
        Pantalla de control de Sys Admin\n
        - Opciones:\n
            - 1) Crear Personal\n
            - 2) Editar Personal\n
            - 3) Salir'''
        op = 0
        finished = False
        while not finished:
            '''Mientras no se lance la bandera de finalizar, el menu volverá a empezar después de cada operación'''
            print("Menu:")
            print("1) Crear  Personal")
            print("2) Editar Personal")
            print("3) Salir")
            while op<=0 or op>3:
                '''Verifica que el input de op esté entre 1 y 3'''
                try:
                    op = int(input("Selecciona una opción: "))
                    if op == 3: finished = True
                        '''Lanza la bandera de finalizar'''
                except Exception as e: print("Error, reiniciando menu")
            
        UI.startLogin()
        '''El programa vuelve a empezar desde el login'''

    def reset(msg):
        '''# Reset Programa\n
        Vuelve a ejecutar el Login '''
        print(msg)
        p = input("Presiona cualquier tecla")

    @staticmethod
    def menuSupervisor(user):'''# Menu Vendedor\n
        Pantalla de control de Vendedor\n
        - Opciones:\n
            - 1) Iniciar Venta\n
            - 2) Añadir Productos\n
            - 3) Editar Inventario Existente\n
            - 4) Salir'''
        finished = False
        while not finished: pass


    @staticmethod
    def menu(rol,user):
        '''# Menu\n Menu generico de los 3 tipos de personal'''
        msg = " Bienvenido {} {} ".format(rol,user["Nombre"])
        print("|"+msg.center(28," ")+"|")
        if rol == "Vendedor": UI.menuVendedor(user)
        elif rol == "Supervisor": UI.menuSupervisor(user)
        elif rol == "Sys_Admin": UI.menuSysAdmin(user)
        else: print("Error desconocido. Contactar con Sys_Admin") #Por si hay un error no controlado

    @staticmethod
    def login():
        '''# Login\n
        Se hace el proceso de verificacion de usuario y devuelve tanto el rol como el objeto Persona'''
        lc = LoginController()
        verified = False
        os.system("cls")
        while not verified:
            usr = input("Ingresa tu usuario:    ")
            psw = input("Ingresa tu contraseña: ")
            if usr == "s": exit()
            if (lc.verificarUsuario(usr,psw)): 
                rol = lc.getRol(usr)
                verified = True
            if not verified:
                ''' Si se detecta que el usuario no existe o no concuerdan las credenciales,
                    volverá a pedirlas'''
                os.system('cls')
                print("Ingresa un usuario válido ")
        os.system("Cls")
        print("Usuario Verificado...")
        print("Cargando Interfaz.",end ="")
        for c in range(0,5): #Para que parezca que está cargando realmente la interfaz.
            time.sleep(0.3)
            print(".",end ="")
        user = lc.getUser(usr+psw)
        os.system('cls')
        return rol,user
    
    def startLogin():
        '''# Start Login\n Método Inicial del Programa\n Debido a que login devuelve tanto el rol como el usuario en si, 
        se usa este método para hacer el Main.py más corto'''
        rol,user = UI.login()
        UI.menu(rol,user)
