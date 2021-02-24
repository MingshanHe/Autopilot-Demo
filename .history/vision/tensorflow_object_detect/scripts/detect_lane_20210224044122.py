#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import UInt8, Float64, Float64[]
from sensor_msgs.msg import Image, CompressedImage
import time

class DetectLane():

    def __init__(self):
        self.sub_image_original = rospy.Subscriber('/camera/image', Image, self.cbFindLane, queue_size = 1)
        self.pub_image_detect   = rospy.Publisher('/detect/lane', Image, queue_size = 1)

        self.pub_center_white_lane  = rospy.Publisher('/control/white_lane', Float64[], queue_size = 1)
        self.pub_center_yellow_lane = rospy.Publisher('/control/yellow_lane', Float64[], queue_size = 1)

        self.cvBridge = CvBridge()

        self.counter = 1

        self.hue_white_l = 0
        self.hue_white_h = 179
        self.saturation_white_l = 0
        self.saturation_white_h = 30
        self.lightness_white_l  = 221
        self.lightness_white_h  = 255

        self.hue_yellow_l = 26
        self.hue_yellow_h = 34
        self.saturation_yellow_l = 43
        self.saturation_yellow_h = 255
        self.lightness_yellow_l  = 46
        self.lightness_yellow_h  = 255

    def cbFindLane(self, image_msg):
        
        # Change the frame rate by yourself. Now, it is set to 1/3 (10fps). 
        # Unappropriate value of frame rate may cause huge delay on entire recognition process.
        # This is up to your computer's operating power.
        if self.counter % 3 != 0:
            self.counter += 1
            return
        else:
            self.counter = 1

        cv_image = self.cvBridge.imgmsg_to_cv2(image_msg, "bgr8")
        # find White and Yellow Lanes
        self.maskLane(cv_image)
        # yellow_fraction, cv_yellow_lane = self.maskYellowLane(cv_image)
    
    def maskLane(self,image):
        # convert image to hsv
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # param of irange hsv(white & yellow)
        Hue_white_h = self.hue_white_l
        Hue_white_l = self.hue_white_h
        Saturation_white_h = self.saturation_white_l
        Saturation_white_l = self.saturation_white_h
        Lightness_white_h = self.lightness_white_h
        Lightness_white_l = self.lightness_white_l
        
        Hue_yellow_h = self.hue_yellow_l
        Hue_yellow_l = self.hue_yellow_h
        Saturation_yellow_h = self.saturation_yellow_l
        Saturation_yellow_l = self.saturation_yellow_h
        Lightness_yellow_h = self.lightness_yellow_h
        Lightness_yellow_l = self.lightness_yellow_l
        # define range of white color in HSV
        lower_white = np.array([Hue_white_h, Saturation_white_h, Lightness_white_l])
        upper_white = np.array([Hue_white_l, Saturation_white_l, Lightness_white_h])
        
        lower_yellow = np.array([Hue_yellow_h, Saturation_yellow_h, Lightness_yellow_l])
        upper_yellow = np.array([Hue_yellow_l, Saturation_yellow_l, Lightness_yellow_h])
        # Threshold the HSV image to get only white colors
        mask_white = cv2.inRange(hsv, lower_white, upper_white)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        kernel = np.ones((5,5))
        erosion_white = cv2.erode(mask_white,kernel)
        erosion_yellow = cv2.erode(mask_yellow,kernel)
        Gaussian_white = cv2.GaussianBlur(erosion_white, (5,5),0)
        Gaussian_yellow = cv2.GaussianBlur(erosion_yellow, (5,5),0)
        # findContours of image
        contours_white, hierarchy_white = cv2.findContours(Gaussian_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours_yellow, hierarchy_yellow = cv2.findContours(Gaussian_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # print contours
        # print(contours_white)
        # print(contours_yellow)
        # draw the contours in origin image
        cv2.drawContours(image, contours_white, -1, (139,104,0), 3)  
        cv2.drawContours(image, contours_yellow, -1, (139,104,0), 3)  

        # center of  white  and yellow lane
        try:
            white_x,white_y = self.calculate_average(contours_white[0])
            print("white: ",white_x,white_y)
            is_detect_white = 1
        except:
            is_detect_white = 0
            print("The Camera Can`t Catch The White Lane.")
        try:
            yellow_x, yellow_y = self.calculate_average(contours_yellow[0])
            print("yellow: ",yellow_x,yellow_y)
            is_detect_yellow = 1
        except:
            is_detect_yellow = 0
            print("The Camera Can`t Catch The Yellow Lane.")
        # print(contours_white[0])
        # yellow_x, yellow_y = self.calculate_average(contours_yellow[0])
        # Publish Image
        self.pub_image_detect.publish(self.cvBridge.cv2_to_imgmsg(image,'bgr8'))
        
        # Publish Center
        self.pub_center_white_lane.publish()
        

    def calculate_average(self,input):
        sum_x = 0
        sum_y = 0
        for i in input:
            sum_x += i[0][0]
            sum_y == i[0][1]
        return sum_x/len(input), sum_y/len(input)

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('detect_lane')
    node = DetectLane()
    node.main()