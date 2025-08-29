# Unitree G1 Control Panel

## Requirements

[Unitree ROS2 package](https://github.com/unitreerobotics/unitree_ros2)

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
