# api/app.py

from flask import Flask
from api.endpoints.prediction import prediction_api

# Create an instance of the Flask class with the default __name__
app = Flask(__name__)

# Register our endpoint
app.register_blueprint(prediction_api)

if __name__ == '__main__':
    # listen on port 8080
    app.run(host="0.0.0.0", port=8080, debug=True)
