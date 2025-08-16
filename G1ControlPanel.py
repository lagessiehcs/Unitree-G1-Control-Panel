# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'G1ControlPanel.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_G1ControlPanel(object):
    def setupUi(self, G1ControlPanel):
        if not G1ControlPanel.objectName():
            G1ControlPanel.setObjectName(u"G1ControlPanel")
        G1ControlPanel.resize(1265, 519)
        self.centralwidget = QWidget(G1ControlPanel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(40, 30, 40, 30)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelArms = QLabel(self.centralwidget)
        self.labelArms.setObjectName(u"labelArms")
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        font.setPointSize(13)
        font.setBold(True)
        self.labelArms.setFont(font)
        self.labelArms.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.labelArms.setMargin(10)

        self.verticalLayout.addWidget(self.labelArms)

        self.horizontalLayoutArms = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayoutArms.setSpacing(-1)
#endif
        self.horizontalLayoutArms.setObjectName(u"horizontalLayoutArms")
        self.verticalLayoutLeftArm = QVBoxLayout()
        self.verticalLayoutLeftArm.setObjectName(u"verticalLayoutLeftArm")
        self.verticalLayoutLeftArm.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayoutLeftShoulder = QVBoxLayout()
        self.verticalLayoutLeftShoulder.setObjectName(u"verticalLayoutLeftShoulder")
        self.verticalLayoutLeftShoulder.setContentsMargins(-1, -1, -1, 30)
        self.labelLeftShoulder = QLabel(self.centralwidget)
        self.labelLeftShoulder.setObjectName(u"labelLeftShoulder")
        self.labelLeftShoulder.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u".AppleSystemUIFont"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.labelLeftShoulder.setFont(font1)

        self.verticalLayoutLeftShoulder.addWidget(self.labelLeftShoulder)

        self.formLayoutLeftShoulder = QFormLayout()
        self.formLayoutLeftShoulder.setObjectName(u"formLayoutLeftShoulder")
        self.formLayoutLeftShoulder.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLeftShoulderPitch = QLabel(self.centralwidget)
        self.labelLeftShoulderPitch.setObjectName(u"labelLeftShoulderPitch")
        font2 = QFont()
        font2.setFamilies([u".AppleSystemUIFont"])
        font2.setPointSize(12)
        self.labelLeftShoulderPitch.setFont(font2)
        self.labelLeftShoulderPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftShoulder.setWidget(0, QFormLayout.LabelRole, self.labelLeftShoulderPitch)

        self.horizontalLayoutLeftShoulderPitch = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayoutLeftShoulderPitch.setSpacing(-1)
#endif
        self.horizontalLayoutLeftShoulderPitch.setObjectName(u"horizontalLayoutLeftShoulderPitch")
        self.labelLeftShoulderPitchValue = QLabel(self.centralwidget)
        self.labelLeftShoulderPitchValue.setObjectName(u"labelLeftShoulderPitchValue")
        self.labelLeftShoulderPitchValue.setMinimumSize(QSize(60, 0))
        self.labelLeftShoulderPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftShoulderPitchValue.setFont(font2)

        self.horizontalLayoutLeftShoulderPitch.addWidget(self.labelLeftShoulderPitchValue)

        self.spinBoxLeftShoulderPitch = QSpinBox(self.centralwidget)
        self.spinBoxLeftShoulderPitch.setObjectName(u"spinBoxLeftShoulderPitch")
        self.spinBoxLeftShoulderPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftShoulderPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftShoulderPitch.setFont(font2)
        self.spinBoxLeftShoulderPitch.setMouseTracking(False)
        self.spinBoxLeftShoulderPitch.setReadOnly(False)
        self.spinBoxLeftShoulderPitch.setKeyboardTracking(False)
        self.spinBoxLeftShoulderPitch.setMinimum(-999)
        self.spinBoxLeftShoulderPitch.setMaximum(999)

        self.horizontalLayoutLeftShoulderPitch.addWidget(self.spinBoxLeftShoulderPitch)


        self.formLayoutLeftShoulder.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutLeftShoulderPitch)

        self.labelLeftShoulderRoll = QLabel(self.centralwidget)
        self.labelLeftShoulderRoll.setObjectName(u"labelLeftShoulderRoll")
        self.labelLeftShoulderRoll.setFont(font2)
        self.labelLeftShoulderRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftShoulder.setWidget(1, QFormLayout.LabelRole, self.labelLeftShoulderRoll)

        self.horizontalLayoutLeftShoulderRoll = QHBoxLayout()
        self.horizontalLayoutLeftShoulderRoll.setObjectName(u"horizontalLayoutLeftShoulderRoll")
        self.labelLeftShoulderRollValue = QLabel(self.centralwidget)
        self.labelLeftShoulderRollValue.setObjectName(u"labelLeftShoulderRollValue")
        self.labelLeftShoulderRollValue.setMinimumSize(QSize(60, 0))
        self.labelLeftShoulderRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftShoulderRollValue.setFont(font2)

        self.horizontalLayoutLeftShoulderRoll.addWidget(self.labelLeftShoulderRollValue)

        self.spinBoxLeftShoulderRoll = QSpinBox(self.centralwidget)
        self.spinBoxLeftShoulderRoll.setObjectName(u"spinBoxLeftShoulderRoll")
        self.spinBoxLeftShoulderRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftShoulderRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftShoulderRoll.setFont(font2)
        self.spinBoxLeftShoulderRoll.setReadOnly(False)
        self.spinBoxLeftShoulderRoll.setKeyboardTracking(False)
        self.spinBoxLeftShoulderRoll.setMinimum(-999)
        self.spinBoxLeftShoulderRoll.setMaximum(999)

        self.horizontalLayoutLeftShoulderRoll.addWidget(self.spinBoxLeftShoulderRoll)


        self.formLayoutLeftShoulder.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutLeftShoulderRoll)

        self.labelLeftShoulderYaw = QLabel(self.centralwidget)
        self.labelLeftShoulderYaw.setObjectName(u"labelLeftShoulderYaw")
        self.labelLeftShoulderYaw.setFont(font2)
        self.labelLeftShoulderYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftShoulder.setWidget(2, QFormLayout.LabelRole, self.labelLeftShoulderYaw)

        self.horizontalLayoutLeftShoulderYaw = QHBoxLayout()
        self.horizontalLayoutLeftShoulderYaw.setObjectName(u"horizontalLayoutLeftShoulderYaw")
        self.labelLeftShoulderYawValue = QLabel(self.centralwidget)
        self.labelLeftShoulderYawValue.setObjectName(u"labelLeftShoulderYawValue")
        self.labelLeftShoulderYawValue.setMinimumSize(QSize(60, 0))
        self.labelLeftShoulderYawValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftShoulderYawValue.setFont(font2)

        self.horizontalLayoutLeftShoulderYaw.addWidget(self.labelLeftShoulderYawValue)

        self.spinBoxLeftShoulderYaw = QSpinBox(self.centralwidget)
        self.spinBoxLeftShoulderYaw.setObjectName(u"spinBoxLeftShoulderYaw")
        self.spinBoxLeftShoulderYaw.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftShoulderYaw.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftShoulderYaw.setFont(font2)
        self.spinBoxLeftShoulderYaw.setReadOnly(False)
        self.spinBoxLeftShoulderYaw.setKeyboardTracking(False)
        self.spinBoxLeftShoulderYaw.setMinimum(-999)
        self.spinBoxLeftShoulderYaw.setMaximum(999)

        self.horizontalLayoutLeftShoulderYaw.addWidget(self.spinBoxLeftShoulderYaw)


        self.formLayoutLeftShoulder.setLayout(2, QFormLayout.FieldRole, self.horizontalLayoutLeftShoulderYaw)


        self.verticalLayoutLeftShoulder.addLayout(self.formLayoutLeftShoulder)


        self.verticalLayoutLeftArm.addLayout(self.verticalLayoutLeftShoulder)

        self.verticalLayoutLeftElbow = QVBoxLayout()
        self.verticalLayoutLeftElbow.setObjectName(u"verticalLayoutLeftElbow")
        self.verticalLayoutLeftElbow.setContentsMargins(-1, -1, -1, 30)
        self.labelLeftElbow = QLabel(self.centralwidget)
        self.labelLeftElbow.setObjectName(u"labelLeftElbow")
        self.labelLeftElbow.setMaximumSize(QSize(16777215, 20))
        self.labelLeftElbow.setFont(font1)

        self.verticalLayoutLeftElbow.addWidget(self.labelLeftElbow)

        self.formLayoutLeftElbow = QFormLayout()
        self.formLayoutLeftElbow.setObjectName(u"formLayoutLeftElbow")
        self.formLayoutLeftElbow.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayoutLeftElbow.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLeftElbowPitch = QLabel(self.centralwidget)
        self.labelLeftElbowPitch.setObjectName(u"labelLeftElbowPitch")
        self.labelLeftElbowPitch.setFont(font2)
        self.labelLeftElbowPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftElbow.setWidget(0, QFormLayout.LabelRole, self.labelLeftElbowPitch)

        self.horizontalLayoutLeftElbowPitch = QHBoxLayout()
        self.horizontalLayoutLeftElbowPitch.setObjectName(u"horizontalLayoutLeftElbowPitch")
        self.labelLeftElbowPitchValue = QLabel(self.centralwidget)
        self.labelLeftElbowPitchValue.setObjectName(u"labelLeftElbowPitchValue")
        self.labelLeftElbowPitchValue.setMinimumSize(QSize(60, 0))
        self.labelLeftElbowPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftElbowPitchValue.setFont(font2)

        self.horizontalLayoutLeftElbowPitch.addWidget(self.labelLeftElbowPitchValue)

        self.spinBoxLeftElbowPitch = QSpinBox(self.centralwidget)
        self.spinBoxLeftElbowPitch.setObjectName(u"spinBoxLeftElbowPitch")
        self.spinBoxLeftElbowPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftElbowPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftElbowPitch.setFont(font2)
        self.spinBoxLeftElbowPitch.setReadOnly(False)
        self.spinBoxLeftElbowPitch.setKeyboardTracking(False)
        self.spinBoxLeftElbowPitch.setMinimum(-999)
        self.spinBoxLeftElbowPitch.setMaximum(999)

        self.horizontalLayoutLeftElbowPitch.addWidget(self.spinBoxLeftElbowPitch)


        self.formLayoutLeftElbow.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutLeftElbowPitch)


        self.verticalLayoutLeftElbow.addLayout(self.formLayoutLeftElbow)


        self.verticalLayoutLeftArm.addLayout(self.verticalLayoutLeftElbow)

        self.verticalLayoutLeftWrist = QVBoxLayout()
        self.verticalLayoutLeftWrist.setObjectName(u"verticalLayoutLeftWrist")
        self.verticalLayoutLeftWrist.setContentsMargins(-1, -1, -1, 0)
        self.labelLeftWrist = QLabel(self.centralwidget)
        self.labelLeftWrist.setObjectName(u"labelLeftWrist")
        self.labelLeftWrist.setMaximumSize(QSize(16777215, 20))
        self.labelLeftWrist.setFont(font1)

        self.verticalLayoutLeftWrist.addWidget(self.labelLeftWrist)

        self.formLayoutLeftWrist = QFormLayout()
        self.formLayoutLeftWrist.setObjectName(u"formLayoutLeftWrist")
        self.formLayoutLeftWrist.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLeftWristPitch = QLabel(self.centralwidget)
        self.labelLeftWristPitch.setObjectName(u"labelLeftWristPitch")
        self.labelLeftWristPitch.setFont(font2)
        self.labelLeftWristPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.labelLeftWristPitch.setIndent(-1)

        self.formLayoutLeftWrist.setWidget(0, QFormLayout.LabelRole, self.labelLeftWristPitch)

        self.labelLeftWristRoll = QLabel(self.centralwidget)
        self.labelLeftWristRoll.setObjectName(u"labelLeftWristRoll")
        self.labelLeftWristRoll.setFont(font2)
        self.labelLeftWristRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftWrist.setWidget(1, QFormLayout.LabelRole, self.labelLeftWristRoll)

        self.labelLeftWristYaw = QLabel(self.centralwidget)
        self.labelLeftWristYaw.setObjectName(u"labelLeftWristYaw")
        self.labelLeftWristYaw.setFont(font2)
        self.labelLeftWristYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftWrist.setWidget(2, QFormLayout.LabelRole, self.labelLeftWristYaw)

        self.horizontalLayoutLeftWristPitch = QHBoxLayout()
        self.horizontalLayoutLeftWristPitch.setObjectName(u"horizontalLayoutLeftWristPitch")
        self.labelLeftWristPitchValue = QLabel(self.centralwidget)
        self.labelLeftWristPitchValue.setObjectName(u"labelLeftWristPitchValue")
        self.labelLeftWristPitchValue.setMinimumSize(QSize(60, 0))
        self.labelLeftWristPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftWristPitchValue.setFont(font2)

        self.horizontalLayoutLeftWristPitch.addWidget(self.labelLeftWristPitchValue)

        self.spinBoxLeftWristPitch = QSpinBox(self.centralwidget)
        self.spinBoxLeftWristPitch.setObjectName(u"spinBoxLeftWristPitch")
        self.spinBoxLeftWristPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftWristPitch.setMaximumSize(QSize(60, 16777215))
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(13)
        self.spinBoxLeftWristPitch.setFont(font3)
        self.spinBoxLeftWristPitch.setReadOnly(False)
        self.spinBoxLeftWristPitch.setKeyboardTracking(False)
        self.spinBoxLeftWristPitch.setMinimum(-999)
        self.spinBoxLeftWristPitch.setMaximum(999)

        self.horizontalLayoutLeftWristPitch.addWidget(self.spinBoxLeftWristPitch)


        self.formLayoutLeftWrist.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutLeftWristPitch)

        self.horizontalLayoutLeftWristRoll = QHBoxLayout()
        self.horizontalLayoutLeftWristRoll.setObjectName(u"horizontalLayoutLeftWristRoll")
        self.labelLeftWristRollValue = QLabel(self.centralwidget)
        self.labelLeftWristRollValue.setObjectName(u"labelLeftWristRollValue")
        self.labelLeftWristRollValue.setMinimumSize(QSize(60, 0))
        self.labelLeftWristRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftWristRollValue.setFont(font2)

        self.horizontalLayoutLeftWristRoll.addWidget(self.labelLeftWristRollValue)

        self.spinBoxLeftWristRoll = QSpinBox(self.centralwidget)
        self.spinBoxLeftWristRoll.setObjectName(u"spinBoxLeftWristRoll")
        self.spinBoxLeftWristRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftWristRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftWristRoll.setFont(font2)
        self.spinBoxLeftWristRoll.setReadOnly(False)
        self.spinBoxLeftWristRoll.setKeyboardTracking(False)
        self.spinBoxLeftWristRoll.setMinimum(-999)
        self.spinBoxLeftWristRoll.setMaximum(999)

        self.horizontalLayoutLeftWristRoll.addWidget(self.spinBoxLeftWristRoll)


        self.formLayoutLeftWrist.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutLeftWristRoll)

        self.horizontalLayoutLeftWristYaw = QHBoxLayout()
        self.horizontalLayoutLeftWristYaw.setObjectName(u"horizontalLayoutLeftWristYaw")
        self.labelLeftWristYawValue = QLabel(self.centralwidget)
        self.labelLeftWristYawValue.setObjectName(u"labelLeftWristYawValue")
        self.labelLeftWristYawValue.setMinimumSize(QSize(60, 0))
        self.labelLeftWristYawValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftWristYawValue.setFont(font2)

        self.horizontalLayoutLeftWristYaw.addWidget(self.labelLeftWristYawValue)

        self.spinBoxLeftWristYaw = QSpinBox(self.centralwidget)
        self.spinBoxLeftWristYaw.setObjectName(u"spinBoxLeftWristYaw")
        self.spinBoxLeftWristYaw.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftWristYaw.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftWristYaw.setFont(font2)
        self.spinBoxLeftWristYaw.setReadOnly(False)
        self.spinBoxLeftWristYaw.setKeyboardTracking(False)
        self.spinBoxLeftWristYaw.setMinimum(-999)
        self.spinBoxLeftWristYaw.setMaximum(999)

        self.horizontalLayoutLeftWristYaw.addWidget(self.spinBoxLeftWristYaw)


        self.formLayoutLeftWrist.setLayout(2, QFormLayout.FieldRole, self.horizontalLayoutLeftWristYaw)


        self.verticalLayoutLeftWrist.addLayout(self.formLayoutLeftWrist)


        self.verticalLayoutLeftArm.addLayout(self.verticalLayoutLeftWrist)


        self.horizontalLayoutArms.addLayout(self.verticalLayoutLeftArm)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayoutArms.addWidget(self.line)

        self.verticalLayoutRightArm = QVBoxLayout()
        self.verticalLayoutRightArm.setObjectName(u"verticalLayoutRightArm")
        self.verticalLayoutRightArm.setContentsMargins(20, -1, -1, -1)
        self.verticalLayoutRightShoulder = QVBoxLayout()
        self.verticalLayoutRightShoulder.setObjectName(u"verticalLayoutRightShoulder")
        self.verticalLayoutRightShoulder.setContentsMargins(-1, -1, -1, 30)
        self.labelRightShoulder = QLabel(self.centralwidget)
        self.labelRightShoulder.setObjectName(u"labelRightShoulder")
        self.labelRightShoulder.setMaximumSize(QSize(16777215, 20))
        self.labelRightShoulder.setFont(font1)

        self.verticalLayoutRightShoulder.addWidget(self.labelRightShoulder)

        self.formLayoutRightShoulder = QFormLayout()
        self.formLayoutRightShoulder.setObjectName(u"formLayoutRightShoulder")
        self.formLayoutRightShoulder.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRightShoulderPitch = QLabel(self.centralwidget)
        self.labelRightShoulderPitch.setObjectName(u"labelRightShoulderPitch")
        self.labelRightShoulderPitch.setFont(font2)
        self.labelRightShoulderPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightShoulder.setWidget(0, QFormLayout.LabelRole, self.labelRightShoulderPitch)

        self.labelRightShoulderRoll = QLabel(self.centralwidget)
        self.labelRightShoulderRoll.setObjectName(u"labelRightShoulderRoll")
        self.labelRightShoulderRoll.setFont(font2)
        self.labelRightShoulderRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightShoulder.setWidget(1, QFormLayout.LabelRole, self.labelRightShoulderRoll)

        self.labelRightShoulderYaw = QLabel(self.centralwidget)
        self.labelRightShoulderYaw.setObjectName(u"labelRightShoulderYaw")
        self.labelRightShoulderYaw.setFont(font2)
        self.labelRightShoulderYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightShoulder.setWidget(2, QFormLayout.LabelRole, self.labelRightShoulderYaw)

        self.horizontalLayoutRightShoulderPitch = QHBoxLayout()
        self.horizontalLayoutRightShoulderPitch.setObjectName(u"horizontalLayoutRightShoulderPitch")
        self.labelRightShoulderPitchValue = QLabel(self.centralwidget)
        self.labelRightShoulderPitchValue.setObjectName(u"labelRightShoulderPitchValue")
        self.labelRightShoulderPitchValue.setMinimumSize(QSize(60, 0))
        self.labelRightShoulderPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightShoulderPitchValue.setFont(font2)

        self.horizontalLayoutRightShoulderPitch.addWidget(self.labelRightShoulderPitchValue)

        self.spinBoxRightShoulderPitch = QSpinBox(self.centralwidget)
        self.spinBoxRightShoulderPitch.setObjectName(u"spinBoxRightShoulderPitch")
        self.spinBoxRightShoulderPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxRightShoulderPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightShoulderPitch.setFont(font2)
        self.spinBoxRightShoulderPitch.setReadOnly(False)
        self.spinBoxRightShoulderPitch.setKeyboardTracking(False)
        self.spinBoxRightShoulderPitch.setMinimum(-999)
        self.spinBoxRightShoulderPitch.setMaximum(999)

        self.horizontalLayoutRightShoulderPitch.addWidget(self.spinBoxRightShoulderPitch)


        self.formLayoutRightShoulder.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutRightShoulderPitch)

        self.horizontalLayoutRightShoulderRoll = QHBoxLayout()
        self.horizontalLayoutRightShoulderRoll.setObjectName(u"horizontalLayoutRightShoulderRoll")
        self.labelRightShoulderRollValue = QLabel(self.centralwidget)
        self.labelRightShoulderRollValue.setObjectName(u"labelRightShoulderRollValue")
        self.labelRightShoulderRollValue.setMinimumSize(QSize(60, 0))
        self.labelRightShoulderRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightShoulderRollValue.setFont(font2)

        self.horizontalLayoutRightShoulderRoll.addWidget(self.labelRightShoulderRollValue)

        self.spinBoxRightShoulderRoll = QSpinBox(self.centralwidget)
        self.spinBoxRightShoulderRoll.setObjectName(u"spinBoxRightShoulderRoll")
        self.spinBoxRightShoulderRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxRightShoulderRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightShoulderRoll.setFont(font2)
        self.spinBoxRightShoulderRoll.setReadOnly(False)
        self.spinBoxRightShoulderRoll.setKeyboardTracking(False)
        self.spinBoxRightShoulderRoll.setMinimum(-999)
        self.spinBoxRightShoulderRoll.setMaximum(999)

        self.horizontalLayoutRightShoulderRoll.addWidget(self.spinBoxRightShoulderRoll)


        self.formLayoutRightShoulder.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutRightShoulderRoll)

        self.horizontalLayoutRightShoulderYaw = QHBoxLayout()
        self.horizontalLayoutRightShoulderYaw.setObjectName(u"horizontalLayoutRightShoulderYaw")
        self.labelRightShoulderYawValue = QLabel(self.centralwidget)
        self.labelRightShoulderYawValue.setObjectName(u"labelRightShoulderYawValue")
        self.labelRightShoulderYawValue.setMinimumSize(QSize(60, 0))
        self.labelRightShoulderYawValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightShoulderYawValue.setFont(font2)

        self.horizontalLayoutRightShoulderYaw.addWidget(self.labelRightShoulderYawValue)

        self.spinBoxRightShoulderYaw = QSpinBox(self.centralwidget)
        self.spinBoxRightShoulderYaw.setObjectName(u"spinBoxRightShoulderYaw")
        self.spinBoxRightShoulderYaw.setMinimumSize(QSize(60, 0))
        self.spinBoxRightShoulderYaw.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightShoulderYaw.setFont(font2)
        self.spinBoxRightShoulderYaw.setReadOnly(False)
        self.spinBoxRightShoulderYaw.setKeyboardTracking(False)
        self.spinBoxRightShoulderYaw.setMinimum(-999)
        self.spinBoxRightShoulderYaw.setMaximum(999)

        self.horizontalLayoutRightShoulderYaw.addWidget(self.spinBoxRightShoulderYaw)


        self.formLayoutRightShoulder.setLayout(2, QFormLayout.FieldRole, self.horizontalLayoutRightShoulderYaw)


        self.verticalLayoutRightShoulder.addLayout(self.formLayoutRightShoulder)


        self.verticalLayoutRightArm.addLayout(self.verticalLayoutRightShoulder)

        self.verticalLayoutRightElbow = QVBoxLayout()
        self.verticalLayoutRightElbow.setObjectName(u"verticalLayoutRightElbow")
        self.verticalLayoutRightElbow.setContentsMargins(-1, -1, -1, 30)
        self.labelRightElbow = QLabel(self.centralwidget)
        self.labelRightElbow.setObjectName(u"labelRightElbow")
        self.labelRightElbow.setMaximumSize(QSize(16777215, 20))
        self.labelRightElbow.setFont(font1)

        self.verticalLayoutRightElbow.addWidget(self.labelRightElbow)

        self.formLayoutRightElbow = QFormLayout()
        self.formLayoutRightElbow.setObjectName(u"formLayoutRightElbow")
        self.formLayoutRightElbow.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayoutRightElbow.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRightElbowPitch = QLabel(self.centralwidget)
        self.labelRightElbowPitch.setObjectName(u"labelRightElbowPitch")
        self.labelRightElbowPitch.setFont(font2)
        self.labelRightElbowPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightElbow.setWidget(0, QFormLayout.LabelRole, self.labelRightElbowPitch)

        self.horizontalLayoutRightElbowPitch = QHBoxLayout()
        self.horizontalLayoutRightElbowPitch.setObjectName(u"horizontalLayoutRightElbowPitch")
        self.labelRightElbowPitchValue = QLabel(self.centralwidget)
        self.labelRightElbowPitchValue.setObjectName(u"labelRightElbowPitchValue")
        self.labelRightElbowPitchValue.setMinimumSize(QSize(60, 0))
        self.labelRightElbowPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightElbowPitchValue.setFont(font2)

        self.horizontalLayoutRightElbowPitch.addWidget(self.labelRightElbowPitchValue)

        self.spinBoxRightElbowPitch = QSpinBox(self.centralwidget)
        self.spinBoxRightElbowPitch.setObjectName(u"spinBoxRightElbowPitch")
        self.spinBoxRightElbowPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxRightElbowPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightElbowPitch.setFont(font2)
        self.spinBoxRightElbowPitch.setReadOnly(False)
        self.spinBoxRightElbowPitch.setKeyboardTracking(False)
        self.spinBoxRightElbowPitch.setMinimum(-999)
        self.spinBoxRightElbowPitch.setMaximum(999)

        self.horizontalLayoutRightElbowPitch.addWidget(self.spinBoxRightElbowPitch)


        self.formLayoutRightElbow.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutRightElbowPitch)


        self.verticalLayoutRightElbow.addLayout(self.formLayoutRightElbow)


        self.verticalLayoutRightArm.addLayout(self.verticalLayoutRightElbow)

        self.verticalLayoutRightWrist = QVBoxLayout()
        self.verticalLayoutRightWrist.setObjectName(u"verticalLayoutRightWrist")
        self.verticalLayoutRightWrist.setContentsMargins(-1, -1, -1, 0)
        self.labelRightWrist = QLabel(self.centralwidget)
        self.labelRightWrist.setObjectName(u"labelRightWrist")
        self.labelRightWrist.setMaximumSize(QSize(16777215, 20))
        self.labelRightWrist.setFont(font1)

        self.verticalLayoutRightWrist.addWidget(self.labelRightWrist)

        self.formLayoutRightWrist = QFormLayout()
        self.formLayoutRightWrist.setObjectName(u"formLayoutRightWrist")
        self.formLayoutRightWrist.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRightWristPitch = QLabel(self.centralwidget)
        self.labelRightWristPitch.setObjectName(u"labelRightWristPitch")
        self.labelRightWristPitch.setFont(font2)
        self.labelRightWristPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightWrist.setWidget(0, QFormLayout.LabelRole, self.labelRightWristPitch)

        self.labelRightWristRoll = QLabel(self.centralwidget)
        self.labelRightWristRoll.setObjectName(u"labelRightWristRoll")
        self.labelRightWristRoll.setFont(font2)
        self.labelRightWristRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightWrist.setWidget(1, QFormLayout.LabelRole, self.labelRightWristRoll)

        self.labelRightWristYaw = QLabel(self.centralwidget)
        self.labelRightWristYaw.setObjectName(u"labelRightWristYaw")
        self.labelRightWristYaw.setFont(font2)
        self.labelRightWristYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightWrist.setWidget(2, QFormLayout.LabelRole, self.labelRightWristYaw)

        self.horizontalLayoutRightWristPitch = QHBoxLayout()
        self.horizontalLayoutRightWristPitch.setObjectName(u"horizontalLayoutRightWristPitch")
        self.labelRightWristPitchValue = QLabel(self.centralwidget)
        self.labelRightWristPitchValue.setObjectName(u"labelRightWristPitchValue")
        self.labelRightWristPitchValue.setMinimumSize(QSize(60, 0))
        self.labelRightWristPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightWristPitchValue.setFont(font2)

        self.horizontalLayoutRightWristPitch.addWidget(self.labelRightWristPitchValue)

        self.spinBoxRightWristPitch = QSpinBox(self.centralwidget)
        self.spinBoxRightWristPitch.setObjectName(u"spinBoxRightWristPitch")
        self.spinBoxRightWristPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxRightWristPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightWristPitch.setFont(font2)
        self.spinBoxRightWristPitch.setReadOnly(False)
        self.spinBoxRightWristPitch.setKeyboardTracking(False)
        self.spinBoxRightWristPitch.setMinimum(-999)
        self.spinBoxRightWristPitch.setMaximum(999)

        self.horizontalLayoutRightWristPitch.addWidget(self.spinBoxRightWristPitch)


        self.formLayoutRightWrist.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutRightWristPitch)

        self.horizontalLayoutRightWristRoll = QHBoxLayout()
        self.horizontalLayoutRightWristRoll.setObjectName(u"horizontalLayoutRightWristRoll")
        self.labelRightWristRollValue = QLabel(self.centralwidget)
        self.labelRightWristRollValue.setObjectName(u"labelRightWristRollValue")
        self.labelRightWristRollValue.setMinimumSize(QSize(60, 0))
        self.labelRightWristRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightWristRollValue.setFont(font2)

        self.horizontalLayoutRightWristRoll.addWidget(self.labelRightWristRollValue)

        self.spinBoxRightWristRoll = QSpinBox(self.centralwidget)
        self.spinBoxRightWristRoll.setObjectName(u"spinBoxRightWristRoll")
        self.spinBoxRightWristRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxRightWristRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightWristRoll.setFont(font2)
        self.spinBoxRightWristRoll.setReadOnly(False)
        self.spinBoxRightWristRoll.setKeyboardTracking(False)
        self.spinBoxRightWristRoll.setMinimum(-999)
        self.spinBoxRightWristRoll.setMaximum(999)

        self.horizontalLayoutRightWristRoll.addWidget(self.spinBoxRightWristRoll)


        self.formLayoutRightWrist.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutRightWristRoll)

        self.horizontalLayoutRightWristYaw = QHBoxLayout()
        self.horizontalLayoutRightWristYaw.setObjectName(u"horizontalLayoutRightWristYaw")
        self.labelRightWristYawValue = QLabel(self.centralwidget)
        self.labelRightWristYawValue.setObjectName(u"labelRightWristYawValue")
        self.labelRightWristYawValue.setMinimumSize(QSize(60, 0))
        self.labelRightWristYawValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightWristYawValue.setFont(font2)

        self.horizontalLayoutRightWristYaw.addWidget(self.labelRightWristYawValue)

        self.spinBoxRightWristYaw = QSpinBox(self.centralwidget)
        self.spinBoxRightWristYaw.setObjectName(u"spinBoxRightWristYaw")
        self.spinBoxRightWristYaw.setMinimumSize(QSize(60, 0))
        self.spinBoxRightWristYaw.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightWristYaw.setFont(font2)
        self.spinBoxRightWristYaw.setReadOnly(False)
        self.spinBoxRightWristYaw.setKeyboardTracking(False)
        self.spinBoxRightWristYaw.setMinimum(-999)
        self.spinBoxRightWristYaw.setMaximum(999)

        self.horizontalLayoutRightWristYaw.addWidget(self.spinBoxRightWristYaw)


        self.formLayoutRightWrist.setLayout(2, QFormLayout.FieldRole, self.horizontalLayoutRightWristYaw)


        self.verticalLayoutRightWrist.addLayout(self.formLayoutRightWrist)


        self.verticalLayoutRightArm.addLayout(self.verticalLayoutRightWrist)


        self.horizontalLayoutArms.addLayout(self.verticalLayoutRightArm)


        self.verticalLayout.addLayout(self.horizontalLayoutArms)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayoutWaistReadOnly = QVBoxLayout()
        self.verticalLayoutWaistReadOnly.setObjectName(u"verticalLayoutWaistReadOnly")
        self.verticalLayoutWaistReadOnly.setContentsMargins(30, -1, 30, -1)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setFont(font2)
        self.radioButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setChecked(True)

        self.verticalLayoutWaistReadOnly.addWidget(self.radioButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutWaistReadOnly.addItem(self.verticalSpacer)

        self.horizontalLayoutWaist = QHBoxLayout()
        self.horizontalLayoutWaist.setObjectName(u"horizontalLayoutWaist")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayoutWaist.addWidget(self.line_4)

        self.verticalLayoutWaist = QVBoxLayout()
        self.verticalLayoutWaist.setObjectName(u"verticalLayoutWaist")
        self.verticalLayoutWaist.setContentsMargins(30, -1, 30, -1)
        self.labelWaist = QLabel(self.centralwidget)
        self.labelWaist.setObjectName(u"labelWaist")
        self.labelWaist.setMaximumSize(QSize(16777215, 20))
        self.labelWaist.setFont(font1)

        self.verticalLayoutWaist.addWidget(self.labelWaist)

        self.formLayoutWaist = QFormLayout()
        self.formLayoutWaist.setObjectName(u"formLayoutWaist")
        self.formLayoutWaist.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelWaistPitch = QLabel(self.centralwidget)
        self.labelWaistPitch.setObjectName(u"labelWaistPitch")
        self.labelWaistPitch.setFont(font2)
        self.labelWaistPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutWaist.setWidget(0, QFormLayout.LabelRole, self.labelWaistPitch)

        self.horizontalLayoutWaistPitch = QHBoxLayout()
        self.horizontalLayoutWaistPitch.setObjectName(u"horizontalLayoutWaistPitch")
        self.labelWaistPitchValue = QLabel(self.centralwidget)
        self.labelWaistPitchValue.setObjectName(u"labelWaistPitchValue")
        self.labelWaistPitchValue.setMinimumSize(QSize(60, 0))
        self.labelWaistPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelWaistPitchValue.setFont(font2)

        self.horizontalLayoutWaistPitch.addWidget(self.labelWaistPitchValue)

        self.spinBoxWaistPitch = QSpinBox(self.centralwidget)
        self.spinBoxWaistPitch.setObjectName(u"spinBoxWaistPitch")
        self.spinBoxWaistPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxWaistPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxWaistPitch.setFont(font2)
        self.spinBoxWaistPitch.setReadOnly(False)
        self.spinBoxWaistPitch.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBoxWaistPitch.setAccelerated(False)
        self.spinBoxWaistPitch.setKeyboardTracking(False)
        self.spinBoxWaistPitch.setMinimum(-999)
        self.spinBoxWaistPitch.setMaximum(999)

        self.horizontalLayoutWaistPitch.addWidget(self.spinBoxWaistPitch)


        self.formLayoutWaist.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutWaistPitch)

        self.labelWaistRoll = QLabel(self.centralwidget)
        self.labelWaistRoll.setObjectName(u"labelWaistRoll")
        self.labelWaistRoll.setFont(font2)
        self.labelWaistRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutWaist.setWidget(1, QFormLayout.LabelRole, self.labelWaistRoll)

        self.horizontalLayoutWaistRoll = QHBoxLayout()
        self.horizontalLayoutWaistRoll.setObjectName(u"horizontalLayoutWaistRoll")
        self.labelWaistRollValue = QLabel(self.centralwidget)
        self.labelWaistRollValue.setObjectName(u"labelWaistRollValue")
        self.labelWaistRollValue.setMinimumSize(QSize(60, 0))
        self.labelWaistRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelWaistRollValue.setFont(font2)

        self.horizontalLayoutWaistRoll.addWidget(self.labelWaistRollValue)

        self.spinBoxWaistRoll = QSpinBox(self.centralwidget)
        self.spinBoxWaistRoll.setObjectName(u"spinBoxWaistRoll")
        self.spinBoxWaistRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxWaistRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxWaistRoll.setFont(font2)
        self.spinBoxWaistRoll.setReadOnly(False)
        self.spinBoxWaistRoll.setKeyboardTracking(False)
        self.spinBoxWaistRoll.setMinimum(-999)
        self.spinBoxWaistRoll.setMaximum(999)

        self.horizontalLayoutWaistRoll.addWidget(self.spinBoxWaistRoll)


        self.formLayoutWaist.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutWaistRoll)

        self.labelWaistYaw = QLabel(self.centralwidget)
        self.labelWaistYaw.setObjectName(u"labelWaistYaw")
        self.labelWaistYaw.setFont(font2)
        self.labelWaistYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutWaist.setWidget(2, QFormLayout.LabelRole, self.labelWaistYaw)

        self.horizontalLayoutWaistYaw = QHBoxLayout()
        self.horizontalLayoutWaistYaw.setObjectName(u"horizontalLayoutWaistYaw")
        self.labelWaistYawValue = QLabel(self.centralwidget)
        self.labelWaistYawValue.setObjectName(u"labelWaistYawValue")
        self.labelWaistYawValue.setMinimumSize(QSize(60, 0))
        self.labelWaistYawValue.setMaximumSize(QSize(60, 16777215))
        self.labelWaistYawValue.setFont(font2)

        self.horizontalLayoutWaistYaw.addWidget(self.labelWaistYawValue)

        self.spinBoxWaistYaw = QSpinBox(self.centralwidget)
        self.spinBoxWaistYaw.setObjectName(u"spinBoxWaistYaw")
        self.spinBoxWaistYaw.setMinimumSize(QSize(60, 0))
        self.spinBoxWaistYaw.setMaximumSize(QSize(60, 16777215))
        self.spinBoxWaistYaw.setFont(font2)
        self.spinBoxWaistYaw.setReadOnly(False)
        self.spinBoxWaistYaw.setKeyboardTracking(False)
        self.spinBoxWaistYaw.setMinimum(-999)
        self.spinBoxWaistYaw.setMaximum(999)

        self.horizontalLayoutWaistYaw.addWidget(self.spinBoxWaistYaw)


        self.formLayoutWaist.setLayout(2, QFormLayout.FieldRole, self.horizontalLayoutWaistYaw)


        self.verticalLayoutWaist.addLayout(self.formLayoutWaist)


        self.horizontalLayoutWaist.addLayout(self.verticalLayoutWaist)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayoutWaist.addWidget(self.line_3)


        self.verticalLayoutWaistReadOnly.addLayout(self.horizontalLayoutWaist)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutWaistReadOnly.addItem(self.verticalSpacer_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutWaistReadOnly.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayoutWaistReadOnly)

        self.verticalLayoutLegs = QVBoxLayout()
        self.verticalLayoutLegs.setObjectName(u"verticalLayoutLegs")
        self.labelLegs = QLabel(self.centralwidget)
        self.labelLegs.setObjectName(u"labelLegs")
        self.labelLegs.setFont(font)
        self.labelLegs.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.labelLegs.setMargin(10)

        self.verticalLayoutLegs.addWidget(self.labelLegs)

        self.horizontalLayoutLegs = QHBoxLayout()
        self.horizontalLayoutLegs.setObjectName(u"horizontalLayoutLegs")
        self.verticalLayoutLeftLeg = QVBoxLayout()
        self.verticalLayoutLeftLeg.setObjectName(u"verticalLayoutLeftLeg")
        self.verticalLayoutLeftLeg.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayoutLeftHip = QVBoxLayout()
        self.verticalLayoutLeftHip.setObjectName(u"verticalLayoutLeftHip")
        self.verticalLayoutLeftHip.setContentsMargins(-1, -1, -1, 30)
        self.labelLeftHip = QLabel(self.centralwidget)
        self.labelLeftHip.setObjectName(u"labelLeftHip")
        self.labelLeftHip.setMaximumSize(QSize(16777215, 20))
        self.labelLeftHip.setFont(font1)

        self.verticalLayoutLeftHip.addWidget(self.labelLeftHip)

        self.formLayoutLeftHip = QFormLayout()
        self.formLayoutLeftHip.setObjectName(u"formLayoutLeftHip")
        self.formLayoutLeftHip.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLeftHipPitch = QLabel(self.centralwidget)
        self.labelLeftHipPitch.setObjectName(u"labelLeftHipPitch")
        self.labelLeftHipPitch.setFont(font2)
        self.labelLeftHipPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftHip.setWidget(0, QFormLayout.LabelRole, self.labelLeftHipPitch)

        self.horizontalLayoutLeftHipPitch = QHBoxLayout()
        self.horizontalLayoutLeftHipPitch.setObjectName(u"horizontalLayoutLeftHipPitch")
        self.labelLeftHipPitchValue = QLabel(self.centralwidget)
        self.labelLeftHipPitchValue.setObjectName(u"labelLeftHipPitchValue")
        self.labelLeftHipPitchValue.setMinimumSize(QSize(60, 0))
        self.labelLeftHipPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftHipPitchValue.setFont(font2)

        self.horizontalLayoutLeftHipPitch.addWidget(self.labelLeftHipPitchValue)

        self.spinBoxLeftHipPitch = QSpinBox(self.centralwidget)
        self.spinBoxLeftHipPitch.setObjectName(u"spinBoxLeftHipPitch")
        self.spinBoxLeftHipPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftHipPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftHipPitch.setFont(font2)
        self.spinBoxLeftHipPitch.setReadOnly(False)
        self.spinBoxLeftHipPitch.setKeyboardTracking(False)
        self.spinBoxLeftHipPitch.setMinimum(-144)
        self.spinBoxLeftHipPitch.setMaximum(165)

        self.horizontalLayoutLeftHipPitch.addWidget(self.spinBoxLeftHipPitch)


        self.formLayoutLeftHip.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutLeftHipPitch)

        self.labelLeftHipRoll = QLabel(self.centralwidget)
        self.labelLeftHipRoll.setObjectName(u"labelLeftHipRoll")
        self.labelLeftHipRoll.setFont(font2)
        self.labelLeftHipRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftHip.setWidget(1, QFormLayout.LabelRole, self.labelLeftHipRoll)

        self.horizontalLayoutLeftHipRoll = QHBoxLayout()
        self.horizontalLayoutLeftHipRoll.setObjectName(u"horizontalLayoutLeftHipRoll")
        self.labelLeftHipRollValue = QLabel(self.centralwidget)
        self.labelLeftHipRollValue.setObjectName(u"labelLeftHipRollValue")
        self.labelLeftHipRollValue.setMinimumSize(QSize(60, 0))
        self.labelLeftHipRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftHipRollValue.setFont(font2)

        self.horizontalLayoutLeftHipRoll.addWidget(self.labelLeftHipRollValue)

        self.spinBoxLeftHipRoll = QSpinBox(self.centralwidget)
        self.spinBoxLeftHipRoll.setObjectName(u"spinBoxLeftHipRoll")
        self.spinBoxLeftHipRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftHipRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftHipRoll.setFont(font2)
        self.spinBoxLeftHipRoll.setReadOnly(False)
        self.spinBoxLeftHipRoll.setKeyboardTracking(False)
        self.spinBoxLeftHipRoll.setMinimum(-30)
        self.spinBoxLeftHipRoll.setMaximum(170)
        self.spinBoxLeftHipRoll.setValue(0)

        self.horizontalLayoutLeftHipRoll.addWidget(self.spinBoxLeftHipRoll)


        self.formLayoutLeftHip.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutLeftHipRoll)

        self.labelLeftHipYaw = QLabel(self.centralwidget)
        self.labelLeftHipYaw.setObjectName(u"labelLeftHipYaw")
        self.labelLeftHipYaw.setFont(font2)
        self.labelLeftHipYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftHip.setWidget(2, QFormLayout.LabelRole, self.labelLeftHipYaw)

        self.horizontalLayoutLeftHipYaw = QHBoxLayout()
        self.horizontalLayoutLeftHipYaw.setObjectName(u"horizontalLayoutLeftHipYaw")
        self.labelLeftHipYawValue = QLabel(self.centralwidget)
        self.labelLeftHipYawValue.setObjectName(u"labelLeftHipYawValue")
        self.labelLeftHipYawValue.setMinimumSize(QSize(60, 0))
        self.labelLeftHipYawValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftHipYawValue.setFont(font2)

        self.horizontalLayoutLeftHipYaw.addWidget(self.labelLeftHipYawValue)

        self.spinBoxLeftHipYaw = QSpinBox(self.centralwidget)
        self.spinBoxLeftHipYaw.setObjectName(u"spinBoxLeftHipYaw")
        self.spinBoxLeftHipYaw.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftHipYaw.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftHipYaw.setFont(font2)
        self.spinBoxLeftHipYaw.setReadOnly(False)
        self.spinBoxLeftHipYaw.setKeyboardTracking(False)
        self.spinBoxLeftHipYaw.setMinimum(-157)
        self.spinBoxLeftHipYaw.setMaximum(157)

        self.horizontalLayoutLeftHipYaw.addWidget(self.spinBoxLeftHipYaw)


        self.formLayoutLeftHip.setLayout(2, QFormLayout.FieldRole, self.horizontalLayoutLeftHipYaw)


        self.verticalLayoutLeftHip.addLayout(self.formLayoutLeftHip)


        self.verticalLayoutLeftLeg.addLayout(self.verticalLayoutLeftHip)

        self.verticalLayoutLeftKnee = QVBoxLayout()
        self.verticalLayoutLeftKnee.setObjectName(u"verticalLayoutLeftKnee")
        self.verticalLayoutLeftKnee.setContentsMargins(-1, -1, -1, 30)
        self.labelLeftKnee = QLabel(self.centralwidget)
        self.labelLeftKnee.setObjectName(u"labelLeftKnee")
        self.labelLeftKnee.setMaximumSize(QSize(16777215, 20))
        self.labelLeftKnee.setFont(font1)

        self.verticalLayoutLeftKnee.addWidget(self.labelLeftKnee)

        self.formLayoutLeftKnee = QFormLayout()
        self.formLayoutLeftKnee.setObjectName(u"formLayoutLeftKnee")
        self.formLayoutLeftKnee.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayoutLeftKnee.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLeftKneePitch = QLabel(self.centralwidget)
        self.labelLeftKneePitch.setObjectName(u"labelLeftKneePitch")
        self.labelLeftKneePitch.setFont(font2)
        self.labelLeftKneePitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftKnee.setWidget(0, QFormLayout.LabelRole, self.labelLeftKneePitch)

        self.horizontalLayoutLeftKneePitch = QHBoxLayout()
        self.horizontalLayoutLeftKneePitch.setObjectName(u"horizontalLayoutLeftKneePitch")
        self.labelLeftKneePitchValue = QLabel(self.centralwidget)
        self.labelLeftKneePitchValue.setObjectName(u"labelLeftKneePitchValue")
        self.labelLeftKneePitchValue.setMinimumSize(QSize(60, 0))
        self.labelLeftKneePitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftKneePitchValue.setFont(font2)

        self.horizontalLayoutLeftKneePitch.addWidget(self.labelLeftKneePitchValue)

        self.spinBoxLeftKneePitch = QSpinBox(self.centralwidget)
        self.spinBoxLeftKneePitch.setObjectName(u"spinBoxLeftKneePitch")
        self.spinBoxLeftKneePitch.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftKneePitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftKneePitch.setFont(font2)
        self.spinBoxLeftKneePitch.setReadOnly(False)
        self.spinBoxLeftKneePitch.setKeyboardTracking(False)
        self.spinBoxLeftKneePitch.setMinimum(-999)
        self.spinBoxLeftKneePitch.setMaximum(999)

        self.horizontalLayoutLeftKneePitch.addWidget(self.spinBoxLeftKneePitch)


        self.formLayoutLeftKnee.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutLeftKneePitch)


        self.verticalLayoutLeftKnee.addLayout(self.formLayoutLeftKnee)


        self.verticalLayoutLeftLeg.addLayout(self.verticalLayoutLeftKnee)

        self.verticalLayoutLeftAnkle = QVBoxLayout()
        self.verticalLayoutLeftAnkle.setObjectName(u"verticalLayoutLeftAnkle")
        self.verticalLayoutLeftAnkle.setContentsMargins(-1, -1, -1, 0)
        self.labelLeftAnkle = QLabel(self.centralwidget)
        self.labelLeftAnkle.setObjectName(u"labelLeftAnkle")
        self.labelLeftAnkle.setMaximumSize(QSize(16777215, 20))
        self.labelLeftAnkle.setFont(font1)

        self.verticalLayoutLeftAnkle.addWidget(self.labelLeftAnkle)

        self.formLayoutLeftAnkle = QFormLayout()
        self.formLayoutLeftAnkle.setObjectName(u"formLayoutLeftAnkle")
        self.formLayoutLeftAnkle.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLeftAnklePitch = QLabel(self.centralwidget)
        self.labelLeftAnklePitch.setObjectName(u"labelLeftAnklePitch")
        self.labelLeftAnklePitch.setFont(font2)
        self.labelLeftAnklePitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftAnkle.setWidget(0, QFormLayout.LabelRole, self.labelLeftAnklePitch)

        self.horizontalLayoutLeftAnklePitch = QHBoxLayout()
        self.horizontalLayoutLeftAnklePitch.setObjectName(u"horizontalLayoutLeftAnklePitch")
        self.labelLeftAnklePitchValue = QLabel(self.centralwidget)
        self.labelLeftAnklePitchValue.setObjectName(u"labelLeftAnklePitchValue")
        self.labelLeftAnklePitchValue.setMinimumSize(QSize(60, 0))
        self.labelLeftAnklePitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftAnklePitchValue.setFont(font2)

        self.horizontalLayoutLeftAnklePitch.addWidget(self.labelLeftAnklePitchValue)

        self.spinBoxLeftAnklePitch = QSpinBox(self.centralwidget)
        self.spinBoxLeftAnklePitch.setObjectName(u"spinBoxLeftAnklePitch")
        self.spinBoxLeftAnklePitch.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftAnklePitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftAnklePitch.setFont(font2)
        self.spinBoxLeftAnklePitch.setReadOnly(False)
        self.spinBoxLeftAnklePitch.setKeyboardTracking(False)
        self.spinBoxLeftAnklePitch.setMinimum(-999)
        self.spinBoxLeftAnklePitch.setMaximum(999)

        self.horizontalLayoutLeftAnklePitch.addWidget(self.spinBoxLeftAnklePitch)


        self.formLayoutLeftAnkle.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutLeftAnklePitch)

        self.labelLeftAnkleRoll = QLabel(self.centralwidget)
        self.labelLeftAnkleRoll.setObjectName(u"labelLeftAnkleRoll")
        self.labelLeftAnkleRoll.setFont(font2)
        self.labelLeftAnkleRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftAnkle.setWidget(1, QFormLayout.LabelRole, self.labelLeftAnkleRoll)

        self.horizontalLayoutLeftAnkleRoll = QHBoxLayout()
        self.horizontalLayoutLeftAnkleRoll.setObjectName(u"horizontalLayoutLeftAnkleRoll")
        self.labelLeftAnkleRollValue = QLabel(self.centralwidget)
        self.labelLeftAnkleRollValue.setObjectName(u"labelLeftAnkleRollValue")
        self.labelLeftAnkleRollValue.setMinimumSize(QSize(60, 0))
        self.labelLeftAnkleRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelLeftAnkleRollValue.setFont(font2)

        self.horizontalLayoutLeftAnkleRoll.addWidget(self.labelLeftAnkleRollValue)

        self.spinBoxLeftAnkleRoll = QSpinBox(self.centralwidget)
        self.spinBoxLeftAnkleRoll.setObjectName(u"spinBoxLeftAnkleRoll")
        self.spinBoxLeftAnkleRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxLeftAnkleRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxLeftAnkleRoll.setFont(font2)
        self.spinBoxLeftAnkleRoll.setReadOnly(False)
        self.spinBoxLeftAnkleRoll.setKeyboardTracking(False)
        self.spinBoxLeftAnkleRoll.setMinimum(-999)
        self.spinBoxLeftAnkleRoll.setMaximum(999)

        self.horizontalLayoutLeftAnkleRoll.addWidget(self.spinBoxLeftAnkleRoll)


        self.formLayoutLeftAnkle.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutLeftAnkleRoll)


        self.verticalLayoutLeftAnkle.addLayout(self.formLayoutLeftAnkle)


        self.verticalLayoutLeftLeg.addLayout(self.verticalLayoutLeftAnkle)


        self.horizontalLayoutLegs.addLayout(self.verticalLayoutLeftLeg)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayoutLegs.addWidget(self.line_2)

        self.verticalLayoutRightLeg = QVBoxLayout()
        self.verticalLayoutRightLeg.setObjectName(u"verticalLayoutRightLeg")
        self.verticalLayoutRightLeg.setContentsMargins(20, -1, -1, -1)
        self.verticalLayoutRightHip = QVBoxLayout()
        self.verticalLayoutRightHip.setObjectName(u"verticalLayoutRightHip")
        self.verticalLayoutRightHip.setContentsMargins(-1, -1, -1, 30)
        self.labelRightHip = QLabel(self.centralwidget)
        self.labelRightHip.setObjectName(u"labelRightHip")
        self.labelRightHip.setMaximumSize(QSize(16777215, 20))
        self.labelRightHip.setFont(font1)

        self.verticalLayoutRightHip.addWidget(self.labelRightHip)

        self.formLayoutRightHip = QFormLayout()
        self.formLayoutRightHip.setObjectName(u"formLayoutRightHip")
        self.formLayoutRightHip.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRightHipPitch = QLabel(self.centralwidget)
        self.labelRightHipPitch.setObjectName(u"labelRightHipPitch")
        self.labelRightHipPitch.setFont(font2)
        self.labelRightHipPitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightHip.setWidget(0, QFormLayout.LabelRole, self.labelRightHipPitch)

        self.labelRightHipRoll = QLabel(self.centralwidget)
        self.labelRightHipRoll.setObjectName(u"labelRightHipRoll")
        self.labelRightHipRoll.setFont(font2)
        self.labelRightHipRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightHip.setWidget(1, QFormLayout.LabelRole, self.labelRightHipRoll)

        self.labelRightHipYaw = QLabel(self.centralwidget)
        self.labelRightHipYaw.setObjectName(u"labelRightHipYaw")
        self.labelRightHipYaw.setFont(font2)
        self.labelRightHipYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightHip.setWidget(2, QFormLayout.LabelRole, self.labelRightHipYaw)

        self.horizontalLayoutRightHipPitch = QHBoxLayout()
        self.horizontalLayoutRightHipPitch.setObjectName(u"horizontalLayoutRightHipPitch")
        self.labelRightHipPitchValue = QLabel(self.centralwidget)
        self.labelRightHipPitchValue.setObjectName(u"labelRightHipPitchValue")
        self.labelRightHipPitchValue.setMinimumSize(QSize(60, 0))
        self.labelRightHipPitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightHipPitchValue.setFont(font2)

        self.horizontalLayoutRightHipPitch.addWidget(self.labelRightHipPitchValue)

        self.spinBoxRightHipPitch = QSpinBox(self.centralwidget)
        self.spinBoxRightHipPitch.setObjectName(u"spinBoxRightHipPitch")
        self.spinBoxRightHipPitch.setMinimumSize(QSize(60, 0))
        self.spinBoxRightHipPitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightHipPitch.setFont(font2)
        self.spinBoxRightHipPitch.setReadOnly(False)
        self.spinBoxRightHipPitch.setKeyboardTracking(False)
        self.spinBoxRightHipPitch.setMinimum(-999)
        self.spinBoxRightHipPitch.setMaximum(999)

        self.horizontalLayoutRightHipPitch.addWidget(self.spinBoxRightHipPitch)


        self.formLayoutRightHip.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutRightHipPitch)

        self.horizontalLayoutRightHipRoll = QHBoxLayout()
        self.horizontalLayoutRightHipRoll.setObjectName(u"horizontalLayoutRightHipRoll")
        self.labelRightHipRollValue = QLabel(self.centralwidget)
        self.labelRightHipRollValue.setObjectName(u"labelRightHipRollValue")
        self.labelRightHipRollValue.setMinimumSize(QSize(60, 0))
        self.labelRightHipRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightHipRollValue.setFont(font2)

        self.horizontalLayoutRightHipRoll.addWidget(self.labelRightHipRollValue)

        self.spinBoxRightHipRoll = QSpinBox(self.centralwidget)
        self.spinBoxRightHipRoll.setObjectName(u"spinBoxRightHipRoll")
        self.spinBoxRightHipRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxRightHipRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightHipRoll.setFont(font2)
        self.spinBoxRightHipRoll.setReadOnly(False)
        self.spinBoxRightHipRoll.setKeyboardTracking(False)
        self.spinBoxRightHipRoll.setMinimum(-999)
        self.spinBoxRightHipRoll.setMaximum(999)

        self.horizontalLayoutRightHipRoll.addWidget(self.spinBoxRightHipRoll)


        self.formLayoutRightHip.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutRightHipRoll)

        self.horizontalLayoutRightHipYaw = QHBoxLayout()
        self.horizontalLayoutRightHipYaw.setObjectName(u"horizontalLayoutRightHipYaw")
        self.labelRightHipYawValue = QLabel(self.centralwidget)
        self.labelRightHipYawValue.setObjectName(u"labelRightHipYawValue")
        self.labelRightHipYawValue.setMinimumSize(QSize(60, 0))
        self.labelRightHipYawValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightHipYawValue.setFont(font2)

        self.horizontalLayoutRightHipYaw.addWidget(self.labelRightHipYawValue)

        self.spinBoxRightHipYaw = QSpinBox(self.centralwidget)
        self.spinBoxRightHipYaw.setObjectName(u"spinBoxRightHipYaw")
        self.spinBoxRightHipYaw.setMinimumSize(QSize(60, 0))
        self.spinBoxRightHipYaw.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightHipYaw.setFont(font2)
        self.spinBoxRightHipYaw.setReadOnly(False)
        self.spinBoxRightHipYaw.setKeyboardTracking(False)
        self.spinBoxRightHipYaw.setMinimum(-999)
        self.spinBoxRightHipYaw.setMaximum(999)

        self.horizontalLayoutRightHipYaw.addWidget(self.spinBoxRightHipYaw)


        self.formLayoutRightHip.setLayout(2, QFormLayout.FieldRole, self.horizontalLayoutRightHipYaw)


        self.verticalLayoutRightHip.addLayout(self.formLayoutRightHip)


        self.verticalLayoutRightLeg.addLayout(self.verticalLayoutRightHip)

        self.verticalLayoutRightKnee = QVBoxLayout()
        self.verticalLayoutRightKnee.setObjectName(u"verticalLayoutRightKnee")
        self.verticalLayoutRightKnee.setContentsMargins(-1, -1, -1, 30)
        self.labelRightKnee = QLabel(self.centralwidget)
        self.labelRightKnee.setObjectName(u"labelRightKnee")
        self.labelRightKnee.setMaximumSize(QSize(16777215, 20))
        self.labelRightKnee.setFont(font1)

        self.verticalLayoutRightKnee.addWidget(self.labelRightKnee)

        self.formLayoutRightKnee = QFormLayout()
        self.formLayoutRightKnee.setObjectName(u"formLayoutRightKnee")
        self.formLayoutRightKnee.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayoutRightKnee.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRightKneePitch = QLabel(self.centralwidget)
        self.labelRightKneePitch.setObjectName(u"labelRightKneePitch")
        self.labelRightKneePitch.setFont(font2)
        self.labelRightKneePitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightKnee.setWidget(0, QFormLayout.LabelRole, self.labelRightKneePitch)

        self.horizontalLayoutRightKneePitch = QHBoxLayout()
        self.horizontalLayoutRightKneePitch.setObjectName(u"horizontalLayoutRightKneePitch")
        self.labelRightKneePitchValue = QLabel(self.centralwidget)
        self.labelRightKneePitchValue.setObjectName(u"labelRightKneePitchValue")
        self.labelRightKneePitchValue.setMinimumSize(QSize(60, 0))
        self.labelRightKneePitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightKneePitchValue.setFont(font2)

        self.horizontalLayoutRightKneePitch.addWidget(self.labelRightKneePitchValue)

        self.spinBoxRightKneePitch = QSpinBox(self.centralwidget)
        self.spinBoxRightKneePitch.setObjectName(u"spinBoxRightKneePitch")
        self.spinBoxRightKneePitch.setMinimumSize(QSize(60, 0))
        self.spinBoxRightKneePitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightKneePitch.setFont(font2)
        self.spinBoxRightKneePitch.setReadOnly(False)
        self.spinBoxRightKneePitch.setKeyboardTracking(False)
        self.spinBoxRightKneePitch.setMinimum(-999)
        self.spinBoxRightKneePitch.setMaximum(999)

        self.horizontalLayoutRightKneePitch.addWidget(self.spinBoxRightKneePitch)


        self.formLayoutRightKnee.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutRightKneePitch)


        self.verticalLayoutRightKnee.addLayout(self.formLayoutRightKnee)


        self.verticalLayoutRightLeg.addLayout(self.verticalLayoutRightKnee)

        self.verticalLayoutRightAnkle = QVBoxLayout()
        self.verticalLayoutRightAnkle.setObjectName(u"verticalLayoutRightAnkle")
        self.verticalLayoutRightAnkle.setContentsMargins(-1, -1, -1, 0)
        self.labelRightAnkle = QLabel(self.centralwidget)
        self.labelRightAnkle.setObjectName(u"labelRightAnkle")
        self.labelRightAnkle.setMaximumSize(QSize(16777215, 20))
        self.labelRightAnkle.setFont(font1)

        self.verticalLayoutRightAnkle.addWidget(self.labelRightAnkle)

        self.formLayoutRightAnkle = QFormLayout()
        self.formLayoutRightAnkle.setObjectName(u"formLayoutRightAnkle")
        self.formLayoutRightAnkle.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelRightAnklePitch = QLabel(self.centralwidget)
        self.labelRightAnklePitch.setObjectName(u"labelRightAnklePitch")
        self.labelRightAnklePitch.setFont(font2)
        self.labelRightAnklePitch.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightAnkle.setWidget(0, QFormLayout.LabelRole, self.labelRightAnklePitch)

        self.horizontalLayoutRightAnklePitch = QHBoxLayout()
        self.horizontalLayoutRightAnklePitch.setObjectName(u"horizontalLayoutRightAnklePitch")
        self.labelRightAnklePitchValue = QLabel(self.centralwidget)
        self.labelRightAnklePitchValue.setObjectName(u"labelRightAnklePitchValue")
        self.labelRightAnklePitchValue.setMinimumSize(QSize(60, 0))
        self.labelRightAnklePitchValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightAnklePitchValue.setFont(font2)

        self.horizontalLayoutRightAnklePitch.addWidget(self.labelRightAnklePitchValue)

        self.spinBoxRightAnklePitch = QSpinBox(self.centralwidget)
        self.spinBoxRightAnklePitch.setObjectName(u"spinBoxRightAnklePitch")
        self.spinBoxRightAnklePitch.setMinimumSize(QSize(60, 0))
        self.spinBoxRightAnklePitch.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightAnklePitch.setFont(font2)
        self.spinBoxRightAnklePitch.setReadOnly(False)
        self.spinBoxRightAnklePitch.setKeyboardTracking(False)
        self.spinBoxRightAnklePitch.setMinimum(-999)
        self.spinBoxRightAnklePitch.setMaximum(999)

        self.horizontalLayoutRightAnklePitch.addWidget(self.spinBoxRightAnklePitch)


        self.formLayoutRightAnkle.setLayout(0, QFormLayout.FieldRole, self.horizontalLayoutRightAnklePitch)

        self.labelRightAnkleRoll = QLabel(self.centralwidget)
        self.labelRightAnkleRoll.setObjectName(u"labelRightAnkleRoll")
        self.labelRightAnkleRoll.setFont(font2)
        self.labelRightAnkleRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightAnkle.setWidget(1, QFormLayout.LabelRole, self.labelRightAnkleRoll)

        self.horizontalLayoutRightAnkleRoll = QHBoxLayout()
        self.horizontalLayoutRightAnkleRoll.setObjectName(u"horizontalLayoutRightAnkleRoll")
        self.labelRightAnkleRollValue = QLabel(self.centralwidget)
        self.labelRightAnkleRollValue.setObjectName(u"labelRightAnkleRollValue")
        self.labelRightAnkleRollValue.setMinimumSize(QSize(60, 0))
        self.labelRightAnkleRollValue.setMaximumSize(QSize(60, 16777215))
        self.labelRightAnkleRollValue.setFont(font2)

        self.horizontalLayoutRightAnkleRoll.addWidget(self.labelRightAnkleRollValue)

        self.spinBoxRightAnkleRoll = QSpinBox(self.centralwidget)
        self.spinBoxRightAnkleRoll.setObjectName(u"spinBoxRightAnkleRoll")
        self.spinBoxRightAnkleRoll.setMinimumSize(QSize(60, 0))
        self.spinBoxRightAnkleRoll.setMaximumSize(QSize(60, 16777215))
        self.spinBoxRightAnkleRoll.setFont(font2)
        self.spinBoxRightAnkleRoll.setReadOnly(False)
        self.spinBoxRightAnkleRoll.setKeyboardTracking(False)
        self.spinBoxRightAnkleRoll.setMinimum(-999)
        self.spinBoxRightAnkleRoll.setMaximum(999)

        self.horizontalLayoutRightAnkleRoll.addWidget(self.spinBoxRightAnkleRoll)


        self.formLayoutRightAnkle.setLayout(1, QFormLayout.FieldRole, self.horizontalLayoutRightAnkleRoll)


        self.verticalLayoutRightAnkle.addLayout(self.formLayoutRightAnkle)


        self.verticalLayoutRightLeg.addLayout(self.verticalLayoutRightAnkle)


        self.horizontalLayoutLegs.addLayout(self.verticalLayoutRightLeg)


        self.verticalLayoutLegs.addLayout(self.horizontalLayoutLegs)


        self.horizontalLayout.addLayout(self.verticalLayoutLegs)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        G1ControlPanel.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(G1ControlPanel)
        self.statusbar.setObjectName(u"statusbar")
        G1ControlPanel.setStatusBar(self.statusbar)

        self.retranslateUi(G1ControlPanel)

        QMetaObject.connectSlotsByName(G1ControlPanel)
    # setupUi

    def retranslateUi(self, G1ControlPanel):
        G1ControlPanel.setWindowTitle(QCoreApplication.translate("G1ControlPanel", u"G1 Control Panel", None))
        self.labelArms.setText(QCoreApplication.translate("G1ControlPanel", u"Arms", None))
        self.labelLeftShoulder.setText(QCoreApplication.translate("G1ControlPanel", u"Left Shoulder", None))
        self.labelLeftShoulderPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelLeftShoulderPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.spinBoxLeftShoulderPitch.setSpecialValueText("")
        self.labelLeftShoulderRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelLeftShoulderRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftShoulderYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelLeftShoulderYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftElbow.setText(QCoreApplication.translate("G1ControlPanel", u"Left Elbow", None))
        self.labelLeftElbowPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelLeftElbowPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftWrist.setText(QCoreApplication.translate("G1ControlPanel", u"Left Wrist", None))
        self.labelLeftWristPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelLeftWristRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelLeftWristYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelLeftWristPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftWristRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftWristYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightShoulder.setText(QCoreApplication.translate("G1ControlPanel", u"Right Shoulder", None))
        self.labelRightShoulderPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelRightShoulderRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelRightShoulderYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelRightShoulderPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightShoulderRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightShoulderYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightElbow.setText(QCoreApplication.translate("G1ControlPanel", u"Right Elbow", None))
        self.labelRightElbowPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelRightElbowPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightWrist.setText(QCoreApplication.translate("G1ControlPanel", u"Right Wrist", None))
        self.labelRightWristPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelRightWristRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelRightWristYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelRightWristPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightWristRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightWristYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.radioButton.setText(QCoreApplication.translate("G1ControlPanel", u"Read Only", None))
        self.labelWaist.setText(QCoreApplication.translate("G1ControlPanel", u"Waist", None))
        self.labelWaistPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelWaistPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelWaistRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelWaistRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelWaistYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelWaistYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLegs.setText(QCoreApplication.translate("G1ControlPanel", u"Legs", None))
        self.labelLeftHip.setText(QCoreApplication.translate("G1ControlPanel", u"Left Hip", None))
        self.labelLeftHipPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelLeftHipPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftHipRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelLeftHipRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftHipYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelLeftHipYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftKnee.setText(QCoreApplication.translate("G1ControlPanel", u"Left Knee", None))
        self.labelLeftKneePitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelLeftKneePitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftAnkle.setText(QCoreApplication.translate("G1ControlPanel", u"Left Ankle", None))
        self.labelLeftAnklePitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelLeftAnklePitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelLeftAnkleRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelLeftAnkleRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightHip.setText(QCoreApplication.translate("G1ControlPanel", u"Right Hip", None))
        self.labelRightHipPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelRightHipRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelRightHipYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelRightHipPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightHipRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightHipYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightKnee.setText(QCoreApplication.translate("G1ControlPanel", u"Right Knee", None))
        self.labelRightKneePitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelRightKneePitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightAnkle.setText(QCoreApplication.translate("G1ControlPanel", u"Right Ankle", None))
        self.labelRightAnklePitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelRightAnklePitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelRightAnkleRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelRightAnkleRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
    # retranslateUi

