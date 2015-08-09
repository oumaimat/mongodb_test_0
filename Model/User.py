__author__ = 'OTurki'

class User :

    userPseudo = ""
    userNom = ""
    userPrenom = ""

    def __init__(self, userPseudo, userNom, userPrenom):
        self.userPseudo = userPseudo
        self.userNom = userNom
        self.userPrenom = userPrenom


    def parseToDict(self):
        User = {}
        User["userPseudo"] = self.userPseudo
        User["userNom"] = self.userNom
        User["userPrenom"] = self.userPrenom

        #Function return result
        return User