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
        pass#Probebly need some variables in here 
    
    def setUp(self):
        pass

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

        
if __name__ == "__main__":
    arm = armSDK()
    #arm.ledOn() #This is basically an abstraction of a message, later we can start doing things like if gui button click then arm.ledOn()