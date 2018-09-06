#!/usr/bin/python3.5


import pandas as pd
import numpy as np

filePath = '../macros/'
fileName = 'run_30theta_60phi.mac'

with open(filePath+fileName) as file:
    file_contents = file.read()

    energy_index = file_contents.find('/gps/energy')
    energy = file_contents[energy_index+12:energy_index+20]
    #print(energy)

    run_index = file_contents.find('/run/beamOn')
    runNumber = file_contents[run_index+12:run_index+20]
    print("E = " + energy + "\nParticles = " + str(runNumber))
    #print(file_contents)
