# Unitree G1 Control Panel

## Requirements and Dependencies

### ROS2 Distros and Unitree ROS2 package
The Unitree G1 Control Panel requires a ROS 2 environment along with the Unitree ROS 2 package, which provides the necessary ROS 2 interfaces.
For details on supported ROS 2 distributions and instructions for installing the package, see the **System Requirements** and **Install Unitree ROS2 Package** subsections in the **Configuration** section of the [Unitree ROS2 package's README](https://github.com/unitreerobotics/unitree_ros2/blob/master/README.md)

### Setup Environment
Open setup.sh file.
```bash
sudo gedit ~/unitree_ros2/setup.sh
```
```bash
#!/bin/bash
echo "Setup unitree ros2 environment"
source /opt/ros/foxy/setup.bash
source $HOME/unitree_ros2/cyclonedds_ws/install/setup.bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI='<CycloneDDS><Domain><General><Interfaces>
                            <NetworkInterface name="enp3s0" priority="default" multicast="default" />
                        </Interfaces></General></Domain></CycloneDDS>'
```
where "enp3s0" is the network interface name of unitree robot connected.
Modify it to the corresponding network interface according to the actual situation. 

Source the environment to setup the ROS2 support of Unitree robot: 
```bash
source ~/unitree_ros2/setup.sh
```
If you don't want to source the bash script every time when a new terminal opens, you can write the content of bash script into ~/.bashrc, but attention should be paid when there are multiple ROS environments coexisting in the system.

If your computer is not connected to the robot but you still want to use Unitree ROS2 for simulation and other functions, you can use the local loopback "lo" as the network interface.
```bash
source ~/unitree_ros2/setup_local.sh # use "lo" as the network interface
```
or
```bash
source ~/unitree_ros2/setup_default.sh # No network network interface specified 
```

If you are using a ROS 2 distribution other than Foxy, you will need to update the ROS2 distro's name accordingly in all three setup files: setup.sh, setup_local.sh, and setup_default.sh.

(Optional) To make it easier to select the appropriate setup file, you can add the following snippet to your ~/.bashrc:
```bash
# Only run this in interactive shells
if [[ $- == *i* ]]; then
    # Define root directory (change this one if the root directory of unitree_ros2 is different)
    ROOT_DIR=~

    # Save the original HOME
    ORIG_HOME=$HOME
    
    # Set HOME to ROOT_DIR
    export HOME=$ROOT_DIR
    
    # Run commands with new HOME
    echo "Select environment:"
    echo "    1: unitree ros2 environment"
    echo "    2: unitree ros2 simulation environment"
    echo "Enter: unitree ros2 environment with default interface"
    read -p "Enter choice [1/2/Enter]: " choice

    case $choice in
        1)
            source "$ROOT_DIR/unitree_ros2/setup.sh"
            ;;
        2)
            source "$ROOT_DIR/unitree_ros2/setup_local.sh"
            ;;
        *)
            source "$ROOT_DIR/unitree_ros2/setup_default.sh"
            ;;
    esac

    # Restore original HOME
    export HOME=$ORIG_HOME
fi

```
### Install Dependencies
````
pip install PySide6
sudo apt update
sudo apt install libxcb-cursor0
sudo apt install libgl1-mesa-glx
````

## Run
````
pyside6-uic G1ControlPanel.ui -o G1ControlPanel.py
python3 main.py
````
