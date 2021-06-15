import flask
import requests
from flask import request, jsonify
from flask_cors import cross_origin

from sample_objects import *
from input_object import *
from output_object import *
from check_template import *


def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    @cross_origin()
    def home():
        input_object = pupin_input()
        res = validate_input(input_object)
        return jsonify(res)

    @app.route('/simulator', methods=['POST'])
    @cross_origin()
    def simulator():
        content = request.json
        res = validate_input(content)
        if res['valid']:
            val = pupin_output()
            val['valid'] = True
            val['description'] = 'Ok'
            return jsonify(val)
        else:
            return jsonify(res)

    @app.route('/output', methods=['GET'])
    @cross_origin()
    def test_output():
        input_object = pupin_output()
        res = validate_output(input_object)
        return jsonify(res)

    def validate_output(output_object):
        template = template_output()
        return check_field(output_object, template, "")

    def validate_input(input_object):
        template = template_input()
        return check_field(input_object, template, "")

    @app.route('/elevation', methods=['GET'])
    @cross_origin(origin='localhost',allow_headers=['Content-Type','Authorization','Access-Control-Allow-Origin','Accept'])
    def get_elevation():
        url = "https://api.opentopodata.org/v1/eudem25m"
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        payload = {'locations': str(lat) + ',' + str(lon)}
        return str(requests.get(url, params=payload, headers={'Content-Type': 'application/json','Access-Control-Allow-Origin': '*', 'Accept':'application/json'}).content)

    @app.route('/countryCode', methods=['GET'])
    @cross_origin(origin='localhost',allow_headers=['Content-Type','Authorization','Access-Control-Allow-Origin'])
    def get_country_code():
        url = "http://api.timezonedb.com/v2.1/get-time-zone?key=4LKS6TLZTRJW&format=json&by=position"
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        payload = {'lat': lat , 'lng' : lon}
        r = requests.get(url, params=payload, headers={'Access-Control-Allow-Origin': '*', "Content-Type": "application/json"})
        print(r.url)
        return str(requests.get(url, params=payload, headers={'Access-Control-Allow-Origin': '*'}).content)
    return app




