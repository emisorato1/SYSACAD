import logging
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config import config

db = SQLAlchemy()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    #https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    db.init_app(app)

    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
