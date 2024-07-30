from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pymongo import MongoClient
from config import Config

db = SQLAlchemy()
migrate = Migrate()
mongo_client = MongoClient(Config.MONGO_URI)
mongo_db = mongo_client.get_database()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
