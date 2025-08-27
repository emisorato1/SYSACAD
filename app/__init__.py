import logging
from flask import Flask
import os
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_hashids import Hashids
from flask_caching import Cache
from app.config.cache_config import cache_config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
hashids = Hashids()
cache = Cache()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    # https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    # use custom template folder name 'template' (project uses singular)
    app = Flask(__name__, template_folder='template')
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    app.config.from_mapping(cache_config)  # Agrega la config de caché
    db.init_app(app)
    migrate.init_app(app, db)
    hashids.init_app(app)
    ma.init_app(app)
    cache.init_app(app)

    from app.resources import (home, universidad_bp, area_bp, tipodocumento_bp, tipodedicacion_bp, categoriacargo_bp, grupo_bp, grado_bp,
                                departamento_bp, certificado_bp, tipo_especialidad_bp, plan_bp,cargo_bp, alumno_bp, autoridad_bp, facultad_bp,especialidad_bp, materia_bp, orientacion_bp)
    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(universidad_bp, url_prefix='/api/v1')
    app.register_blueprint(area_bp, url_prefix='/api/v1')
    app.register_blueprint(tipodocumento_bp, url_prefix='/api/v1')
    app.register_blueprint(tipodedicacion_bp, url_prefix='/api/v1')
    app.register_blueprint(categoriacargo_bp, url_prefix='/api/v1')
    app.register_blueprint(grupo_bp, url_prefix='/api/v1')
    app.register_blueprint(grado_bp, url_prefix='/api/v1')
    app.register_blueprint(departamento_bp, url_prefix='/api/v1')
    app.register_blueprint(certificado_bp, url_prefix='/api/v1')
    app.register_blueprint(tipo_especialidad_bp, url_prefix='/api/v1')   
    app.register_blueprint(plan_bp, url_prefix='/api/v1')
    app.register_blueprint(cargo_bp, url_prefix='/api/v1') 
    app.register_blueprint(alumno_bp, url_prefix='/api/v1')
    app.register_blueprint(autoridad_bp, url_prefix='/api/v1')
    app.register_blueprint(facultad_bp, url_prefix='/api/v1')
    app.register_blueprint(especialidad_bp, url_prefix='/api/v1')
    app.register_blueprint(materia_bp, url_prefix='/api/v1')
    app.register_blueprint(orientacion_bp, url_prefix='/api/v1')  

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
