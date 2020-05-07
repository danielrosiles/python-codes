import os, sys
import serial
import time
import _thread

def readSerialOne(Thread):
   ser = serial.Serial('/dev/ttyACM0', 19200, timeout = 0)

   while True:
      line = ser.readline().decode()
      if len(line) > 0:
         print(line)

      time.sleep(0.1)

def readSerialTwo(Thread):
   ser = serial.Serial('/dev/ttyACM1', 19200, timeout = 0)

   while True:
      line = ser.readline().decode()
      if len(line) > 0:
         print(line)

      time.sleep(0.1)

try:
   _thread.start_new_thread( readSerialOne, ("QR-1", ) )
   _thread.start_new_thread( readSerialTwo, ("QR-2", ) )
except:
   print ("Error: unable to start thread")
while 1:
   pass
