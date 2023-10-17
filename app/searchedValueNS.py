from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2

SearchedValue = Namespace('value')
conn = psycopg2.connect(database="ExEa_main", user="postgres", password="mohi1234", host="localhost", port="5432")
cursor = conn.cursor()


def get_paramname(paramid):
    query_paramname = 'SELECT parameterabbreviation FROM parametertype WHERE id = %s'
    cursor.execute(query_paramname, (paramid,))
    value = cursor.fetchone()[0]
    cursor.close()
    return value

def get_sensorid(paramid, stationid):
    cursor = conn.cursor()
    query_sensorid = 'SELECT sensorid FROM airqualityobserved WHERE measuredparameterid = %s AND stationid = %s'
    cursor.execute(query_sensorid, (paramid, stationid,))
    value = cursor.fetchone()[0]
    cursor.close()
    return value

@SearchedValue.route('/pavlovo/<elementid>/<timeframe>') ## search value from a specific element in the specified timeframe from the pavlovo table
class PavlovoValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the pavlovo table')
    def get(self, elementid, timeframe):
        stationid = 1 ##Pavlovo has the station id 1 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE measuredparameterid = {elementid} AND measurementdatetime = \'{timeframe}\' AND stationid = {stationid}') 
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe
        paramName = get_paramname(elementid)
        sensorid = get_sensorid(elementid, stationid)

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': paramName,
            'Value': value,
            'Station id': stationid,
            'Sensor id': sensorid,
        })

@SearchedValue.route('/hipodruma/<elementid>/<timeframe>') ## search value from a specific element in the specified timeframe from the hipodruma table
class HipodrumaValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the hipodruma table')
    def get(self, elementid, timeframe):
        stationid = 2 ##hipodruma has the station id 2 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE measuredparameterid = {elementid} AND measurementdatetime = \'{timeframe}\' AND stationid = {stationid}') 
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe
        paramName = get_paramname(elementid)
        sensorid = get_sensorid(elementid, stationid)

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': paramName,
            'Value': value,
            'Station id': stationid,
            'Sensor id': sensorid,
        })
        
@SearchedValue.route('/nadezhda/<elementid>/<timeframe>') ## search value from a specific element in the specified timeframe from the nadezhda table
class NadezhdaValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the nadezhda table')
    def get(self, elementid, timeframe):
        stationid = 3 ##nadezhda has the station id 3 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE measuredparameterid = {elementid} AND measurementdatetime = \'{timeframe}\' AND stationid = {stationid}') 
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe
        paramName = get_paramname(elementid)
        sensorid = get_sensorid(elementid, stationid)

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': paramName,
            'Value': value,
            'Station id': stationid,
            'Sensor id': sensorid,
        })


@SearchedValue.route('/mladost/<elementid>/<timeframe>') ## search value from a specific element in the specified timeframe from the mladost table
class MladostValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the mladost table')
    def get(self, elementid, timeframe):
        stationid = 4 ##mladost has the station id 4 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE measuredparameterid = {elementid} AND measurementdatetime = \'{timeframe}\' AND stationid = {stationid}') 
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe
        paramName = get_paramname(elementid)
        sensorid = get_sensorid(elementid, stationid)

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': paramName,
            'Value': value,
            'Station id': stationid,
            'Sensor id': sensorid,
        })

@SearchedValue.route('/druzhba/<elementid>/<timeframe>') ## search value from a specific element in the specified timeframe from the druzhba table
class DruzhbaValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the druzhba table')
    def get(self, elementid, timeframe):
        stationid = 5 ##druzhba has the station id 5 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE measuredparameterid = {elementid} AND measurementdatetime = \'{timeframe}\' AND stationid = {stationid}') 
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe
        paramName = get_paramname(elementid)
        sensorid = get_sensorid(elementid, stationid)

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': paramName,
            'Value': value,
            'Station id': stationid,
            'Sensor id': sensorid,
        })
