from flask import Flask, render_template, redirect, url_for,request,flash
from mixologymaster import app, db
from werkzeug.utils import secure_filename
from .models import User
from .models import Cocktail
from .models import RegisterForm
from .models import LoginForm
from . import bcrypt
from flask_login import LoginManager, current_user, login_user, login_required, logout_user


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Ensure redirection to login page if not authenticated

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def index():
    # Render index(home) page as landing page
    return render_template("index.html")


@app.route("/specs")
def specs():
    #Render specs(recipes) page
    cocktails = list(Cocktail.query.order_by(Cocktail.cocktail_name).all())
    return render_template("specs.html", cocktails=cocktails)

@app.route("/add_cocktail", methods=['GET', 'POST'])
def add_cocktail():
    if request.method == 'POST':
        cocktail_name = request.form['cocktail_name']
        cocktail_category = request.form['cocktail_category']
        ingredients = request.form['ingredients']
        prep_instructions = request.form['prep_instructions']
        user_id = current_user.id
        description = request.form.get('description') 

        # Ensure all required fields are filled
        if not all([cocktail_name, cocktail_category, ingredients, prep_instructions]):
            return "All fields are required", 400

        new_cocktail = Cocktail(
            cocktail_name=cocktail_name,
            cocktail_category=cocktail_category,
            ingredients=ingredients,
            prep_instructions=prep_instructions,
            user_id=user_id,
            description=description
        )
        db.session.add(new_cocktail)
        db.session.commit()
        return redirect(url_for('specs'))
    
    return render_template("add_cocktail.html")

@app.route("/edit_cocktail/<int:cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):
    cocktail = Cocktail.query.get_or_404(cocktail_id)
    
    if request.method == "POST":
        cocktail.cocktail_name = request.form.get("cocktail_name")
        cocktail.category = request.form.get("category")
        cocktail.description = request.form.get("description")
        cocktail.ingredients = request.form.get("ingredients")
        cocktail.prep_instructions = request.form.get("prep_instructions")

        db.session.commit()
        return redirect(url_for("specs"))
    
    return render_template("edit_cocktail.html", cocktail=cocktail)


@app.route("/delete_cocktail/<int:cocktail_id>")
def delete_cocktail(cocktail_id):
    cocktail = Cocktail.query.get_or_404(cocktail_id)
    db.session.delete(cocktail)
    db.session.commit()
    return redirect(url_for("specs"))


@app.route("/contact")
def contact():
    #Render contact page
     return render_template("contact.html")


@app.route("/confirmation")
def confirmation():
    #Render thank you page
    return render_template("confirmation.html")


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'GET': 
        return render_template("register.html", form=form)
    elif request.method ==  'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf8')

        user = User(username=username, password=hashed_password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter(User.username == username).first()

        if user is None:
            flash('User does not exist.', 'danger')
            return redirect(url_for('login'))

        # Debugging output
        print(f"User found: {user.username}")

        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            print(f"Login successful for user: {user.username}")
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')
            print(f"Login failed for user: {username}")

            return redirect(url_for('index'))

    return 'Failed'  # Fallback response


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))