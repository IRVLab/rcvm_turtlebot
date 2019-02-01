#! /usr/bin/python

import sys, math, threading, signal
from time import sleep
from math import pi
from numpy import sign

import rospy
from tf.transformations import euler_from_quaternion

from rcvm_core.srv import Affirmative, Attention, Danger, FollowMe, IndicateMovement, IndicateObject
from rcvm_core.srv import IndicateStay, Lost, Malfunction, Negative, Possibly, RepeatLast, ReportBattery


'''
    Service handlers.
'''
def affirmative_handler(req):    
    return True

def attention_handler(req):
    return True

def danger_handler(req):
    return True

def follow_me_handler(req):
    return True


# TODO: Respond to movement vector. Right now it just indicates down.
def indicate_movement_handler(req):
    return True
 
# TODO: Respond to object orientation.
def indicate_object_handler(req):
    return True

def indicate_stay_handler(req):
     return True

def lost_handler(req):
    return True

def malfunction_handler(req):
    return True
    

def negative_handler(req):
    return True

def possibly_handler(req):
    return True

def repeat_last_handler(req):
    return True

def report_battery_handler(req):
    return True


if __name__ == "__main__":
    rospy.loginfo('Initializing Turtlebot RCVM server...')

    rospy.Service('/rcvm/affirmative', Affirmative, affirmative_handler)
    rospy.Service('/rcvm/attention', Attention, attention_handler)
    rospy.Service('/rcvm/danger', Danger, danger_handler)
    rospy.Service('/rcvm/follow_me', FollowMe, follow_me_handler)
    rospy.Service('/rcvm/indicate_movement', IndicateMovement, indicate_movement_handler)
    rospy.Service('/rcvm/indicate_object', IndicateObject, indicate_object_handler)
    rospy.Service('/rcvm/indicate_stay', IndicateStay, indicate_stay_handler)
    rospy.Service('/rcvm/lost', Lost, lost_handler)
    rospy.Service('/rcvm/malfunction', Malfunction, malfunction_handler)
    rospy.Service('/rcvm/negative', Negative, negative_handler)
    rospy.Service('/rcvm/possibly', Possibly, possibly_handler)
    rospy.Service('/rcvm/repeat_last', RepeatLast, repeat_last_handler)
    rospy.Service('/rcvm/report_battery', ReportBattery, report_battery_handler)

    rospy.loginfo('      Service advertising completed...')
    rospy.loginfo('RCVM server ready for business!')
    rospy.loginfo('Spinning forever until a service request is recieved.')    

    # Spin forever to avoid early shutdown.
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rate.sleep()
        
else:
    pass
