from flask_restx import Resource, Namespace, reqparse
from .extensions import api
from flask import jsonify
import psycopg2


Airquality_apis= Namespace('airquality')

conn = psycopg2.connect(database="ExEa_main", user="postgres", password="mohi1234", host="localhost", port="5432")


def get_paramName(paramIds): ### function that gets all the ids for all the elements that we recive from the db and serches for the paramabreviation in the paramtype table
    cursor = conn.cursor()
    all_params = []
    for param in paramIds:
        cursor.execute('SELECT parameterabbreviation FROM parametertype WHERE id = %s', (param,))
        paramname = cursor.fetchone()[0]
        all_params.append(paramname)
    return all_params



@Airquality_apis.route('/api/stations')
class AllStations(Resource):
    @api.doc(description='Get all info about every station we have in the database')
    def get(self):
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
            cursor.execute('SELECT stationlatitude, stationlongitude FROM stationlocation WHERE id = %s', (stationid,))
            longlat = cursor.fetchall() ## get the long lang for the current station
            
            cursor.execute('SELECT brandname FROM stationmodel WHERE id = %s', (stationmodelid,))
            model = cursor.fetchone()[0] ## get the brand name of the model
            
            
            cursor.execute('SELECT operatorname, operatorweb, operatoremail FROM stationoperator WHERE id = %s', (stationoperatorid,))
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
        cursor.execute('SELECT * FROM airqualitystation WHERE stationid = %s', (stationId,))
        stationinfo = cursor.fetchone() ## get all info about the station in the database
        
        stationname = stationinfo[1] ## station name
        stationserialnumber = stationinfo[2] ## serial number 
        stationmodelid = stationinfo[3] ## station model ID
        stationoperatorid = stationinfo[5] ## station operator ID 
        
        cursor = conn.cursor()
        cursor.execute('SELECT stationlatitude, stationlongitude FROM stationlocation WHERE id = %s', (stationId,))
        longlat = cursor.fetchall() ## get the long lang for the current station
        
        cursor.execute('SELECT brandname FROM stationmodel WHERE id = %s', (stationmodelid,))
        model = cursor.fetchone()[0] ## get the brand name of the model
        
        
        cursor.execute('SELECT operatorname, operatorweb, operatoremail FROM stationoperator WHERE id = %s', (stationoperatorid,))
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

@Airquality_apis.route('/api/telemetry/<stationId>/values/lasthour')
class AllValuesLastHour(Resource):
    @api.doc(description='gets the value in the last hour for each element and for the specific station')
    def get(self, stationId):
        cursor = conn.cursor()
        
        cursor.execute(f'SELECT MAX(measurementdatetime) FROM airqualityobserved')
        recent_datetime = cursor.fetchone()[0] ## most recent time added to the database
        
        cursor.execute('SELECT measuredparameterid, measuredvalue FROM airqualityobserved WHERE measurementdatetime = %s AND stationid = %s', (recent_datetime, stationId))
        val_element = cursor.fetchall() ## get all the values and elements at the most recent datetime
        
        elemntIds = [el[0] for el in val_element] ## all the ids for the elements
        elementNames = get_paramName(elemntIds) ## func to get the names of the elements
        elementNames.insert(0, 'Time') ## time column is a default col
                
        values = [val[1] for val in val_element] ## all the values for each element in the most recent time
        values.insert(0, recent_datetime) ## insert the time with the values
        
        return(jsonify({
            'columns': elementNames,
            'values': values,
        }))
        
# parser to parse the 'selectedElements' query parameter as a list of integers
parser = reqparse.RequestParser()
parser.add_argument('selectedElements', type=int, action='split', help='List of selected elements', required=True)

@Airquality_apis.route('/api/telemetry/values/<stationId>/<timeframe>')
class SelectedData(Resource):
    @api.doc(description='retrives information about AQ values for a list of specified elements in the specified timeframe')
    @api.expect(parser)
    def get(self, stationId, timeframe):
        
        cursor = conn.cursor()
        args = parser.parse_args()
        selectedElements = args['selectedElements'] ## list of the chosen element ids
        
        all_elements = get_paramName(selectedElements) ## selected elements is a list of ids for the specified elements we call to func to covert to param abreviation
                
        values = []
        for elId in selectedElements:
             cursor.execute('SELECT measuredvalue FROM airqualityobserved WHERE measuredparameterid = %s AND measurementdatetime = %s AND stationid = %s', (elId, timeframe, stationId))
             value = cursor.fetchone()[0]
             values.append(value)
            
        cursor.close()
        return jsonify({
            'dateTime': timeframe,
            'elements': all_elements,
            'values': values,
        })
        
@Airquality_apis.route('/api/telemetry/values/<elementId>/<stationId>/<fromDate>/<toDate>')
class SelectedDatetime(Resource):
    @api.doc(description = 'get specific element values fromdate todate')
    def get(self, elementId, stationId, fromDate, toDate):
        cursor = conn.cursor()
        
        cursor.execute('SELECT parameterabbreviation FROM parametertype WHERE id = %s', (elementId,) )
        elementName = cursor.fetchone()[0]
        
        cursor.execute('SELECT measurementdatetime, measuredvalue FROM airqualityobserved WHERE stationid = %s AND measuredparameterid = %s AND measurementdatetime BETWEEN %s AND %s', (stationId, elementId, fromDate, toDate))
        data = cursor.fetchall()
        
        return jsonify({
            'element': elementName,
            'fromDate': fromDate,
            'toDate': toDate,
            'values': data,
            
        })
        
@Airquality_apis.route('/api/telemetry/values/<elementId>/<stationId>/<fromDate>/<toDate>')
class SelectedDatetimeValues(Resource):
    @api.doc(description = 'get elements values fromdate todate ')
    @api.expect(parser)
    def get(self, elementId, stationId, fromDate, toDate):
        cursor = conn.cursor()
        args = parser.parse_args()
        selectedElements = args['selectedElements'] ## list of the chosen element ids