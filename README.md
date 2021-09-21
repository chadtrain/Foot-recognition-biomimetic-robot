# Foot-recognition-biomimetic-robot
Hi! We are UmmJocker. This is our university project. 

Our training code is the same as the code https://github.com/AlexeyAB/darknet

We use the code to build a foot/shoes recognition model 
and combine realtime recognition, ultrasonic detector and motor with python code to control the biomimetic robot.

## Foot recognition model
We have trained a foot recognition model which achieve 1.1 avg loss, 77.76% IoU and 92.4% mAP.

This model can recognize two label: shoes and bare foot. 

To use this model, follow the steps below:

1.Download "yolov4-custom_best.weight" file in this drive(https://drive.google.com/drive/u/1/folders/1yqYuwfXCdLMhQDoRSn6yHAYVS6cgdeSy), 
and add it to "Robot_V3" folder.

2.Run "foot_recognize_model.py", adjust the corresponding path. 

3.Asure that your camara is available, then you can start using it!
(P.S. We're not proffesional in computer, so we cannot promise whether the code is compatible in every personal devices.)

## Robot control code
Before using this, you should install all the following modules, such as pymata, opencv and also the corresponding settings in arduino.
And just download all the file sttached above, then you can use it( But acctually you should have your own robot first.

