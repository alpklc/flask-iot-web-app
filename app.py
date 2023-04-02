from flask import Flask
from flask import render_template, redirect, url_for, request, session, flash
from dotenv import load_dotenv
import os
from datetime import timedelta

app = Flask(__name__)

load_dotenv()

app.secret_key = os.environ["SESSION_SECRET_KEY"]
app.permanent_session_lifetime = timedelta(minutes=15)


@app.route("/", methods=['GET'])
@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


@app.route("/", methods=['POST'])
@app.route("/dashboard", methods=['POST'])
def dashboard_post():
    text = request.form['text']
    language = request.form['language']
    secret_key = os.environ['KEY']
    print(text)
    print(language)
    print(secret_key)
    return render_template('dashboard.html')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/api/user', methods=['GET'])
def user_api():
    return {
        "username": "John",
        "surname": "Doe",
        "age": 30
    }


@app.route("/admin")
def admin():
    return redirect(url_for("dashboard"));


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("You have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)