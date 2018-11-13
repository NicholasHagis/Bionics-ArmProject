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

#For Ed's computer use the left port, otherwise user appropriate port name
import serial
import time

ar = serial.Serial('/dev/cu.usbmodem14101', 9600) #Arduino's serial port and Baud rate
time.sleep(5);

def turnOn():
### Function using serial communications to turn Arduino led on. Developed with Arduino code ArduinoLEDSerial.
    ar.write('1'.encode()) #Send whatever you want to send to the Arduino's serial. Should be received by Arduino code.

def turnOff():
### Function using serial communication to turn Arduino led off. Developed with Arduino code ArduinoLEDSerial.
    ar.write('0'.encode()) #Send whatever you want to send to the Arduino's serial. Should be received by Arduino code.
    
def getPotPosition():
### Function using serial communication to read state of a potentiometer
    ar.write('2'.encode())
    position = float(ar.readline())
    print(position)
        