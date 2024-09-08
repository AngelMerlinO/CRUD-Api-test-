
### Instrucciones para hacer funcionar el API

Este archivo describe cómo hacer funcionar la API de flores, incluyendo la instalación de dependencias, configuración de la base de datos, y ejemplos de cURL para interactuar con la API.

---

#### 1. **Dependencias necesarias y su instalación**

Para que el proyecto funcione correctamente, asegúrate de instalar las siguientes dependencias:

- **FastAPI**: Para crear la API.
- **Uvicorn**: Para ejecutar el servidor ASGI.
- **SQLAlchemy**: Para la conexión y manejo de la base de datos.
- **mysql-connector-python**: Para la conexión a MySQL.

Ejecuta el siguiente comando para instalar todas las dependencias:

```bash
pip install fastapi uvicorn sqlalchemy mysql-connector-python
```

---

#### 2. **Cómo cambiar los datos para conectar a la base de datos en tu PC**

El archivo `models.py` contiene la configuración para la conexión a la base de datos MySQL. Para conectarte a tu propia base de datos local, debes modificar las siguientes líneas con tus credenciales y detalles de conexión:

```python
MYSQL_HOST = 'localhost'  # Cambia si tu base de datos está en otro host
MYSQL_USER = 'tu_usuario'  # Reemplaza con tu nombre de usuario
MYSQL_PASSWORD = 'tu_contraseña'  # Reemplaza con tu contraseña de MySQL
MYSQL_DB = 'floristeria'  # Nombre de la base de datos que usarás
```

Si MySQL está en otro puerto o servidor, ajusta el valor de `MYSQL_HOST` y agrega un puerto, si es necesario, así:

```python
MYSQL_HOST = 'localhost:3306'  # Cambia el puerto si no es el predeterminado 3306
```

---

#### 3. **Cómo ejecutar el archivo que genera la tabla necesaria (nombre del archivo: `create_db.py`)**

El archivo `create_db.py` se encarga de crear las tablas necesarias en la base de datos.

Para ejecutarlo, simplemente usa Python desde la terminal o consola de comandos:

```bash
python create_db.py
```

Esto generará las tablas necesarias en la base de datos especificada en `models.py` (en este caso, la tabla `flores`).

---

#### 4. **cURLs para ejecutar y su funcionamiento**

Puedes interactuar con la API utilizando los siguientes ejemplos de cURL desde la terminal. Si prefieres, también puedes usar Postman para ejecutar estas solicitudes.

##### a) Obtener todas las flores (GET):

Este comando obtiene todas las flores disponibles en el inventario:

```bash
curl -X 'GET'   'http://127.0.0.1:8000/flores'   -H 'accept: application/json'
```

##### b) Obtener una flor por ID (GET):

Este comando obtiene los detalles de una flor específica a través de su ID:

```bash
curl -X 'GET'   'http://127.0.0.1:8000/flores/1'   -H 'accept: application/json'
```

(Reemplaza el `1` con el ID de la flor que deseas obtener.)

##### c) Agregar una nueva flor (POST):

Este comando agrega una nueva flor al inventario. Debes pasar los datos de la flor en formato JSON en el cuerpo de la solicitud.

```bash
curl -X 'POST'   'http://127.0.0.1:8000/flores'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "nombre": "Rosa",
  "descripcion": "Flor roja hermosa",
  "cantidad": 10,
  "disponible": true
}'
```

##### d) Actualizar una flor existente (PUT):

Este comando actualiza una flor existente. Necesitas especificar el ID de la flor en la URL y pasar los nuevos datos en el cuerpo de la solicitud.

```bash
curl -X 'PUT'   'http://127.0.0.1:8000/flores/1'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "nombre": "Rosa actualizada",
  "descripcion": "Flor roja actualizada",
  "cantidad": 5,
  "disponible": true
}'
```

##### e) Eliminar una flor (DELETE):

Este comando elimina una flor a través de su ID.

```bash
curl -X 'DELETE'   'http://127.0.0.1:8000/flores/1'   -H 'accept: application/json'
```

(Reemplaza el `1` con el ID de la flor que deseas eliminar.)

---

### Notas adicionales:
- Asegúrate de que el servidor esté en ejecución en `http://127.0.0.1:8000` o cambia la URL de los cURL si el servidor está en otro host o puerto.
- Puedes verificar la documentación interactiva de la API en `http://127.0.0.1:8000/docs` una vez que el servidor esté en ejecución.
# CRUD-Api-test-
