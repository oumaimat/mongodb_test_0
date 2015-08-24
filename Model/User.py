__author__ = 'OTurki'

class User :

    _id = ""
    userLogin = ""
    userPwd = ""
    userLastName = ""
    userName = ""
    userEmail = ""
    userCountry = ""
    userSubmittedChoices = []

    def __init__(self, userLogin, userPwd, userLastName, userName, userEmail, userCountry):
        self.userLogin = userLogin
        self.userPwd = userPwd
        self.userLastName = userLastName
        self.userName = userName
        self.userEmail = userEmail
        self.userCountry = userCountry


    def parseToDict(self):
        user = {}

        user["userLogin"] = self.userLogin
        user["userPwd"] = self.userPwd
        user["userLastName"] = self.userLastName
        user["userName"] = self.userName
        user["userEmail"] = self.userEmail
        user["userCountry"] = self.userCountry

        #Function return result
        return user

    def parseToUser(userDict):


        user = User(userDict["userLogin"], userDict["userPwd"], userDict["userLastName"], userDict["userName"], userDict["userEmail"], userDict["userCountry"])

        user._id = userDict["_id"]

        #Function return result
        return user