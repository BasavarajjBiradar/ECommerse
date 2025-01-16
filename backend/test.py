from flask import Flask, request, jsonify,send_file,render_template
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, admin, Userss, category, product,  supplier,userordersss,productt
from werkzeug.utils import secure_filename  # To handle file uploads securely


from flask_marshmallow import Marshmallow

pymysql.install_as_MySQLdb()
app=Flask(__name__)
CORS(app)


@app.route('/productts',methods=['POST'])   #products...........
def create_products():
    data=request.get_json()
    new_products=product(name=data['name'],category_id=data['category_id'],supplier_id=data['supplier_id'],price=data['price'],Description=data['Description'],image_url=data['image_url'])
    db.session.add(new_products)
    db.session.commit()
    return ({'message':'product is created'})


@app.route('/products',methods=['GET'])
def get_products():
    products=productt.query.all()
    return jsonify([{'id':product.id,'name':product.name,'category_id':product.category_id,"supplier_id":product.supplier_id,"price":product.price,"Description":product.Description,product.image_url:"image_url"} for product in products])


@app.route('/productts/<int:id>',methods=['PUT'])
def update_product(id):
    data=request.get_json()
    Product=productt.query.get_or_404(id)
    Product.name=data['name']
    Product.category_id=data['category_id']
    Product.supplier_id=data['supplier_id']
    Product.price=data['price']
    Product.Description=data['Description']
    Product.image_url=data['image_url']
    db.session.commit()
    return jsonify({'message':'product updated'})


@app.route('/productts/<int:id>',methods=['DELETE'])

def del_product(id):
    Product=productt.query.get_or_404(id)
    db.session.delete(Product)
    db.session.commit()
    return jsonify({'message':'product is deleted'})



@app.route('/productsjoin',methods=['GET'])
def get_pro_cat():
    products=db.session.query(productt,category).join(category).all()
    result=[]
    for j,k in products:
        result.append({

            "id":j.id,
            'name':j.name,
            'Description':j.Description,
            'category_id':j.category_id,
            'category_name':k.name
            
        })
    return jsonify(result)