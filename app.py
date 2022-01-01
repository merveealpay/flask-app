from flask import Flask, jsonify
import requests
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.routing import ValidationError

app = Flask(__name__)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:merve123@localhost:5432/rates_api"
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
cache = Cache(app)
api = Api(app)



class ExchangeRates(Resource):
    # @cache.cached(timeout=30, query_string=True)
    def get(self):
        API_URL = "https://openexchangerates.org/api/latest.json?app_id=1c826c16fd724747a9e0b01e9c35c103%27"
        r = requests.get(f"{API_URL}")
        all_rates = r.json()["rates"]
        try_eur_rates = {"base": "TRY", "USD": all_rates["TRY"]}
        return try_eur_rates


api.add_resource(ExchangeRates, '/rates')


# Global Error Handling
@app.errorhandler(Exception)
def handler_global_error(error):
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return jsonify({"error": str(error)}), code


app.run(port=5000, host="0.0.0.0", debug=True)
