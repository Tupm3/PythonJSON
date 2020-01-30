import json ## Esta clase manejará todo lo relacionado con JSON y Base de Datos ##
class Context:
    '''# Clase Context\n
    Esta Clase será la conección directa con la base de datos\n
    Todos los métodos de manejo de JSON están aquí''' 
    PERSONALDB = "./DB/Personal.json" 
    '''Ruta de la base de datos del Personal '''
    INVENTARIODB = "./DB/Inventario.json"
    '''Ruta de la base de datos del inventario '''
    @staticmethod
    def cargarInventario():
        '''Carga los contenidos de Inventario.json'''
        lista = []
        try:
            '''Abrir el archivo JSON de Inventario para cargar los contenidos en una lista'''
            with open(Context.INVENTARIODB, 'r') as jsonFile: lines = jsonFile.read()
            lista = json.loads(lines)
        except FileNotFoundError as fnf: 
            print("No hay archivo JSON Existente") 
            '''Si no hay archivo'''
        return lista
    
    @staticmethod
    def updateInventario(inventario):
        '''Actualiza los contenidos de Inventario.json'''
        update = json.dumps(inventario)
        try:
            with open(Context.INVENTARIODB,'w') as jsonFile: jsonFile.write(update)
        except Exception as e:
            print("Error en la escritura del archivo")
            print("Error: ",e)
    
    @staticmethod
    def cargarPersonal():
        '''Carga los contenidos de Personal.json'''
        lista = []
        try:
            '''Abrir el archivo JSON de Personal para cargar los contenidos en una lista'''
            with open(Context.PERSONALDB, 'r') as jsonFile: lines = jsonFile.read()
            lista = json.loads(lines)
        except FileNotFoundError as fnf: 
            print("No hay archivo JSON Existente") 
            '''Si no hay archivo'''
        return lista
    
    @staticmethod
    def updatePersonal(personal):
        '''Actualiza los contenidos de Personal.json'''
        update = json.dumps(inventario)
        try:
            with open(Context.PERSONALDB,'w') as jsonFile: jsonFile.write(update)
        except Exception as e:
            print("Error en la escritura del archivo")
            print("Error: ",e)