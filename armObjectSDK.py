#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:11:43 2018

@author: ehsc1997
"""

'''First you need to install the serial module:
    For Windows: https://www.youtube.com/watch?v=NdS5sCuGAFA
    For Mac: >> sudo pip install pyserial #(using terminal)#
'''

#insert imports here:
import os
import serial
import time

#class definition
class armSDK ():
    def __init__(self): 
        #jointObject1:
            #curPos
            #curSpeed
        #jointObject2:
            #curPos
            #curSpeed
        #jointObject3:
            #curPos
            #curSpeed
        #kinematicModel, function with new values
        pass
    
    def setUp(self):
        pass
    
    def sendData(data):
        #send data (write to serial?)
        #wait for confirmation of receipt
        #timeout error if time exceeds limit
        #end, no return value
    
    def requestData(datatype):
        #send request
        #store data
        #assign received and stored data in sdk properties for kinematic model update
    
    def update():
        #call kinematicModel to reassign property values depending on new requested data.
    
########################## Testing Methods #################################################
        
    def turnOn():
    ### Function using serial communications to turn Arduino led on. Developed with Arduino code ArduinoLEDSerial.
        ar.write('1'.encode()) #Send whatever you want to send to the Arduino's serial. Should be received by Arduino code.

    def turnOff():
    ### Function using serial communication to turn Arduino led off. Developed with Arduino code ArduinoLEDSerial.
        ar.write('0'.encode()) #Send whatever you want to send to the Arduino's serial. Should be received by Arduino code.

    def getVoltage():
    ### Function using serial communication to read state of a potentiometer
        ar.write('2'.encode())
        position = float(ar.readline())
        print(position)

class UI():

class gesture():
        
if __name__ == "__main__":
    arm = armSDK()
    #arm.ledOn() #This is basically an abstraction of a message, later we can start doing things like if gui button click then arm.ledOn()