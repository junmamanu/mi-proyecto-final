# Proyecto final Coder house
Proyecto final desarrollado en conjuto por Juan Manuel Godoy Gandaria, Lorenzo Peña y Leandro Moll

El proyecto se compone a base de Django ver **4.1.2** y python ver **3.10.6**



 Realizado por Godoy Juan Manuel, Lorenzo Peña y Leandro Moll

# Instalación

- El primer paso es instalar [python] con el siguiente comando:

```bash
sudo apt install python
```

- Se debe utilzar [pip](https://pip.pypa.io/en/stable/) para instalar el framework django:

```bash
pip install django
```

- Generar migraciones:

```bash
python3 manage.py migrate
```

- Popular la base de datos:

```bash
python3 manage.py shell < seed_data.py
```

- Iniciar ejecución local del servidor:

```bash
python3 manage.py runserver
```

- Por defecto se inicia en el puerto 8000, pero puede ser cambiado modificando <otro_port> en el comando:

```bash
python3 manage.py runserver 127.0.0.1:<otro_port>
```

# Crear superuser
Para poder utilizar el proyecto debemos crear un super usuario para poder modificar aspectos esenciales a para la administracion del sitio web

Se realiza desde la linea de comandos ejecuntando la siguente linea 

```bash
python3 manage.py createsuperuser
```

Indicamos el usuario:
```bash
Nombre de usuario (leave blank to use '***'):
```
Indicamos el correo electronico:
```bash
Dirección de correo electrónico:
```
Indicamos la password o contraseña:
```bash
Password: 
```

repetimos la password:
```bash
Password (again): 

Superuser created successfully.
```

# Ingresamos por primera vez a nuestra app
Al ingresar por primera vez a la web utilizando el link **127.0.0.1/admin/**

Loguearnos y realizar la carga de el título y el about del mismo. 

Una vez realizado eso la web se encuentra lista para poder ser usada

# Primeros pasos

La web nos permite realizar carga de posteos con titulo de hasta 100 caracteres,  una descripción breve de unos 255 caracteres y una segunda descripción de hasta 3000 caracteres


Contiene las funcionalidades de crear/modificar y editar post,
Creación de usuarios y edición del mismo

# A disfutrar del Blog !!!





