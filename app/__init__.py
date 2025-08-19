import logging
from flask import Flask
import os
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_hashids import Hashids

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
hashids = Hashids()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    # https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    db.init_app(app)
    migrate.init_app(app, db)
    hashids.init_app(app)
    ma.init_app(app)

    from app.resources import home, universidad_bp, area_bp, tipodocumento_bp, tipodedicacion_bp, categoriacargo_bp, grupo_bp, grado_bp, departamento_bp, certificado_bp, tipo_especialidad_bp, plan_bp,cargo_bp
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

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
