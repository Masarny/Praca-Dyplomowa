from flask import render_template
from app import app

@app.route('/')
@app.route('/login_1')
def login_1():
    return render_template('login_1.html')


@app.route("/login_2")
def login_2():
    return render_template("login_2.html")


@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/guidelines")
def guidelines():
    return render_template("guidelines.html")


@app.route("/creator")
def creator():
    return render_template("creator.html")


@app.route("/tester")
def tester():
    return render_template("tester.html")


@app.route("/user_passwords")
def user_passwords():
    return render_template("user_passwords.html")