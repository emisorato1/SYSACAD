from dataclasses import dataclass
from app.models.categoriacargo import CategoriaCargo
from app.models.tipodedicacion import TipoDedicacion

@dataclass(init=False, repr=True, eq=True)
class Cargo():
    nombre: str
    puntos: int
    categoria_cargo: CategoriaCargo
    tipo_dedicacion: TipoDedicacion