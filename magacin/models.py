from magacin import db 
from datetime import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.String(200), nullable=False)
    

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name=db.column(db.Integer, db.ForeignKey(Category.title), nullable=False)
    name = db.Column(db.String(100), unique=True)
    description=db.Column(db.String(100))
    post_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)