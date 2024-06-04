from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the config file
    app.config.from_pyfile('config.py', silent=True)
    
    with app.app_context():
        # Include our Routes
        from . import routes
        
        return app
