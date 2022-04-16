from flask import Flask
import dotenv, os

app = Flask(__name__)
app.secret_key = 'AMBIENTESOPERACIONAIS'

@app.route("/")
def index():
    try:
        dotenv.load_dotenv(dotenv.find_dotenv())
        return f"HOST: {os.environ}"
    except Exception as ex:
        return str(ex)


@app.route("/config", methods = ['POST'])
def config():
    try:
        dotenv.load_dotenv(dotenv.find_dotenv())
        dotenv.set_key(dotenv.find_dotenv(), "HOST", "HOST DB")

        return f"HOST: {os.environ}"
    except Exception as ex:
        return str(ex)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')