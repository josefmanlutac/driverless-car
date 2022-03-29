# driverless-car
# Realtime object detection on Raspberry Pi

#### Based on tutorial from PyImageSearch: [https://www.pyimagesearch.com/2017/10/16/raspberry-pi-deep-learning-object-detection-with-opencv/]

## Instructions
1. opencv is needed

#runs both object detection and video recorder
`python3 real_time_object_detection_new.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel & python3 record_video.py`

#runs only object detection
`python3 real_time_object_detection_new.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel`

#runs only video recorder
`python3 record_video.py`

#on GUI window press `q` to quit - stop object detection first and recording second
