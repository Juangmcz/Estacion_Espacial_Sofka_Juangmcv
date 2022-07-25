# Estación espacial Sofka

Este proyecto es la solución al reto propuesto por [Sofka](https://www.sofka.com.co/ "Sofka") para el proceso de selección de la liga de entrenamiento.

---

## Descripción

El programa consiste en un inventario de naves espaciales, el cual sirve para almacenar naves de tipo:

> - Tripuladas
> - No Tripuladas
> - Lanzaderas

A su vez estas entidades poseen atributos y métodos que nos van a permitir interactuar con ellas mediante la interfaz gráfica que se diseño para la ejecución del programa.

---

## Modelamiento

### Objetos (Naves)

En el siguiente diagrama se muestran cada una de las clases junto con sus atributos y métodos, asi también como la relación entre ellas.

![Diagrama UML](/recursos/Naves-POO.png)

### Base de datos

En los siguientes diagramas, se aprecian las caracteristicas de cada una de las tablas de la base de datos.

![Diagrama DER lanzaderas](/recursos/DER_lanzaderas.png)
![Diagrama DER No Tripuladas](/recursos/DER_no_tripuladas.png)
![Diagrama DER Tripuladas](/recursos/DER_tripuladas.png)

---

## Caracteristicas

- Crear naves de tipo: tripuladas, no tripuladas y lanzaderas.
- Realizar consultas simples y avanzadas de cada una de las naves almacenadas.
- Interaccción gráfica con los comportamientos que posee cada tipo de nave.

---

## Recursos externos

Para el desarrollo del frontend de la aplicación, se recurrio al framework [QT Designer](https://doc.qt.io/all-topics.html "QT Designer"), el cual posee toda la documentación oficial debidamente organizada para comprender y/o modificar el comportamiento de la interfaz gráfica de la aplicación.

El programa esta desarrollado completamente en [Python](https://www.python.org/ "Python"), especificamente en la versión 3.10.5 [Link de descarga](https://www.python.org/downloads/ "Link de descarga")

---

## Ejecución

### Librerias

Para ejecutar el programa, se deben de instalar todas las librerias descritas en el archivo requirements.txt. Esta instalación se puede hacer de manera rapida con el siguiente comando:

```bash
pip install requirements.txt
```

Para verificar que todo ha sido instalado correctamente, ejecutamos el siguiente comando:

```
pip frezee
```

Y verificamos que aparezcan todas las librerias en la lista.

### Base de datos

En este caso se hizo uso del motor de bases SQL SERVER, por lo tanto se debe de tener instalado el siguiente [driver](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16 "driver") para poder realizar la conexión a la base de datos.

#### Restauración

Para reconstruir la base de datos, se hace uso del archivo de respaldo de la base de datos, el cual esta almacenado en la siguiente ruta:

```
respaldo_bd/Estacion_Espacial_Sofka.bak
```

En caso de que no funcione el método anterior, se puede recurrir a los scripts de creación de cada una de las tres tablas de la base de datos, los cuales estan almacenados en la siguiente ruta:

```
respaldo_bd/tablas
```

En donde se encuentran los siguientes archivos:

> - Tripuladas.sql
> - No_Tripuladas.sql
> - Lanzaderas.sql

#### Conexión

Para cambiar la conexión a la base de datos, se debe de ingresar a la siguiente ruta:

```
comunicaciones/conexion_bd.py
```

Y se debe modificar la siguiente cadena de conexión:

```
"DRIVER={SQL Server};SERVER=MR-PC;UID=sa;PWD=3220"
```

De la siguiente manera:

> - DRIVER, es el driver instalado del motor de la base de datos.
> - SERVER, es el nombre de la equipo donde se encuentra la base de datos.
> - UID, es el nombre del usuario de la conexión de la base de datos.
> - PWD, es la contraseña de la conexión de la base de datos.

---

## Mantente en contacto

Autor - [Juan Guillermo Muñoz Correa](www.linkedin.com/in/juan-guillermo-muñoz-correa-95b817128)

---

## Licencia

![Documentación oficial QT](https://doc.qt.io/style/qt-logo-documentation.svg) [Terminos y condiciones](https://www.qt.io/terms-conditions/ "Terminos y condiciones")

![Python](https://www.python.org/static/img/python-logo.png "Python") [Terminos y condiciones](https://docs.python.org/3/license.html "Terminos y condiciones")
