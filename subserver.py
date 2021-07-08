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

def predict_price(CName,Cloc,year,km,f_t,trans,o_t,milg,egie,po,se): 
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

def get_location_names():
    return __locations
def get_car_names():
    return __name
def get_car_Transmission():
    return __Transmission
def get_car_Fuel_Type():
    return __Fuel_Type
def get_car_Owner_Type():
    return __Owner_Type

def get_data_columns():
    return __data_columns

# just example to run the code properly 

if __name__ == '__main__':
    load_saved_pickles()
    print(predict_price('Maruti','Mumbai',2010,72000,'CNG','Manual','First',26.6,998,58.16,5)) #example
    