from flask import Flask, render_template
from mixologymaster import app, db
from .models import User


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)