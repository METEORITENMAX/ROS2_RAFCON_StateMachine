import sys
from rclpy.node import Node
from std_msgs.msg import String

def execute(self, inputs, outputs, gvm):

    node = gvm.get_variable("new_ros2_node", True)
    test_pub = node.create_publisher(String, '/topic', 10)
    msg = String()
    i = 1
    while i <= inputs["count"]: 
        msg.data = 'Hello World %i' % i 
        test_pub.publish(msg)
        print('Publishing: Hello World %i' % i)
        i +=1
    
    return "success"
    