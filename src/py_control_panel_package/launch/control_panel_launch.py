import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cpp_interface_package',
            executable='interface_pubsub',
            name='cpp_interface'
        ),
        Node(
            package='py_control_panel_package',
            executable='control_panel',
            name='py_control_panel',
            output='screen'
        ),
    ])