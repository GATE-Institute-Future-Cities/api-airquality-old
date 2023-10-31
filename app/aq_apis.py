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
        cursor.execute(f'SELECT * FROM airqualitystation')
        all_stations = cursor.fetchall() ## get all the stations in the database
        result = []

        for station in all_stations:
            stationid = station[0] ## station id
            stationname = station[1] ## station name
            stationserialnumber = station[2] ## serial number 
            stationmodelid = station[3] ## station model ID
            stationoperatorid = station[5] ## station operator ID 
            
            cursor = conn.cursor()
            cursor.execute(f'SELECT stationlatitude, stationlongitude FROM stationlocation WHERE id = {stationid}')
            longlat = cursor.fetchall() ## get the long lang for the current station
            
            cursor.execute(f'SELECT brandname FROM stationmodel WHERE id = {stationmodelid}')
            model = cursor.fetchone()[0] ## get the brand name of the model
            
            
            cursor.execute(f'SELECT operatorname, operatorweb, operatoremail FROM stationoperator WHERE id = {stationoperatorid}')
            operator = cursor.fetchall() ## get the operator name
            
            
            record = {
                'id': stationid,
                'name': stationname,## name
                'serialNumber': stationserialnumber, ## serial number 
                'model': model, # brand name of the model
                'latitude': longlat[0][0], ## LATIDUTE
                'longitude':longlat[0][1], ## LONGITUDE
                'operator': operator[0][0], ## operator name
                'operatorWeb': operator[0][1], ## operator website
                'operatorEmail': operator[0][2] ## operator email
            }
            result.append(record)

        cursor.close()
        return jsonify(result)