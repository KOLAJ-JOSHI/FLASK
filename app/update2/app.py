import os
import smtplib
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=['POST'])
def register():
    name=request.form.get("name")
    email=request.form.get('email')
    dorm=request.form.get('dorm')

    if not name or not email or not dorm:
        return render_template('failure.html')
    
    message = "You are registered!"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("joshikolaj1997@gmail.com",os.environ.get('GPASS'))
    server.sendmail("joshikolaj1997@gmail.com",email,message)
    return render_template("success.html")