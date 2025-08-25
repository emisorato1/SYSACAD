
# SYSACAD

## Descripción

SYSACAD es un sistema académico desarrollado en Python con Flask. Permite gestionar entidades universitarias como alumnos, universidades, materias, certificados y más, está organizado en módulos con servicios, repositorios y mapeos.
Este proyecto también aplica **TDD (Test-Driven Development)**: cada funcionalidad se desarrolla con pruebas unitarias previas, garantizando calidad, mantenibilidad y detección temprana de errores.

---

## Integrantes del equipo

- **Emiliano Sorato**

---


## Requerimientos

- Python 3.10 o superior
- Base de Datos (Por ejemplo: PostgreSQL)
- Dependencias (se instalan con `pip install -r requirements.txt`):
  - Flask
  - Flask-SQLAlchemy
  - Flask-Migrate
  - flask-marshmallow
  - marshmallow
  - SQLAlchemy
  - psycopg2
  - python-dotenv
  - weasyprint
  - python-odt-template
  - docxtpl
  - Flask-hashids

---

## Instalación y ejecución desde cero

### 1. Clonar el repositorio

```bash
git clone https://github.com/emisorato1/SYSACAD.git
cd SYSACAD
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

- Crea una base de datos PostgreSQL (por ejemplo, `dbsysacad`).
- Edita el archivo `.env` (puedes copiar y renombrar `env-example` si existe) y completa los datos de conexión:

```env
TEST_DATABASE_URI='postgresql+psycopg2://usuario:password@localhost:5432/dbsysacad'
DEV_DATABASE_URI='postgresql+psycopg2://usuario:password@localhost:5432/dbsysacad'
PROD_DATABASE_URI='postgresql://usuario:password@localhost:5432/dbsysacad'
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_RECORD_QUERIES=True
SECRET_KEY=tu_clave_secreta
```

### 5. Inicializar la carpeta de migraciones

```bash
flask db init
```

### 6. Crear una migración con los modelos actuales

```bash
flask db migrate -m "Primera migración"
```

### 7. Aplicar la migración a la base de datos

```bash
flask db upgrade
```

---

### 8. Poblar la Base de Datos
```bash
python .\poblar_db.py
```
Se agregaran datos a la base de datos.

---

### 9. Ejecución del servidor

```bash
python app.py
```
La aplicación estará disponible en [http://localhost:5000](http://localhost:5000).

---

## Uso básico

- Accede a los endpoints REST desde el navegador, Postman o curl.
- Ejemplo para obtener universidades:
  ```
  GET http://localhost:5000/api/v1/universidad
  ```
- Ejemplo para generar certificado PDF de un alumno:
  ```
  GET http://localhost:5000/api/v1/certificado/<id>/pdf
  ```
  (Reemplaza `<id>` por el ID de un alumno existente.)

  - Ejemplo para obtener planes:
  ```
  GET http://localhost:5000/api/v1/plan
  ```
  - Ejemplo para obtener cargo:
  ```
  GET http://localhost:5000/api/v1/cargo
  ```
---

## Estructura del proyecto

- `app/` - Código principal (modelos, servicios, repositorios, recursos, mapeos)
- `test/` - Pruebas unitarias y helpers para testeo
- `requirements.txt` - Dependencias del proyecto
- `app.py` - Archivo principal para ejecutar el servidor Flask
- `migrations/` - Migraciones de la base de datos (no se sube a git)
- `.env` - Configuración de entorno (no se sube a git)
- `env-example` - Ejemplo de configuración de entorno

---

## Pruebas

Para ejecutar los tests:

```bash
python -m unittest discover test
```
Tambien se pueden configurar los unitests
---


