from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email."), Email("Please enter a valid email")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password."), Length(min=6,message="passowrds should be at least 6 characters")])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter your email"),Email("Please enter your email")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password"),Length(min=6,message="Please enter your password")])
    submit = SubmitField("Sign in")

class AddressForm(FlaskForm):
    address = StringField("Address", validators=[DataRequired("Please enter an address")])
    submit = SubmitField("Search")