from flask_restx import Resource, Namespace
from .extensions import api
from flask import jsonify
import psycopg2

all_val_station= Namespace('all info about station')

conn = psycopg2.connect(database="ExEa_main", user="postgres", password="mohi1234", host="localhost", port="5432")
cursor = conn.cursor()
