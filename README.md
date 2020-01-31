# PythonJSON
=============

Prueba para guardar datos en archivos JSON teniendo 2 principales de "base de datos".

Dentro del archivo "Personal.json" se encuentran los objetos que pueden:
------------------------------------------------------------------------
+ Supervisor
        + Vender
        + Agregar o modificar inventario
+ Vendedor
        + Vender
+ Sys_Admin
        + Crear o modificar Personal
        
Dentro del archivo "Inventario.json" se encuentran los objetos:
    + Productos

En el código hay varios paquetes:
---------------------------------
+ UI: Dentro está la clase UI que contiene las pantallas de menu y login para los diferentes objetos.
+ Models: Dentro se encuentra todo lo relacionado a los JSONs.
        Plantillas para objetos:\n
        + Persona:\n
            + Requiere:\n
                + Nombre\n
                + Edad\n
                + Rol\n
                + Usuario\n
                + Contraseña\n
                + Status (//TODO)\n
        + Producto: \n
            + Requiere:
                + ID\n
                + Existencias\n
                + Nombre del Producto\n
                + Precio Unitario\n
        Manejo de archivos:\n
        + Context: Conección directa con los archivos JSON.\n
            + Contiene métodos para escribir y leer dichos archivos.\n
+ Controllers: Controladores para los objetos:\n
        + LoginController:\n
            + Contiene los métodos para verificacion de usuarios, keycode y login.\n
        + SupervisorController:\n
            + Hereda de VendedorController\n
            + Contiene métodos para crear y editar inventario\n
        + VendedorController:\n
            + Contiene métodos para venta de inventario\n
        + Sys_AdminController:\n
            + Contiene métodos para editar y crear personal\n
 + DB: Contiene ambos archivos JSON de Base de Datos:\n
        + Inventario.json\n
            + Guarda todos los objetos producto creados\n
        + Personal.json\n
            + Guarda todos los objetos de personal creados.\n
