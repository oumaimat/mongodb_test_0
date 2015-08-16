__author__ = 'OTurki'

import pymongo


class ConnectionToDatabase :

    database = None

    #penser � cr�er un pool de connections r�utilisables vers la base
    #solution actuelle non envisageable en prod

    def __init__(self):
        self.connectToDatabase()


    def connectToDatabase(self) :
        # Connexion au serveur de Mongo DB
        db_conn=None

        try:
            db_conn=pymongo.MongoClient()
            print("Connected successfully!!!")
            print(db_conn)
        except pymongo.errors.ConnectionFailure :
            print("Could not connect to MongoDB: %s")


        # Connexion a la base du projet
        db = db_conn["project_database"]

        #function result
        ConnectionToDatabase.database = db


    def getCollection(self, collection_name):

        #Connexion a la collection
        collection = ConnectionToDatabase.database[collection_name]

        #function result
        return collection

class GenericDAO :

    connectionToDatabase = ConnectionToDatabase()

    # Ins�rer un enregistrement dans une collection
    def insertObject(self, collectionName, object):

        collection =  GenericDAO.connectionToDatabase.getCollection(collectionName)
        insertionResult = collection.insert_one(object)

        return insertionResult

    # Supprimer un enregistrement dans une collection
    def removeOneObject(self, collectionName, objectID ):

        collection =  GenericDAO.connectionToDatabase.getCollection(collectionName)
        removeResult = collection.remove(objectID)

        return removeResult

    # Supprimer un ou plusieurs enregistrements dans une collection
    def removeObjects(self, collectionName, objectCriteria):

        collection =  GenericDAO.connectionToDatabase.getCollection(collectionName)
        removeResult = collection.remove(objectCriteria)

        return removeResult

    # Mettre � jour un ou plusieurs enregistrements dans une collection
    def updateObjects(self, collectionName, objectCriteria, objectUpdate):

        collection =  GenericDAO.connectionToDatabase.getCollection(collectionName)

        # Mettre le update operator � $set
        addedUpdateOperator = {"$set": objectUpdate}
        updateResult = collection.update_many(objectCriteria, addedUpdateOperator)

        return updateResult

    # M�thode � n'utiliser que dans certains cas par la suite � cause du tr�s grand nombre d'enregistrements
    def getAllObjects(collectionName):

        collection = GenericDAO.connectionToDatabase.getCollection(collectionName)
        recordsList = list(collection.find())

        return recordsList

    # Extraire un enregistrement
    def getOneObject(collectionName, objectCriteria):

        collection = GenericDAO.connectionToDatabase.getCollection(collectionName)

        if(collectionName == "users") :
            foundObject = collection.find_one(objectCriteria, {"userPwd" : False})
        else :
            foundObject = collection.find_one(objectCriteria)

        return foundObject

    # Extraire un ou plusieurs enregistrements
    def getObjects(collectionName, objectCriteria):

        collection = GenericDAO.connectionToDatabase.getCollection(collectionName)

        if(collectionName == "users") :
            foundObjects = list(collection.find(objectCriteria, {"userPwd" : False}))
        else :
            foundObjects = list(collection.find(objectCriteria))

        return foundObjects

