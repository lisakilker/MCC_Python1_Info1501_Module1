#Class file
class Rectangle:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width

    #Gets length
    def get_length(self):
        return self._length

    #Sets length
    def set_length(self, length):
        self._length = length

    #Gets width
    def get_width(self):
        return self._width

    #Sets width
    def set_width(self, width):
        self._width = width

    #Gets area
    def get_area(self):
        return self._length * self._width
