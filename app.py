from flask import Flask
from flask import render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/dashboard")
def dashboard():
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