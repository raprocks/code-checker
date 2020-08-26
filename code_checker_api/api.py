from flask import Flask, request, url_for
from code_checker_api import code_checker

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def base():
    if request.method == 'POST':
        return "Please do a GET request to find available endpoints"
    return json.dumps(dict("code_checker_api"=url_for(code_check)))

@app.route('/code_check', methods=['POST'])
def code_check():
    print(request.form)
