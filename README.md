# pyramidlogin

## tabla de contenidos

* [Descipcion](#Descripcion)
* [Intalacion y levantar la aplicacion](#Instalacion)
* [Utilizacion](#Utilizacion)

## Descripcion.

la aplicacion utiliza el framework pyramid para levantar una aplicacion web con templates jinja. utilize el framework bootstrap 4 para responsive design.

la aplicacion cuenta con dos url con el formato (`nombreRuta`,`ruta`):

1. (`login`,`/`) es el login principal.
1. (`home`,`/home`) es el home que solo se puede tener acceso si solo se esta logeado.

## Instalacion

1. modificar el url para conectar la base de datos en el archivo development.ini

   `postgresql://{usuario}:{password}@localhost/ihribernik`

1. Generar la base de datos(se puede usar cualquiera yo utilize esta).


    ```
    -- Database: ihribernik

    -- DROP DATABASE ihribernik;

    CREATE DATABASE ihribernik
    WITH OWNER = ihribernik
        ENCODING = 'UTF8'
        TABLESPACE = pg_default
        LC_COLLATE = 'es_AR.UTF-8'
        LC_CTYPE = 'es_AR.UTF-8'
        CONNECTION LIMIT = -1;
    ```

1. Crear primero el virtual env.

   `make virtual-env`

1. Activar manualmente el virtual-env(no pude levantarlo en el makefile y que funcione correctamente)

   `. env/bin/activate`

1. Actualizar setuptools e instalar los paquetes

   `make install`

1. generar tablas.

   `make generate-db`

1. carga de datos iniciales para la prueba.

   `make generate-data`

1. Ejecutar el servidor.

   `make run`

## Utilizacion

1. realizar los pasos anteriores y proceder a realizar el login del mismo:

   ![alt](img/login.png)

1. cuando se quiere logearse con un usuario o contraseña incorrecta pasa lo siguiente:
   ![alt](img/contraseña_erronea.png)
    da como respuesta:
   ![alt](img/fallo.png)

1. cuando se logra conectar correctamente:

   ![alt](img/si_se_conecto.png)

   ![alt](img/captura_home.png)

1. la siguiente pagina, `http://localhost:6543/home` muestra un abm (falta la parte de la modificacion, no la hice porque necesitaba generar otro html), en el cual se pueden dar de alta nuevos instrumentos y borrarlos de la lista.
