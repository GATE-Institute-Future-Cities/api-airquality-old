from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2

all_info_station= Namespace('all info about station')

conn = psycopg2.connect(database="ExEa_main", user="postgres", password="mohi1234", host="localhost", port="5432")
cursor = conn.cursor()

def get_station_name(stationname):
    query = 'SELECT * FROM airqualitystation WHERE stationname = %s'
    cursor.execute(query, (stationname,))
    value = cursor.fetchone()[0]
    cursor.close()
    return value

@all_info_station.route('/info/<stationName>') ## all info for station
class AllInfo(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the nadezhda table')
    def get(self, elementid, timeframe):
        pass
