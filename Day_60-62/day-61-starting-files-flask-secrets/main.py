from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, InputRequired
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    # name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password")
    # confirm = PasswordField("Confirm Password")
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Log In")



app = Flask(__name__)
app.secret_key = "my secret key"
bootstrap = Bootstrap5(app)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # print(login_form.email.data)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "123456789":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    # print(form.password.data)
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
