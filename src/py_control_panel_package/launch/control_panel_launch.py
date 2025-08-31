import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('py_control_panel_package'),
        'config',
        'launch_params.yaml'
        )
    
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
            parameters=[config],
            output='screen'
        ),
    ])