__author__ = 'OTurki'


class SubmittedChoice :

    _id = ""
    user_id = ""
    choiceCountry = ""

    choiceUploadDate = ""
    item1 = ""
    item2 = ""

    nbItem1 = 0
    nbItem2 = 0
    nbTotal = 0

    nbOriginRequests = 0
    originItem1 = ""
    originItem2 = ""

    catNb = ""
    catName = ""
    catNbValidationDays = 0




    def __init__(self, user_id, choiceCountry, choiceUploadDate, item1, item2
                 , nbItem1, nbItem2, nbTotal, nbOriginRequests, originItem1, originItem2
                 , catNb, catName, catNbValidationDays):

        self.user_id = user_id
        self.choiceCountry = choiceCountry

        self.choiceUploadDate = choiceUploadDate
        self.item1 = item1
        self.item2 = item2

        self.nbItem1 = nbItem1
        self.nbItem2 = nbItem2
        self.nbTotal = nbTotal

        self.nbOriginRequests = nbOriginRequests
        self.originItem1 = originItem1
        self.originItem2 = originItem2

        self.catNb = catNb
        self.catName = catName
        self.catNbValidationDays = catNbValidationDays



    def parseToDict(self):
        subChoice = {}
        #
        # subChoice["user_id"] = self.user_id
        # subChoice["choiceCountry"] = self.choiceCountry
        #
        #
        # subChoice["choiceUploadDate"] = self.choiceUploadDate
        # subChoice["item1"] = self.item1
        # subChoice["item2"] = self.item2
        #
        # subChoice["nbItem1"] = self.nbItem1
        # subChoice["nbItem2"] = self.nbItem2
        # subChoice["nbTotal"] = self.nbTotal
        #
        # subChoice["nbOriginRequests"] = self.nbOriginRequests
        # subChoice["originItem1"] = self.originItem1
        # subChoice["originItem2"] = self.originItem2
        #
        # subChoice["catNb"] = self.catNb
        # subChoice["catName"] = self.catName
        # subChoice["catNbValidationDays"] = self.catNbValidationDays

        #Function return result
        # return subChoice

    def parseToSubChoice(subChoiceDict):

        subChoice = SubmittedChoice(
        #     subChoiceDict["user_id"],
        #     subChoiceDict["choiceCountry"]
        )
        #
        # subChoice._id = subChoiceDict["_id"]
        #
        # #Function return result
        # return subChoice