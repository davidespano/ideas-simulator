import pytest
from sample_objects import *
from flask import request, jsonify

from api import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.mark.usefixtures('client_class')
class TestSuite:

    def test_connection(self):
        assert self.client.get("http://127.0.0.1:5000/").status_code == 200

    def test_post(self):
        input_object = pupin_input()
        response = self.client.post(
            "/simulator",
            json=jsonify(input_object).get_json(),
            headers={"Content-Type": "application/json"},
        )

        assert response.status_code == 200;

        output_object = response.json
        print(response.json)
        assert output_object['description'] == 'Ok'

    def test_elevation(self):
        payload = {"lat": 41.161758, "lon": -8.583933}
        response = self.client.get(
            "/elevation",
            json=jsonify(payload).get_json(),
            headers={"Content-Type": "application/json"},
        )

        assert response.status_code == 200
        assert response.json["results"]["elevation"] == 117
