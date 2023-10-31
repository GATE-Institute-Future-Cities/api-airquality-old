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
                'operatorEmail': operator[0][2], ## operator email
                'contactEmail': '', ## empty for now
                'contactPhone': '',
            }
            result.append(record)

        cursor.close()
        return jsonify(result)
    
@Airquality_apis.route('/api/stations/<stationId>')
class StationInfo(Resource):
    @api.doc(description='Get all info about a specific station we have in the database')
    def get(self, stationId):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM airqualitystation WHERE stationid = {stationId}')
        stationinfo = cursor.fetchone() ## get all info about the station in the database
        
        stationname = stationinfo[1] ## station name
        stationserialnumber = stationinfo[2] ## serial number 
        stationmodelid = stationinfo[3] ## station model ID
        stationoperatorid = stationinfo[5] ## station operator ID 
        
        cursor = conn.cursor()
        cursor.execute(f'SELECT stationlatitude, stationlongitude FROM stationlocation WHERE id = {stationId}')
        longlat = cursor.fetchall() ## get the long lang for the current station
        
        cursor.execute(f'SELECT brandname FROM stationmodel WHERE id = {stationmodelid}')
        model = cursor.fetchone()[0] ## get the brand name of the model
        
        
        cursor.execute(f'SELECT operatorname, operatorweb, operatoremail FROM stationoperator WHERE id = {stationoperatorid}')
        operator = cursor.fetchall() ## get the operator name
            
            
        cursor.close()
        return jsonify({
            'id': stationId,
            'name': stationname,## name
            'serialNumber': stationserialnumber, ## serial number 
            'model': model, # brand name of the model
            'latitude': longlat[0][0], ## LATIDUTE
            'longitude':longlat[0][1], ## LONGITUDE
            'operator': operator[0][0], ## operator name
            'operatorWeb': operator[0][1], ## operator website
            'operatorEmail': operator[0][2], ## operator email
            'contactEmail': '', ## empty for now
            'contactPhone': '',
        })

@Airquality_apis.route('/api/telemetry/<stationId>/values')
class AllValuesLastHour(Resource):
    @api.doc(description='All the values in the last hour for the specific station')
    def get(self, stationId):
        pass