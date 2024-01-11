#!/usr/bin/env python
import cv2
import numpy as np
import time
import sys
import signal
from PyMata.pymata import PyMata
from time import sleep
import imageio
import urllib.request
uno = PyMata('COM6')
net = cv2.dnn.readNet('yolov4-custom_best.weights','yolov4-custom.cfg')
classes = []
with open('MyObject.names','r') as f:
    classes = f.read().splitlines()
# print(classes)
count=0
123

def GIF():
#    url = "https://media.giphy.com/media/kiOGNdQMj04SI/giphy.gif"
    fname = "naruto.gif"

    ## Read the gif from the web, save to the disk
    '''imdata = urllib.request.urlopen(url).read()
    imbytes = bytearray(imdata)
    open(fname,"wb+").write(imdata)'''

    ## Read the gif from disk to `RGB`s using `imageio.miread` 
    gif = imageio.mimread(fname)
    nums = len(gif)
    #print("Total {} frames in the gif!".format(nums))

    # convert form RGB to BGR 
    imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]
    ## Display the gif
    i = 0
    cap.release()
    while True:
        cv2.imshow("gif", imgs[i])
        if cv2.waitKey(100)&0xFF == 100:
            break
        i = (i+1)%nums

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    global count
    count=count+1
    if (uno is not None) and (count==1):
        uno.digital_write(d8, 0)
        uno.digital_write(d7, 0)

#        uno.close()
#        sys.exit(0)
        GIF()
    else:
        uno.reset()
        uno.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
time.sleep(0.5)

def Go_Left():
    print("Left = %d, Right = %d" %(left, right))
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
    time.sleep(1.4)
    uno.analog_write(d6, 90)
    time.sleep(1)      
    uno.analog_write(d5, 180)
    time.sleep(1.3)
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
    print("Left = %d, Right = %d" %(left, right))
    uno.analog_write(d3, 73) # 90 degree CW
    time.sleep(0.4) # tail
    uno.analog_write(d3, 90)
    time.sleep(1)

    uno.analog_write(d10, 0) # 
    time.sleep(1.4) # left side
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


d3 = 3  # sonar's TOP pin
d5 = 5  # servo attached to this pin
d6 = 6
d7 = 7  # 7->red  8->green
d8 = 8
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
uno.set_pin_mode(d7, PyMata.OUTPUT, PyMata.DIGITAL)
time.sleep(0.1)
uno.set_pin_mode(d8, PyMata.OUTPUT, PyMata.DIGITAL)
time.sleep(0.1)
# Configure the trigger and echo pins
uno.sonar_config(12, 11) # set trigger/echo pin
time.sleep(0.5)
left = 0 # initialize left & right
right = 0
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    height, width, _ = img.shape # 前兩個維度是圖片的高度與寬度
    # 第三個維度則是圖片的 channel,彩色=3
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB = True, crop = False)
    # Normalize the pixel by value 255
    # conver BGR to RGB
    '''
    for b in blob:
        for n, img_blob in enumerate(b):
            cv2.imshow(str(n), img_blob)
    '''
    net.setInput(blob) # set the input from the blob into the network
    ouput_layers_names = net.getUnconnectedOutLayersNames() # To get the output layers names
    layerOutputs = net.forward(ouput_layers_names) # passing names to forward function
    # run the forward pass and obtain their output layer
    boxes = []
    confidences = []
    class_ids = []
    for output in layerOutputs: # extract all the information
        for detection in output: # extract information from each of the output
            scores = detection[5:]  # store all the acting classes prediction
            class_id = np.argmax(scores)  # find out the location contains the higher scores
            confidence = scores[class_id]  # class_ids?
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)
                # the value in detection is normalized
                # get the position for the upper left corner
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                # bounding boxes information
                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)
                
                if (center_x < (0.3*width)):  # 0.3 / 0.4 / 0.3
                    left = 1
                    right = 0
                    print('left')
                    #time.sleep(0.3)
                elif (center_x > (0.7*width)):
                    left = 0
                    right = 1
                    print('right')
                    #time.sleep(0.3)
                else:
                    left = 0
                    right = 0
                    print('forward')
                    #time.sleep(0.3)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4) # ??
    font = cv2.FONT_HERSHEY_PLAIN # choose font
    colors = np.random.uniform(0, 255, size=(len(boxes), 3)) # 3channels

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255, 255, 255), 2)
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL) # 讓視窗可以自由縮放大小
    cv2.imshow('Image', img)
    key = cv2.waitKey(1)  # 用來等待與讀取使用者按下的按鍵，而其參數是等待時間（毫秒）
    if key==27:
        break

    data = uno.get_sonar_data()
    print(str(data[12][1]) + ' cm')
    time.sleep(1)
    sonar_d = float(data[12][1])
    uno.digital_write(d8, 1)
    if ((float(confidence) > 0.8) and (sonar_d > 30.0)):
        uno.digital_write(d8, 0)
        open = 1
        try:
            while (open == 1):
                if (left == 1):
                    uno.digital_write(d7, 1)
                    Go_Left()
                    uno.digital_write(d7, 0)
                elif(right == 1):
                    uno.digital_write(d7, 1)
                    Go_Right()
                    uno.digital_write(d7, 0)
                else:
                    uno.digital_write(d7, 1)
                    Go_Forward()
                    uno.digital_write(d7, 0)
                uno.digital_write(d8, 1)
                open = 0
        except KeyboardInterrupt:
            uno.close()

cap.release()
cv2.destroyAllWindows # 關閉所有 OpenCV 的視窗


