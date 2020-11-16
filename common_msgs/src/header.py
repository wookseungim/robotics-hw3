#!/usr/bin/env python
import rospy
from common_msgs.msg import Message


rospy.init_node('header', anonymous=True)


msg = Message()


pub = rospy.Publisher("testing_msg", Message, queue_size = 1)
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    pub.publish(msg)
    print("published")
    rate.sleep()
