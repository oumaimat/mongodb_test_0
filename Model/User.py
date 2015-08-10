__author__ = 'OTurki'

class User :

    _id = ""
    userPseudo = ""
    userNom = ""
    userPrenom = ""

    def __init__(self, userPseudo, userNom, userPrenom):
        self.userPseudo = userPseudo
        self.userNom = userNom
        self.userPrenom = userPrenom


    def parseToDict(self):
        user = {}

        user["userPseudo"] = self.userPseudo
        user["userNom"] = self.userNom
        user["userPrenom"] = self.userPrenom

        #Function return result
        return user

    def parseToUser(userDict):


        user = User(userDict["userPseudo"], userDict["userNom"], userDict["userPrenom"])

        user._id = userDict["_id"]

        #Function return result
        return user