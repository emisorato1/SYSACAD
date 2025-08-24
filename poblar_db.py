# poblar_db.py
from app import create_app, db
from app.models.universidad import Universidad
from app.models.facultad import Facultad
from app.models.categoriacargo import CategoriaCargo
from app.models.tipodedicacion import TipoDedicacion
from app.models.cargo import Cargo
from app.models.area import Area
from app.models.tipodocumento import TipoDocumento
from app.models.grupo import Grupo
from app.models.grado import Grado
from app.models.departamento import Departamento
from app.models.tipoespecialidad import TipoEspecialidad
from app.models.plan import Plan
from app.models.materia import Materia
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.autoridad import Autoridad
from app.models.alumno import Alumno

from datetime import date

app = create_app()
app.app_context().push()

# 1. Universidades
u1 = Universidad(nombre="Universidad Nacional", sigla="UN")
u2 = Universidad(nombre="Universidad Tecnológica", sigla="UT")
db.session.add_all([u1, u2])
db.session.commit()

# 2. Facultades
f1 = Facultad(
    nombre="Facultad de Ciencias",
    abreviatura="FC",
    directorio="Directorio Ciencias",
    sigla="FCN",
    codigopostal="1000",
    ciudad="Ciudad A",
    domicilio="Calle 1",
    telefono="123456",
    contacto="Contacto Ciencias",
    email="ciencias@universidad.edu",
    universidad_id=u1.id
)
f2 = Facultad(
    nombre="Facultad de Ingeniería",
    abreviatura="FI",
    directorio="Directorio Ingeniería",
    sigla="FING",
    codigopostal="2000",
    ciudad="Ciudad B",
    domicilio="Calle 2",
    telefono="654321",
    contacto="Contacto Ingeniería",
    email="ingenieria@universidad.edu",
    universidad_id=u2.id
)
db.session.add_all([f1, f2])
db.session.commit()

# 3. Categoría de Cargo
cc1 = CategoriaCargo(nombre="Titular")
cc2 = CategoriaCargo(nombre="Adjunto")
cc3 = CategoriaCargo(nombre="JTP")
db.session.add_all([cc1, cc2, cc3])
db.session.commit()

# 4. Tipos de Dedicación
td1 = TipoDedicacion(nombre="Exclusiva")
td2 = TipoDedicacion(nombre="Semi-exclusiva")
td3 = TipoDedicacion(nombre="Simple")
db.session.add_all([td1, td2, td3])
db.session.commit()

# 5. Cargos
cargo1 = Cargo(nombre="Profesor", categoria_cargo_id=cc1.id, tipo_dedicacion_id=td1.id)
cargo2 = Cargo(nombre="Ayudante", categoria_cargo_id=cc2.id, tipo_dedicacion_id=td2.id)
db.session.add_all([cargo1, cargo2])
db.session.commit()

# 6. Áreas
a1 = Area(nombre="Ciencias Exactas")
a2 = Area(nombre="Ingeniería")
a3 = Area(nombre="Humanidades")
db.session.add_all([a1, a2, a3])
db.session.commit()

# 7. Tipos de Documento
tdoc1 = TipoDocumento(dni=12345678, libreta_civica="LC123", libreta_enrolamiento="LE456", pasaporte="P789")
tdoc2 = TipoDocumento(dni=87654321, libreta_civica="LC987", libreta_enrolamiento="LE654", pasaporte="P321")
db.session.add_all([tdoc1, tdoc2])
db.session.commit()

# 8. Grupos
g1 = Grupo(nombre="Grupo A")
g2 = Grupo(nombre="Grupo B")
db.session.add_all([g1, g2])
db.session.commit()

# 9. Grados
gr1 = Grado(nombre="Licenciado", descripcion="Título de grado universitario")
gr2 = Grado(nombre="Ingeniero", descripcion="Título de grado universitario")
gr3 = Grado(nombre="Doctor", descripcion="Título de posgrado")
db.session.add_all([gr1, gr2, gr3])
db.session.commit()

# 10. Departamentos
d1 = Departamento(nombre="Departamento de Matemática")
d2 = Departamento(nombre="Departamento de Física")
db.session.add_all([d1, d2])
db.session.commit()

# 11. Tipo de Especialidad
te1 = TipoEspecialidad(nombre="Especialidad A")
te2 = TipoEspecialidad(nombre="Especialidad B")
db.session.add_all([te1, te2])
db.session.commit()

# 12. Planes
p1 = Plan(nombre="Plan 2020", fecha_inicio=date(2020,1,1), fecha_fin=date(2024,12,31))
p2 = Plan(nombre="Plan 2025", fecha_inicio=date(2025,1,1), fecha_fin=date(2029,12,31))
db.session.add_all([p1, p2])
db.session.commit()

# 13. Materias
m1 = Materia(nombre="Matemática I", codigo="MAT1")
m2 = Materia(nombre="Física I", codigo="FIS1")
db.session.add_all([m1, m2])
db.session.commit()

# 14. Especialidades
e1 = Especialidad(nombre="Especialidad X", letra="X", tipoespecialidad_id=te1.id, facultad_id=f1.id)
e2 = Especialidad(nombre="Especialidad Y", letra="Y", tipoespecialidad_id=te2.id, facultad_id=f2.id)
db.session.add_all([e1, e2])
db.session.commit()

# 15. Orientaciones
o1 = Orientacion(nombre="Orientación A", especialidad_id=e1.id, plan_id=p1.id, materia_id=m1.id)
o2 = Orientacion(nombre="Orientación B", especialidad_id=e2.id, plan_id=p2.id, materia_id=m2.id)
db.session.add_all([o1, o2])
db.session.commit()

# 16. Autoridades
aut1 = Autoridad(nombre="Rector", cargo_id=cargo1.id)
aut2 = Autoridad(nombre="Decano", cargo_id=cargo2.id)
db.session.add_all([aut1, aut2])
db.session.commit()

# 17. Alumnos
al1 = Alumno(
    nombre="Juan",
    apellido="Pérez",
    nrodocumento="12345678",
    tipo_documento_id=tdoc1.id,
    fecha_nacimiento=date(2000,1,1),
    sexo="M",
    nro_legajo=1001,
    fecha_ingreso=date(2018,3,1),
    especialidad_id=e1.id
)
al2 = Alumno(
    nombre="Ana",
    apellido="Gómez",
    nrodocumento="87654321",
    tipo_documento_id=tdoc2.id,
    fecha_nacimiento=date(2001,2,2),
    sexo="F",
    nro_legajo=1002,
    fecha_ingreso=date(2019,3,1),
    especialidad_id=e2.id
)
db.session.add_all([al1, al2])
db.session.commit()

print("¡Datos cargados correctamente!")