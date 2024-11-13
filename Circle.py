# We create the Circle class above the main function, and then
# create a Circle object within the main function

import math

class Circle:
    def __init__(self, rad):
        self.setRadius(rad)

    def getRadius(self):
        return self.__radius

    def setRadius(self, rad):
        if rad < 0:
            rad = 1
        self.__radius = rad

    def getDiameter(self):
        return self.__radius * 2

    def getCircumference(self):
        return 2 * math.pi * self.__radius

    def getArea(self):
        return math.pi * (self.__radius * self.__radius)


def main():
    c = Circle(2)
    print("Radius:", c.getRadius())
    print("Diameter:", c.getDiameter())
    print("Circumference:", c.getCircumference())
    print("Area", c.getArea(), "uom squared") # unit of measurement


if "__main__":
    main()
