#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import numpy as np
from std_msgs.msg import UInt8, Float64
from geometry_msgs.msg import Twist
import time
# from vision_msgs.msg import Center

class DetectLane():

    def __init__(self):
        self.sub_image_original = rospy.Subscriber('/camera/image', Image, self.cbFindLane, queue_size = 1)
        self.pub_image_detect   = rospy.Publisher('/detect/lane', Image, queue_size = 1)

        self.pub_angle_control  = rospy.Publisher('/cmd_vel', Float64, queue_size = 1)

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('detect_lane')
    node = DetectLane()
    node.main()