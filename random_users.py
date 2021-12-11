import requests
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class RandomUser(Resource):
    def get(self):
        response = requests.get('https://randomuser.me/api/')
        data = response.json()
        email = data["results"][0]["email"]
        return email


api.add_resource(RandomUser, '/users')

app.run(port=5000, debug=True)
