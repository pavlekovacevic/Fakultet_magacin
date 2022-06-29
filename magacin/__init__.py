from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from magacin.config import MagacinConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(MagacinConfig)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from magacin.routes import users_blueprint, blog_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(blog_blueprint)
    
    return app