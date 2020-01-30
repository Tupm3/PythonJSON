class Sys_AdminController:
    '''# Controlador de Sys_Admin\n
    Puede:
    - Crear Personal\n
    - Editar Personal\n
    Contiene:\n
    - Lista de Personal'''

    def __init__(self):
        '''Carga la lista de Personal al instanciarse'''
        self.listaPersonal = Context.cargarPersonal()

    def updateListaPersonal(self):
        '''# Actualizar\n
        Manda actualizar la lista de Personal al Context'''
        Context.updatePersonal(self.listaPersonal)
        self.updateListaPersonal()
    
    def cargarListaPersonal(self):
        '''# Cargar\n
        Carga la lista de Personal recibida de Context '''
        self.listaPersonal = Context.cargarPersonal()
    
    def crearPersona(self,nombre,edad,username,password,rol):
        '''# Crear Persona\n
        Agrega una nueva Persona a la lista de Personal y manda actualizar el JSON'''
        if rol == "Vendedor": username = "ven"+username
        if rol == "Supervisor": username = "sup"+username
        if rol == "Sys_Admin": username = "sys"+username
        persona = Persona(nombre,edad,username,password,rol)
        self.listaPersonal.append(persona)
        self.updateListaPersonal()