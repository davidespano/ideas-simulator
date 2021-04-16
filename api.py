import flask
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

    return app



