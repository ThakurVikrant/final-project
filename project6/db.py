from app import db

class Accessory(db.Model):
	__tablename__ = 'Accessories'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	quantity_ordered = db.Column(db.Integer)
	quantity_remaining = db.Column(db.Integer)
	vendor_name = db.Column(db.String)
	purchase_price = db.Column
        


class user(db.Model):
    uid = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(20), nullable=False)


    
        
