# Proyecto Final - Curso Python - Coderhouse

## Alumno: Gaspari Waldo

## Comisión: 55630

## Nombre del proyecto: Wiki: Estética vehicular

## Desarrollo:

- Objetivo: Se trata de una Wiki relacionada a la estética vehicular, tarea que hoy en día esta creciendo mucho por los productos que se usan y por el acabado final que se logra en los vehículos.
Con esta página, se intenta dar a conocer de qué trata esto y de cómo se compone, dejando que cada usuario que ingrese a la página pueda también aportar alguna información relevante sobre este tema. 

- Descripción: Presenta una página principal en la cual muestra información introductoria acerca del tema, además de tener un Login, un Registro y un "Acerca de mi" con información acerca del desarrollador de la página.
Luego, tenemos 3 vistas que aplican a nuestros modelos en el proyecto: Servicios, Vehículos y Productos. Las mismas solo se pueden acceder logueandose; caso contrario se requiere que el usuario se registre.
En cada una de estas vistas, se podrá ver el listado de todos los elementos que hasta el momento se encuentran cargados y se podrá tanto agregar un nuevo elemento como buscar o eliminar aquellos registros que esten ya cargados en la página. De esta manera, en la base de datos se encuentran cargados algunos registros para cada uno de los modelos mencionados.
una vez logueados, el usuario podra ver su Avatar al lado de su nombre en el menú principal. Cuando un usuario nuevo se registra se genera un avatar por default que luego lo podrá modificar apretando en el botón que se encuentra al lado del mismo. Además, el usuario podrá modificar sus datos personales desde la parte de "Editar usuario".
Por último, si el usuario lo desea puede cerrar su sesión desde "Loguot".

- Modelos: los modelos descritos anteriormente se componen de los siguientes atributos:

* Servicio: - nombre
            - tipo
            - descripcion
* Vehículo: - marca
            - modelo
            - tipo
* Producto: - nombre
            - marca
            - uso

## Superusuario o usuario administrador:

- Usuario: Waldo
- Contraseña: Python2023
