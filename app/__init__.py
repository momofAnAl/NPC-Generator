import os
from flask import Flask
from .routes.character_routes import bp
from .db import db, migrate
from .models import character, greeting
from dotenv import load_dotenv

load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        db_to_use = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        db_to_use = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = db_to_use

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(bp)

    return app