from flask import Flask

def create_app():
    a = Flask(__name__, instance_relative_config=True)
    
    from app import app
    
    a.register_blueprint(app.bp)
    
    return app