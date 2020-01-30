from Models.Context import Context
from Models.Persona import Persona
from Models.Producto import Producto
class VendedorController:
    '''# Controlador de vendedor\n
    Puede:\n
    - Hacer Ventas\n
    Contiene:\n
    - Lista de inventario'''
    def __init__(self):
        '''Inicia la lista de inventario recibiendo de Context'''
        self.cargarListaInventario()
    
    def cargarListaInventario(self):
        '''# Cargar\n
        Carga la lista de inventario recibiendo de Context'''
       self.listaInventario = Context.cargarInventario()
    
    def updateListaInventario(self):
        '''# Actualizar\nEnvía la lista de inventario al Context para actualizar el archivo JSON'''
        Context.updateInventario(self.listaInventario)
        self.cargarListaInventario()

    def vender(self,idn,cantidad,ticket):
        ''' #Vender\n
        Metodo llamable cada vez que se quiere hacer una venta\n
        Requiere:\n
        - ID de Producto\n
        - Cantidad\n
        - Lista Bidimensional Ticket\n'''
        index = 0
        inList = False
        registrado = False
        disponible = False
        for element in self.listaInventario:
            if element.ID == int(idn): 
                registrado = True
                if (element.Existencias - cantidad)>=0:
                    element.Existencias -= cantidad
                    disponible = True
                    miProducto = element
                else:
                    print("No quedán disponibles suficientes articulos para la venta")
                    print("Articulos Disponibles: "+element.Existencias)
                    break
        if registrado and disponible:
            for producto in ticket[0]:
                if idn == producto:
                    ticket[1][index] = miProducto.Nombre_Producto
                    ticket[2][index] += cantidad
                    ticket[3][index] = miProducto.Precio_Unitario
                    inList = True
                index +=1
            if not inList:
                ticket[0].append(miProducto.ID)
                ticket[1].append(miProducto.Nombre_Producto)
                ticket[2].append(cantidad)
                ticket[3].append(miProducto.Precio_Unitario)
        return ticket

class SupervisorController(VendedorController):
    '''# Controlador de Supervisor\n
    Puede:
    - Vender\n
    - Crear y añadir Productos\n
    Hereda:\n
    - Lista de inventario'''

    def __init__(self):
        '''Hace atributo suyo la lista después de cargarla del super'''
        super().__init__()
        self.listaInventario = super.listaInventario
        
    
    def agregarExistencias(self,idn,cantidad):
        '''# Agregar Producto\n
        Modifica la cantidad de existencias de un producto'''
        for product in self.listaInventario:
            if product.ID == idn: product.Existencias += cantidad
    
    def crearProducto(self,idn,existencias,nombre,precio):
        '''# Crear Producto\n
        Agrega un nuevo Producto a la lista de Inventario y manda actualizar el JSON'''
        producto = Producto(idn,existencias,nombre,precio)
        self.listaInventario.append(producto)
        self.updateListaInventario()

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

    def updateListaPersonal():
        '''# Actualizar\n
        Manda actualizar la lista de Personal al Context'''
        Context.updatePersonal(self.listaPersonal)
        self.updateListaPersonal()
    
    def cargarListaPersonal():
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
            if user.Keycode == keycode:
                exists = True
        return exists
    
    def getRol(self,usr):
        '''# Get Rol\nObtiene el rol del usuario'''
        return self.roles[usr[0:3]]