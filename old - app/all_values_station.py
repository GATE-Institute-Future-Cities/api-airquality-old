from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2
from config import db_config

all_val_station= Namespace('all values for station')

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()


@all_val_station.route('/pavlovo') ## get all values for a specific station
class PavlovoAllValues(Resource):
    @api.doc(description='Get all values for pavlovo station')
    def get(self):
        stationid = 1 ##Pavlovo has the station id 1 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE stationid = {stationid}') 
        value = cursor.fetchall() # Fetch all values for a pavlovo station
        cursor.close()
        
        return jsonify({
                        'Values' : value,    
                }) 
        
        
@all_val_station.route('/hipodruma') ## get all values for a specific station
class HipodrumaAllValues(Resource):
    @api.doc(description='Get all values for hipodruma station')
    def get(self):
        stationid = 2 ##hipodruma has the station id 1 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE stationid = {stationid}') 
        value = cursor.fetchall() # Fetch all values for a hipodruma station
        cursor.close()
        
        return jsonify({
                        'Values' : value,    
                }) 
        
@all_val_station.route('/nadezhda') ## get all values for a specific station
class NadezhdaAllValues(Resource):
    @api.doc(description='Get all values for nadezhda station')
    def get(self):
        stationid = 3 ##nadezhda has the station id 1 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE stationid = {stationid}') 
        value = cursor.fetchall() # Fetch all values for a nadezhda station
        cursor.close()
        
        return jsonify({
                        'Values' : value,    
                }) 
        
@all_val_station.route('/mladost') ## get all values for a specific station
class MladostAllValues(Resource):
    @api.doc(description='Get all values for mladost station')
    def get(self):
        stationid = 4 ##mladost has the station id 1 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE stationid = {stationid}') 
        value = cursor.fetchall() # Fetch all values for a mladost station
        cursor.close()
        
        return jsonify({
                        'Values' : value,    
                }) 
        
@all_val_station.route('/druzhba') ## get all values for a specific station
class DruzhbatAllValues(Resource):
    @api.doc(description='Get all values for druzhba station')
    def get(self):
        stationid = 5 ##druzhba has the station id 1 in the database
        cursor = conn.cursor()
        cursor.execute(f'SELECT measuredvalue FROM airqualityobserved WHERE stationid = {stationid}') 
        value = cursor.fetchall() # Fetch all values for a druzhba station
        cursor.close()
        
        return jsonify({
                        'Values' : value,    
                }) 