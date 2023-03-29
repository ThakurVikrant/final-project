class Accessory():
    def __init__(self,id,name,quantity_ordered,quantity_remaining,vendor_name,purchase_price ):
        self.id=id
        self.name=name
        self.quantity_ordered=quantity_ordered
        self.quantity_remaining=quantity_remaining
        self.vendor_name=vendor_name
        self.purchase_price=purchase_price

        def __repr__(self):
          return f"id:{self.id},name:{self.name},quantity_ordered:{self.quantity_ordered},quantity_remaininge:{self.quantity_remaining},vendor_name{self.vendor_name},purchase_price{self.purchase_price}"
    
class user():

    def __init__(self,username,email,password,phone,):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone

        def __repr__(self):
           return f"username:{self.username},email:{self.email},password:{self.password},phone:{self.phone}"



