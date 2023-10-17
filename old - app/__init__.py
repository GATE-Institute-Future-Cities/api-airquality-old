from flask import Flask
from .extensions import api, db
from .searchedValueNS import SearchedValue
from .stationsNS import station


def create_app():
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mohi1234@localhost/ExEA'
    
    api.init_app(app)
    db.init_app(app)
    api.add_namespace(SearchedValue)
    api.add_namespace(station)
    return app