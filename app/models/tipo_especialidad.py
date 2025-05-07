from dataclasses import dataclass


@dataclass(init=False, repr=True, eq=True)
class TipoEspecialidad:
    nombre: str
    nivel: str