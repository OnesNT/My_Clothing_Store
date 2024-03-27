from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clothing_store.db'
app.config['SECRET_KEY'] = 'thisisasecretekey'
db = SQLAlchemy(app)

# # Define models
# class Customer(db.Model):
#     customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     customer_nm = db.Column(db.String(40), nullable=False)
#     customer_surname = db.Column(db.String(40), nullable=False)
#     customer_patronymic = db.Column(db.String(40))
#     birth_dt = db.Column(db.Date)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     overall_transactions_amt = db.Column(db.BigInteger)
#     advertising_subscribe_flg = db.Column(db.Boolean)

# class Order(db.Model):
#     order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     employee_id = db.Column(db.BigInteger, nullable=False)
#     store_id = db.Column(db.BigInteger, nullable=False)
#     customer_id = db.Column(db.BigInteger, nullable=False)
#     delivery_dttm = db.Column(db.DateTime)
#     purchase_dtm = db.Column(db.DateTime)

# class ClothesInOrder(db.Model):
#     order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), primary_key=True)
#     clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.clothes_id'), primary_key=True)
#     item_count = db.Column(db.Integer, nullable=False)

# class Employee(db.Model):
#     employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     valid_from_dttm = db.Column(db.DateTime, nullable=False)
#     delivery_point_id = db.Column(db.BigInteger, nullable=False)
#     employee_nm = db.Column(db.String(40), nullable=False)
#     employee_surname = db.Column(db.String(40), nullable=False)
#     employee_patronymic = db.Column(db.String(40))
#     valid_to_dttm = db.Column(db.DateTime, nullable=False)
#     birth_dt = db.Column(db.Date, nullable=False)
#     email = db.Column(db.String(50), nullable=False)
#     salary_amt = db.Column(db.Integer)
#     position_nm = db.Column(db.String(100), nullable=False)

# class DeliveryPoint(db.Model):
#     delivery_point_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     store_id = db.Column(db.BigInteger, nullable=False)
#     address = db.Column(db.String(40))
#     city = db.Column(db.String(40))
#     phone_no = db.Column(db.Integer)

# class Store(db.Model):
#     store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     store_nm = db.Column(db.String(60), nullable=False)
#     create_dt = db.Column(db.Date)
#     head_office_address = db.Column(db.String(40))
#     head_office_country_nm = db.Column(db.String(40))

# class ClothesInStore(db.Model):
#     store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), primary_key=True)
#     clothes_id = db.Column(db.Integer, db.ForeignKey('clothes.clothes_id'), primary_key=True)
#     item_count = db.Column(db.Integer, nullable=False)

# class Clothes(db.Model):
#     clothes_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     brand_id = db.Column(db.BigInteger, nullable=False)
#     clothes_nm = db.Column(db.String(100), nullable=False)
#     category_nm = db.Column(db.String(40), nullable=False)
#     color_nm = db.Column(db.String(40))
#     price_amt = db.Column(db.Integer, nullable=False)
#     sex_nm = db.Column(db.String(50))

# class Brand(db.Model):
#     brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     brand_nm = db.Column(db.String(40), nullable=False)
#     head_designer_nm = db.Column(db.String(40), nullable=False)
#     head_designer_surname = db.Column(db.String(40), nullable=False)
#     head_designer_patronymic = db.Column(db.String(40))
#     foundation_dt = db.Column(db.Date)

# # Create tables
# with app.app_context():
#     db.create_all()

# # Optionally, populate data
# # Example:
# customer1 = Customer(customer_nm='John', customer_surname='Doe', email='john@example.com')
# db.session.add(customer1)
# db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
