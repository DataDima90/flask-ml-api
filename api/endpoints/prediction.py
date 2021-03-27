# api/endpoints/prediction.py

from flask import Blueprint, request
import pickle
import json

prediction_api = Blueprint('prediction_api', __name__)

# load our ML model
MODEL = pickle.load(open("api/models/model.pkl", 'rb+'))


@prediction_api.route('/prediction')
def prediction():
    # Get access to sample data stored in request
    sample = [float(x) for x in json.loads(request.data).values()]

    # predict the species
    species = MODEL.predict([sample]).tolist()[0]

    # convert species class into class name
    if species == 0:
        s = "Setosa"
    elif species == 1:
        s = "VersiColor"
    else:
        s = "Virginica"

    return {"prediction": s}
