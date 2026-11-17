from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Length,EqualTo,DataRequired,Email,ValidationError



class RegisterForm(FlaskForm):
    username= StringField(label='UserName:',validators=[Length(min=2,max=25),DataRequired()])
    email_address= StringField(label='Email:',validators=[Email(),DataRequired()])
    password1= PasswordField(label='Password1:',validators=[Length(min=6),DataRequired()])
    password2= PasswordField(label='Confirm Password:',validators=[EqualTo("password1"),DataRequired()])
    submit= SubmitField(label='Submit')
    
    # def validate_username(self,username_to_check):
    #     from data import User
    #     user = User.query.filter_by(username=username_to_check.data).first()
    #     if user:
    #         raise ValidationError("Username Already Exists! Please try a different username")
    # def validate_email_address(self,email_address_to_check):
    #     from data import User    
    #     email = User.query.filter_by(email_address=email_address_to_check.data).first()
    #     if email:
    #       raise ValidationError("Email Already Exists! Please try a different email address")   

class LoginForm(FlaskForm):
    username = StringField(label='User Name:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')