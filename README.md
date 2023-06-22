# Bank API
"Bank API: A comprehensive banking API with essential endpoints for user management, client information, account operations, transfers, and transactions."


## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente en tu entorno de desarrollo:

- Python (Version >= 3.8)

**NOTA: Estos requisitos están especificados en el archivo `requirements.txt`**


## Configuración del entorno

1. Clona este repositorio en tu máquina local:
```shell
   git clone https://github.com/magnusmartinez/bankapi.git
```

2. Accede al directorio del proyecto:
```shell
cd bankapi
```

3. Crea y activa un entorno virtual (opcional pero recomendado):
```shell
python -m venv env
source env/bin/activate
```

**Para Windows:**
```shell
python -m venv env
.\env\Scripts\activate
```

4. Instala las dependencias del proyecto:
```shell
pip install -r requirements.txt
```

5. Crear las variables de entornos del sistema, el archivo debe llamarse `.env` y estar en la raiz del proyecto:
- Asegurate de que la variable de entorno ENGINE_DB este correctamente configurada con tu motor de base de datos. Para MySQL ENGINE_DB=django.db.backends.mysql

```shell
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=95bd10dd5c75ce17add9791cbc193299e6fe3e039f79593d

# Your username, password, host and port for the database
USER_DB=tu_usuario_db
PASSWORD_DB=tu_contraseña_db
HOST_DB=127.0.0.1
PORT_DB=3306

# The name of the database
NAME_DB=bank

# The engine of the database (postgresql, mysql, sqlite3 or oracle)
ENGINE_DB=django.db.backends.mysql

# Debug mode (True or False). Set False in production
DEBUG=True
```

6. Configuración de la base de datos:
- Crea una base de datos para el proyecto en tu sistema de gestión de bases de datos (por ejemplo, PostgreSQL, MySQL, SQLite, etc.).

7. Realiza y aplica las migraciones para la base de datos:

    - Realiza las migraciones para la base de datos
        ```shell
        python manage.py makemigrations
        ```
    - Aplica las migraciones para la base de datos
        ```shell
        python manage.py migrate
        ```

## Ejecución del proyecto

1. Ejecuta el servidor de desarrollo de django
```shell
python manage.py runserver
```
2. Accede al proyecto en tu navegador web en la siguiente dirección: http://localhost:8000/docs para acceder a la documentación en Swagger.

**¡Listo! Ahora deberías poder ejecutar el proyecto Bank API en tu entorno local.** 
