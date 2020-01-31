# PythonJSON
-------------
Prueba para guardar datos en archivos JSON teniendo 2 principales de "base de datos".

**Nota: El programa debe ejecutarse desde Main.py**

## Archivos JSON
Dentro del archivo "Personal.json" se encuentran los objetos que pueden:
* Supervisor
    * Vender
    * Agregar o modificar inventario
* Vendedor
    * Vender
* Sys_Admin
    * Crear o modificar Personal
        
Dentro del archivo "Inventario.json" se encuentran los objetos:
* Productos

## Paquetes y Código
En el código hay varios paquetes:
* UI: Dentro está la clase UI que contiene las pantallas de Menu y Login para los diferentes objetos.
* Models: Dentro se encuentra todo lo relacionado a los JSONs.
    * Plantillas para objetos:
        * Persona:
            * Requiere:
                * Nombre
                * Edad
                * Rol
                * Usuario
                * Contraseña
                * Status (//TODO)
        * Producto: 
            * Requiere:
                * ID
                * Existencias
                * Nombre del Producto
                * Precio Unitario
    * Manejo de archivos:
        * Context: Conección directa con los archivos JSON.
            * Contiene métodos para escribir y leer dichos archivos.
* Controllers: Controladores para los objetos:
    * LoginController:
        * Contiene los métodos para verificacion de usuarios, keycode y login.
    * SupervisorController:
        * Hereda de VendedorController
        * Contiene métodos para crear y editar inventario
    * VendedorController:
        * Contiene métodos para venta de inventario
    * Sys_AdminController:
        * Contiene métodos para editar y crear personal
* DB: Contiene ambos archivos JSON de Base de Datos:
    * Inventario.json
        * Guarda todos los objetos producto creados
    * Personal.json
        * Guarda todos los objetos de personal creados.
