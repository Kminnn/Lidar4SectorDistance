from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lidar_processing',
            executable='sector_distance_node',
            name='sector_distance_node',
            output='screen'
        )
    ])