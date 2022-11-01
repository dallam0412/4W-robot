#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def callback1(data):
    print("Received velocity for front left motor - ", data.data)

def callback2(data):
    print("Received velocity for front right motor - ", data.data)
    print("------------------------------------------------------------------------")

def sub():
    rospy.init_node('straight_line_subscriber')
    sub1 = rospy.Subscriber("/urdf_file/left_wheel_controller/command", Float64, callback1, queue_size=10)
    sub2 = rospy.Subscriber("/urdf_file/right_wheel_controller/command", Float64, callback2, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        sub()
    except rospy.ROSInterruptException:
        pass
