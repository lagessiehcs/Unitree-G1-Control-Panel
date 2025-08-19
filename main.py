import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from G1ControlPanel import Ui_G1ControlPanel
from MotorAnglePubSub import *
import threading

from motor_crc import *

MOTOR_NUMBER = 29

class MainWindow(QMainWindow, Ui_G1ControlPanel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lock = threading.Lock()
        
        self.motorAnglesPubSub = MotorAnglesPubSub()

        self.motorAngles = [0]*MOTOR_NUMBER

        self.radioButtonArms.toggled.connect(self.toggleArms)
        self.radioButtonLegs.toggled.connect(self.toggleLegs)
        self.radioButtonWaist.toggled.connect(self.toggleWaist)

        self.pushButtonOn.clicked.connect(lambda: self.setEnableddoubleSpinBoxes('all', True))
        self.pushButtonOff.clicked.connect(lambda: self.setEnableddoubleSpinBoxes('all', False))

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

        self.setEnableddoubleSpinBoxes('all', False)

        for i in range(MOTOR_NUMBER):
            self.doubleSpinBoxes[i].valueChanged.connect(lambda value, idx=i: self.doubleSpinBox_changed(value, idx))

    def update_label(self):
        rclpy.spin_once(self.motorAnglesPubSub, timeout_sec=0.01)
        for i in range (MOTOR_NUMBER):
            deg = self.motorAnglesPubSub.latest_angles_deg[i]
            self.labels[i].setText(f"{deg:.2f}")
    
    def publish_angles(self):
        motor_idx = []

        if self.radioButtonLegs.isChecked():
            motor_idx.extend(range(12))
        if self.radioButtonWaist.isChecked():
            motor_idx.extend(range(12,15))
        if self.radioButtonArms.isChecked():
            motor_idx.extend(range(15,29))

        if motor_idx != []:
            msg = LowCmd()
            with self.lock:
                for i in motor_idx:
                    msg.motor_cmd[i].mode = 1
                    msg.motor_cmd[i].q = float(self.motorAngles[i])
                    msg.motor_cmd[i].kp = self.motorAnglesPubSub.kp
                    msg.motor_cmd[i].kd = self.motorAnglesPubSub.kd
                    
            get_crc(msg)
            self.motorAnglesPubSub.publisher.publish(msg)
    

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
                self.doubleSpinBoxes[i].setValue(self.motorAnglesPubSub.latest_angles_deg[i])
                self.motorAngles[i] = self.motorAnglesPubSub.latest_angles_deg[i]


def main():
    rclpy.init()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()