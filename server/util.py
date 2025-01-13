import json
import joblib
import numpy as np

__locations=[]
__data=[]
__model=None

def get_locations():
    return __locations

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__data.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk

    if loc_index>=0 :
        x[loc_index]=1

    return __model.predict([x])[0]

def load_locations():
    print("Loading Locations....")
    global __locations
    global __data
    global __model
    with open("./artifacts/columns.json") as f:
        __data=json.load(f)["data_columns"]
        __locations=__data[3:]
    print("Locations loaded Succesfully")

    with open("./artifacts/Banglore_price_prediction_model","rb") as f:
        __model=joblib.load(f)
    print("Model Loaded Successfully")

if __name__=="__main__":
    load_locations()
    print(get_locations())