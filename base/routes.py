from flask import render_template, url_for, request, abort
from base import app
from base.forms import CodeCheck

hits = 0
@app.route("/check_code", methods=['GET', 'POST'])
def check():
    global hits
    hits += 1
    form = CodeCheck()
    if request.method == "POST":
        return request.form
    return render_template("code_check.html", hits = hits,
                form = form)

@app.route('/', methods=["GET"])
def home():
    return "Home"

@app.route('/register', methods=['GET', 'POST'])
def register():
    return "register"

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "login"

