from flask import Flask, request
import yaml, traceback, os, json

app = Flask(__name__)
app.secret_key = 'AMBIENTESOPERACIONAIS'

@app.route("/")
def index():
    try:
        config = None
        with open(f"{os.getcwd()}/app/config.yaml", "r") as file:    
            config= json.loads(yaml.load(file, Loader=yaml.FullLoader))
        return f"HOST: {config['HOST']}"
    except Exception as ex:
        return f"{traceback.format_exc()}, {os.getcwd()}"


@app.route("/config", methods = ['POST'])
def config():
    try:
        config = None
        with open(f"{os.getcwd()}/app/config.yaml", "r") as file:
    
            config= yaml.load(file, Loader=yaml.FullLoader)

        config["HOST"] = request.json['host']
        config["DB"] = request.json['bd']
        config["USER"] = request.json['usuario']
        config["PWD"] = request.json['senha']

        # with open(f"{os.getcwd()}/app/config.yaml", "w") as file:
        #     yaml.dump(config, file)
      
        return f"HOST: {config}"
    except Exception as ex:
        return traceback.format_exc()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')