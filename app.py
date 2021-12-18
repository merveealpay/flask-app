from flask import Flask, request, jsonify
import requests
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ExchangeRates(Resource):
    def get(self):
        API_URL = "https://openexchangerates.org/api/latest.json?app_id=1c826c16fd724747a9e0b01e9c35c103%27"
        r = requests.get(f"{API_URL}")
        data = jsonify(r.json())
        return data


api.add_resource(ExchangeRates, '/rates')

app.run(port=5000, debug=True)