from app import db

class FacultadRepositorio:
    @staticmethod
    def crear(facultad: db.Model):
        """
        Crea una nueva facultad en la base de datos.
        :param facultad: Objeto Facultad a crear.
        :return: El objeto Facultad creado.
        """
        # Aquí iría la lógica para guardar la facultad en la base de datos
        
        db.session.add(facultad)
        db.session.commit()
        