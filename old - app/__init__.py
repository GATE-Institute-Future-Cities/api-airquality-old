from flask import Flask
from .extensions import api, db
from .searchedValueNS import SearchedValue
from .stationsNS import station
from config import db_uri

def create_app():
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    
    api.init_app(app)
    db.init_app(app)
    api.add_namespace(SearchedValue)
    api.add_namespace(station)
    return app