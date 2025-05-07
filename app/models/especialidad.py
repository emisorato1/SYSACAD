from dataclasses import dataclass
from app.models.tipo_especialidad import TipoEspecialidad


@dataclass(init=False, repr=True, eq=True)
class Especialidad:
    nombre: str
    letra: str
    observacion: str
    tipo_especialidad: TipoEspecialidad




