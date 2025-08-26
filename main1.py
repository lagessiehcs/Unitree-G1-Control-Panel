import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

import math

import rclpy
from rclpy.node import Node
from unitree_hg.msg import (LowState,LowCmd)
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup


from G1ControlPanel import Ui_G1ControlPanel
from MotorAnglePubSub import *
import threading

from utils.crc import CRC
import time
import signal

MOTOR_NUMBER = 29
UPDATE_LABEL_TIME = 0.02 # 50 Hz
PUBLISH_ANGLES_TIME = 0.002 # 500 Hz

class MainWindow(QMainWindow, Ui_G1ControlPanel, Node):
    def __init__(self):
        super().__init__('motor_angles_pubsub')
        self.setupUi(self)

        self.kp = 50.0
        self.kd = 1.0

        self.latest_angles_deg = [0]*29

        self.main_window_opened = True

        self.crc = CRC()

        self.lock = threading.Lock()
        
        self.motorAnglesPubSub = MotorAnglesPubSub()

        self.motorAngles = [0]*MOTOR_NUMBER

        self.radioButtonArms.toggled.connect(self.toggleArms)
        self.radioButtonLegs.toggled.connect(self.toggleLegs)
        self.radioButtonWaist.toggled.connect(self.toggleWaist)

        self.pushButtonOn.clicked.connect(lambda: self.setEnableddoubleSpinBoxes('all', True))
        self.pushButtonOff.clicked.connect(lambda: self.setEnableddoubleSpinBoxes('all', False))

        self.subscription = self.create_subscription(LowState, '/lowstate', self.listener_callback, 10, callback_group=ReentrantCallbackGroup())
        self.publisher = self.create_publisher(LowCmd, '/lowcmd', 10)

        self.update_label_thread = threading.Thread(target=self.update_label)
        # self.publish_angles_thread = threading.Thread(target=self.publish_angles)

        self.update_label_thread.start()
        # self.publish_angles_thread.start()
        
        self.lowcmd_msg = LowCmd()
        self.lowcmd_msg.mode_pr = 0
        self.lowcmd_msg.mode_machine = 4
        self.timer = self.create_timer(PUBLISH_ANGLES_TIME, self.publish_angles, callback_group=ReentrantCallbackGroup())

        self.doubleSpinBoxes = [
            # Left Hip
            self.doubleSpinBoxLeftHipPitch,
            self.doubleSpinBoxLeftHipRoll,
            self.doubleSpinBoxLeftHipYaw,

            # Left Knee
            self.doubleSpinBoxLeftKneePitch,

            # Left Ankle
            self.doubleSpinBoxLeftAnklePitch,
            self.doubleSpinBoxLeftAnkleRoll,

            # Right Hip
            self.doubleSpinBoxRightHipPitch,
            self.doubleSpinBoxRightHipRoll,
            self.doubleSpinBoxRightHipYaw,

            # Right Knee
            self.doubleSpinBoxRightKneePitch,

            # Right Ankle
            self.doubleSpinBoxRightAnklePitch,
            self.doubleSpinBoxRightAnkleRoll,

            # Waist
            self.doubleSpinBoxWaistYaw,
            self.doubleSpinBoxWaistRoll,
            self.doubleSpinBoxWaistPitch,

            # Left Shoulder
            self.doubleSpinBoxLeftShoulderPitch,
            self.doubleSpinBoxLeftShoulderRoll,
            self.doubleSpinBoxLeftShoulderYaw,

            # Left Elbow
            self.doubleSpinBoxLeftElbowPitch,

            # Left Wrist
            self.doubleSpinBoxLeftWristRoll,
            self.doubleSpinBoxLeftWristPitch,
            self.doubleSpinBoxLeftWristYaw,
     
            # Right Shoulder
            self.doubleSpinBoxRightShoulderPitch,
            self.doubleSpinBoxRightShoulderRoll,
            self.doubleSpinBoxRightShoulderYaw,

            # Right Elbow
            self.doubleSpinBoxRightElbowPitch,

            # Right Wrist
            self.doubleSpinBoxRightWristRoll,
            self.doubleSpinBoxRightWristPitch,
            self.doubleSpinBoxRightWristYaw,
        ]

        self.labels = [
            # Left Hip
            self.labelLeftHipPitchValue,
            self.labelLeftHipRollValue,
            self.labelLeftHipYawValue,

            # Left Knee
            self.labelLeftKneePitchValue,

            # Left Ankle
            self.labelLeftAnklePitchValue,
            self.labelLeftAnkleRollValue,

            # Right Hip
            self.labelRightHipPitchValue,
            self.labelRightHipRollValue,
            self.labelRightHipYawValue,

            # Right Knee
            self.labelRightKneePitchValue,

            # Right Ankle
            self.labelRightAnklePitchValue,
            self.labelRightAnkleRollValue,

            # Waist
            self.labelWaistYawValue,
            self.labelWaistRollValue,
            self.labelWaistPitchValue,
  
            # Left Shoulder
            self.labelLeftShoulderPitchValue,
            self.labelLeftShoulderRollValue,
            self.labelLeftShoulderYawValue,

            # Left Elbow
            self.labelLeftElbowPitchValue,

            # Left Wrist
            self.labelLeftWristRollValue,
            self.labelLeftWristPitchValue,
            self.labelLeftWristYawValue,
     
            # Right Shoulder
            self.labelRightShoulderPitchValue,
            self.labelRightShoulderRollValue,
            self.labelRightShoulderYawValue,

            # Right Elbow
            self.labelRightElbowPitchValue,

            # Right Wrist
            self.labelRightWristRollValue,
            self.labelRightWristPitchValue,
            self.labelRightWristYawValue,
        ]


        for i in range(MOTOR_NUMBER):
            self.doubleSpinBoxes[i].valueChanged.connect(lambda value, idx=i: self.doubleSpinBox_changed(value, idx))

    def listener_callback(self, msg):
        motor_state = msg.motor_state[:29]
        self.latest_angles_deg = [math.degrees(state.q) for state in motor_state]
    
    def update_label(self):
        while self.main_window_opened:
            for i in range (MOTOR_NUMBER):
                deg = self.latest_angles_deg[i]
                self.labels[i].setText(f"{deg:.2f}")
            time.sleep(UPDATE_LABEL_TIME)
    
    def publish_angles(self):        

        while self.main_window_opened:
            motor_idx = []

            if self.radioButtonLegs.isChecked():
                motor_idx.extend(range(12))
            if self.radioButtonWaist.isChecked():
                motor_idx.extend(range(12,15))
            if self.radioButtonArms.isChecked():
                motor_idx.extend(range(15,29))

            if motor_idx != []:
                
                with self.lock:
                    for i in motor_idx:
                        self.lowcmd_msg.motor_cmd[i].mode = 1
                        self.lowcmd_msg.motor_cmd[i].q = float(self.motorAngles[i])
                        self.lowcmd_msg.motor_cmd[i].dq = 0.0
                        self.lowcmd_msg.motor_cmd[i].kp = self.kp
                        self.lowcmd_msg.motor_cmd[i].kd = self.kd
                        self.lowcmd_msg.motor_cmd[i].tau = 0.0

                self.lowcmd_msg.crc = self.crc.Crc(self.lowcmd_msg)
                self.publisher.publish(self.lowcmd_msg)

    def toggleArms(self, checked):
        if checked:
            self.setEnableddoubleSpinBoxes('arm', True)
        else:
            self.setEnableddoubleSpinBoxes('arm', False)
      

    def toggleLegs(self, checked):
        if checked:
            self.setEnableddoubleSpinBoxes('leg', True)
        else:
            self.setEnableddoubleSpinBoxes('leg', False)
    

    def toggleWaist(self, checked):
        if checked:
            self.setEnableddoubleSpinBoxes('waist', True)
        else:
            self.setEnableddoubleSpinBoxes('waist', False)
       

    def doubleSpinBox_changed(self, value, idx):
        with self.lock:
            self.motorAngles[idx] = math.radians(value)


    def setEnableddoubleSpinBoxes(self, part, bool_value):

        if part == 'leg':
            motor_range = range(0,12)
        elif part == 'waist':
            motor_range = range(12,15)
        elif part == 'arm':
            motor_range = range(15,29)
        elif part == 'all':
            motor_range = range(0,29)
            self.radioButtonArms.setChecked(bool_value)
            self.radioButtonWaist.setChecked(bool_value)
            self.radioButtonLegs.setChecked(bool_value)

        for i in motor_range:
            self.doubleSpinBoxes[i].setEnabled(bool_value)
            if bool_value:
                self.doubleSpinBoxes[i].setValue(self.latest_angles_deg[i])
                self.motorAngles[i] = math.radians(self.latest_angles_deg[i])

    def closeEvent(self, event):
        self.main_window_opened = False
        self.update_label_thread.join()
        # self.publish_angles_thread.join()
        self.destroy_node()
        rclpy.shutdown()
        event.accept()


def main():
    rclpy.init()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    executor = MultiThreadedExecutor(num_threads=2)
    executor.add_node(window)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        print("Ctrl+C pressed. Exiting...")
        app.quit()
        executor.shutdown()
        window.destroy_node()
        rclpy.shutdown()

    # handle Ctrl+C
    def sigint_handler(sig, frame):
        print("Ctrl+C pressed. Exiting...")
        app.quit()

    signal.signal(signal.SIGINT, sigint_handler)

    # QTimer keeps event loop responsive to SIGINT
    timer = QTimer()
    timer.start(100)  # check every 100 ms
    timer.timeout.connect(lambda: None)  # no-op

    sys.exit(app.exec())


if __name__ == "__main__":
    main()