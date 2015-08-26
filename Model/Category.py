__author__ = 'OTurki'


class Category :

    _id = ""
    catName = ""
    catNbValidationDays = 0


    def __init__(self, catName, catNbValidationDays):
        self.catName = catName
        self.catNbValidationDays = catNbValidationDays


    def parseToDict(self):
        category = {}

        category["catName"] = self.catName
        category["catNbValidationDays"] = self.catNbValidationDays

        #Function return result
        return category

    def parseToCategory(catDict):


        category = Category(catDict["catName"], catDict["catNbValidationDays"])

        category._id = catDict["_id"]

        #Function return result
        return category