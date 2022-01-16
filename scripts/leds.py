#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
import time

def cb(message):
  rospy.loginfo(message.data)
  #if message == x:
   #print('OK') 



rospy.init_node('answer_dis')
sub = rospy.Subscriber('answer_up', Float32, cb)
rospy.spin()
