from flask import Flask,render_template,request
import csv

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register",methods=["POST"])
def register():
    name = request.form.get('name')
    dorm = request.form.get('dorm')
    if not name or not dorm:
        return render_template('failure.html')
    file=open('registered.csv','a')
    writer=csv.writer(file)
    writer.writerow((name,dorm))
    file.close()
    return render_template("success.html")

@app.route('/registered')
def registered():
    file = open("registered.csv","r")
    reader=csv.reader(file)
    students=list(reader)
    file.close()
    return render_template("registered.html",students=students)