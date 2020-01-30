class Producto:
    '''# Producto
    Molde de objeto Producto.\n 
    Los datos de esta clase son lo que se exportaran a su respectivo objeto en el archivo JSON\n'''
    def __init__(self,idn = "",existencias = "", nombre = "", precio = ""):
        '''El constructor puede iniciarse vacío o bien puede acceder los valores desde ahí.\n
        Valores:\n- ID\n- Existencias\n- Nombre_Producto\n- Precio_Unitario'''
        self.ID = idn
        self.Existencias = existencias
        self.Nombre_Producto = nombre
        self.Precio_Unitario = precio