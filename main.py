from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Email,Length

app = Flask(__name__)
app.secret_key = "some secret string"
Bootstrap(app)

class Myform(FlaskForm):
    email = StringField(label="Email: ", validators=[DataRequired(),Email()])
    password = PasswordField(label="Password: ", validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="Login")

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login():
    form = Myform()
    if form.validate_on_submit():
        if form.email.data=="admin@email.com" and form.password.data=="12345678":
            return render_template("success.html")
        else:
            return render_template('denied.html')
    return render_template("login.html",form=form)


if __name__ == '__main__':
    app.run(debug=True)