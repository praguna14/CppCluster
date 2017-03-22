"""Util file for all the utility funciton"""
from pathlib import Path
import json

def readFile(path):
    """checks the validity of file given in path and then reads data given in file"""
    fileToRead = Path(path)
    if fileToRead.is_file():
        with open(path, 'r')  as fileToRead:
            data = json.load(fileToRead)
        return data
    else:
        print("The path given: %s is not a valid path to a file.")
        return -1