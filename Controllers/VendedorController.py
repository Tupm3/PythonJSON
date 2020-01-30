from Models.Context import Context
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
                if (element["Existencias"] - cantidad)>=0:
                    element["Existencias"] -= cantidad
                    disponible = True
                    miProducto = element
                else:
                    print("No quedán disponibles suficientes articulos para la venta")
                    print("Articulos Disponibles: "+element["Existencias"])
                    break
        if registrado and disponible:
            for producto in ticket[0]:
                if idn == producto:
                    ticket[1][index] = miProducto["Nombre_Producto"]
                    ticket[2][index] += cantidad
                    ticket[3][index] = miProducto["Precio_Unitario"]
                    inList = True
                index +=1
            if not inList:
                ticket[0].append(miProducto["ID"])
                ticket[1].append(miProducto["Nombre_Producto"])
                ticket[2].append(cantidad)
                ticket[3].append(miProducto["Precio_Unitario"])
        return ticket