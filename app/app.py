from flask import Flask, request
import yaml, traceback, os
import psycopg2

app = Flask(__name__)
app.secret_key = 'AMBIENTESOPERACIONAIS'

@app.route("/")
def index():
    try:
        config = None
        try:
            with open(f"{os.getcwd()}/app/config.yaml", "r") as file:    
                config= yaml.load(file, Loader=yaml.FullLoader)
        except: 
            pass
        return f"OK"
    except Exception as ex:
        return f"{traceback.format_exc()}, {os.getcwd()}"


@app.route("/config", methods = ['POST'])
def config():
    try:
        config = {}
        try:
            with open(f"{os.getcwd()}/app/config.yaml", "r") as file:
        
                config= yaml.load(file, Loader=yaml.FullLoader)
        except:
            pass

        config["HOST"] = request.json['host']
        config["DB"] = request.json['bd']
        config["USER"] = request.json['usuario']
        config["PWD"] = request.json['senha']

        with open(f"{os.getcwd()}/app/config.yaml", "w") as file:
            yaml.dump(config, file)
      
        return "OK"
    except Exception as ex:
        return traceback.format_exc()


@app.route("/sql", methods = ['POST'])
def sql():
    try:
        config = {}
        try:
            with open(f"{os.getcwd()}/app/config.yaml", "r") as file:
        
                config= yaml.load(file, Loader=yaml.FullLoader)
        except:
            raise Exception("Conexão não configurada")

        con = psycopg2.connect(host=config["HOST"], database=config["DB"],
        user=config["USER"], password=config["PWD"])
        cur = con.cursor()
        sql = request.json['sql']
        r = cur.execute(sql)       
        con.commit()
        # cur.execute('select * from cidade')
        # recset = cur.fetchall()
        # for rec in recset:
        # print (rec)
        con.close()
      
        return r
    except Exception as ex:
        return traceback.format_exc()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')