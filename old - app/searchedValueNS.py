from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2
from config import db_config

SearchedValue = Namespace('value')
conn = psycopg2.connect(**db_config)



@SearchedValue.route('/mladost/<element>/<timeframe>') ## search value from a specific element in the specified timeframe from the MLADOST table
class MladostValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the mladost table')
    def get(self, element, timeframe):
        cursor = conn.cursor()
        cursor.execute(f'SELECT "{element}" FROM mladost WHERE "Time" = \'{timeframe}\'') 
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': element,
            'Value': value,
        })


@SearchedValue.route('/nadezhda/<element>/<timeframe>')## search value from a specific element in the specified timeframe from the NADEZHDA table
class NadezhdaValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the nadezhda table')
    def get(self, element, timeframe):
        cursor = conn.cursor()
        cursor.execute(f'SELECT "{element}" FROM nadezhda WHERE "Time" = \'{timeframe}\'')
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': element,
            'Value': value,
        })


@SearchedValue.route('/druzhba/<element>/<timeframe>')## search value from a specific element in the specified timeframe from the DRUZHBA table
class DruzhbaValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the druzhba table')
    def get(self, element, timeframe):
        cursor = conn.cursor()
        cursor.execute(f'SELECT "{element}" FROM druzhba WHERE "Time" = \'{timeframe}\'')
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': element,
            'Value': value,
        })



@SearchedValue.route('/hipodruma/<element>/<timeframe>')## search value from a specific element in the specified timeframe from the HIPODRUMA table
class HipodrumaValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the hipodruma table')
    def get(self, element, timeframe):
        cursor = conn.cursor()
        cursor.execute(f'SELECT "{element}" FROM hipodruma WHERE "Time" = \'{timeframe}\'')
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': element,
            'Value': value,
        })



@SearchedValue.route('/pavlovo/<element>/<timeframe>')## search value from a specific element in the specified timeframe from the PAVLOVO table
class PavlovoValue(Resource):
    @api.doc(description='Get value for a specific element in the specified timeframe from the pavlovo table')
    def get(self, element, timeframe):
        cursor = conn.cursor()
        cursor.execute(f'SELECT "{element}" FROM pavlovo WHERE "Time" = \'{timeframe}\'')
        value = cursor.fetchone()[0]  # Fetch the value for the specified element at the given timeframe

        cursor.close()
        return jsonify({
            'Time': timeframe,
            'Element': element,
            'Value': value,
        })
