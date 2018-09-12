#!/usr/bin/python3.5


import pandas as pd
import numpy as np
import sys

class RunFileParser:
    def __init__(self, fileName=None):
        self._filePath = '../macros/'
        self._fileName = fileName

        if fileName is None:
            self._fileName = self.callForFilename()

        self.energy = self.getAttributeFromFile("/gps/energy")
        self.numberOfParticles = self.getAttributeFromFile("/run/beamOn")

    def callForFilename(self):
        try:
            fileName = sys.argv[1]
        except IndexError:
            print("Enter filename to parse: ")
            fileName = input()
            pass
        return fileName

    def getAttributeFromFile(self, attr):
        with open(self._filePath+self._fileName) as file:
            file_contents = file.read()

            index = file_contents.find(attr)
            return file_contents[index+12:index+20]

    def getEnergy(self):
        return self.energy
    def getNumParticles(self):
        return self.numberOfParticles
