from flask import Flask
from flask import render_template, redirect, url_for, request
# from dotenv import load_dotenv

app = Flask(__name__)

# load_dotenv()

@app.route("/", methods=['GET'])
@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


@app.route("/", methods=['POST'])
@app.route("/dashboard", methods=['POST'])
def dashboard_post():
    text = request.form['text']
    language = request.form['language']
    print(text)
    print(language)
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