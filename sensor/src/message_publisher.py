#!/usr/bin/env python
import rospy
from common_msgs.msg import Message
from common_msgs.srv import Service, ServiceRequest


rospy.init_node('message_publisher', anonymous=True)
requester = rospy.ServiceProxy('reset', Service)
count = 0
msg = Message()

pub = rospy.Publisher("DateTime_msg", Message, queue_size = 1)
rate = rospy.Rate(1)
msg.number.data = 0
msg.rotation.orientation.x = 0.0
msg.rotation.orientation.y = 0.0
msg.rotation.orientation.z = 0.0
msg.rotation.orientation.w = 0.0
msg.rotation.position.x = 0.0
msg.rotation.position.y = 0.0
msg.rotation.position.z = 0.0

while not rospy.is_shutdown():
    count += 1
    msg.number.data += 1
    msg.rotation.orientation.x += 1
    msg.rotation.orientation.y += 1
    msg.rotation.orientation.z += 1
    msg.rotation.orientation.w += 1
    msg.rotation.position.x += 1
    msg.rotation.position.y += 2
    msg.rotation.position.z += 3
    pub.publish(msg)
    if count == 10:
        req = ServiceRequest(type1 = True, type2 = False)
        res = requester(req)
    elif count == 20:
        req = ServiceRequest(type1 = True, type2 = True)
        res = requester(req)
        count = 0
    
    
    print(msg.number)
    print(msg.rotation)
    rate.sleep()
