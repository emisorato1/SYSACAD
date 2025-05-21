from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Plan():
    nombre: str
    fecha_inicio: str
    fecha_fin: str
    observacion: str