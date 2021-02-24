# AutoPilot Demo 

> This is the final project in the 2021 Winter Camp of Cambridge University and I am following the Prof. Thomas. 
>
> Author: Beal.MS(河明山)
>
> Date: 2021/2/25

<img src="https://github.com/ROBOTIS-GIT/emanual/blob/master/assets/images/platform/turtlebot3/logo_turtlebot3.png" width="300">

## ROS Packages for AutoPilot(Turtlebot3) Demo ![GitHub watchers](https://img.shields.io/github/watchers/MingshanHe/Autopilot-Demo?label=Watch&style=social)

|                           Version                            |                           License                            |                             Size                             |                            Noetic                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| ![GitHub release (latest by date)](https://img.shields.io/github/v/release/MingshanHe/Autopilot-Demo) | ![Github](https://img.shields.io/github/license/MingshanHe/Autopilot-Demo?style=flat-square) | ![GitHub repo size](https://img.shields.io/github/repo-size/MingshanHe/Autopilot-Demo) | ![Build Status](https://travis-ci.com/ROBOTIS-GIT/turtlebot3_simulations.svg?branch=develop) |

------

## Run Environment

* Operating System: Ubuntu 20.04<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/ubuntu/ubuntu.png" alt="ubuntu"></code>
* Tensorflow: 2.4.1<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/tensorflow/tensorflow.png" alt="tensorflow"></code>
* Cuda: 11.2.0 <code><img height="20" src="Pictures/cuda.png" alt="cuda"></code>

* Python: 3.8.5 <code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Python"></code>
* Robot Operate System: Noetic<code><img height="20" src="Pictures/ros.jpeg" alt="ros"></code>

------

## Object Detector

  This module consists of training model and application model. The part of the training model is mainly supported by [Tensorflow Api](https://github.com/tensorflow/models). The preliminary work is the calibration and processing of the data set, and then the model training is completed according to the target detection training step in [Tensorflow Api](https://github.com/tensorflow/models). The part of the application model is mainly provided by ROS exactly tensorflow object detection which is in the vision folder. The model prediction is performed by calling the camera data, and finally the target detection result is output to the image.