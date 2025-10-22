import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler, EmitEvent
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('py_control_panel_package'),
        'config',
        'launch_params.yaml'
    )

    control_panel_node = Node(
        package='py_control_panel_package',
        executable='control_panel',
        name='py_control_panel',
        parameters=[config],
        output='screen'
    )

    interface_node = Node(
        package='cpp_interface_package',
        executable='interface_pubsub',
        name='cpp_interface'
    )

    # Shutdown the launch when control_panel exits
    shutdown_on_exit = RegisterEventHandler(
        OnProcessExit(
            target_action=control_panel_node,
            on_exit=[EmitEvent(event=Shutdown())]
        )
    )

    return LaunchDescription([
        control_panel_node,
        interface_node,
        shutdown_on_exit,
    ])
