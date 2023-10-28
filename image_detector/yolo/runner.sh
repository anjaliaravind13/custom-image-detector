#!/bin/bash

cd yolo/darknet
./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights tmp/image.jpg > output.txt