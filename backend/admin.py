from flask import Flask, request, jsonify,send_file,render_template
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, admin, Userss, category, product,  supplier,userordersss,productt
from werkzeug.utils import secure_filename  # To handle file uploads securely
from sqlalchemy import func



from flask_marshmallow import Marshmallow

pymysql.install_as_MySQLdb()
app=Flask(__name__)
CORS(app)
app
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Basavaraj$17@127.0.0.1/database2'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db.init_app(app)

    

@app.route('/login', methods=['POST'])
def memberLogin():
    data=request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message":"missing email or password"})
    adm = admin.query.filter_by(email=email).first()
    if not adm:
        return jsonify({'message': 'Invalid email or password'}), 401
    if adm.password != password:
        return jsonify({'message': 'Invalid email or password'}), 401
    return jsonify({'name':adm.name, 'email':adm.email})



with app.app_context():
    db.create_all()

# READ ALL USERS

@app.route('/signup', methods=['GET'])
def get_users(): 
    mem = Userss.query.all()
    return jsonify([{'name':user.name, 'email':user.email, 'mobile':user.mobile,'address':user.address}for user in mem])

# Signup

@app.route('/signup', methods=['POST'])
def userSignup():
    data = request.get_json()
    new=Userss(name=data['name'], email=data['email'], password=data['password'], mobile=data['mobile'],address=data['address'])
    db.session.add(new)
    db.session.commit()
    return jsonify({"message":"Signed up successfully"})

#login
@app.route('/userlogin', methods=['POST'])
def userlogin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "missing email or password"}), 400

    # Query the user by email
    user = Userss.query.filter_by(email=email).first()

    # Check if user exists
    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Check if password matches
    if user.password != password:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Create the response data
    response_data = {
        'name': user.name,
        'email': user.email,
        'mobile': user.mobile,
        'address': user.address,
        'role': user.role  # Include the role in the response
    }
    print(response_data)

    # If the user is an admin, you can also customize the response
    if user.role == 'admin':
        response_data['role'] = 'admin'
        # You can add additional admin-specific information here if needed

    return jsonify(response_data)

@app.route('/categories',methods=['POST']) #categories-----------------------------------

def create_category():
    data=request.get_json()        
    new_category=category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({"message":"category is created"})


@app.route('/categories',methods=['GET'])    #categories-----------------------------------

def get_categories():
    categories=category.query.all()
    return jsonify([{'id':category.id,'name':category.name} for category in categories])


@app.route('/categories/<int:id>',methods=['PUT'])   #categories-----------------------------------

def update_category(id):
    data=request.get_json()
    Category=category.query.get_or_404(id)
    Category.name=data['name']
    db.session.commit()
    return jsonify({'message':'category is updated'})

@app.route('/categories/<int:id>',methods=['DELETE'])

def del_category(id):
    Category=category.query.get_or_404(id)
    db.session.delete(Category)
    db.session.commit()
    return jsonify({'message':'catory is deleted'})

@app.route('/supplier',methods=['POST'])           #supplier.................................

def create_supplier():
    data=request.get_json()
    supply=supplier(name=data['name'],location=data['location'],phone=data['phone'])
    db.session.add(supply)
    db.session.commit()
    return jsonify({"message":"supplier is created"})


@app.route('/supplier',methods=['GET'])      #supplier.................................

def get_supplier():
    suppliers=supplier.query.all()
    return jsonify([{'id':supplier.id,'name':supplier.name,'location':supplier.location,'phone':supplier.phone} for supplier in suppliers])


@app.route('/supplier/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    supply=supplier .query.get_or_404(id)
    db.session.delete(supply)                             #supplier delete...........................
    db.session.commit()
    return jsonify({"message":"supplier is deleted"})

@app.route("/supplier/<int:id>", methods=['PUT'])
def update_supply(id):
    data=request.get_json()
    supply=supplier.query.get_or_404(id)           #supplier data update..............................
    supply.name=data['name']
    supply.location=data['location']
    supply.phone=data['phone']
    db.session.commit()
    return jsonify({"message":"supplier data updated"})

@app.route('/products',methods=['GET'])
def get_products():
    products=productt.query.all()
    return jsonify([{'id':product.id,'name':product.name,'category_id':product.category_id,"supplier_id":product.supplier_id,"price":product.price,"Description":product.Description,"image_url":product.image_url} for product in products])


@app.route('/products',methods=['POST'])   #products...........
def create_products():
    data=request.get_json()
    new_products=productt(name=data['name'],category_id=data['category_id'],supplier_id=data['supplier_id'],price=data['price'],Description=data['Description'],image_url=data['image_url'])
    db.session.add(new_products)
    db.session.commit()
    return ({'message':'product is created'})
@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = productt.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    product_data = {
        'id': product.id,
        'name': product.name,
        'category_id': product.category_id,
        'supplier_id': product.supplier_id,
        'price': product.price,
        'description': product.description,
        'image_url': product.image_url
    }
    return jsonify(product_data), # prodcut by id

@app.route('/products/<int:id>',methods=['PUT'])
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


@app.route('/products/<int:id>',methods=['DELETE'])

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












@app.route('/shopping',methods=['GET'])
def getProducts():
    products=db.session.query(product,category,supplier).join(category).join(supplier).all()
    result=[]
    for i,j,k in products:
        result.append({
            "id":i.id,
            'name':i.name,
            'category_id':i.category_id,
            'category_name':j.name,
            'Description':i.Description,
            'price':i.price,
            'supplier_id':i.supplier_id,
            'supplier_name':k.name,
            'supplier_address':k.location,
            'supplier_phone':k.phone
        })
    return jsonify(result)

#another table======+++++
@app.route('/shoppings', methods=['GET'])
def getProductts():
    products = db.session.query(productt, category, supplier).join(category).join(supplier).all()
    
    result = []
    for i, j, k in products:
        result.append({
            "id": i.id,
            'name': i.name,
            'category_id': i.category_id,
            'category_name': j.name,
            'Description': i.Description,
            'price': i.price,
            'supplier_id': i.supplier_id,
            'supplier_name': k.name,
            'supplier_address': k.location,
            'supplier_phone': k.phone,
            'image_url': i.image_url  # Include the image URL from the product table
        })
    
    return jsonify(result)



@app.route('/orders', methods=['GET'])
def get_orders():
    order=userordersss.query.all()
    return jsonify([{'id':userorder.id,'user_id':userorder.user_id,'product_id':userorder.product_id,'quantity':userorder.quantity,'price':userorder.price}for userorder in order])


@app.route('/myorders/<string:user_id>', methods=['GET'])
def myorders(user_id):
    items = (
        db.session.query(userordersss, productt)
        .filter(userordersss.user_id == user_id)
        .join(productt, userordersss.product_id == productt.id) 
        .all()
    )

    result = []
    for order, prod in items:
        result.append({
            "product_id": order.product_id,
            "Name": prod.name,
            "description": prod.Description,  
            "Quantity": order.quantity,
            "price": prod.price,
            "total": order.price  
        })
    return jsonify(result)

    #return jsonify([{'id':userorder.id,'use_id':userorder.user_id,'product_id':userorder.product_id,'quantity':userorder.quantity,'price':userorder.price}for userorder in order])
@app.route('/orders', methods=['POST'])

def create_order():
    data = request.get_json()

    try:
        if not data.get('user_id') or not data.get('orderedItems'):
            return jsonify({'error': 'Missing required fields'}), 400

        for item in data['orderedItems']:
            db.session.merge(userordersss(  

                user_id=data['user_id'],
                product_id=item['product_id'],
                quantity=item['quantity'],
                price=item['price']
            ))

        db.session.commit()


        return jsonify({'message': 'Order created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/sales-data', methods=['GET'])
def get_sales_data():
    try:
        # Aggregate total sales data
        sales_data = db.session.query(
            productt.name.label("product_name"),
            func.sum(userordersss.quantity).label("total_quantity"),
            func.sum(userordersss.price).label("total_revenue")
        ).join(productt, userordersss.product_id == productt.id).group_by(productt.name).all()

        # Format the response
        result = [
            {
                "product_name": row.product_name,
                "total_quantity": row.total_quantity,
                "total_revenue": row.total_revenue
            }
            for row in sales_data
        ]

        return jsonify({"success": True, "data": result}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


if (__name__)=='__main__':
    app.run(debug=True)