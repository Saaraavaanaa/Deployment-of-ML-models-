from types import MethodType
from flask import Flask, request, jsonify,render_template
# from gevent.pywsgi import WSGIServer
# from flask_cors import CORS, cross_origin

# import subserver

app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/secondPage')
def index1():
    return render_template("secondPage/index.html")
@app.route('/Thirdpage')
def index2():
    return render_template("Thirdpage/index.html")
@app.route('/landing')
def index3():
    return render_template("Thirdpage/landing.html")
@app.route('/404')
def index4():
    return render_template("Thirdpage/404.html")


# Load the location in the  Html 
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    print("It comes server.py")
    response = jsonify({
        'locations':get_location_names1()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


#Load the names in the Htmal
@app.route('/get_car_names', methods=['GET'])
def get_car_names():
    response = jsonify({
        'name': get_car_names1()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#load the Transmission in the Html

@app.route('/get_car_Transmission', methods=['GET'])
def get_car_Transmission():
    response = jsonify({
        'transmission': get_car_Transmission1()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#Load the Fuel Type in the Html

@app.route('/get_car_Fuel_Type', methods=['GET'])
def get_car_Fuel_Type():
    response = jsonify({
        'fuel_type': get_car_Fuel_Type1()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#Load the Owner_Type in the Html

@app.route('/get_car_Owner_Type', methods=['GET'])
def get_car_Owner_Type():
    response = jsonify({
        'Owner_Type': get_car_Owner_Type1()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


#price Pridiction Code


@app.route('/predict_price', methods=['POST'])
def predict_price():

    km = float(request.form['kilo'])
    milg = float(request.form['mille'])
    egie= float(request.form['engine'])
    po = float(request.form['power'])
    se = int(request.form['seats'])
    year = int(request.form['year'])
    CName = request.form['name']
    Cloc = request.form['location']
    f_t = request.form['fuel']
    trans = request.form['Trans']
    o_t = request.form['owner']
    

    response = jsonify({
        'estimated_price': predict_price1(CName,Cloc,year,km,f_t,trans,o_t,milg,egie,po,se)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

import pickle
import json
import numpy as np


__locations = None
__data_columns = None
__model = None
__name= None
__Fuel_Type=None
__Transmission=None
__Owner_Type=None

# price prediction function

def predict_price1(CName,Cloc,year,km,f_t,trans,o_t,milg,egie,po,se): 
    try:   
        loc_index4 = __data_columns.index(CName.upper())
        loc_index3 = __data_columns.index(Cloc.upper())
        loc_index2 = __data_columns.index(f_t.upper())
        loc_index = __data_columns.index(trans.upper())
        loc_index1 = __data_columns.index(o_t.upper())
    except:
        loc_index = -1

    X = np.zeros(len(__data_columns))
    X[0] = year
    X[1] = km
    X[2] = milg
    X[3] = egie
    X[4] = po
    X[5] = se
    if loc_index >= 0:
        X[loc_index] = 1
    if loc_index1 >= 0:
        X[loc_index1] = 1
    if loc_index2 >= 0:
        X[loc_index2] = 1
    if loc_index3 >= 0:
        X[loc_index3] = 1
    if loc_index4 >= 0:
        X[loc_index4] = 1

    return round(__model.predict([X])[0],3)




# load the pickles from model function

def load_saved_pickles():
    print("loading saved pickles...start")
    global  __data_columns
    global __locations
    global __Fuel_Type
    global __name
    global __Transmission
    global __Owner_Type

    with open(r".\Model\columns1.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __Transmission=__data_columns[6:8]
        __Owner_Type=__data_columns[8:12]
        __Fuel_Type=__data_columns[12:17]
        __locations = __data_columns[17:28]
        __name=__data_columns[28:]

    global __model
    if __model is None:
        with open(r'.\Model\Used_car_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved pickles...done")

#functions of loading 

def get_location_names1():
    print("it come in subserver.py")
    return __locations
def get_car_names1():
    return __name
def get_car_Transmission1():
    return __Transmission
def get_car_Fuel_Type1():
    return __Fuel_Type
def get_car_Owner_Type1():
    return __Owner_Type

def get_data_columns1():
    return __data_columns

    

# server Run Code

if __name__ == "__main__":
    print("Starting Python Flask Server For Used Cars Price Prediction...")
    load_saved_pickles()
    app.run(debug=True)

    # http_server = WSGIServer(('127.0.0.1', 5000), app)
    # http_server.serve_forever()