#!/usr/bin/env python
import cv2
import numpy as np
import time
import sys
import signal
from time import sleep
import urllib.request
net = cv2.dnn.readNet("C:/Users/wenchih/Desktop/Robot_V3/yolov4-custom_best.weights","C:/Users/wenchih/Desktop/Robot_V3/yolov3.cfg")
classes = []
with open('MyObject.names','r') as f:
    classes = f.read().splitlines()
# print(classes)
count=0


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
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL) # windows can adjust the size automatically
    cv2.imshow('Image', img)
    key = cv2.waitKey(1)  # Wait for user's instruct, the parameter is the time to wait(minisecond)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows #  shut down all the windows of OpenCV