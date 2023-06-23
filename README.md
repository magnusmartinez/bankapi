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


## Ejemplo de uso

#### 1. Crear un usuario

Este usuario que vamos a crear representa a un cajero o quién esta realizando las acciones dentro del sistema. 

##### Request
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/user/create/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "password": "1234",
  "is_superuser": false,
  "username": "manager",
  "first_name": "John",
  "last_name": "Smith",
  "email": "john.smith@gmail.com",
  "is_staff": false,
  "groups": [],
  "user_permissions": []
}'
```
##### Response
```json
{
  "id": 10,
  "last_login": null,
  "is_superuser": false,
  "username": "manager",
  "first_name": "John",
  "last_name": "Smith",
  "email": "john.smith@gmail.com",
  "is_staff": false,
  "is_active": true,
  "date_joined": "2023-06-22T23:36:59.876372Z",
  "image": "http://127.0.0.1:8000/media/user/image/default.png",
  "groups": [],
  "user_permissions": []
}
```

#### 2. Iniciar sesión
Para iniciar sesión en el sistema, es necesario enviar el usuario y la contraseña establecidos en el paso `1. Crear un usuario`.

##### Request
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/user/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "manager",
  "password": "1234"
}'
```

##### Response
```json
{
  "username": "manager",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzM3MjY4LCJpYXQiOjE2ODc0NzgwNjgsImp0aSI6IjFiMjFmNWQxMTM2NzQ1Yzc4YjJlZGI2ZTEyZmE3NGYwIiwidXNlcl9pZCI6MTB9.wyrV6pONt-mTApCeMsUqF37kl-iwKrUfdC5cb66NdxM",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4ODM0MjA2OCwiaWF0IjoxNjg3NDc4MDY4LCJqdGkiOiIyNmJiOTYyODUxNDc0ZDg1YTJiZTdhNzQxODZhNzUxNSIsInVzZXJfaWQiOjEwfQ.fEBzWPdJ2JlKdL78BE2U4CGMOY_Ih-JZBnW30ZusdWo",
  "user_id": 10
}
```
`username` es el nombre de usuario que acaba de iniciar sesión en el sistema.
`access` es el token de acceso para todas las peticiones que realizará el usuario en el sistema. Este token debe ser incluido en las cabezera de todas las peticiones a la API donde requiera autenticación de usuario.
`refresh` es el token que permite refrecar el inicio de sesión en el sistema sin necesidad de volver a iniciar sesión. Este token tiene una vida util de 10 días.
`user_id` es el id del usuario en la base de datos, con este puedes hacer peticiones para obtener información complementaria del usuario. 

#### 3. Crear una sucursal
La sucursal es la representación de una sucursal de un banco donde estará registrados todos los clientes. No implica que un cliente de una sucursal no pueda realizar operaciones bancarias con un cliente de una sucursal distinta.

##### Request
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/sucursal/create/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzM3MjY4LCJpYXQiOjE2ODc0NzgwNjgsImp0aSI6IjFiMjFmNWQxMTM2NzQ1Yzc4YjJlZGI2ZTEyZmE3NGYwIiwidXNlcl9pZCI6MTB9.wyrV6pONt-mTApCeMsUqF37kl-iwKrUfdC5cb66NdxM' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "BANK BHD",
  "address": "Dominican Republic"
}'
```

##### Response
```json
{
  "id": 3,
  "name": "BANK BHD",
  "address": "Dominican Republic",
  "create_at": "2023-06-23T00:56:18.262987Z",
  "update_at": "2023-06-23T00:56:18.262987Z"
}
```
#### 4. Crear un cliente

Crear un cliente permite posteriormente asociar a este cliente una o varias cuentas donde se puede realizar operaciones como transferencias o transacciones entre sus cuentas o entre cuentas de otros clientes.

##### Request

```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/client/create/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzM3MjY4LCJpYXQiOjE2ODc0NzgwNjgsImp0aSI6IjFiMjFmNWQxMTM2NzQ1Yzc4YjJlZGI2ZTEyZmE3NGYwIiwidXNlcl9pZCI6MTB9.wyrV6pONt-mTApCeMsUqF37kl-iwKrUfdC5cb66NdxM' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Mark",
  "last_name": "Doe",
  "gender": "M",
  "address": "123 Main Street",
  "phone_number": "11234567890",
  "email": "mark.doe@gmail.com",
  "dni": "A1234567",
  "birthday": "1990-01-01",
  "marital_status": "MS1",
  "occupation": "Engineer",
  "place_of_birth": "New York",
  "is_active": true,
  "sucursal": 3
}
'
```

##### Response
```json
{
  "id": 2,
  "first_name": "Mark",
  "last_name": "Doe",
  "gender": "M",
  "address": "123 Main Street",
  "image": "http://127.0.0.1:8000/media/client/image/default.png",
  "phone_number": "11234567890",
  "email": "mark.doe@gmail.com",
  "dni": "A1234567",
  "birthday": "1990-01-01",
  "marital_status": "MS1",
  "occupation": "Engineer",
  "place_of_birth": "New York",
  "is_active": true,
  "create_at": "2023-06-22",
  "update_at": "2023-06-22",
  "sucursal": 3
}
```
#### 5. Crear un cuenta
Crear una cuenta permite a los clientes realizar las operaciones bancarias. Para este ejemplo, crearemos dos cuentas pertenecientes al mismo cliente para realizar operaciones bancarias entre ellas.

*Cuenta #1*
##### Request
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/account/create/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzM3MjY4LCJpYXQiOjE2ODc0NzgwNjgsImp0aSI6IjFiMjFmNWQxMTM2NzQ1Yzc4YjJlZGI2ZTEyZmE3NGYwIiwidXNlcl9pZCI6MTB9.wyrV6pONt-mTApCeMsUqF37kl-iwKrUfdC5cb66NdxM' \
  -H 'Content-Type: application/json' \
  -d '{
  "balance": "2500",
  "account_type": "A001",
  "is_active": true,
  "owner": 2
}'
```
##### Response
```json
{
  "id": 3,
  "balance": "2500.00",
  "account_type": "A001",
  "is_active": true,
  "create_at": "2023-06-22",
  "update_at": "2023-06-22",
  "owner": 2
}
```

*Cuenta #2*
##### Request
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/account/create/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzM3MjY4LCJpYXQiOjE2ODc0NzgwNjgsImp0aSI6IjFiMjFmNWQxMTM2NzQ1Yzc4YjJlZGI2ZTEyZmE3NGYwIiwidXNlcl9pZCI6MTB9.wyrV6pONt-mTApCeMsUqF37kl-iwKrUfdC5cb66NdxM' \
  -H 'Content-Type: application/json' \
  -d '{
  "balance": "8000",
  "account_type": "A001",
  "is_active": true,
  "owner": 2
}'
```
##### Response
```json
{
  "id": 4,
  "balance": "8000.00",
  "account_type": "A001",
  "is_active": true,
  "create_at": "2023-06-22",
  "update_at": "2023-06-22",
  "owner": 2
}
```

#### 6. Listar todas las cuentas
Vamos a listar todas las cuentas (en este caso solo tenemos dos) para poder ver su balance.

##### Request
```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/account/list/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzM3MjY4LCJpYXQiOjE2ODc0NzgwNjgsImp0aSI6IjFiMjFmNWQxMTM2NzQ1Yzc4YjJlZGI2ZTEyZmE3NGYwIiwidXNlcl9pZCI6MTB9.wyrV6pONt-mTApCeMsUqF37kl-iwKrUfdC5cb66NdxM'
```

##### Response
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "balance": "2000.00",
      "number": "41066296600",
      "account_type": "A001",
      "is_active": true,
      "create_at": "2023-06-22",
      "update_at": "2023-06-22",
      "owner": 2
    },
    {
      "id": 4,
      "balance": "8000.00",
      "number": "57611936376",
      "account_type": "A001",
      "is_active": true,
      "create_at": "2023-06-22",
      "update_at": "2023-06-22",
      "owner": 2
    }
  ]
}
```
#### 7. Realizar un transferencia
Podemos realizar transferencias entre cuentas indistintamente quien sea su cliente, en este ejemplo transferiremos 1000 (unidades monetarias) desde `cuenta #1` hacia `cuenta #2` 

##### Request
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/transfer/create/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzM3MjY4LCJpYXQiOjE2ODc0NzgwNjgsImp0aSI6IjFiMjFmNWQxMTM2NzQ1Yzc4YjJlZGI2ZTEyZmE3NGYwIiwidXNlcl9pZCI6MTB9.wyrV6pONt-mTApCeMsUqF37kl-iwKrUfdC5cb66NdxM' \
  -H 'Content-Type: application/json' \
  -d '{
  "amount": "1000",
  "description": "Payment for services",
  "reference": "INV-2023-001",
  "source_account": 3,
  "destination_account": 4
}'
```
##### Response
```json
{
  "id": 12,
  "source_account": 3,
  "destination_account": 4,
  "amount": 1000,
  "description": "Payment for services",
  "status": "S02",
  "reference": "INV-2023-001",
  "code": "6578401300071578",
  "is_active": true
}
```

### Realice nuevamente el paso `6. Listar todas las cuentas`
Al volver a listar las cuentas, podrá evidenciar el cambio en el balance de las cuentas. 

La respuesta debería ser similar a:
##### Response
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "balance": "998.50",
      "number": "41066296600",
      "account_type": "A001",
      "is_active": true,
      "create_at": "2023-06-22",
      "update_at": "2023-06-22",
      "owner": 2
    },
    {
      "id": 4,
      "balance": "9000.00",
      "number": "57611936376",
      "account_type": "A001",
      "is_active": true,
      "create_at": "2023-06-22",
      "update_at": "2023-06-22",
      "owner": 2
    }
  ]
}
```

Aqui podemos observar el movimiento entre las cuentas, el balance de la `cuenta #1` se redujo de 2000 a 998.50, en cambio, el balance de la `cuenta #2` a incrementado de 8000 a 9000.
