from flask import Flask
from config import Config
from flask_cors import CORS

# import sys
# print(sys.path)
def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static', static_folder='../static')
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config_class)

    from app import routes
    app.register_blueprint(routes.main)

    return app

