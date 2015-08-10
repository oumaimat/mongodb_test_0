__author__ = 'OTurki'

import pymongo


class ConnectionToDatabase :

    database = None

    #penser à créer un pool de connections réutilisables vers la base
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

    # Insérer un enregistrement dans une collection
    def insertObjectInCollection(self, collectionName, object):

        collection =  GenericDAO.connectionToDatabase.getCollection(collectionName)
        insertionResult = collection.insert_one(object)

        return insertionResult

    # Supprimer un enregistrement dans une collection
    def removeOneObjectFromCollection(self,collectionName, objectID ):

        collection =  GenericDAO.connectionToDatabase.getCollection(collectionName)
        removeResult = collection.remove(objectID)

        return removeResult

    # Supprimer un ou plusieurs enregistrements dans une collection
    def removeObjectFromCollection(self,collectionName, objectCriteria):

        collection =  GenericDAO.connectionToDatabase.getCollection(collectionName)
        removeResult = collection.remove(objectCriteria)

        return removeResult

    # Méthode à n'utiliser que dans certains cas par la suite à cause du très grand nombre d'enregistrements
    def getAllRecords(collectionName):

        collection = GenericDAO.connectionToDatabase.getCollection(collectionName)
        recordsList = list(collection.find())

        return recordsList

    # Extraire un enregistrement
    def getOneRecord(collectionName, objectID):

        collection = GenericDAO.connectionToDatabase.getCollection(collectionName)
        foundObject = collection.find_one(objectID)

        return foundObject
