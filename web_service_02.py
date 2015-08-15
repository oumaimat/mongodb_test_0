from pandas.tseries.offsets import DateOffset

__author__ = 'OTurki'

from Model.User import  User
from DAO.GenericDAO import GenericDAO

from flask import Flask, jsonify, request
from bson.objectid import ObjectId
import json
import datetime


class MongoJsonEncoder(json.JSONEncoder):
    def default(self, objectToEncode):
        if isinstance(objectToEncode, (datetime.datetime, datetime.date)):
            return objectToEncode.isoformat()
        elif isinstance(objectToEncode, ObjectId):
            return str(objectToEncode)
        return json.JSONEncoder.default(self, objectToEncode)

app = Flask(__name__)

genericDAO = GenericDAO()

collectionName = "users"

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/servus/users', methods=['GET'])
def get_users():
    usersList = GenericDAO.getAllObjects(collectionName)

    res = json.dumps(usersList, cls=MongoJsonEncoder)

    return res

@app.route('/servus/user', methods=['POST'])
def get_user():

    request_data = request.json

    user = GenericDAO.getObjects(collectionName, request_data)

    res = json.dumps(user, cls=MongoJsonEncoder)

    return res

if __name__ == '__main__':
     app.run()


