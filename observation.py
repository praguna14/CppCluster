"""class for observation"""

class observation(object):

    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def printData(self):
        print(self.data)
