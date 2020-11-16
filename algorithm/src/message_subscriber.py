#!/usr/bin/env python
import rospy
from common_msgs.msg import Message
from common_msgs.srv import Service, ServiceResponse

count = 0

def service_callback(request):
    response = ServiceResponse(result = request.type1 and request.type2)
    if response.result == False:
        print("--------10 seconds passed----------")
    elif response.result == True:
        print("-----------Reset count--------------")
    return response

def callback(msg):
    print("subscribed")
    cal1 = msg.number.data * msg.rotation.position.x
    cal2 = msg.rotation.orientation.x * msg.rotation.position.y
    print(cal1)
    print(cal2)
    print("----------")
    
rospy.init_node("message_subscriber")
sub = rospy.Subscriber("DateTime_msg", Message, callback)
service = rospy.Service('reset', Service, service_callback)
rospy.spin()
