from Models.Context import Context
class LoginController:
    '''# Controlador de Login\n
    Puede:\n
    - Verificar Usuarios\n
    Contiene:\n
    - Lista de Personal'''
    roles = {"sys": "Sys_Admin","ven": "Vendedor","sup": "Supervisor"}
    def __init__(self):
        '''Iniciar LoginController'''
        self.cargarListaPersonal()

    def cargarListaPersonal(self):
        '''# Cargar\n
        Carga la lista de Personal recibida de Context '''
        self.listaPersonal = Context.cargarPersonal()
    
    def verificarUsuario(self,username,password):
        '''# Verificar Usuario\nVerifica que el usuario exista y su Rol'''
        keycode = username + password
        exists = False
        rol = ""
        for user in self.listaPersonal:
            if user["Keycode"] == keycode:
                exists = True
        return exists

    def getRol(self,usr):
        '''# Get Rol\nObtiene el rol del usuario'''
        return self.roles[usr[0:3]]
    
    def getUser(self,keycode):
        '''# Get User\n Regresa el objeto usuario (__dict__) '''
        for user in self.listaPersonal:
            if user["Keycode"] == keycode:
                return user
        