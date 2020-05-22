import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubClass(Node):

    def __init__(self):
        super().__init__('Node')
        self.sub_ = self.create_subscription(String, '/topic', self.sub_cb, 10 )
        self.end = False
        self.count = 0
        self.until_end = 0
    def sub_cb(self, msg):
        print('I heard: %s'% msg.data)
        if self.count == self.until_end-1:
            self.end = True
        self.count += 1



def execute(self, inputs, outputs, gvm):
    
    obj = SubClass()
    obj.until_end = inputs["count"]
    while not obj.end:
        rclpy.spin_once(obj)
    return "success"
