__author__ = 'OTurki'


class Category :

    _id = ""
    catNb = ""
    catName = ""
    catNbValidationDays = 0


    def __init__(self, catNb, catName, catNbValidationDays):
        self.catNb = catNb
        self.catName = catName
        self.catNbValidationDays = catNbValidationDays


    def parseToDict(self):
        category = {}

        category["catNb"] = self.catNb
        category["catName"] = self.catName
        category["catNbValidationDays"] = self.catNbValidationDays

        #Function return result
        return category

    def parseToCategory(catDict):


        category = Category(catDict["catNb"], catDict["catName"], catDict["catNbValidationDays"])

        category._id = catDict["_id"]

        #Function return result
        return category