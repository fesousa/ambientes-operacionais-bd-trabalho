from flask import Flask
import yaml, traceback, os

app = Flask(__name__)
app.secret_key = 'AMBIENTESOPERACIONAIS'

@app.route("/")
def index():
    try:
        config = None
        with open("config.yaml", "r") as stream:
    
            config= yaml.safe_load(stream)
 
        return f"HOST: {config}"
    except Exception as ex:
        return f"{traceback.format_exc()}, {os.getcwd()}"


@app.route("/config", methods = ['POST'])
def config():
    try:
      
        return f"HOST: "
    except Exception as ex:
        return traceback.format_exc()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')