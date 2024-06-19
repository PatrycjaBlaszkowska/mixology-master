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
    # Handles categories filter
    categories = set([cocktail.cocktail_category for cocktail in cocktails])
    return render_template("specs.html", cocktails=cocktails, categories=categories)

@app.route("/add_cocktail", methods=['GET', 'POST'])
@login_required
def add_cocktail():
    # Push user input into database
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

        # Combine all key-value pairs into one object instance in order to add it to database
        new_cocktail = Cocktail(
            cocktail_name=cocktail_name,
            cocktail_category=cocktail_category,
            ingredients=ingredients,
            prep_instructions=prep_instructions,
            user_id=user_id,
            description=description
        )
        # Adds and commits cocktail to the database
        db.session.add(new_cocktail)
        db.session.commit()
        flash('Cocktail added successfully', 'success')
        return redirect(url_for('specs'))
    
    return render_template("add_cocktail.html")

@app.route("/edit_cocktail/<int:cocktail_id>", methods=["GET", "POST"])
def edit_cocktail(cocktail_id):
    cocktail = Cocktail.query.get_or_404(cocktail_id)
    
    # Gets new user input and alter existing columns in the database
    if request.method == "POST":
        cocktail.cocktail_name = request.form.get("cocktail_name")
        cocktail.category = request.form.get("category")
        cocktail.description = request.form.get("description")
        cocktail.ingredients = request.form.get("ingredients")
        cocktail.prep_instructions = request.form.get("prep_instructions")

        # Commit changes to the database
        db.session.commit()
        return redirect(url_for("specs"))
    
    return render_template("edit_cocktail.html", cocktail=cocktail)


@app.route("/delete_cocktail/<int:cocktail_id>")
def delete_cocktail(cocktail_id):
    # Deletes cocktail out of database
    cocktail = Cocktail.query.get_or_404(cocktail_id)
    db.session.delete(cocktail)
    db.session.commit()
    flash('Cocktail deleted successfully', 'success')
    return redirect(url_for("specs"))


@app.route('/cocktail/<int:cocktail_id>')
def view_cocktail(cocktail_id):
    # Renders a separate cocktail dedicated page.
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

        # Render message for a user and redirect to the login page
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

        # Render a warning if account doesn't exist
        if user is None:
            flash('User does not exist.', 'danger')
            return redirect(url_for('login'))

        # Console output to help test login process during development
        print(f"User found: {user.username}")

        # Generate output in the console necessary for debugging or a message for a user if login details are invalid
        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            print(f"Login successful for user: {user.username}")
            
            # Redirect user to the dashboard after sucessfull login
            return redirect(url_for('dashboard', username=user.username))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
            print(f"Login failed for user: {username}")

            # Return user back to login page if authentication fails
            return redirect(url_for('login'))

    return 'Failed'  # Fallback response


@app.route("/dashboard/<username>")
@login_required
def dashboard(username):
    if current_user.is_admin:
        # Admin 
        cocktails = Cocktail.query.all()
    else:
        # Regular user 
        cocktails = Cocktail.query.filter_by(user_id=current_user.id).all()
    
    # Render user dashboard
    return render_template("dashboard.html", username=username, cocktails=cocktails)

@app.route('/logout')
def logout():
    # Log user out
    logout_user()
    return redirect(url_for('index'))


@app.route('/change_username/<username>', methods=["GET", "POST"])
def change_username(username):
    # Fetch user data from database
    user = User.query.filter_by(username=username).first_or_404()
    
    # Takes user input from the form
    if request.method == "POST":
        new_username = request.form.get("username")

        # check if username is already in use
        if new_username:
            existing_user = User.query.filter_by(username=new_username).first()
            if existing_user:
                # Generate a message to let user know username can't be changed
                flash('Username already taken. Please choose a different one.', 'danger')
                return redirect(url_for('change_username', username=username))
            user.username = new_username
            db.session.commit()
            #  Generate a message to let user know username has been changed
            flash('Username updated successfully', 'success')
            return redirect(url_for('dashboard', username=user.username))
    
    return render_template("edit_username.html", username=username)


@app.route('/delete_account/<username>')
def delete_account(username):
    # Allow user to delete their account
    user = User.query.filter_by(username=username).first_or_404()
    db.session.delete(user)
    db.session.commit()
    flash('Account deleted successfully', 'success')
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error), 500