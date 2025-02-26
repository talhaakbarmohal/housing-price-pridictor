import pickle
import joblib
import json
import numpy as np

__regionMaping = None
__model = None
feature_order = ['Rooms', 'Distance', 'Bathroom', 'Landsize', 'Region_encoded']

def get_estimated_price(region_encoded, landsize, rooms, bathroom, distance):

    x = np.zeros(len(feature_order))
    x[0] = rooms
    x[1] = distance
    x[2] = bathroom
    x[3] = landsize
    x[4] = region_encoded
    print(x)
    pridicted_value = round(__model.predict([x])[0],2)
    print(pridicted_value)
    return np.exp(pridicted_value)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __regionMaping

    with open("./artifacts/label_mappings.json", "r") as f:
        __regionMaping = json.load(f)['Region']

    global __model
    if __model is None:
        with open('./artifacts/melbourne_house_priceing_model.pkl', 'rb') as f:
            model_data = joblib.load(f)
            __model = model_data["model"]
    print("loading saved artifacts...done")

def get_region_mapping():
    return __regionMaping

if __name__ == '__main__':
    load_saved_artifacts()
