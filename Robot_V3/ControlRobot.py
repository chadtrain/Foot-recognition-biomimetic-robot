#!/usr/bin/env python
import cv2
import numpy as np
import time
import sys
import signal
#import serial  # 引用pySerial模組
#COM_PORT = 'COM6'    # 指定通訊埠名稱
#BAUD_RATES = 9600    # 設定傳輸速率
#ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

from time import sleep
from PyMata.pymata import PyMata
uno = PyMata('COM6')

def signal_handler(sig, frame): # Maybe it don't work
    print('You pressed Ctrl+C')
    if uno is not None:
        uno.reset()
        uno.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
# control the servo - note that you don't need to set pin mode
time.sleep(2)

d3 = 3  # sonar's TOP pin
d5 = 5  # servo attached to this pin
d6 = 6
d9 = 9  # right side servo (Turn Left)
d10 = 10  # left side servo (Turn Right)
uno.servo_config(d3) # setting the servo in pymata.py
uno.analog_write(d3, 90)
time.sleep(0.1)
uno.servo_config(d5) # setting the servo in pymata.py
uno.analog_write(d5, 90) # stop the servo
time.sleep(0.1)
uno.servo_config(d6) # setting the servo in pymata.py
uno.analog_write(d6, 90)
time.sleep(0.1)
uno.servo_config(d9) # setting the servo in pymata.py
uno.analog_write(d9, 90)
time.sleep(0.1)
uno.servo_config(d10) # setting the servo in pymata.py
uno.analog_write(d10, 90)
time.sleep(0.1)
def Go_Forward():
    uno.analog_write(d5, 0) # 
    time.sleep(1.6) # middle
    uno.analog_write(d5, 90)
    time.sleep(1)
    uno.analog_write(d6, 0) # 
    time.sleep(1.6) # tail
    uno.analog_write(d6, 90)
    time.sleep(1)

    uno.analog_write(d6, 180) 
    time.sleep(1.3)
    uno.analog_write(d6, 90)
    time.sleep(1)      
    uno.analog_write(d5, 180)
    time.sleep(1.4)
    uno.analog_write(d5, 90)
    time.sleep(1)


def Go_Left():
    uno.analog_write(d3, 105) # 90 degree CCW
    time.sleep(0.5)
    uno.analog_write(d3, 90)
    time.sleep(1)
 
    uno.analog_write(d9, 0) # 
    time.sleep(1.2) # right side
    uno.analog_write(d9, 90)
    time.sleep(1)
 
    uno.analog_write(d5, 0) # three circle
    time.sleep(1.6) # middle
    uno.analog_write(d5, 90)
    time.sleep(1)
  
    uno.analog_write(d6, 0) # three point five circle
    time.sleep(1.6) # tail
    uno.analog_write(d6, 90)
    time.sleep(1)
  
    uno.analog_write(d6, 180) 
    time.sleep(1.3)
    uno.analog_write(d6, 90)
    time.sleep(1)   
   
    uno.analog_write(d5, 180)
    time.sleep(1.4)
    uno.analog_write(d5, 90)
    time.sleep(1)


    uno.analog_write(d9, 180) # 
    time.sleep(0.9) # right side
    uno.analog_write(d9, 90)
    time.sleep(1)
 

    uno.analog_write(d3, 73) # 90 degree CW
    time.sleep(0.3) # tail
    uno.analog_write(d3, 90)
    time.sleep(1)



def Go_Right():
    uno.analog_write(d3, 73) # 90 degree CW
    time.sleep(0.4) # tail
    uno.analog_write(d3, 90)
    time.sleep(1)

    uno.analog_write(d10, 0) # 
    time.sleep(1.5) # right side
    uno.analog_write(d10, 90)
    time.sleep(1)

    uno.analog_write(d5, 0) # three circle

    time.sleep(1.6) # middle
    uno.analog_write(d5, 90)
    time.sleep(1)
    uno.analog_write(d6, 0) # three point five circle
    time.sleep(1.6) # tail
    uno.analog_write(d6, 90)
    time.sleep(1)
    uno.analog_write(d6, 180) 
    time.sleep(1.3)
    uno.analog_write(d6, 90)
    time.sleep(1)      
    uno.analog_write(d5, 180)
    time.sleep(1.4)
    uno.analog_write(d5, 90)
    time.sleep(1)

    uno.analog_write(d10, 180) # 
    time.sleep(0.9) # right side
    uno.analog_write(d10, 90)
    time.sleep(1)

    uno.analog_write(d3, 105) # 90 degree CCW
    time.sleep(0.4)
    uno.analog_write(d3, 90)
    time.sleep(1)

open = 1
try:

    while (open == 1):
       # Go_Forward()
    #Go_Left()
        Go_Right()
        open = 0

except KeyboardInterrupt:
    uno.close()




