from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index1.html')

@app.route('/register', methods=['POST'])

def register():
    name = request.form.get('name')
    dorm=request.form.get('dorm')
    if not name or not dorm:
        return 'Failure'
    return render_template('success.html')