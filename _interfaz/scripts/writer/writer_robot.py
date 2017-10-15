"""Samples's writer."""

from sys import path as sysPath
from os import path as osPath
from time import sleep
from random import randint
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../")
import rticonnextdds_connector as rti
import socket
import fcntl
import struct
from random import randint



connector = rti.Connector("MyParticipantLibrary::Infinity",
                          filepath + "/../XML/robot.xml")
outputDDS = connector.getOutput("MyPublisher::MyRobotWriter")
equipo = socket.gethostname()
print equipo

for i in range(1, 500):
    outputDDS.instance.setNumber("cam", 1)
<<<<<<< HEAD
    outputDDS.instance.setNumber("temperature", randint(1, 50))
=======
    outputDDS.instance.setNumber("temperature", randint(1,50))
>>>>>>> 3c499ee41e3b676d4bbfe62fc3094d9b3ecf5566
    outputDDS.instance.setNumber("humidity", i)
    outputDDS.instance.setNumber("robot_id", 0)
    outputDDS.instance.setNumber("servo_angle_position", 34)
    outputDDS.write()
    sleep(1)

sys.exit()