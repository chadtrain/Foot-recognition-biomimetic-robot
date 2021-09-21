# Foot-recognition-biomimetic-robot
Hi! We are UmmJocker. This is our university project. 

Our training code is the same as the code https://github.com/AlexeyAB/darknet

We use the code to build a foot/shoes recognition model 
and combine realtime recognition, ultrasonic detector and motor with python code to control the biomimetic robot.

## Foot recognition model
We have trained a foot recognition model which achieve 1.1 avg loss, 77.76%IoU and 92.4%mAP.

This model can recognize two label: shoes and bare foot. 

To use this model, follow the steps below:
1.Download "yolov4-custom_best.waight" file in this drive, and add it to "Robot_V3" folder.
2.Run "Robot_V3.py", adjust the corresponding path. 
