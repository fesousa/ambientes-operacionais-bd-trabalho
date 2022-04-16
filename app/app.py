from crypt import methods
from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'AMBIENTESOPERACIONAIS'

@app.route("/")
def index():
    session['username'] = 'Fernando'
    return "Hello World!"


@app.route("/config", methods = ['POST'])
def config():
    return f"Session: {session['username']}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')