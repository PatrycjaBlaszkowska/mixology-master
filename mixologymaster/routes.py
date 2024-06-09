from flask import Flask, render_template, redirect, url_for, request, flash
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
@login_required
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


@app.route('/cocktail/<int:cocktail_id>')
def view_cocktail(cocktail_id):
    cocktail = Cocktail.query.get_or_404(cocktail_id)
    ingredients = cocktail.ingredients.split(',')
    return render_template('view_cocktail.html', cocktail=cocktail, ingredients=ingredients)

@app.route("/contact")
def contact():
    #Render contact page
     return render_template("contact.html")


@app.route("/confirmation")
def confirmation():
    #Render thank you page
    return render_template("confirmation.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Takes user data and handle register/ validation process

    form = RegisterForm()

    if request.method == 'GET': 
        return render_template("register.html", form=form)
    elif request.method ==  'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf8')

        user = User(username=username, password=hashed_password)

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already taken. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Takes user data and handle login verification process
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
            return redirect(url_for('dashboard', username=user.username))
        else:
            flash('Invalid username or password.', 'danger')
            print(f"Login failed for user: {username}")

            return redirect(url_for('index'))

    return 'Failed'  # Fallback response


@app.route("/dashboard/<username>")
@login_required
def dashboard(username):
    # Get cocktails for the current user
    cocktails = Cocktail.query.filter_by(user_id=current_user.id).all()
    # Render user dashboard
    return render_template("dashboard.html", username=username, cocktails=cocktails)


@app.route('/logout')
def logout():
    # Log user out
    logout_user()
    return redirect(url_for('index'))


@app.route("/change_username/<username>", methods=["GET", "POST"])
def change_username(username):
    user = User.query.filter_by(username=username).first_or_404()
    
    if request.method == "POST":
        new_username = request.form.get("username")
        if new_username:
            user.username = new_username
            db.session.commit()
            return redirect(url_for('dashboard', username=user.username))
    
    return render_template("edit_username.html", username=username)

@app.route('/delete_account/<username>')
def delete_account(username):
    user = User.query.filter_by(username=username).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))