"""class for observation"""
import pprint
class observation(object):
    data = []
    def __init__(self, data):
        self.data = data

    def printData(self):
        print(self.data)