from mixologymaster import db
from flask_login import UserMixin, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


class User(db.Model, UserMixin):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return str(self.id)


class Cocktail(db.Model):
    # schema for the Cocktail model
    cocktail_id = db.Column(db.Integer, primary_key=True)
    cocktail_name = db.Column(db.String, nullable=False, unique=True)
    cocktail_category = db.Column(db.String, nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="SET NULL"),
        nullable=True)
    ingredients = db.Column(db.String, nullable=False)
    prep_instructions = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Cocktail {self.cocktail_name}>'


class RegisterForm(FlaskForm):
    # username field and length validation
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Username"}
    )

    # password field and length validation
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=8, max=20)
        ],
        render_kw={"placeholder": "Password"}
    )

    # submit field
    submit = SubmitField('Register')


def validate_username(self, username):
    # validation to check if username already exists
    existing_user_username = User.query.filter_by(
        username=username.data).first()
    # raise error if username is already in use
    if existing_user_username:
        raise ValidationError(
            'Sorry, that username is already in use.')


class LoginForm(FlaskForm):
    # Authenticate user through flask form
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=20)
        ],
        render_kw={"placeholder": "Username"}
    )

    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=8, max=20)
        ],
        render_kw={"placeholder": "Password"}
    )

    submit = SubmitField('Login')
