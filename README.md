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

------

**Command:**

```bash
# Training the model
$ python3 object_detection/model_main_tf2.py \
--pipeline_config_path="/home/hemingshan/auto_ws/src/vision/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/pipeline.config"\
--model_dir="/home/hemingshan/auto_ws/src/vision/training"\
--alsologtostderr\
$ python3 object_detection/export_inference_graph.py\
--input_type image_tensor \
--pipeline_config_path="/home/hemingshan/auto_ws/src/vision/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/pipeline.config" \
--trained_checkpoint_prefix="/home/hemingshan/auto_ws/src/vision/training/checkpoint.ckpt" \
--output_directory="/home/hemingshan/model"\
```

```bash
# Run the file
$ roslaunch turtlebot3_gazebo turtlebot3_autorace.launch
$ rosrun tensorflow_object_detector detect_ros.py 
$ rqt_image_view
```

------

### The model training progress visualized by tensorboard:

![](Pictures/loss.gif)

------

### The result in the simulation:

![](Pictures/object_detector.gif)

------

## Lane Detector

  The pavement detection module is mainly to enable the car to follow the traffic rules to operate within the range of the road. There are two methods for comparison in this module. The first is to use opencv's image processing and PID control method to complete the task of the module, but through the following figure, it can be found that this method will cause the existence of other routes that do not continue to move according to the current path after identifying other routes. Happening. In order to improve this method, adjust the position of the camera and aim it at the ground instead of facing forward as in the previous method, which shows that the position of the camera is very important.

------

**Command:**

```bash
$ roslaunch turtlebot3_gazebo turtlebot3_auto.launch
$ rosrun tensorflow_object_detector detect_lane.py 
```

------

### The result used the first method:

![](Pictures/lane_detector.gif)

------

### The result used the second method which have a better performance:

![](Pictures/lane_detector_enhanced.gif)

## Obstacle Avoidance

  In the obstacle avoidance algorithm, the principle of lidar ranging is simply used. After the obstacle is identified, the specific location is located, and finally the obstacle avoidance route is predicted through a simple A* algorithm. Here, Git mainly uses the following [innovative ideas](https://github.com/zacdeng/Obstacle-avoidance-for-smartcar-with-monocular-vision-.git) of my classmates

  The result in the simulation:

![](Pictures/obstacle_avoidance.gif)