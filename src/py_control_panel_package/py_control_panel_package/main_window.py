import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

try: # Relative import within the package
    from .g1_control_panel import Ui_G1ControlPanel
    from .motor_angle_pubsub import *  
    from .utils.crc import CRC
except ImportError: # Normal import when running directly
    from g1_control_panel import Ui_G1ControlPanel
    from motor_angle_pubsub import *  
    from utils.crc import CRC

    
import threading

import time
import signal

MOTOR_NUMBER = 29
UPDATE_LABEL_TIME = 0.02 # 50 Hz
PUBLISH_ANGLES_TIME = 0.0 # 500 Hz

class MainWindow(QMainWindow, Ui_G1ControlPanel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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

        self.updateLabel_thread = threading.Thread(target=self.updateLabel)
        self.publishAngles_thread = threading.Thread(target=self.publishAngles)

        self.updateLabel_thread.start()
        self.publishAngles_thread.start()
        

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

    def updateLabel(self):
        while self.main_window_opened:
            rclpy.spin_once(self.motorAnglesPubSub, timeout_sec=0.01)
            for i in range (MOTOR_NUMBER):
                deg = self.motorAnglesPubSub.latest_angles_deg[i]
                self.labels[i].setText(f"{deg:.2f}")
            time.sleep(UPDATE_LABEL_TIME)
    
    def publishAngles(self):

        while self.main_window_opened:
            motor_idx = []

            if self.radioButtonLegs.isChecked():
                motor_idx.extend(range(12))
            if self.radioButtonWaist.isChecked():
                motor_idx.extend(range(12,15))
            if self.radioButtonArms.isChecked():
                motor_idx.extend(range(15,29))

            if motor_idx != []:
                msg = LowCmd()
                msg.mode_pr = 0
                msg.mode_machine = 4
                
                with self.lock:
                    for i in motor_idx:
                        msg.motor_cmd[i].mode = 1
                        msg.motor_cmd[i].q = float(self.motorAngles[i])
                        msg.motor_cmd[i].dq = 0.0
                        msg.motor_cmd[i].kp = self.motorAnglesPubSub.kp
                        msg.motor_cmd[i].kd = self.motorAnglesPubSub.kd
                        msg.motor_cmd[i].tau = 0.0

                msg.crc = self.crc.Crc(msg)
                self.motorAnglesPubSub.publisher.publish(msg)
            time.sleep(PUBLISH_ANGLES_TIME)

    def toggleArms(self, checked):
        self.setEnableddoubleSpinBoxes('arm', checked)
        
      

    def toggleLegs(self, checked):
        self.setEnableddoubleSpinBoxes('leg', checked)
    

    def toggleWaist(self, checked):
        self.setEnableddoubleSpinBoxes('waist', checked)
       

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
                self.motorAngles[i] = math.radians(self.motorAnglesPubSub.latest_angles_deg[i])

    def closeEvent(self, event):
        self.main_window_opened = False
        self.updateLabel_thread.join()
        self.publishAngles_thread.join()
        self.motorAnglesPubSub.destroy_node()
        rclpy.shutdown()
        event.accept()


def main():
    rclpy.init()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

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