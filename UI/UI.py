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
            print("Menu:") #Capacidades de un sys_admin
            print("1) Crear  Personal")
            print("2) Editar Personal")
            print("3) Salir")
            while op<=0 or op>3:
                '''Verifica que el input de op esté entre 1 y 3'''
                try:
                    op = int(input("Selecciona una opción: "))
                    if op == 3: finished = True
                        '''Lanza la bandera de finalizar'''
                except Exception as e: print("Error, reiniciando menu") #En caso de un error no controlado
            
        UI.startLogin()
        '''El programa vuelve a empezar desde el login'''

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
        print("|"+msg.center(28," ")+"|") #Formato de la impresion del mensaje
        if rol == "Vendedor": UI.menuVendedor(user)
        elif rol == "Supervisor": UI.menuSupervisor(user)
        elif rol == "Sys_Admin": UI.menuSysAdmin(user)
        else: print("Error desconocido. Contactar con Sys_Admin") #Por si hay un error no controlado

    @staticmethod
    def login():
        '''# Login\n
        Se hace el proceso de verificacion de usuario y devuelve tanto el rol como el objeto Persona'''
        lc = LoginController() #Se requiere la instanciacion de un objeto de tipo LoginController
        verified = False
        os.system("cls") #Limpia la pantalla antes de iniciar
        while not verified:
            usr = input("Ingresa tu usuario:    ")
            psw = input("Ingresa tu contraseña: ")
            if usr == "s": exit() #Se teclea 's' en el usuario para salir del loop de Login
            if (lc.verificarUsuario(usr,psw)): #Si el keycode coincide con algún usuario registrado
                rol = lc.getRol(usr) #Manda llamar el Rol del usuario desde el LoginController
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
            time.sleep(0.3) #"Detiene el tiempo por 0.3 segundos "
            print(".",end ="")#Imprime los puntos de "carga"
        user = lc.getUser(usr+psw) #Manda llamar al usuario desde el LoginController
        os.system('cls')
        return rol,user
    
    def startLogin():
        '''# Start Login\n Método Inicial del Programa\n Debido a que login devuelve tanto el rol como el usuario en si, 
        se usa este método para hacer el Main.py más corto'''
        rol,user = UI.login() #Recibe el rol y el usuario
        UI.menu(rol,user) #Los manda al menu genérico para que acceda según sus capacidades
