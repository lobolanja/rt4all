"""Samples's reader."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep
import json, ast, sys
filepath = osPath.dirname(osPath.realpath(__file__))

sysPath.append((filepath + "/../"))
import rticonnextdds_connector as rti


def createTXT(file, data):
    myfile = open(filepath+ "/../../report/"+file, 'a')
    myfile.write(str(data)+",")
    myfile.close()


connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/shovel.xml")
inputDDS = connector.getInput("MySubscriber::MyShovelReader")

for i in range(1, 500):
    inputDDS.take()
    numOfSamples = inputDDS.samples.getLength()
    for j in range(1, numOfSamples+1):
        if inputDDS.infos.isValid(j):
          
            sample = inputDDS.samples.getDictionary(j)
            salida = ast.literal_eval(json.dumps(sample))
            print(salida)

    sleep(2)

sys.exit()




