import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    this_dir = os.path.dirname(__file__)   # folder containing this launch file
    script_path = os.path.join(this_dir, '../..', 'py_control_panel', 'main.py')
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