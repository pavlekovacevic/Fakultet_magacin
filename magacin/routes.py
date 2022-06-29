from flask import  jsonify, request
from marshmallow import ValidationError
from magacin.models import  Category, Product
from magacin import db
from magacin.schemas import  CreateCategoryInputSchema, CreateProductInputSchema
from magacin import create_app as app

@app.route('/category', methods=['POST'])
def add_category():
    try:
        category_data = CreateCategoryInputSchema().load(request.get_json())
    except ValidationError as err:
        return err.messages, 400
        
    category=Category.query.filter_by(category=category_data['title']).first()
    
    if not category:
        new_category = Category(**category_data)
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message':'New category created'}), 201    
    
    return ({'message':"Category already exists"}), 400
@app.route('/magacin', methods=['POST'])
def create_product(product):
    try:
        product_data = CreateProductInputSchema().load(request.get_json())
    except ValidationError as err:
        return err.messages, 400

    new_product = Product(category=product.id, **product_data)
    
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'id': new_product.id}), 201

@app.route('/magacin', methods=['GET'])
def get_all_products(product):
    posts = Product.query.all()
    results = CreateProductInputSchema(many=True).dump(posts)
   
    return jsonify(results)

@app.route('/magacin/<id>', methods=['GET'])
def get_single_product_by_id(product, id):
    product = Product.query.filter_by(id=id).first()
    results = CreateProductInputSchema.dump(product)
   
    return jsonify(results)

@app.route('/magacin/<id>', methods=['PUT'])
def update_product(product, id):
    try:
        product_data = CreateProductInputSchema().load(request.get_json())
    except ValidationError as err:
        return err.messages, 400
    
    post = Product.query.filter_by(id=id).first()
    if not post:
        return {"message": "We dont have a product with matching id!"}, 403
   
    product.name = product_data['name']
    product.description = product_data['description']
    db.session.commit()
    updated_product = CreateProductInputSchema().dump(post)
    
    return jsonify(updated_product)

@app.route('/magacin/<id>', methods=['DELETE'])
def delete_product_by_id(product, id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return {"message":"We dont have a product with matching id!"}, 403
    
    db.session.delete(product)
    db.session.commit()

    return jsonify("Product deleted"), 200