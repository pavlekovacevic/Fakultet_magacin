import os

class MagacinConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "postgresql://postgres:postgres@localhost:5432")
    
    SECRET_KEY = os.environ.get("SECRET-KEY", "very-very-very-secret")