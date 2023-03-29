#Flask Application

from model import user,Accessory
from flask import Flask,render_template,request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import request, flash
from flask import redirect
import os

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir,"manager.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"]="randomString"

db = SQLAlchemy(app)

@app.route("/register" , methods = ["GET", "POST"])
def register():
    if request.method=="POST":

        if not request.form["email"] or not request.form["username"] or not request.form["phone"] or not request.form["password"]:
            print("Please enter correct details")
            
            return redirect("/register")

        else:
            print(request.form["username"])
            print(request.form["email"])
            print(request.form["password"])
            print(request.form["phone"])
            result=0
            user = user(request.form["username"],request.form["email"],request.form["password"],request.form["phone"])
            db.session.add(user)
            db.session.commit()
            return redirect("/")

    return render_template("register.html")

check_email=""
@app.route("/login" , methods=["GET", "POST"])
def login():
    print("check")
    global check_email
    if request.method=="POST":
        print(request.form["email"])
        print(request.form["password"])
        if not request.form["email"] or not request.form["password"]:
            print("Please enter correct details")
            # flash('Please enter correct details')

        else:

            email = request.form["email"]
            user = user.query.filter_by(email=email).first()
            print(user.email)
            print(user.password)
            if(user.password==request.form["password"]):
                print("Login Successfull")
                check_email = user.email
                return redirect("/quiz")
            
    
    return render_template("login/login.html")

@app.route("/manager",methods=["GET","POST"])
def home():
    if request.method=="POST":
        # print(request.form)
        if not request.form["id"] or not request.form["name"] or not request.form["quantity_ordered"] or not request.form["quantity_remaining "] or not request.form["vendor_name"] or not request.form["purchase_price"]:
    
            print("Please enter all the fields")
            return redirect("/manager")

        else:
            rows = db.session.query(user).count() #no of rows in database
            mcq = Accessory(request.form["id"],request.form["name"],request.form["quantity_ordered"],request.form["quantity_remaining"],request.form["vendor_name"],request.form["purchase_price"])
            db.session.add(Accessory)
            db.session.commit()

            
            print("Accessory was added successfully") 
            
    userList = user.query.all()   
    AccessoryList =Accessory.query.all()
    print(len(userList))
    print(len(Accessory))
    return render_template("manager.html",AccessoryList= AccessoryList,userList=userList)




@app.route("/update",methods=["POST"])
def update():
    
    newid = request.form.get("new_id")
    newname = request.form.get("new_name")
    newquantity_ordered = request.form.get("new_quantity_ordered")
    newquantity_remaining = request.form.get("new_quantity_remaining")
    newvendor_name = request.form.get("new_vendor_name")
    newpurchase_price = request.form.get("new_purchase_price")

    oldQuestion = request.form.get("old_question")
    Accessory = Accessory.query.filter_by(Accessory=Accessory).first()
    if request.form["new_id"]:
        Accessory.id=newid

    if request.form["new_name"]:
        Accessory.name=newname

    if request.form["new_quantity_ordered"]:
        Accessory.quantity_ordered=newquantity_ordered

    if request.form["new_quantity_remaining"]:
        Accessory.quantity_remaining=newquantity_remaining

    if request.form["new_vendor_name"]:
        Accessory.vendor_name=newvendor_name

    if request.form["new_purchase_price"]:
        Accessory.purchase_price=newpurchase_price

    db.session.commit()
    return redirect("/manager")


@app.route("/delete",methods=["POST"])
def delete():
    Accessory = request.form.get("del_Accesory")
    mcq = Accessory.query.filter_by(Accessory=Accessory).first()
    db.session.delete(Accessory)
    db.session.commit()
    return redirect("/manager")
