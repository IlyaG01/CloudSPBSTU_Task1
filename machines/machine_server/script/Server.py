from crypt import methods
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Get! Get! Get!</p>"

@app.route("/", methods=['PUT'])
def hello_world_put():
    return "<p>Put! Put! Put!</p>"

@app.route("/name", methods=['POST'])
def login():
    return f"<p>Hello, dear {request.form['username']}</p>\n"

app.run(host='0.0.0.0', port=5000)