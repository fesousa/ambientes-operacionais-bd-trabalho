from flask import Flask
import dotenv, os, traceback

app = Flask(__name__)
app.secret_key = 'AMBIENTESOPERACIONAIS'

@app.route("/")
def index():
    try:
        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)
        return f"HOST: {os.environ}, {dotenv_file}"
    except Exception as ex:
        return str(ex)


@app.route("/config", methods = ['POST'])
def config():
    try:
        dotenv_file = dotenv.find_dotenv()
        dotenv.load_dotenv(dotenv_file)
        dotenv.set_key(dotenv_file, "HOST", "HOST DB")

        return f"HOST: {os.environ}"
    except Exception as ex:
        return dotenv_file

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')