from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/dashboard")
def hello_world():
    return render_template('dashboard.html')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('api/user')
def user_api():
    return {
        "username": "John",
        "surname": "Doe",
        "age": 30
    }