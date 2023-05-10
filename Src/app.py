from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        valida_login (request.form["name"] + request.form["pwd"])
        return
    return render_template("login.html")

def valida_login(name, pwd):
    pass
