from flask import Flask
from .extensions import api, db
from .searchedValueNS import SearchedValue
from .all_values import all_values
from .all_values_station import all_val_station

def create_app():
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mohi1234@localhost/ExEa_main'
    
    api.init_app(app)
    db.init_app(app)
    api.add_namespace(SearchedValue)
    api.add_namespace(all_values)
    api.add_namespace(all_val_station)
    return app