from flask import Flask
import dotenv

app = Flask(__name__)
app.secret_key = 'AMBIENTESOPERACIONAIS'

@app.route("/")
def index():
    try:
        config = dotenv.dotenv_values(".env") 
        return f"HOST: "
    except Exception as ex:
        return str(ex)


@app.route("/config", methods = ['POST'])
def config():
    
    dotenv.load_dotenv(".env")
    dotenv.set_key(dotenv_file, "HOST", "HOST DB")

    config = dotenv.dotenv_values(".env") 
    return f"HOST: {config['HOST']}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')