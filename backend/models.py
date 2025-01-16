from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

db=SQLAlchemy()


class admin(db.Model):
    name=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(120), primary_key=True, nullable=False)
    password=db.Column(db.String(45), nullable=False)

    def _repr_(self):
        return f'<adm {self.name}>'
    
class Userss(db.Model):
    
    name=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(120), primary_key=True, nullable=False)
    password=db.Column(db.String(40), nullable=False)
    mobile=db.Column(db.String(10), nullable=False)
    address=db.Column(db.String(40), nullable=False)
    role=db.Column(db.String(40), nullable=True)


    def _repr_(self):
        return f'<user {self.name}>'
    
class category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return f'<category {self.name}>' 
    
class supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    phone=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f'<supplier {self.name}>'
    







    
class product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    supplier_id=db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    Description = db.Column(db.String(200), nullable=False)



    def __repr__(self):
        return f'<product{self.name}>'
    
class productt(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    supplier_id=db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    Description = db.Column(db.String(200), nullable=False)
    image_url =db.Column(db.String(500))

    def __repr__(self):
        return f'<product{self.name}>'





class userordersss(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.String(90), db.ForeignKey('userss.email'), nullable=False)

    product_id=db.Column(db.Integer, db.ForeignKey('productt.id'), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    price=db.Column(db.Integer, nullable=False)

    

    

    def __repr__(self):
        return f"<Order {self.id}>"

 

