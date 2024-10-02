from flask import Flask
from .routes import main
# from .models import db  # Uncomment if using a database

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_pyfile('../config/config.py')

    # Register blueprints
    app.register_blueprint(main)

    return app
