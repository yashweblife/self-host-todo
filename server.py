from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from helpers import create_user, validate_login, validate_signup

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = '_sqlite:///site.db_'

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        name= request.form['username']
        password = request.form['password']
        if(validate_login(name, password)):
            return redirect(url_for('lists'))
    return render_template('login.html')

@app.route('/signup', methods=['POST', "GET"])
def signup():
    if(request.method == 'POST'):
        name= request.form['username']
        password = request.form['password']
        if(validate_signup(name, password)):
            create_user(name, password)
            return redirect(url_for('lists'))
    return render_template('signup.html')

@app.route('/sad_password')
def sad_password():
    return render_template('passwordRecover.html')

@app.route('/lists')
def lists():
    return render_template('lists.html') 

@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)