# Contact Class file

class Contact:
    def __init__(self, fn, ln, pn):
        self.__firstName = fn
        self.__lastName = ln
        self.__phoneNum = pn

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getPhoneNum(self):
        return self.__phoneNum

    def setFirstName(self, fn):
        self.__firstName = fn

    def setLastName(self, ln):
        self.__lastName = ln

    def setPhoneNum(self, pn):
        self.__phoneNum = pn

    def __str__(self):
        return "Name: " + self.__firstName + " " + self.__lastName + "\nPhone Number: " + self.__phoneNum

