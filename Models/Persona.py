class Persona:
    '''# Persona
    Molde de objeto Persona.\n 
    Los datos de esta clase son lo que se exportaran a su respectivo objeto en el archivo JSON\n'''
    def __init__(self,nombre = "",edad = "",username = "",password = "",rol="",status = 1):
        '''El constructor puede iniciarse vacío o bien puede acceder los valores desde ahí.\n
        Valores:\n- Nombre\n- Edad\n- Nombre de Usuario\n- Contraseña\n- Rol '''
        self.Nombre = nombre
        self.Edad = edad 
        self.Rol = rol 
        self.Keycode = username+password
        self.Status = status
        ### KeyCode Generado combinando el usuario con la contraseña y hacer más fácil la validación ###