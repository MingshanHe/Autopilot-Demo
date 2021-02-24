#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import numpy as np
from std_msgs.msg import UInt8, Float64
from geometry_msgs.msg import Twist
import time
# from vision_msgs.msg import Center

class DL_Control():

    def __init__(self):
        self.sub_white_lane_center    = rospy.Subscriber('/control/white_lane', Float64, self.cbFindWhiteLane, queue_size = 1)
        self.sub_yellow_lane_center   = rospy.Subscriber('/control/yellow_lane', Float64, self.cbFindYellowLane, queue_size = 1)
        self.pub_image_detect   = rospy.Publisher('/detect/lane', Image, queue_size = 1)

        self.pub_angle_control  = rospy.Publisher('/cmd_vel', Float64, queue_size = 1)

        self.white_center = None
        self.yellow_center = None
    def cbFindWhiteLane(self, center_msg):
        self.white_center = center_msg.data
        print(self.white_center)
    def cbFindYellowLane(self, center_msg):
        self.yellow_center = center_msg.data
        print(self.yellow_center)

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('DL_Control')
    node = DL_Control()
    node.main()