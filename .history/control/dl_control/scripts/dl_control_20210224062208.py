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

        self.ub_cmd_vel  = rospy.Publisher('/cmd_vel', Float64, queue_size = 1)

        self.white_center = None
        self.yellow_center = None

        self.lastError = 0
        self.desired_center = 154
        self.MAX_VEL = 0.12
        rospy.on_shutdown(self.fnShutDown)

    def cbFindWhiteLane(self, center_msg):
        self.white_center = center_msg.data
        print(self.white_center)
    def cbFindYellowLane(self, center_msg):
        self.yellow_center = center_msg.data
        print(self.yellow_center)

    def fnShutDown(self):
        rospy.loginfo("Shutting down. cmd_vel will be 0")

        twist = Twist()
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        self.pub_cmd_vel.publish(twist) 

    def main(self):
        center = (self.white_center+self.yellow_center)/2

        error = center - self.desired_center

        Kp = 0.0025
        Kd = 0.007

        angular_z = Kp * error + Kd * (error - self.lastError)
        self.lastError = error
        twist = Twist()
        twist.linear.x = min(self.MAX_VEL * ((1 - abs(error) / self.desired_center) ** 2.2), 0.2)
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = -max(angular_z, -2.0) if angular_z < 0 else -min(angular_z, 2.0)
        self.pub_cmd_vel.publish(twist)

        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('DL_Control')
    node = DL_Control()
    node.main()