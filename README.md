# SYSACAD - Sistema Académico

## Descripción del Proyecto

SYSACAD es una API REST desarrollada en Flask para la gestión de un sistema académico universitario. El sistema permite administrar entidades académicas como universidades, estudiantes, planes de estudio, materias, especialidades, departamentos y más.

### Características Principales

- **Arquitectura en Capas**: Implementa una arquitectura limpia con separación de responsabilidades
- **API RESTful**: Endpoints organizados para operaciones CRUD en todas las entidades
- **Base de Datos**: Integración con PostgreSQL usando SQLAlchemy como ORM
- **Migración de Datos**: Soporte para migraciones con Flask-Migrate
- **Serialización**: Manejo de datos con Marshmallow
- **Generación de Documentos**: Capacidad de generar PDFs y documentos Office
- **Containerización**: Soporte completo para Docker
- **Testing**: Suite de pruebas unitarias incluida

### Arquitectura del Sistema

```
      Test
       ↓
    Service (reglas de negocio)
       ↓
 Repository (consulta y guarda datos)
       ↓
  Base de datos
```

### Entidades del Dominio

El sistema maneja las siguientes entidades académicas:

- **Universidad**: Institución educativa principal
- **Facultad**: Divisiones dentro de la universidad
- **Departamento**: Unidades organizacionales académicas
- **Area**: Áreas de conocimiento
- **Alumno**: Estudiantes del sistema
- **Plan**: Planes de estudio
- **Materia**: Materias/asignaturas
- **Especialidad**: Especializaciones académicas
- **Grado**: Grados académicos
- **Cargo**: Cargos del personal
- **Autoridad**: Autoridades institucionales
- Y más...

## Requerimientos del Sistema

### Prerequisitos

- **Python**: 3.10 o superior
- **PostgreSQL**: 12 o superior
- **Docker** (opcional): Para containerización
- **Git**: Para control de versiones

### Dependencias Principales

- Flask 3.1.1
- Flask-SQLAlchemy 3.1.1
- psycopg2 2.9.10 (driver PostgreSQL)
- Flask-Migrate 4.1.0
- Marshmallow 4.0.0
- WeasyPrint 65.1 (generación de PDFs)
- python-dotenv 1.1.0

## Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/emisorato1/SYSACAD.git
cd SYSACAD
```

### 2. Configuración del Entorno

#### Opción A: Instalación Local

**2.1. Crear Entorno Virtual**

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

**2.2. Instalar Dependencias**

```bash
# Instalar dependencias desde requirements.txt
pip install -r requirements.txt

# O usar el script de instalación
chmod +x install.sh
./install.sh
```

**2.3. Configurar Base de Datos PostgreSQL**

```bash
# Instalar PostgreSQL (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Crear usuario y bases de datos
sudo -u postgres psql
CREATE USER usuario WITH PASSWORD 'password';
CREATE DATABASE DEV_SYSACAD OWNER usuario;
CREATE DATABASE TEST_SYSACAD OWNER usuario;
CREATE DATABASE SYSACAD OWNER usuario;
GRANT ALL PRIVILEGES ON DATABASE DEV_SYSACAD TO usuario;
GRANT ALL PRIVILEGES ON DATABASE TEST_SYSACAD TO usuario;
GRANT ALL PRIVILEGES ON DATABASE SYSACAD TO usuario;
\q
```

### 3. Configuración de Variables de Entorno

**3.1. Crear archivo de configuración**

```bash
# Copiar el archivo de ejemplo
cp env-example .env
```

**3.2. Editar variables de entorno**

```bash
# Editar .env con tus configuraciones
nano .env
```

Configurar las siguientes variables:

```env
# Configuración de Base de Datos
TEST_DATABASE_URI='postgresql+psycopg2://usuario:password@localhost:5432/TEST_SYSACAD'
DEV_DATABASE_URI='postgresql+psycopg2://usuario:password@localhost:5432/DEV_SYSACAD'
PROD_DATABASE_URI='postgresql://usuario:password@localhost:5432/SYSACAD'

# Configuración de SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_RECORD_QUERIES=True

# Configuración de Hashids (opcional)
HASHIDS_MIN_LENGTH=8
HASHIDS_ALPHABET=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
HASHIDS_SALT=tu_salt_secreto

# Clave secreta de Flask
SECRET_KEY=tu_clave_secreta_muy_segura
```

### 4. Inicializar Base de Datos

```bash
# Crear las tablas en la base de datos
python3 -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
```

## Ejecución de la Aplicación

### Método 1: Ejecución Directa

```bash
# Ejecutar en modo desarrollo
python3 app.py

# O usar el script de boot
chmod +x boot.sh
./boot.sh development
```

### Método 2: Con Variables de Entorno

```bash
# Configurar entorno y ejecutar
export FLASK_CONTEXT=development
python3 app.py
```

### Método 3: Usando Docker

**3.1. Construir la imagen**

```bash
docker build -t flask-sysacad:v1.0.0 .
```

**3.2. Ejecutar con Docker Compose**

```bash
cd docker
docker-compose up -d
```

## Verificación de la Instalación

Una vez iniciada la aplicación, puedes verificar que funciona correctamente:

```bash
# Verificar que la API responde
curl http://localhost:5000/api/v1/

# Deberías recibir una respuesta: "OK"
```

## Uso de la API

### Endpoints Principales

La API está disponible en `http://localhost:5000/api/v1/` y incluye endpoints para:

#### Universidades
- `GET /api/v1/universidad` - Listar todas las universidades
- `GET /api/v1/universidad/{id}` - Obtener universidad por ID
- `POST /api/v1/universidad` - Crear nueva universidad
- `PUT /api/v1/universidad/{id}` - Actualizar universidad
- `DELETE /api/v1/universidad/{id}` - Eliminar universidad

#### Planes de Estudio
- `GET /api/v1/plan` - Listar todos los planes
- `GET /api/v1/plan/{id}` - Obtener plan por ID
- `POST /api/v1/plan` - Crear nuevo plan
- `PUT /api/v1/plan/{id}` - Actualizar plan
- `DELETE /api/v1/plan/{id}` - Eliminar plan

#### Áreas
- `GET /api/v1/area` - Listar todas las áreas
- `GET /api/v1/area/{id}` - Obtener área por ID
- `POST /api/v1/area` - Crear nueva área
- `PUT /api/v1/area/{id}` - Actualizar área
- `DELETE /api/v1/area/{id}` - Eliminar área

#### Grados
- `GET /api/v1/grado` - Listar todos los grados
- `GET /api/v1/grado/{id}` - Obtener grado por ID
- `POST /api/v1/grado` - Crear nuevo grado
- `PUT /api/v1/grado/{id}` - Actualizar grado
- `DELETE /api/v1/grado/{id}` - Eliminar grado

#### Departamentos
- `GET /api/v1/departamento` - Listar todos los departamentos
- `GET /api/v1/departamento/{id}` - Obtener departamento por ID
- `POST /api/v1/departamento` - Crear nuevo departamento
- `PUT /api/v1/departamento/{id}` - Actualizar departamento
- `DELETE /api/v1/departamento/{id}` - Eliminar departamento

#### Tipos de Documento
- `GET /api/v1/tipodocumento` - Listar todos los tipos de documento
- `GET /api/v1/tipodocumento/{id}` - Obtener tipo de documento por ID
- `POST /api/v1/tipodocumento` - Crear nuevo tipo de documento
- `PUT /api/v1/tipodocumento/{id}` - Actualizar tipo de documento
- `DELETE /api/v1/tipodocumento/{id}` - Eliminar tipo de documento

#### Tipos de Dedicación
- `GET /api/v1/tipodedicacion` - Listar todos los tipos de dedicación
- `GET /api/v1/tipodedicacion/{id}` - Obtener tipo de dedicación por ID
- `POST /api/v1/tipodedicacion` - Crear nuevo tipo de dedicación
- `PUT /api/v1/tipodedicacion/{id}` - Actualizar tipo de dedicación
- `DELETE /api/v1/tipodedicacion/{id}` - Eliminar tipo de dedicación

#### Categorías de Cargo
- `GET /api/v1/categoriacargo` - Listar todas las categorías de cargo
- `GET /api/v1/categoriacargo/{id}` - Obtener categoría de cargo por ID
- `POST /api/v1/categoriacargo` - Crear nueva categoría de cargo
- `PUT /api/v1/categoriacargo/{id}` - Actualizar categoría de cargo
- `DELETE /api/v1/categoriacargo/{id}` - Eliminar categoría de cargo

#### Grupos
- `GET /api/v1/grupo` - Listar todos los grupos
- `GET /api/v1/grupo/{id}` - Obtener grupo por ID
- `POST /api/v1/grupo` - Crear nuevo grupo
- `PUT /api/v1/grupo/{id}` - Actualizar grupo
- `DELETE /api/v1/grupo/{id}` - Eliminar grupo

#### Certificados
- `GET /api/v1/certificado` - Listar todos los certificados
- `GET /api/v1/certificado/{id}` - Obtener certificado por ID
- `POST /api/v1/certificado` - Crear nuevo certificado
- `PUT /api/v1/certificado/{id}` - Actualizar certificado
- `DELETE /api/v1/certificado/{id}` - Eliminar certificado

#### Tipos de Especialidad
- `GET /api/v1/tipo_especialidad` - Listar todos los tipos de especialidad
- `GET /api/v1/tipo_especialidad/{id}` - Obtener tipo de especialidad por ID
- `POST /api/v1/tipo_especialidad` - Crear nuevo tipo de especialidad
- `PUT /api/v1/tipo_especialidad/{id}` - Actualizar tipo de especialidad
- `DELETE /api/v1/tipo_especialidad/{id}` - Eliminar tipo de especialidad

#### Cargos
- `GET /api/v1/cargo` - Listar todos los cargos
- `GET /api/v1/cargo/{id}` - Obtener cargo por ID
- `POST /api/v1/cargo` - Crear nuevo cargo
- `PUT /api/v1/cargo/{id}` - Actualizar cargo
- `DELETE /api/v1/cargo/{id}` - Eliminar cargo

### Ejemplo de Uso

```bash
# Crear una nueva universidad
curl -X POST http://localhost:5000/api/v1/universidad \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Universidad Nacional", "direccion": "Calle 123"}'

# Obtener todas las universidades
curl http://localhost:5000/api/v1/universidad

# Crear un nuevo plan de estudio
curl -X POST http://localhost:5000/api/v1/plan \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Ingeniería en Sistemas", "descripcion": "Plan de estudios para ingeniería en sistemas"}'

# Obtener un plan específico
curl http://localhost:5000/api/v1/plan/1
```

## Desarrollo

### Estructura del Proyecto

```
SYSACAD/
├── app/
│   ├── __init__.py          # Factory de la aplicación Flask
│   ├── config/              # Configuraciones por entorno
│   │   ├── __init__.py
│   │   └── config.py        # Configuraciones de desarrollo, testing y producción
│   ├── models/              # Modelos de base de datos
│   │   ├── __init__.py
│   │   ├── alumno.py        # Modelo de estudiante
│   │   ├── universidad.py   # Modelo de universidad
│   │   ├── plan.py          # Modelo de plan de estudios
│   │   ├── materia.py       # Modelo de materia
│   │   └── ...              # Otros modelos
│   ├── services/            # Lógica de negocio
│   │   ├── alumno_service.py
│   │   ├── universidad_service.py
│   │   ├── plan_service.py
│   │   └── ...              # Otros servicios
│   ├── repositories/        # Acceso a datos
│   │   ├── alumno_repositorio.py
│   │   ├── universidad_repositorio.py
│   │   ├── plan_repositorio.py
│   │   └── ...              # Otros repositorios
│   ├── resources/           # Endpoints de la API
│   │   ├── __init__.py
│   │   ├── home.py          # Endpoint principal
│   │   ├── universidad_resource.py
│   │   ├── plan_resource.py
│   │   └── ...              # Otros recursos
│   ├── mapping/             # Serialización con Marshmallow
│   │   ├── universidad_mapping.py
│   │   ├── plan_mapping.py
│   │   └── ...              # Otros mappings
│   ├── validators/          # Validaciones personalizadas
│   ├── static/              # Archivos estáticos
│   └── template/            # Plantillas
├── test/                    # Pruebas unitarias
│   ├── __init__.py
│   ├── instancias.py        # Instancias de prueba
│   ├── test_alumno.py
│   ├── test_universidad.py
│   ├── test_plan.py
│   └── ...                  # Otras pruebas
├── docker/                  # Configuración Docker
│   └── docker-compose.yml
├── app.py                   # Punto de entrada
├── requirements.txt         # Dependencias
├── Dockerfile              # Imagen Docker
├── boot.sh                 # Script de arranque
├── install.sh              # Script de instalación
├── env-example             # Ejemplo de variables de entorno
└── README.md               # Este archivo
```

### Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
python3 -m unittest discover test/

# Ejecutar una prueba específica
python3 -m unittest test.test_plan

# Ejecutar una prueba específica con detalle
python3 -m unittest test.test_plan.PlanTestCase.test_crear -v

# Ejecutar con coverage (si está instalado)
pip install coverage
coverage run -m unittest discover test/
coverage report
coverage html  # Generar reporte HTML
```

### Agregar Nueva Entidad

Para agregar una nueva entidad al sistema, sigue estos pasos:

1. **Crear el modelo** en `app/models/nueva_entidad.py`
2. **Crear el repositorio** en `app/repositories/nueva_entidad_repositorio.py`
3. **Crear el servicio** en `app/services/nueva_entidad_service.py`
4. **Crear el recurso** en `app/resources/nueva_entidad_resource.py`
5. **Crear el mapping** en `app/mapping/nueva_entidad_mapping.py`
6. **Registrar el blueprint** en `app/__init__.py`
7. **Crear las pruebas** en `test/test_nueva_entidad.py`
8. **Actualizar imports** en los archivos `__init__.py` correspondientes

### Ejemplo de Modelo

```python
from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class NuevaEntidad(db.Model):
    __tablename__ = 'nuevas_entidades'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    descripcion: str = db.Column(db.Text, nullable=True)
```

## Configuración de Entornos

El sistema soporta tres entornos diferentes:

### Desarrollo
```bash
export FLASK_CONTEXT=development
python3 app.py
```

### Producción
```bash
export FLASK_CONTEXT=production
python3 app.py
```

### Testing
```bash
export FLASK_CONTEXT=testing
python3 -m unittest discover test/
```

## Troubleshooting

### Problemas Comunes

**Error de conexión a PostgreSQL:**
- Verificar que PostgreSQL esté ejecutándose: `sudo systemctl status postgresql`
- Comprobar las credenciales en el archivo `.env`
- Asegurar que las bases de datos existan: `psql -U usuario -l`
- Verificar que el usuario tenga permisos en las bases de datos

**Error de dependencias:**
- Activar el entorno virtual: `source venv/bin/activate`
- Reinstalar dependencias: `pip install -r requirements.txt --force-reinstall`
- Verificar la versión de Python: `python3 --version`

**Error de puertos:**
- Verificar que el puerto 5000 esté disponible: `netstat -tulpn | grep :5000`
- Cambiar el puerto en `app.py` si es necesario
- Usar otro puerto: `app.run(host="0.0.0.0", debug=True, port=8000)`

**Error de importación de módulos:**
- Verificar que el PYTHONPATH incluya el directorio del proyecto
- Activar el entorno virtual
- Reinstalar dependencias

**Error de variables de entorno:**
- Verificar que el archivo `.env` exista
- Comprobar que las variables estén correctamente definidas
- Usar `export` para definir variables manualmente

### Logs y Debugging

```bash
# Habilitar logs detallados
export FLASK_DEBUG=1
export FLASK_ENV=development

# Ver logs de la aplicación
tail -f logs/app.log  # Si tienes configurado logging en archivos

# Debugging con pdb
# Agregar en el código: import pdb; pdb.set_trace()
```

## Migración de Base de Datos

Si necesitas realizar migraciones de base de datos:

```bash
# Inicializar migraciones (solo la primera vez)
flask db init

# Crear una migración
flask db migrate -m "Descripción de la migración"

# Aplicar migraciones
flask db upgrade

# Ver el historial de migraciones
flask db history

# Revertir una migración
flask db downgrade
```

## Contribución

### Flujo de Desarrollo

1. **Fork del repositorio** en GitHub
2. **Clonar tu fork** localmente:
   ```bash
   git clone https://github.com/tu-usuario/SYSACAD.git
   cd SYSACAD
   ```
3. **Crear rama feature**:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
4. **Realizar cambios y pruebas**
5. **Commit con mensaje descriptivo**:
   ```bash
   git commit -m "Agregar nueva funcionalidad: descripción detallada"
   ```
6. **Push a tu fork**:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
7. **Crear Pull Request** en el repositorio original

### Estándares de Código

- **Seguir PEP 8** para estilo de Python
- **Agregar pruebas** para nueva funcionalidad
- **Documentar funciones y clases** importantes
- **Usar type hints** cuando sea posible
- **Escribir docstrings** para métodos públicos
- **Mantener cobertura de pruebas** por encima del 80%

### Ejemplo de Contribución

```python
def nueva_funcion(parametro: str) -> dict:
    """
    Función de ejemplo que demuestra el estilo de código.
    
    Args:
        parametro (str): Descripción del parámetro
        
    Returns:
        dict: Descripción del valor de retorno
        
    Raises:
        ValueError: Si el parámetro no es válido
    """
    if not parametro:
        raise ValueError("El parámetro no puede estar vacío")
    
    return {"resultado": parametro.upper()}
```

## API Documentation

Para documentación detallada de la API, puedes usar herramientas como Swagger o Postman:

### Swagger/OpenAPI

```python
# Instalar Flask-RESTX para documentación automática
pip install flask-restx

# Agregar a tu aplicación
from flask_restx import Api, Resource

api = Api(app, doc='/docs/')
```

### Colección de Postman

Puedes importar una colección de Postman con todos los endpoints disponibles. Contacta a los mantenedores para obtener el archivo de colección.

## Monitoreo y Logging

### Configuración de Logs

```python
import logging

# Configurar logging en app.py o config.py
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
```

### Métricas de Rendimiento

Para monitorear el rendimiento de la aplicación:

```bash
# Usar werkzeug profiler
pip install werkzeug

# Habilitar profiling en modo desarrollo
export FLASK_PROFILER=1
```

## Seguridad

### Mejores Prácticas

- **Nunca commitear** credenciales o claves secretas
- **Usar variables de entorno** para configuración sensible
- **Validar entrada de usuarios** en todos los endpoints
- **Implementar rate limiting** para APIs públicas
- **Usar HTTPS** en producción
- **Mantener dependencias actualizadas**

### Validación de Seguridad

```bash
# Escanear vulnerabilidades en dependencias
pip install safety
safety check

# Análisis estático de código
pip install bandit
bandit -r app/
```

## Performance

### Optimización de Base de Datos

- **Usar índices** en columnas frecuentemente consultadas
- **Implementar paginación** en endpoints que retornen muchos datos
- **Usar lazy loading** apropiadamente en relaciones SQLAlchemy
- **Monitorear queries** lentas

### Ejemplo de Paginación

```python
@app.route('/api/v1/universidad')
def listar_universidades():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    universidades = Universidad.query.paginate(
        page=page, 
        per_page=per_page, 
        error_out=False
    )
    
    return {
        'data': [u.to_dict() for u in universidades.items],
        'total': universidades.total,
        'pages': universidades.pages,
        'current_page': page
    }
```

## Licencia

[Especificar la licencia del proyecto - por ejemplo: MIT, GPL, Apache 2.0]

## Contacto y Soporte

- **Repositorio**: https://github.com/emisorato1/SYSACAD
- **Issues**: https://github.com/emisorato1/SYSACAD/issues
- **Mantenedor**: [Nombre del mantenedor]
- **Email**: [Email de contacto]

## Changelog

### Versión 1.0.0
- Implementación inicial del sistema
- API REST completa para todas las entidades
- Sistema de pruebas unitarias
- Soporte para Docker
- Documentación completa

---

**Nota**: Este proyecto está en desarrollo activo. Consulta la sección de [Issues](https://github.com/emisorato1/SYSACAD/issues) para ver las funcionalidades pendientes y problemas conocidos.

Para reportar bugs o solicitar nuevas funcionalidades, por favor crea un issue en el repositorio con la información detallada y los pasos para reproducir el problema.