#! /usr/bin/python

import sys, math, threading, signal
from time import sleep
from math import pi,radians
from numpy import sign

import rospy
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist

from rcvm_core.srv import Affirmative, Attention, Danger, FollowMe, IndicateMovement, IndicateObject
from rcvm_core.srv import IndicateStay, Lost, Malfunction, Negative, Possibly, RepeatLast, ReportBattery


'''
    Service handlers.
'''
def affirmative_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist() 
    move_cmd.linear.x = .2
    move_cmd.angular.z = 0

    for x in range(0,15):
        cmd_vel.publish(move_cmd)
        move_cmd.linear.x *= -1
        sleep(.5)

         




    return True

def attention_handler(req):
    return True

def danger_handler(req):



    return True

def follow_me_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist()

    move_cmd.linear.x = .05
    move_cmd.angular.z = 0

    # Nudging in direction 
    for x in range(0,2):
        move_cmd.angular.z = 1.5
        cmd_vel.publish(move_cmd)
        sleep(.4)
        cmd_vel.publish(move_cmd)
        sleep(.4)
        if x!=1:
            move_cmd.angular.z = -1.3
            cmd_vel.publish(move_cmd)
            sleep(.5)
            cmd_vel.publish(move_cmd)
            sleep(.2)
    
    sleep(1)

    # Turn 
    move_cmd.angular.z = 3
    move_cmd.linear.x =  0

    cmd_vel.publish(move_cmd)

    sleep(1.5)

    move_cmd.angular.z = 0
    move_cmd.linear.x =  1

    cmd_vel.publish(move_cmd)






 
    return True


# TODO: Respond to movement vector. Right now it just indicates down.

def indicate_movement(cmd_vel,r,move_cmd,turndir):
    
    #turndir indicates which way the robot looks backwards

    move_cmd.linear.x = .5
    move_cmd.angular.z = 0

    for x in range(0,20):
            
        cmd_vel.publish(move_cmd)
        r.sleep()

    move_cmd.linear.x = 0
    move_cmd.angular.z = 1*turndir
        
    for y in range(0,20):
        cmd_vel.publish(move_cmd)
        r.sleep()

    sleep(1)

    move_cmd.linear.x = 0
    move_cmd.angular.z = -1*turndir

    for z in range(0,18):
        cmd_vel.publish(move_cmd)
        r.sleep()

    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    for w in range(0,10):
        cmd_vel.publish(move_cmd)
        r.sleep()
        

    move_cmd.linear.x = .5
    move_cmd.angular.z = 0

    for x in range(0,5):
            
        cmd_vel.publish(move_cmd)
        r.sleep()

    return True 



def indicate_movement_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist()

   
    if req.direction.x == 1 and req.direction.y ==0:

        indicate_movement(cmd_vel,r,move_cmd,1)

    elif req.direction.x == -1 and req.direction.y ==0:
        move_cmd.linear.x = 0
        move_cmd.angular.z = -1
        for x in range(0,33):
            cmd_vel.publish(move_cmd)
            r.sleep()
        move_cmd.angular.z = 0
        for y in range(0,10):
            cmd_vel.publish(move_cmd)
            r.sleep()

        indicate_movement(cmd_vel,r,move_cmd,1)
        return True

    elif req.direction.x == 0 and req.direction.y ==1:
        move_cmd.linear.x = 0
        move_cmd.angular.z = -1
        for x in range(0,17):
            cmd_vel.publish(move_cmd)
            r.sleep()
        move_cmd.angular.z = 0
        for y in range(0,10):
            cmd_vel.publish(move_cmd)
            r.sleep()
        indicate_movement(cmd_vel,r,move_cmd,1)
        return True

    elif req.direction.x == 0 and req.direction.y ==-1:
        move_cmd.linear.x = 0
        move_cmd.angular.z = 1
        for x in range(0,17):
            cmd_vel.publish(move_cmd)
            r.sleep()
        move_cmd.angular.z = 0
        for y in range(0,10):
            cmd_vel.publish(move_cmd)
            r.sleep()
        indicate_movement(cmd_vel,r,move_cmd,-1)
        return True
    else:

        return True 
 
# TODO: Respond to object orientation.
def indicate_object_handler(req):
    

    return True

def indicate_stay_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist()
    move_cmd.linear.x = .5
    move_cmd.angular.z = .5

    now = rospy.Time.now()

    while rospy.Time.now() < now + rospy.Duration.from_sec(25):
        cmd_vel.publish(move_cmd)
    return True

def lost_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(.5)
    move_cmd = Twist()
    move_cmd.linear.x = .05
    direction = 1.5


    move_cmd.angular.z = direction
    cmd_vel.publish(move_cmd)
    r.sleep()
    direction = direction*-1
    move_cmd.linear.x = 0
    move_cmd.angular.z = direction 
    cmd_vel.publish(move_cmd)
    r.sleep()

    move_cmd.angular.z = 0
    move_cmd.linear.x = 1.5
    cmd_vel.publish(move_cmd)

    move_cmd.linear.x = .05
    move_cmd.angular.z = -1.5 


    r.sleep()

    move_cmd.angular.z = direction
    cmd_vel.publish(move_cmd)
    r.sleep()
    direction = direction*-1
    move_cmd.angular.z = direction 
    cmd_vel.publish(move_cmd)
    r.sleep()

    move_cmd.linear.x = .5
    direction = 0
    cmd_vel.publish(move_cmd)
    r.sleep()

    return True

def malfunction_handler(req):
    return True
    

def negative_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist()
    move_cmd.linear.x = 0
    direction = 1

    for x in range(0,5):
        move_cmd.angular.z = direction
        cmd_vel.publish(move_cmd)
        sleep(.7)
        direction = direction*-1
        move_cmd.angular.z = direction 
        cmd_vel.publish(move_cmd)
        sleep(.4)
    return True

def possibly_handler(req):


    return True

def repeat_last_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist()
    move_cmd.linear.x = .3
    move_cmd.angular.z = -2
    cmd_vel.publish(move_cmd)
    sleep(3)
    move_cmd.linear.x =  0
    move_cmd.angular.z = 2
    cmd_vel.publish(move_cmd)



    return True

def report_battery_handler(req):
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
    r = rospy.Rate(10)
    move_cmd = Twist()

    move_cmd.linear.x = 0
    move_cmd.angular.z = radians(45)
    for x in range(0,36): 
        cmd_vel.publish(move_cmd)
        r.sleep()

    r.sleep()
    sleep(3)
    move_cmd.linear.x = -.5
    move_cmd.angular.z = 0

    cmd_vel.publish(move_cmd)
    sleep(4)
    move_cmd.linear.x = 0
    move_cmd.angular.z = radians(45)
    
    for x in range(0,36): 
        cmd_vel.publish(move_cmd)
        r.sleep()





    return True


if __name__ == "__main__":
    rospy.loginfo('Initializing Turtlebot RCVM server...')
    rospy.init_node('rcvm_server', argv=None, anonymous=True)



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

    rospy.loginfo('RCVM server ready for business!')
    rospy.loginfo('Spinning forever until a service request is recieved.')    

    # Spin forever to avoid early shutdown.
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rate.sleep()
        
else:
    pass
