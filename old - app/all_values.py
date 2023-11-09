from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2

all_values = Namespace('all data for element')

conn = psycopg2.connect(database="ExEa_main", user="postgres", password="mohi1234", host="localhost", port="5432")
cursor = conn.cursor()

def get_paramname(paramid):
    query_paramname = 'SELECT parameterabbreviation FROM parametertype WHERE id = %s'
    cursor.execute(query_paramname, (paramid,))
    value = cursor.fetchone()[0]
    cursor.close()
    return value


## all Data for The Pavlovo elements
@all_values.route('/pavlovo/<elementid>')
class PavlovoAllValues(Resource):
    @api.doc(description='Get all data for a specifict element in the pavlovo station')
    def get(self, elementid):
        stationid = 1 ##Pavlovo has the station id 1 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM airqualityobserved WHERE measuredparameterid = {elementid} AND stationid = {stationid}') 
        value = cursor.fetchall()   # Fetch the value for the specified element 
        paramName = get_paramname(elementid)
        result = []

        for v in value:
            record = {
                'Element': paramName,
                'id': v[0],
                'date': v[1],
                'elementid': v[2],
                'value': v[3],
                'stationdid': v[4],
                'sensorid': v[5]
            }
            result.append(record)

        cursor.close()
        return jsonify(result)


@all_values.route('/hipodruma/<elementid>')
class HipodrumaAllValues(Resource):
    @api.doc(description='Get all data for a specifict element in the hipodruma station')
    def get(self, elementid):
        stationid = 2 ##hipodruma has the station id 2 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM airqualityobserved WHERE measuredparameterid = {elementid} AND stationid = {stationid}') 
        value = cursor.fetchall()   # Fetch the value for the specified element 
        paramName = get_paramname(elementid)
        result = []

        for v in value:
            record = {
                'Element': paramName,
                'id': v[0],
                'date': v[1],
                'elementid': v[2],
                'value': v[3],
                'stationdid': v[4],
                'sensorid': v[5]
            }
            result.append(record)

        cursor.close()
        return jsonify(result)


@all_values.route('/nadezhda/<elementid>')
class NadezhdaAllValues(Resource):
    @api.doc(description='Get all data for a specifict element in the nadezhda station')
    def get(self, elementid):
        stationid = 3 ##nadezhda has the station id 3 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM airqualityobserved WHERE measuredparameterid = {elementid} AND stationid = {stationid}') 
        value = cursor.fetchall()  # Fetch the value for the specified element 
        paramName = get_paramname(elementid)
        result = []

        for v in value:
            record = {
                'Element': paramName,
                'id': v[0],
                'date': v[1],
                'elementid': v[2],
                'value': v[3],
                'stationdid': v[4],
                'sensorid': v[5]
            }
            result.append(record)

        cursor.close()
        return jsonify(result)


@all_values.route('/mladost/<elementid>')
class MladostAllValues(Resource):
    @api.doc(description='Get all data for a specifict element in the mladost station')
    def get(self, elementid):
        stationid = 4 ##mladost has the station id 4 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM airqualityobserved WHERE measuredparameterid = {elementid} AND stationid = {stationid}') 
        value = cursor.fetchall()  # Fetch the value for the specified element 
        paramName = get_paramname(elementid)
        result = []

        for v in value:
            record = {
                'Element': paramName,
                'id': v[0],
                'date': v[1],
                'elementid': v[2],
                'value': v[3],
                'stationdid': v[4],
                'sensorid': v[5]
            }
            result.append(record)

        cursor.close()
        return jsonify(result)

@all_values.route('/druzhba/<elementid>')
class DruzhbaAllValues(Resource):
    @api.doc(description='Get all data for a specifict element in the druzhba station')
    def get(self, elementid):
        stationid = 5 ##druzhba has the station id 5 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM airqualityobserved WHERE measuredparameterid = {elementid} AND stationid = {stationid}') 
        value = cursor.fetchall()  # Fetch the value for the specified element 
        paramName = get_paramname(elementid)
        result = []

        for v in value:
            record = {
                'Element': paramName,
                'id': v[0],
                'date': v[1],
                'elementid': v[2],
                'value': v[3],
                'stationdid': v[4],
                'sensorid': v[5]
            }
            result.append(record)

        cursor.close()
        return jsonify(result)


