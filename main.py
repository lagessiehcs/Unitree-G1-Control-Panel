import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from G1ControlPanel import Ui_G1ControlPanel
from MotorAnglePubSub import *
import threading

MOTOR_NUMBER = 29

class MainWindow(QMainWindow, Ui_G1ControlPanel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lock = threading.Lock()
        
        self.motorAnglesPubSub = MotorAnglesPubSub()

        self.motorAngles = [0]*MOTOR_NUMBER

        self.radioButton.toggled.connect(self.radio_changed)

        self.thread_update_label = QThread()
        self.timer_update_label = QTimer()
        self.timer_update_label.moveToThread(self.thread_update_label)
        self.timer_update_label.setInterval(20)
        self.timer_update_label.timeout.connect(self.update_label)
        self.thread_update_label.started.connect(self.timer_update_label.start)
        self.thread_update_label.start()

        self.thread_publish_angles = QThread()
        self.timer_publish_angles = QTimer()
        self.timer_publish_angles.moveToThread(self.thread_publish_angles)
        self.timer_publish_angles.setInterval(20)
        self.timer_publish_angles.timeout.connect(self.publish_angles)
        self.thread_publish_angles.started.connect(self.timer_publish_angles.start)
        self.thread_publish_angles.start()

        self.spinBoxes = [
            # Left Hip
            self.spinBoxLeftHipPitch,
            self.spinBoxLeftHipRoll,
            self.spinBoxLeftHipYaw,

            # Left Knee
            self.spinBoxLeftKneePitch,

            # Left Ankle
            self.spinBoxLeftAnklePitch,
            self.spinBoxLeftAnkleRoll,

            # Right Hip
            self.spinBoxRightHipPitch,
            self.spinBoxRightHipRoll,
            self.spinBoxRightHipYaw,

            # Right Knee
            self.spinBoxRightKneePitch,

            # Right Ankle
            self.spinBoxRightAnklePitch,
            self.spinBoxRightAnkleRoll,

            # Waist
            self.spinBoxWaistYaw,
            self.spinBoxWaistRoll,
            self.spinBoxWaistPitch,

            # Left Shoulder
            self.spinBoxLeftShoulderPitch,
            self.spinBoxLeftShoulderRoll,
            self.spinBoxLeftShoulderYaw,

            # Left Elbow
            self.spinBoxLeftElbowPitch,

            # Left Wrist
            self.spinBoxLeftWristRoll,
            self.spinBoxLeftWristPitch,
            self.spinBoxLeftWristYaw,
     
            # Right Shoulder
            self.spinBoxRightShoulderPitch,
            self.spinBoxRightShoulderRoll,
            self.spinBoxRightShoulderYaw,

            # Right Elbow
            self.spinBoxRightElbowPitch,

            # Right Wrist
            self.spinBoxRightWristRoll,
            self.spinBoxRightWristPitch,
            self.spinBoxRightWristYaw,
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

        self.setEnabledSpinBoxes(False)

        for i in range(MOTOR_NUMBER):
            self.spinBoxes[i].valueChanged.connect(lambda value, idx=i: self.spinbox_changed(value, idx))

    def update_label(self):
        rclpy.spin_once(self.motorAnglesPubSub, timeout_sec=0.01)
        for i in range (MOTOR_NUMBER):
            self.labels[i].setText(str(round(self.motorAnglesPubSub.latest_angles_deg[i], 2)))
    
    def publish_angles(self):
        if not self.radioButton.isChecked():
            msg = LowCmd()
            with self.lock:
                for i in range (MOTOR_NUMBER):
                    msg.motor_cmd[i].q = float(self.motorAngles[i])
            
            self.motorAnglesPubSub.publisher.publish(msg)
    

    def radio_changed(self, checked):
        if checked:
            self.setEnabledSpinBoxes(False)
        else:
            self.setEnabledSpinBoxes(True)
       
            for i in range (MOTOR_NUMBER):
                self.spinBoxes[i].setValue(round(self.motorAnglesPubSub.latest_angles_deg[i]))
                self.motorAngles[i] = round(self.motorAnglesPubSub.latest_angles_deg[i])

    def spinbox_changed(self, value, idx):
        with self.lock:
            self.motorAngles[idx] = math.radians(value)


    def setEnabledSpinBoxes(self, bool_value):
        for spinBoxe in self.spinBoxes:
            spinBoxe.setEnabled(bool_value)
        

def main():
    rclpy.init()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()