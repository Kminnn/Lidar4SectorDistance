# Lidar 4 sector distance data launch

## Setup:
Paste the following in the terminal
<pre lang="markdown"> git clone https://github.com/Kminnn/Lidar4SectorDistance.git  </pre>

In /Lidar4SectorDistance remove build, install, log
<pre lang="markdown"> cd Lidar4SectorDistance  </pre>

<pre lang="markdown"> rm -rf build install log </pre>

## Compile & Install sllidar_ros2 package

Change directory to /Lidar4SectorDistance/src
<pre lang="markdown"> cd src  </pre>

Remove the existing sllidar_ros2 package and reinstall the package
<pre lang="markdown"> rm -rf sllidar_ros2  </pre>
<pre lang="markdown"> git clone https://github.com/Slamtec/sllidar_ros2.git </pre>

Build your workspace in /Lidar4SectorDistance
<pre lang="markdown"> cd .. </pre>
<pre lang="markdown"> colcon build </pre>
<pre lang="markdown"> source install/setup.bash </pre>

Build succesfully

![Screenshot from 2025-06-22 14-55-53](https://github.com/user-attachments/assets/ad630285-f96a-4440-a5ea-e810eac316b4)


## Run sllidar_ros2:

The command for RPLIDAR A1 is :
<pre lang="markdown"> ros2 launch sllidar_ros2 view_sllidar_a1_launch.py </pre>

The command for RPLIDAR C1 is :
<pre lang="markdown"> ros2 launch sllidar_ros2 view_sllidar_c1_launch.py </pre>

The /scan topic will appear on rviz2

![Screenshot from 2025-06-22 14-57-03](https://github.com/user-attachments/assets/3b9448bd-6363-4e17-8c85-c41a286be303)


## Run lidar_processing:

Open another terminal then paste these command
<pre lang="markdown"> cd Lidar4SectorDistance </pre>
<pre lang="markdown"> source install/setup.bash </pre>
<pre lang="markdown"> ros2 launch lidar_processing scan_and_processing.launch.py </pre>

If launch succesfully the data will appear like the picture

![Screenshot from 2025-06-22 14-53-31](https://github.com/user-attachments/assets/fea0217c-ffb1-48ea-a8b3-1121865c8aab)




## RPLIDAR A1 setup

Since the package launch file for RPLIDAR A1 scan_mode is set to 'Sensitivity'
<pre lang="markdown"> cd Lidar4SectorDistance/src/sllidar_ros2/launch/ </pre>
<pre lang="markdown"> gedit view_sllidar_a1_launch.py </pre>

In line 20 change to:
<pre lang="markdown"> scan_mode = LaunchConfiguration('scan_mode', default='Standard') </pre>

Build your workspace
<pre lang="markdown"> cd ../../.. </pre>
<pre lang="markdown"> colcon build  </pre>
<pre lang="markdown"> source install/setup.bash </pre>

