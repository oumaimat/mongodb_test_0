__author__ = 'OTurki'


class MadeChoice :

    _id = ""
    user_id = ""

    submittedChoice_id = ""
    choice_date = ""
    chosenItem = ""

    showFinalChoice = False
    showOriginItems = False


    def __init__(self, catName, catNbValidationDays):
        self.catName = catName


    def parseToDict(self):
        category = {}

        category["catName"] = self.catName

        #Function return result
        return category

    def parseToCategory(catDict):


        category = Category(catDict["catName"], catDict["catNbValidationDays"])

        category._id = catDict["_id"]

        #Function return result
        return category