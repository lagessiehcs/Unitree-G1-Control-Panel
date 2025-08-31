import sys
import math

import rclpy
from rclpy.node import Node
from unitree_hg.msg import (LowState,LowCmd)

class MotorAnglesPubSub(Node):
    def __init__(self):
        super().__init__('motor_angles_pubsub')
        
        self.declare_parameter('publisher_topic', '/lowcmd')
        self.declare_parameter('publish_angle_time', 0.00082)
        
        self.publish_angle_time = self.get_parameter('publish_angle_time').value
        self.publisher_topic = self.get_parameter('publisher_topic').value

        self.kp = 50.0
        self.kd = 1.0

        self.subscription = self.create_subscription(LowState, '/lowstate', self.listener_callback, 10)
        self.publisher = self.create_publisher(LowCmd, self.publisher_topic, 10)

        self.latest_angles_deg = [0]*29

    def listener_callback(self, msg):
        motor_state = msg.motor_state[:29]
        self.latest_angles_deg = [math.degrees(state.q) for state in motor_state]