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
        elif isinstance(objectToEncode, bytes) :
            return str(objectToEncode)
        return json.JSONEncoder.default(self, objectToEncode)

app = Flask(__name__)

genericDAO = GenericDAO()



@app.route('/')
def api_root():
    return 'Welcome'

# Recuperer la liste de tous les utilisateurs
@app.route('/servus/get/users', methods=['GET'])
def get_users():
    collectionName = "users"

    usersList = GenericDAO.getAllObjects(collectionName)

    res = json.dumps(usersList, cls=MongoJsonEncoder)

    return res

# Recuperer un ou plusieurs utilisateur avec un ensemble de criteres
@app.route('/servus/get/user', methods=['POST'])
def get_user():

    request_data = request.json

    collectionName = "users"

    user = GenericDAO.getObjects(collectionName, request_data)

    res = json.dumps(user, cls=MongoJsonEncoder)

    return res

# Proceder a l'authentification de l'utilisateur
@app.route('/servus/authentification/user', methods=['POST'])
def get_authentification_user():

    request_data = request.json

    collectionName = "users"

    # Le hashage se fera a une etape ulterieure
    user = GenericDAO.getOneObject(collectionName, request_data)

    res = json.dumps(user, cls=MongoJsonEncoder)

    return res


# Verifier l'existence du pseudo d'un utilisateur
@app.route('/servus/register/verif_login', methods=['POST'])
def verif_login_existence():

    request_data = request.json

    collectionName = "users"

    user = GenericDAO.getOneObject(collectionName, request_data)

    result = {}
    # exist prend True si login existant et False sinon
    if(user == None) :
        result["login_exists"] = False
    else :
        result["login_exists"] = True

    res = json.dumps(result, cls=MongoJsonEncoder)

    return res

# Enregistrer un utilisateur
# Penser a refaire les tests cote client (longueur du pwd, champs non vides,...)
@app.route('/servus/register/user', methods=['POST'])
def register_user():

    request_data = request.json

    #   La verification des champs doit se faire a ce niveau, renvoyer une erreur si un test echoue

    collectionName = "users"

    insertionRes = genericDAO.insertObject(collectionName, request_data)

    result = {}
    # exist prend True si insertion OK et False sinon
    if(insertionRes == None) :
        result["insertion_OK"] = False
    else :
        result["insertion_OK"] = True

    res = json.dumps(result, cls=MongoJsonEncoder)

    return res


# Main application
if __name__ == '__main__':
     app.run()


