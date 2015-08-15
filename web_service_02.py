__author__ = 'OTurki'

from Model.User import  User
from DAO.GenericDAO import GenericDAO

from flask import Flask, jsonify
from bson.objectid import ObjectId
import json
import datetime


app = Flask(__name__)

genericDAO = GenericDAO()

collectionName = "users"

usersList1111 = [
{ "userPseudo" : "user1", "userNom" : "nom1", "userPrenom" : "prenom1" },
{ "userPseudo" : "user2", "userNom" : "nom2", "userPrenom" : "prenom2" },
{  "userPseudo" : "pseudo test", "userNom" : "nom test", "userPrenom" : "prenom test" },
{ "userPseudo" : "pseudo test 1","userPrenom" : "prenom test 1", "userNom" : "nom test 1" }
]

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/servus/users', methods=['GET'])
def get_tasks():
    usersList = GenericDAO.getAllObjects(collectionName)

    res = json.dump(usersList1111, default=MongoJsonEncoder)

    return res
    #return jsonify({'users': usersList1111})

if __name__ == '__main__':
    app.run()


class MongoJsonEncoder(json.JSONEncoder):
    def default(self, objectToEncode):
        if isinstance(objectToEncode, (datetime.datetime, datetime.date)):
            return objectToEncode.isoformat()
        elif isinstance(objectToEncode, ObjectId):
            return str(objectToEncode)
        return json.JSONEncoder.default(self, objectToEncode)