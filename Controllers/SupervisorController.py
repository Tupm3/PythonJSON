from Models.Producto import Producto
import VendedorController
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
