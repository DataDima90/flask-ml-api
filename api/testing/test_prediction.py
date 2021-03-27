# tests/test_prediction.py

from api.endpoints.prediction import prediction_api
from flask import Flask
import pytest
import json

app = Flask(__name__)
app.register_blueprint(prediction_api)


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_predict_single(client):
    response = client.get(
        "/prediction",
        data=json.dumps({
            "pl": 2,
            "sl": 2,
            "pw": 0.5,
            "sw": 3}),
        content_type="application/json")
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) is not None