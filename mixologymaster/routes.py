from flask import Flask, render_template, redirect, url_for,request
from mixologymaster import app, db
from .models import User
from .models import RegisterForm
from .models import LoginForm
from . import bcrypt

@app.route("/")
def index():
    # Render index(home) page as landing page
    return render_template("index.html")

@app.route("/specs")
def specs():
    #Render specs(recipes) page
    return render_template("specs.html")

@app.route("/contact")
def contact():
    #Render contact page
     return render_template("contact.html")


@app.route("/confirmation")
def confirmation():
    #Render thank you page
    return render_template("confirmation.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method ==  'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter(User.username == username).first()

        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return 'Failed'


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'GET': 
        return render_template("register.html", form=form)
    elif request.method ==  'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password)

        user = User(username=username, password=hashed_password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))