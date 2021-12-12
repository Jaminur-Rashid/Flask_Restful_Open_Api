#################################################################
# This is Restful Open Api using flask and Jwt                   #
# Which can search data from database using multiple properties  #
# Author : Jaminur Rashid                                        #
# Date   : 9-12-2021                                             #
# #################################################################
from flask import Flask, jsonify, request, make_response, redirect
import jwt
import datetime
from functools import wraps
from flask_swagger_ui import get_swaggerui_blueprint
import mysql.connector
import json
import operator

token_id = ''
app = Flask(__name__)
# Configuring Swagger
app.config['SECRET_KEY'] = 'weengineers'
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask_Rest_Api"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


# Token Decorator

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return jsonify({'message': 'Token is not valid'}), 403

        return f(*args, **kwargs)

    return decorated


@app.route('/')
def index():
    return redirect("http://127.0.0.1:5000/login", code=302)


# Unprotected Route and function
@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'This a public route'})


@app.route('/house', methods=['GET'])
def house():
    title = request.args.get('title')
    bedroom = request.args.get('bedroom')
    sleeps = request.args.get('sleeps')
    bathroom = request.args.get('bathroom')
    price = request.args.get('price')
    location = request.args.get('location')

    condo = []
    # Connect with vrboData database which contains the scrapped data
    db_connector = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="vrboDatabase"
    )
    data_fetch_query = "SELECT * FROM vrbo_hotel_info_table WHERE"
    check = "SELECT * FROM vrbo_hotel_info_table WHERE"
    cursor = db_connector.cursor()
    data_container = []
    if title != None:
        if data_fetch_query is check:
            data_fetch_query += " Hotel_Name LIKE" + f"'%{title}%'"
        else:
            data_fetch_query += " AND Hotel_Name LIKE" + f"'%{title}%'"

    if bedroom != None:
        if data_fetch_query is check:
            data_fetch_query += " Bedroom >="+bedroom+""
        else:
            data_fetch_query += " AND Bedroom >="+bedroom+""

    if bathroom != None:
            if data_fetch_query is check:
                data_fetch_query += " Bathroom >="+bathroom+""
            else:
                data_fetch_query += " AND Bathroom >="+bathroom+""

    if sleeps != None:
        if data_fetch_query == check:
            data_fetch_query += " Sleeping >="+sleeps+""
        else:
            data_fetch_query += " AND  Sleeping >="+sleeps+""

    if price != None:
        if data_fetch_query == check:
            data_fetch_query += " Price LIKE" + f"'%{price}%'"
        else:
            data_fetch_query += " Price LIKE" + f"'%{price}%'"

    if location != None:
        if data_fetch_query is check:
            data_fetch_query += " Location LIKE" + f"'%{location}%'"
        else:
            data_fetch_query += " AND Location LIKE" + f"'%{location}%'"
    #data_fetch_query += " ORDER BY Sleeping DESC"
    print(data_fetch_query)
    # Execute select query to fetch data
    cursor.execute(data_fetch_query)
    results = cursor.fetchall()
    print(results)
    # extract the fetched data and format it
    for result in results:
        hotel_data = {
            "Location": result[1],
            "Hotel Name": result[2],
            "Sleeps": result[3],
            "Bedrooms": result[4],
            "Bathrooms": result[5],
            "Price": result[6],
        }
        data_container.append(hotel_data)
    # Sort List of dictionaries by key value
    # Sort hotel data by num of Slepping room in Ascending order
    # Sort is done by using string comparison
    # as our database column name was varchar type
    data_container.sort(key=operator.itemgetter('Bedrooms'))
    #d = sorted(data_container, key=lambda tmp: tmp['Sleeps'])
    # format data into json
    hotel_data_json = json.dumps(data_container, indent=4)
    #print(condo)
    print(hotel_data_json)
    print(data_fetch_query)
    return hotel_data_json


# Redirect to swagger ui page to test api
# after login using jwt token
@app.route('/swaggerPage')
@token_required
def swagger():
    # return jsonify({'message': 'Only available to people with valid tokens.'})

    return redirect("http://127.0.0.1:5000/swagger", code=302)


# Login Route and function
@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == '1234':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=50)},
                           app.config['SECRET_KEY'])
        token_id = token
        return jsonify({'token': token})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm:"Login Required"'})


if __name__ == "__main__":
    app.run()
