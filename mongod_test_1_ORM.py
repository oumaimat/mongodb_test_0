__author__ = 'OTurki'

from mongotor.orm import collection, field
from mongotor.database import Database

import tornado.web
from tornado import gen

# Connection a la base de donnees
Database.connect(['localhost:27017'], 'project_database')

class User(collection.Collection):
    __collection__ = "users"

    _id = field.ObjectIdField()
    userPseudo = field.StringField()
    userNom = field.StringField()
    userPrenom = field.StringField()

class Handler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        user = User()
        user.userPseudo = "pseudo test"
        user.userNom = "nom test"
        user.userPrenom = "prenom test"

        yield gen.Task(user.save)

        # update date
        user.userNom = "nom update"
        yield gen.Task(user.update)

        # find one object
        user_found = yield gen.Task(User.objects.find_one, user._id)

        # find many objects
        new_user = User()
        new_user.name = "new user name"
        new_user.user.active = True
        new_user.created = datetime.now()

        users_actives = yield gen.Task(User.objects.find, {'active': True})

        users_actives[0].active = False
        yield gen.Task(users_actives[0].save)

        # remove object
        yield gen.Task(user_found.remove)