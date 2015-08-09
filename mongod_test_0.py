__author__ = 'OTurki'

from Model.User import  User
from DAO.GenericDAO import GenericDAO

#
# def connectToDatabaseServer() :
#     # Connexion au serveur de Mongo DB
#     db_conn=None
#
#     try:
#         db_conn=pymongo.MongoClient()
#         print("Connected successfully!!!")
#         print(db_conn)
#     except pymongo.errors.ConnectionFailure :
#         print("Could not connect to MongoDB: %s" % e)
#
#     #function result
#     return db_conn
#
# def connectToDatabase(db_conn,database_name) :
#
#     # Connexion a la base du projet
#
#     db = db_conn[database_name]
#
#     #function result
#     return db
#
# def getCollection(db, collection_name) :
#
#     #Connexion a la collection
#
#     collection = db[collection_name]
#
#     #function result
#     return collection
#
# def getAllUsers(users_collection) :
#
#     for user in users_collection.find():
#         print(user)

#for user in users_collection.find() :
#print(user["userPseudo"])


genericDAO = GenericDAO()

collectionName = "users"

# tester la méthode insertObjectInCollection
#
# inserer un user test dans la collection
# userToInsert = User("pseudo test 4","nom test 4", "prénom test 4")
#
# print (genericDAO.insertObjectInCollection(collectionName, userToInsert.parseToDict()))

# tester la méthode getAllRecords
#
for user in GenericDAO.getAllRecords(collectionName):
    print(user)

#Tester les méthodes suppression et getOne

# Données test, à examiner plus tard
# pref1 = {}
# pref1["produit"]="yaourt glacé"
# pref1["prix"] =  11.5
#
# pref2 = {}
# pref2["produit"]="donut"
# pref2["prix"] =  3.25
#
# prefs = []
# prefs.append(pref1)
# prefs.append(pref2)

