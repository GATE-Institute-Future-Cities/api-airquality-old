from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2

Airquality_apis= Namespace('airquality')

conn = psycopg2.connect(database="ExEa_main", user="postgres", password="mohi1234", host="localhost", port="5432")



@Airquality_apis.route('/api/stations')
class AllStations(Resource):
    @api.doc(description='Get all info about every station we have in the database')
    def get(self,):
        cursor = conn.cursor()
        cursor.execute(f'SELECT stationid, stationname, stationserialnumber FROM airqualitystation')
        all_stations = cursor.fetchall() ## get all the stations in the database
        result = []

        for station in all_stations:
            stationid = station[0] ## station id
            
            cursor = conn.cursor()
            cursor.execute(f'SELECT stationlatitude, stationlongitude FROM stationlocation WHERE id = {stationid}')
            longlat = cursor.fetchall() ## get the long lang for the current station
            
            record = {
                'id': stationid,
                'name': station[1],## station name
                'latitude': longlat[0][0], ## getting the first lists element which is the LATIDUTE
                'longitude':longlat[0][1], ## getting the first lists element which is the LONGITUDE
                'serial number': station,
                'model': station,
                'location': station,
            }
            result.append(record)

        cursor.close()
        return jsonify(result)