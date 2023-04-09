from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
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