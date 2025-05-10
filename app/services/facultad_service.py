from app.models import Facultad
from app.repositories import FacultadRepositorio


class FacultadService:
    @staticmethod
    def crear_facultad(facultad: "Facultad"):
        """
        Crea una nueva facultad en la base de datos.
        :param facultad: Objeto Facultad a crear.
        :return: El objeto Facultad creado.
        """
        FacultadRepositorio.crear(Facultad)

