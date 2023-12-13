from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2
from config import db_config

station = Namespace('stations')

conn = psycopg2.connect(**db_config)



## all Data for The MLADOST table
@station.route('/mladost')
class Mladost(Resource):
    @api.doc(description='Get all data from the Mladost table ordered by the time column')
    def get(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM mladost')
        columns = [desc[0] for desc in cursor.description] ## All the column names in the table       -------> same applies to the rest of the routes
        result = {}

        for col in columns:
            cursor.execute(f'SELECT "{col}" FROM mladost ORDER BY "Time"')
            values = [row[0] for row in cursor.fetchall()] ## all the values added row by row to each element
            result[col] = values
            
        cursor.close()

        response = []
        for name, values in result.items(): 
            response.append({
                'Column': name,
                'Values': values
            })
            print(name)
            print(values)
        print(response)
        return jsonify(response)


## all Data for The NADEZHDA table
@station.route('/nadezhda')
class Nadezhda(Resource):
    @api.doc(description='Get all data from the Nadezhda table ordered by the time column')
    def get(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM nadezhda')
        columns = [desc[0] for desc in cursor.description]
        result = {}

        for col in columns:
            cursor.execute(f'SELECT "{col}" FROM nadezhda ORDER BY "Time"')
            values = [row[0] for row in cursor.fetchall()]
            result[col] = values

        cursor.close()

        response = []
        for name, values in result.items():
            response.append({
                'Column': name,
                'Values': values
            })

        return jsonify(response)
    
    
## all Data for The DRUZHBA table
@station.route('/druzhba')
class Druzhba(Resource):
    @api.doc(description='Get all data from the Druzhba table ordered by the time column')
    def get(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM druzhba')
        columns = [desc[0] for desc in cursor.description]
        result = {}

        for col in columns:
            cursor.execute(f'SELECT "{col}" FROM druzhba ORDER BY "Time"')
            values = [row[0] for row in cursor.fetchall()]
            result[col] = values

        cursor.close()

        response = []
        for name, values in result.items():
            response.append({
                'Column': name,
                'Values': values
            })

        return jsonify(response)
    

## all Data for The HIPODRUMA table
@station.route('/hipodruma')
class Hipodruma(Resource):
    @api.doc(description='Get all data from the Hipodruma table ordered by the time column')
    def get(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM hipodruma')
        columns = [desc[0] for desc in cursor.description]
        result = {}

        for col in columns:
            cursor.execute(f'SELECT "{col}" FROM hipodruma ORDER BY "Time"')
            values = [row[0] for row in cursor.fetchall()]
            result[col] = values

        cursor.close()

        response = []
        for name, values in result.items():
            response.append({
                'Column': name,
                'Values': values
            })

        return jsonify(response)
    
    
## all Data for The PAVLOVO table
@station.route('/pavlovo')
class Pavlovo(Resource):
    @api.doc(description='Get all data from the Pavlovo table ordered by the time column')
    def get(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pavlovo')
        columns = [desc[0] for desc in cursor.description]
        result = {}

        for col in columns:
            cursor.execute(f'SELECT "{col}" FROM pavlovo ORDER BY "Time"')
            values = [row[0] for row in cursor.fetchall()]
            result[col] = values

        cursor.close()

        response = []
        for name, values in result.items():
            response.append({
                'Column': name,
                'Values': values
            })

        return jsonify(response)