# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'G1ControlPanel.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_G1ControlPanel(object):
    def setupUi(self, G1ControlPanel):
        if not G1ControlPanel.objectName():
            G1ControlPanel.setObjectName(u"G1ControlPanel")
        G1ControlPanel.resize(1465, 517)
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
        self.horizontalLayoutLabelArms = QHBoxLayout()
        self.horizontalLayoutLabelArms.setObjectName(u"horizontalLayoutLabelArms")
        self.horizontalLayoutLabelArms.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutLabelArms.addItem(self.horizontalSpacer_3)

        self.radioButtonArms = QRadioButton(self.centralwidget)
        self.radioButtonArms.setObjectName(u"radioButtonArms")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.radioButtonArms.setFont(font)
        self.radioButtonArms.setAutoExclusive(False)

        self.horizontalLayoutLabelArms.addWidget(self.radioButtonArms)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutLabelArms.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayoutLabelArms)

        self.horizontalLayoutArms = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayoutArms.setSpacing(-1)
#endif
        self.horizontalLayoutArms.setObjectName(u"horizontalLayoutArms")
        self.horizontalLayoutArms.setContentsMargins(-1, 0, -1, -1)
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

        self.formLayoutLeftShoulder.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelLeftShoulderPitch)

        self.horizontalLayoutLeftShoulderPitch = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayoutLeftShoulderPitch.setSpacing(-1)
#endif
        self.horizontalLayoutLeftShoulderPitch.setObjectName(u"horizontalLayoutLeftShoulderPitch")
        self.labelLeftShoulderPitchValue = QLabel(self.centralwidget)
        self.labelLeftShoulderPitchValue.setObjectName(u"labelLeftShoulderPitchValue")
        self.labelLeftShoulderPitchValue.setMinimumSize(QSize(70, 0))
        self.labelLeftShoulderPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftShoulderPitchValue.setFont(font2)

        self.horizontalLayoutLeftShoulderPitch.addWidget(self.labelLeftShoulderPitchValue)

        self.doubleSpinBoxLeftShoulderPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftShoulderPitch.setObjectName(u"doubleSpinBoxLeftShoulderPitch")
        self.doubleSpinBoxLeftShoulderPitch.setEnabled(False)
        self.doubleSpinBoxLeftShoulderPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftShoulderPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftShoulderPitch.setFont(font2)
        self.doubleSpinBoxLeftShoulderPitch.setMouseTracking(False)
        self.doubleSpinBoxLeftShoulderPitch.setReadOnly(False)
        self.doubleSpinBoxLeftShoulderPitch.setKeyboardTracking(False)
        self.doubleSpinBoxLeftShoulderPitch.setMinimum(-999.990000000000009)
        self.doubleSpinBoxLeftShoulderPitch.setMaximum(999.990000000000009)

        self.horizontalLayoutLeftShoulderPitch.addWidget(self.doubleSpinBoxLeftShoulderPitch)


        self.formLayoutLeftShoulder.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftShoulderPitch)

        self.labelLeftShoulderRoll = QLabel(self.centralwidget)
        self.labelLeftShoulderRoll.setObjectName(u"labelLeftShoulderRoll")
        self.labelLeftShoulderRoll.setFont(font2)
        self.labelLeftShoulderRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftShoulder.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelLeftShoulderRoll)

        self.horizontalLayoutLeftShoulderRoll = QHBoxLayout()
        self.horizontalLayoutLeftShoulderRoll.setObjectName(u"horizontalLayoutLeftShoulderRoll")
        self.labelLeftShoulderRollValue = QLabel(self.centralwidget)
        self.labelLeftShoulderRollValue.setObjectName(u"labelLeftShoulderRollValue")
        self.labelLeftShoulderRollValue.setMinimumSize(QSize(70, 0))
        self.labelLeftShoulderRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftShoulderRollValue.setFont(font2)

        self.horizontalLayoutLeftShoulderRoll.addWidget(self.labelLeftShoulderRollValue)

        self.doubleSpinBoxLeftShoulderRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftShoulderRoll.setObjectName(u"doubleSpinBoxLeftShoulderRoll")
        self.doubleSpinBoxLeftShoulderRoll.setEnabled(False)
        self.doubleSpinBoxLeftShoulderRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftShoulderRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftShoulderRoll.setFont(font2)
        self.doubleSpinBoxLeftShoulderRoll.setReadOnly(False)
        self.doubleSpinBoxLeftShoulderRoll.setKeyboardTracking(False)
        self.doubleSpinBoxLeftShoulderRoll.setMinimum(-999.990000000000009)
        self.doubleSpinBoxLeftShoulderRoll.setMaximum(999.990000000000009)

        self.horizontalLayoutLeftShoulderRoll.addWidget(self.doubleSpinBoxLeftShoulderRoll)


        self.formLayoutLeftShoulder.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftShoulderRoll)

        self.labelLeftShoulderYaw = QLabel(self.centralwidget)
        self.labelLeftShoulderYaw.setObjectName(u"labelLeftShoulderYaw")
        self.labelLeftShoulderYaw.setFont(font2)
        self.labelLeftShoulderYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftShoulder.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelLeftShoulderYaw)

        self.horizontalLayoutLeftShoulderYaw = QHBoxLayout()
        self.horizontalLayoutLeftShoulderYaw.setObjectName(u"horizontalLayoutLeftShoulderYaw")
        self.labelLeftShoulderYawValue = QLabel(self.centralwidget)
        self.labelLeftShoulderYawValue.setObjectName(u"labelLeftShoulderYawValue")
        self.labelLeftShoulderYawValue.setMinimumSize(QSize(70, 0))
        self.labelLeftShoulderYawValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftShoulderYawValue.setFont(font2)

        self.horizontalLayoutLeftShoulderYaw.addWidget(self.labelLeftShoulderYawValue)

        self.doubleSpinBoxLeftShoulderYaw = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftShoulderYaw.setObjectName(u"doubleSpinBoxLeftShoulderYaw")
        self.doubleSpinBoxLeftShoulderYaw.setEnabled(False)
        self.doubleSpinBoxLeftShoulderYaw.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftShoulderYaw.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftShoulderYaw.setFont(font2)
        self.doubleSpinBoxLeftShoulderYaw.setReadOnly(False)
        self.doubleSpinBoxLeftShoulderYaw.setKeyboardTracking(False)
        self.doubleSpinBoxLeftShoulderYaw.setMinimum(-999.990000000000009)
        self.doubleSpinBoxLeftShoulderYaw.setMaximum(999.990000000000009)

        self.horizontalLayoutLeftShoulderYaw.addWidget(self.doubleSpinBoxLeftShoulderYaw)


        self.formLayoutLeftShoulder.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftShoulderYaw)


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

        self.formLayoutLeftElbow.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelLeftElbowPitch)

        self.horizontalLayoutLeftElbowPitch = QHBoxLayout()
        self.horizontalLayoutLeftElbowPitch.setObjectName(u"horizontalLayoutLeftElbowPitch")
        self.labelLeftElbowPitchValue = QLabel(self.centralwidget)
        self.labelLeftElbowPitchValue.setObjectName(u"labelLeftElbowPitchValue")
        self.labelLeftElbowPitchValue.setMinimumSize(QSize(70, 0))
        self.labelLeftElbowPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftElbowPitchValue.setFont(font2)

        self.horizontalLayoutLeftElbowPitch.addWidget(self.labelLeftElbowPitchValue)

        self.doubleSpinBoxLeftElbowPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftElbowPitch.setObjectName(u"doubleSpinBoxLeftElbowPitch")
        self.doubleSpinBoxLeftElbowPitch.setEnabled(False)
        self.doubleSpinBoxLeftElbowPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftElbowPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftElbowPitch.setFont(font2)
        self.doubleSpinBoxLeftElbowPitch.setReadOnly(False)
        self.doubleSpinBoxLeftElbowPitch.setKeyboardTracking(False)
        self.doubleSpinBoxLeftElbowPitch.setMinimum(-999.990000000000009)
        self.doubleSpinBoxLeftElbowPitch.setMaximum(999.990000000000009)

        self.horizontalLayoutLeftElbowPitch.addWidget(self.doubleSpinBoxLeftElbowPitch)


        self.formLayoutLeftElbow.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftElbowPitch)


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

        self.formLayoutLeftWrist.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelLeftWristPitch)

        self.labelLeftWristRoll = QLabel(self.centralwidget)
        self.labelLeftWristRoll.setObjectName(u"labelLeftWristRoll")
        self.labelLeftWristRoll.setFont(font2)
        self.labelLeftWristRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftWrist.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelLeftWristRoll)

        self.labelLeftWristYaw = QLabel(self.centralwidget)
        self.labelLeftWristYaw.setObjectName(u"labelLeftWristYaw")
        self.labelLeftWristYaw.setFont(font2)
        self.labelLeftWristYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftWrist.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelLeftWristYaw)

        self.horizontalLayoutLeftWristPitch = QHBoxLayout()
        self.horizontalLayoutLeftWristPitch.setObjectName(u"horizontalLayoutLeftWristPitch")
        self.labelLeftWristPitchValue = QLabel(self.centralwidget)
        self.labelLeftWristPitchValue.setObjectName(u"labelLeftWristPitchValue")
        self.labelLeftWristPitchValue.setMinimumSize(QSize(70, 0))
        self.labelLeftWristPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftWristPitchValue.setFont(font2)

        self.horizontalLayoutLeftWristPitch.addWidget(self.labelLeftWristPitchValue)

        self.doubleSpinBoxLeftWristPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftWristPitch.setObjectName(u"doubleSpinBoxLeftWristPitch")
        self.doubleSpinBoxLeftWristPitch.setEnabled(False)
        self.doubleSpinBoxLeftWristPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftWristPitch.setMaximumSize(QSize(90, 16777215))
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(13)
        self.doubleSpinBoxLeftWristPitch.setFont(font3)
        self.doubleSpinBoxLeftWristPitch.setReadOnly(False)
        self.doubleSpinBoxLeftWristPitch.setKeyboardTracking(False)
        self.doubleSpinBoxLeftWristPitch.setMinimum(-999.990000000000009)
        self.doubleSpinBoxLeftWristPitch.setMaximum(999.990000000000009)

        self.horizontalLayoutLeftWristPitch.addWidget(self.doubleSpinBoxLeftWristPitch)


        self.formLayoutLeftWrist.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftWristPitch)

        self.horizontalLayoutLeftWristRoll = QHBoxLayout()
        self.horizontalLayoutLeftWristRoll.setObjectName(u"horizontalLayoutLeftWristRoll")
        self.labelLeftWristRollValue = QLabel(self.centralwidget)
        self.labelLeftWristRollValue.setObjectName(u"labelLeftWristRollValue")
        self.labelLeftWristRollValue.setMinimumSize(QSize(70, 0))
        self.labelLeftWristRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftWristRollValue.setFont(font2)

        self.horizontalLayoutLeftWristRoll.addWidget(self.labelLeftWristRollValue)

        self.doubleSpinBoxLeftWristRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftWristRoll.setObjectName(u"doubleSpinBoxLeftWristRoll")
        self.doubleSpinBoxLeftWristRoll.setEnabled(False)
        self.doubleSpinBoxLeftWristRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftWristRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftWristRoll.setFont(font2)
        self.doubleSpinBoxLeftWristRoll.setReadOnly(False)
        self.doubleSpinBoxLeftWristRoll.setKeyboardTracking(False)
        self.doubleSpinBoxLeftWristRoll.setMinimum(-999.990000000000009)
        self.doubleSpinBoxLeftWristRoll.setMaximum(999.990000000000009)

        self.horizontalLayoutLeftWristRoll.addWidget(self.doubleSpinBoxLeftWristRoll)


        self.formLayoutLeftWrist.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftWristRoll)

        self.horizontalLayoutLeftWristYaw = QHBoxLayout()
        self.horizontalLayoutLeftWristYaw.setObjectName(u"horizontalLayoutLeftWristYaw")
        self.labelLeftWristYawValue = QLabel(self.centralwidget)
        self.labelLeftWristYawValue.setObjectName(u"labelLeftWristYawValue")
        self.labelLeftWristYawValue.setMinimumSize(QSize(70, 0))
        self.labelLeftWristYawValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftWristYawValue.setFont(font2)

        self.horizontalLayoutLeftWristYaw.addWidget(self.labelLeftWristYawValue)

        self.doubleSpinBoxLeftWristYaw = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftWristYaw.setObjectName(u"doubleSpinBoxLeftWristYaw")
        self.doubleSpinBoxLeftWristYaw.setEnabled(False)
        self.doubleSpinBoxLeftWristYaw.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftWristYaw.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftWristYaw.setFont(font2)
        self.doubleSpinBoxLeftWristYaw.setReadOnly(False)
        self.doubleSpinBoxLeftWristYaw.setKeyboardTracking(False)
        self.doubleSpinBoxLeftWristYaw.setMinimum(-999.990000000000009)
        self.doubleSpinBoxLeftWristYaw.setMaximum(999.990000000000009)

        self.horizontalLayoutLeftWristYaw.addWidget(self.doubleSpinBoxLeftWristYaw)


        self.formLayoutLeftWrist.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftWristYaw)


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

        self.formLayoutRightShoulder.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelRightShoulderPitch)

        self.labelRightShoulderRoll = QLabel(self.centralwidget)
        self.labelRightShoulderRoll.setObjectName(u"labelRightShoulderRoll")
        self.labelRightShoulderRoll.setFont(font2)
        self.labelRightShoulderRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightShoulder.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelRightShoulderRoll)

        self.labelRightShoulderYaw = QLabel(self.centralwidget)
        self.labelRightShoulderYaw.setObjectName(u"labelRightShoulderYaw")
        self.labelRightShoulderYaw.setFont(font2)
        self.labelRightShoulderYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightShoulder.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelRightShoulderYaw)

        self.horizontalLayoutRightShoulderPitch = QHBoxLayout()
        self.horizontalLayoutRightShoulderPitch.setObjectName(u"horizontalLayoutRightShoulderPitch")
        self.labelRightShoulderPitchValue = QLabel(self.centralwidget)
        self.labelRightShoulderPitchValue.setObjectName(u"labelRightShoulderPitchValue")
        self.labelRightShoulderPitchValue.setMinimumSize(QSize(70, 0))
        self.labelRightShoulderPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightShoulderPitchValue.setFont(font2)

        self.horizontalLayoutRightShoulderPitch.addWidget(self.labelRightShoulderPitchValue)

        self.doubleSpinBoxRightShoulderPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightShoulderPitch.setObjectName(u"doubleSpinBoxRightShoulderPitch")
        self.doubleSpinBoxRightShoulderPitch.setEnabled(False)
        self.doubleSpinBoxRightShoulderPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightShoulderPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightShoulderPitch.setFont(font2)
        self.doubleSpinBoxRightShoulderPitch.setReadOnly(False)
        self.doubleSpinBoxRightShoulderPitch.setKeyboardTracking(False)
        self.doubleSpinBoxRightShoulderPitch.setMinimum(-999.990000000000009)
        self.doubleSpinBoxRightShoulderPitch.setMaximum(999.990000000000009)

        self.horizontalLayoutRightShoulderPitch.addWidget(self.doubleSpinBoxRightShoulderPitch)


        self.formLayoutRightShoulder.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightShoulderPitch)

        self.horizontalLayoutRightShoulderRoll = QHBoxLayout()
        self.horizontalLayoutRightShoulderRoll.setObjectName(u"horizontalLayoutRightShoulderRoll")
        self.labelRightShoulderRollValue = QLabel(self.centralwidget)
        self.labelRightShoulderRollValue.setObjectName(u"labelRightShoulderRollValue")
        self.labelRightShoulderRollValue.setMinimumSize(QSize(70, 0))
        self.labelRightShoulderRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightShoulderRollValue.setFont(font2)

        self.horizontalLayoutRightShoulderRoll.addWidget(self.labelRightShoulderRollValue)

        self.doubleSpinBoxRightShoulderRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightShoulderRoll.setObjectName(u"doubleSpinBoxRightShoulderRoll")
        self.doubleSpinBoxRightShoulderRoll.setEnabled(False)
        self.doubleSpinBoxRightShoulderRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightShoulderRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightShoulderRoll.setFont(font2)
        self.doubleSpinBoxRightShoulderRoll.setReadOnly(False)
        self.doubleSpinBoxRightShoulderRoll.setKeyboardTracking(False)
        self.doubleSpinBoxRightShoulderRoll.setMinimum(-999.990000000000009)
        self.doubleSpinBoxRightShoulderRoll.setMaximum(999.990000000000009)

        self.horizontalLayoutRightShoulderRoll.addWidget(self.doubleSpinBoxRightShoulderRoll)


        self.formLayoutRightShoulder.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightShoulderRoll)

        self.horizontalLayoutRightShoulderYaw = QHBoxLayout()
        self.horizontalLayoutRightShoulderYaw.setObjectName(u"horizontalLayoutRightShoulderYaw")
        self.labelRightShoulderYawValue = QLabel(self.centralwidget)
        self.labelRightShoulderYawValue.setObjectName(u"labelRightShoulderYawValue")
        self.labelRightShoulderYawValue.setMinimumSize(QSize(70, 0))
        self.labelRightShoulderYawValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightShoulderYawValue.setFont(font2)

        self.horizontalLayoutRightShoulderYaw.addWidget(self.labelRightShoulderYawValue)

        self.doubleSpinBoxRightShoulderYaw = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightShoulderYaw.setObjectName(u"doubleSpinBoxRightShoulderYaw")
        self.doubleSpinBoxRightShoulderYaw.setEnabled(False)
        self.doubleSpinBoxRightShoulderYaw.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightShoulderYaw.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightShoulderYaw.setFont(font2)
        self.doubleSpinBoxRightShoulderYaw.setReadOnly(False)
        self.doubleSpinBoxRightShoulderYaw.setKeyboardTracking(False)
        self.doubleSpinBoxRightShoulderYaw.setMinimum(-999.990000000000009)
        self.doubleSpinBoxRightShoulderYaw.setMaximum(999.990000000000009)

        self.horizontalLayoutRightShoulderYaw.addWidget(self.doubleSpinBoxRightShoulderYaw)


        self.formLayoutRightShoulder.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightShoulderYaw)


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

        self.formLayoutRightElbow.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelRightElbowPitch)

        self.horizontalLayoutRightElbowPitch = QHBoxLayout()
        self.horizontalLayoutRightElbowPitch.setObjectName(u"horizontalLayoutRightElbowPitch")
        self.labelRightElbowPitchValue = QLabel(self.centralwidget)
        self.labelRightElbowPitchValue.setObjectName(u"labelRightElbowPitchValue")
        self.labelRightElbowPitchValue.setMinimumSize(QSize(70, 0))
        self.labelRightElbowPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightElbowPitchValue.setFont(font2)

        self.horizontalLayoutRightElbowPitch.addWidget(self.labelRightElbowPitchValue)

        self.doubleSpinBoxRightElbowPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightElbowPitch.setObjectName(u"doubleSpinBoxRightElbowPitch")
        self.doubleSpinBoxRightElbowPitch.setEnabled(False)
        self.doubleSpinBoxRightElbowPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightElbowPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightElbowPitch.setFont(font2)
        self.doubleSpinBoxRightElbowPitch.setReadOnly(False)
        self.doubleSpinBoxRightElbowPitch.setKeyboardTracking(False)
        self.doubleSpinBoxRightElbowPitch.setMinimum(-999.990000000000009)
        self.doubleSpinBoxRightElbowPitch.setMaximum(999.990000000000009)

        self.horizontalLayoutRightElbowPitch.addWidget(self.doubleSpinBoxRightElbowPitch)


        self.formLayoutRightElbow.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightElbowPitch)


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

        self.formLayoutRightWrist.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelRightWristPitch)

        self.labelRightWristRoll = QLabel(self.centralwidget)
        self.labelRightWristRoll.setObjectName(u"labelRightWristRoll")
        self.labelRightWristRoll.setFont(font2)
        self.labelRightWristRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightWrist.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelRightWristRoll)

        self.labelRightWristYaw = QLabel(self.centralwidget)
        self.labelRightWristYaw.setObjectName(u"labelRightWristYaw")
        self.labelRightWristYaw.setFont(font2)
        self.labelRightWristYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightWrist.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelRightWristYaw)

        self.horizontalLayoutRightWristPitch = QHBoxLayout()
        self.horizontalLayoutRightWristPitch.setObjectName(u"horizontalLayoutRightWristPitch")
        self.labelRightWristPitchValue = QLabel(self.centralwidget)
        self.labelRightWristPitchValue.setObjectName(u"labelRightWristPitchValue")
        self.labelRightWristPitchValue.setMinimumSize(QSize(70, 0))
        self.labelRightWristPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightWristPitchValue.setFont(font2)

        self.horizontalLayoutRightWristPitch.addWidget(self.labelRightWristPitchValue)

        self.doubleSpinBoxRightWristPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightWristPitch.setObjectName(u"doubleSpinBoxRightWristPitch")
        self.doubleSpinBoxRightWristPitch.setEnabled(False)
        self.doubleSpinBoxRightWristPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightWristPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightWristPitch.setFont(font2)
        self.doubleSpinBoxRightWristPitch.setReadOnly(False)
        self.doubleSpinBoxRightWristPitch.setKeyboardTracking(False)
        self.doubleSpinBoxRightWristPitch.setMinimum(-999.990000000000009)
        self.doubleSpinBoxRightWristPitch.setMaximum(999.990000000000009)

        self.horizontalLayoutRightWristPitch.addWidget(self.doubleSpinBoxRightWristPitch)


        self.formLayoutRightWrist.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightWristPitch)

        self.horizontalLayoutRightWristRoll = QHBoxLayout()
        self.horizontalLayoutRightWristRoll.setObjectName(u"horizontalLayoutRightWristRoll")
        self.labelRightWristRollValue = QLabel(self.centralwidget)
        self.labelRightWristRollValue.setObjectName(u"labelRightWristRollValue")
        self.labelRightWristRollValue.setMinimumSize(QSize(70, 0))
        self.labelRightWristRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightWristRollValue.setFont(font2)

        self.horizontalLayoutRightWristRoll.addWidget(self.labelRightWristRollValue)

        self.doubleSpinBoxRightWristRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightWristRoll.setObjectName(u"doubleSpinBoxRightWristRoll")
        self.doubleSpinBoxRightWristRoll.setEnabled(False)
        self.doubleSpinBoxRightWristRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightWristRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightWristRoll.setFont(font2)
        self.doubleSpinBoxRightWristRoll.setReadOnly(False)
        self.doubleSpinBoxRightWristRoll.setKeyboardTracking(False)
        self.doubleSpinBoxRightWristRoll.setMinimum(-999.990000000000009)
        self.doubleSpinBoxRightWristRoll.setMaximum(999.990000000000009)

        self.horizontalLayoutRightWristRoll.addWidget(self.doubleSpinBoxRightWristRoll)


        self.formLayoutRightWrist.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightWristRoll)

        self.horizontalLayoutRightWristYaw = QHBoxLayout()
        self.horizontalLayoutRightWristYaw.setObjectName(u"horizontalLayoutRightWristYaw")
        self.labelRightWristYawValue = QLabel(self.centralwidget)
        self.labelRightWristYawValue.setObjectName(u"labelRightWristYawValue")
        self.labelRightWristYawValue.setMinimumSize(QSize(70, 0))
        self.labelRightWristYawValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightWristYawValue.setFont(font2)

        self.horizontalLayoutRightWristYaw.addWidget(self.labelRightWristYawValue)

        self.doubleSpinBoxRightWristYaw = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightWristYaw.setObjectName(u"doubleSpinBoxRightWristYaw")
        self.doubleSpinBoxRightWristYaw.setEnabled(False)
        self.doubleSpinBoxRightWristYaw.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightWristYaw.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightWristYaw.setFont(font2)
        self.doubleSpinBoxRightWristYaw.setReadOnly(False)
        self.doubleSpinBoxRightWristYaw.setKeyboardTracking(False)
        self.doubleSpinBoxRightWristYaw.setMinimum(-999.990000000000009)
        self.doubleSpinBoxRightWristYaw.setMaximum(999.990000000000009)

        self.horizontalLayoutRightWristYaw.addWidget(self.doubleSpinBoxRightWristYaw)


        self.formLayoutRightWrist.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightWristYaw)


        self.verticalLayoutRightWrist.addLayout(self.formLayoutRightWrist)


        self.verticalLayoutRightArm.addLayout(self.verticalLayoutRightWrist)


        self.horizontalLayoutArms.addLayout(self.verticalLayoutRightArm)


        self.verticalLayout.addLayout(self.horizontalLayoutArms)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayoutWaistReadOnly = QVBoxLayout()
        self.verticalLayoutWaistReadOnly.setObjectName(u"verticalLayoutWaistReadOnly")
        self.verticalLayoutWaistReadOnly.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayoutLabelWaist = QHBoxLayout()
        self.horizontalLayoutLabelWaist.setObjectName(u"horizontalLayoutLabelWaist")
        self.horizontalLayoutLabelWaist.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutLabelWaist.addItem(self.horizontalSpacer_5)

        self.radioButtonWaist = QRadioButton(self.centralwidget)
        self.radioButtonWaist.setObjectName(u"radioButtonWaist")
        self.radioButtonWaist.setFont(font)
        self.radioButtonWaist.setAutoExclusive(False)

        self.horizontalLayoutLabelWaist.addWidget(self.radioButtonWaist)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutLabelWaist.addItem(self.horizontalSpacer_6)


        self.verticalLayoutWaistReadOnly.addLayout(self.horizontalLayoutLabelWaist)

        self.horizontalLayoutWaist = QHBoxLayout()
        self.horizontalLayoutWaist.setObjectName(u"horizontalLayoutWaist")
        self.horizontalLayoutWaist.setContentsMargins(-1, -1, -1, 0)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayoutWaist.addWidget(self.line_4)

        self.verticalLayoutWaist = QVBoxLayout()
        self.verticalLayoutWaist.setObjectName(u"verticalLayoutWaist")
        self.verticalLayoutWaist.setContentsMargins(30, 10, 30, -1)
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

        self.formLayoutWaist.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelWaistPitch)

        self.horizontalLayoutWaistPitch = QHBoxLayout()
        self.horizontalLayoutWaistPitch.setObjectName(u"horizontalLayoutWaistPitch")
        self.labelWaistPitchValue = QLabel(self.centralwidget)
        self.labelWaistPitchValue.setObjectName(u"labelWaistPitchValue")
        self.labelWaistPitchValue.setMinimumSize(QSize(70, 0))
        self.labelWaistPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelWaistPitchValue.setFont(font2)

        self.horizontalLayoutWaistPitch.addWidget(self.labelWaistPitchValue)

        self.doubleSpinBoxWaistPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxWaistPitch.setObjectName(u"doubleSpinBoxWaistPitch")
        self.doubleSpinBoxWaistPitch.setEnabled(False)
        self.doubleSpinBoxWaistPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxWaistPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxWaistPitch.setFont(font2)
        self.doubleSpinBoxWaistPitch.setReadOnly(False)
        self.doubleSpinBoxWaistPitch.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.doubleSpinBoxWaistPitch.setAccelerated(False)
        self.doubleSpinBoxWaistPitch.setKeyboardTracking(False)
        self.doubleSpinBoxWaistPitch.setMinimum(-999.990000000000009)
        self.doubleSpinBoxWaistPitch.setMaximum(999.990000000000009)

        self.horizontalLayoutWaistPitch.addWidget(self.doubleSpinBoxWaistPitch)


        self.formLayoutWaist.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutWaistPitch)

        self.labelWaistRoll = QLabel(self.centralwidget)
        self.labelWaistRoll.setObjectName(u"labelWaistRoll")
        self.labelWaistRoll.setFont(font2)
        self.labelWaistRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutWaist.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelWaistRoll)

        self.horizontalLayoutWaistRoll = QHBoxLayout()
        self.horizontalLayoutWaistRoll.setObjectName(u"horizontalLayoutWaistRoll")
        self.labelWaistRollValue = QLabel(self.centralwidget)
        self.labelWaistRollValue.setObjectName(u"labelWaistRollValue")
        self.labelWaistRollValue.setMinimumSize(QSize(70, 0))
        self.labelWaistRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelWaistRollValue.setFont(font2)

        self.horizontalLayoutWaistRoll.addWidget(self.labelWaistRollValue)

        self.doubleSpinBoxWaistRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxWaistRoll.setObjectName(u"doubleSpinBoxWaistRoll")
        self.doubleSpinBoxWaistRoll.setEnabled(False)
        self.doubleSpinBoxWaistRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxWaistRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxWaistRoll.setFont(font2)
        self.doubleSpinBoxWaistRoll.setReadOnly(False)
        self.doubleSpinBoxWaistRoll.setKeyboardTracking(False)
        self.doubleSpinBoxWaistRoll.setMinimum(-999.990000000000009)
        self.doubleSpinBoxWaistRoll.setMaximum(999.990000000000009)

        self.horizontalLayoutWaistRoll.addWidget(self.doubleSpinBoxWaistRoll)


        self.formLayoutWaist.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutWaistRoll)

        self.labelWaistYaw = QLabel(self.centralwidget)
        self.labelWaistYaw.setObjectName(u"labelWaistYaw")
        self.labelWaistYaw.setFont(font2)
        self.labelWaistYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutWaist.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelWaistYaw)

        self.horizontalLayoutWaistYaw = QHBoxLayout()
        self.horizontalLayoutWaistYaw.setObjectName(u"horizontalLayoutWaistYaw")
        self.labelWaistYawValue = QLabel(self.centralwidget)
        self.labelWaistYawValue.setObjectName(u"labelWaistYawValue")
        self.labelWaistYawValue.setMinimumSize(QSize(70, 0))
        self.labelWaistYawValue.setMaximumSize(QSize(70, 16777215))
        self.labelWaistYawValue.setFont(font2)

        self.horizontalLayoutWaistYaw.addWidget(self.labelWaistYawValue)

        self.doubleSpinBoxWaistYaw = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxWaistYaw.setObjectName(u"doubleSpinBoxWaistYaw")
        self.doubleSpinBoxWaistYaw.setEnabled(False)
        self.doubleSpinBoxWaistYaw.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxWaistYaw.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxWaistYaw.setFont(font2)
        self.doubleSpinBoxWaistYaw.setReadOnly(False)
        self.doubleSpinBoxWaistYaw.setKeyboardTracking(False)
        self.doubleSpinBoxWaistYaw.setMinimum(-999.990000000000009)
        self.doubleSpinBoxWaistYaw.setMaximum(999.990000000000009)

        self.horizontalLayoutWaistYaw.addWidget(self.doubleSpinBoxWaistYaw)


        self.formLayoutWaist.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutWaistYaw)


        self.verticalLayoutWaist.addLayout(self.formLayoutWaist)


        self.horizontalLayoutWaist.addLayout(self.verticalLayoutWaist)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayoutWaist.addWidget(self.line_3)


        self.verticalLayoutWaistReadOnly.addLayout(self.horizontalLayoutWaist)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 30, -1, 10)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.pushButtonOn = QPushButton(self.centralwidget)
        self.pushButtonOn.setObjectName(u"pushButtonOn")
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButtonOn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.pushButtonOn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.verticalLayoutWaistReadOnly.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.pushButtonOff = QPushButton(self.centralwidget)
        self.pushButtonOff.setObjectName(u"pushButtonOff")
        self.pushButtonOff.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pushButtonOff)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)


        self.verticalLayoutWaistReadOnly.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutWaistReadOnly.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayoutWaistReadOnly)

        self.verticalLayoutLegs = QVBoxLayout()
        self.verticalLayoutLegs.setObjectName(u"verticalLayoutLegs")
        self.horizontalLayoutLabelLegs = QHBoxLayout()
        self.horizontalLayoutLabelLegs.setObjectName(u"horizontalLayoutLabelLegs")
        self.horizontalLayoutLabelLegs.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutLabelLegs.addItem(self.horizontalSpacer_7)

        self.radioButtonLegs = QRadioButton(self.centralwidget)
        self.radioButtonLegs.setObjectName(u"radioButtonLegs")
        self.radioButtonLegs.setFont(font)
        self.radioButtonLegs.setAutoExclusive(False)

        self.horizontalLayoutLabelLegs.addWidget(self.radioButtonLegs)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutLabelLegs.addItem(self.horizontalSpacer_8)


        self.verticalLayoutLegs.addLayout(self.horizontalLayoutLabelLegs)

        self.horizontalLayoutLegs = QHBoxLayout()
        self.horizontalLayoutLegs.setObjectName(u"horizontalLayoutLegs")
        self.horizontalLayoutLegs.setContentsMargins(-1, 10, -1, -1)
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

        self.formLayoutLeftHip.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelLeftHipPitch)

        self.horizontalLayoutLeftHipPitch = QHBoxLayout()
        self.horizontalLayoutLeftHipPitch.setObjectName(u"horizontalLayoutLeftHipPitch")
        self.labelLeftHipPitchValue = QLabel(self.centralwidget)
        self.labelLeftHipPitchValue.setObjectName(u"labelLeftHipPitchValue")
        self.labelLeftHipPitchValue.setMinimumSize(QSize(70, 0))
        self.labelLeftHipPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftHipPitchValue.setFont(font2)

        self.horizontalLayoutLeftHipPitch.addWidget(self.labelLeftHipPitchValue)

        self.doubleSpinBoxLeftHipPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftHipPitch.setObjectName(u"doubleSpinBoxLeftHipPitch")
        self.doubleSpinBoxLeftHipPitch.setEnabled(False)
        self.doubleSpinBoxLeftHipPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftHipPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftHipPitch.setFont(font2)
        self.doubleSpinBoxLeftHipPitch.setReadOnly(False)
        self.doubleSpinBoxLeftHipPitch.setKeyboardTracking(False)
        self.doubleSpinBoxLeftHipPitch.setMinimum(-145.000000000000000)
        self.doubleSpinBoxLeftHipPitch.setMaximum(165.000000000000000)

        self.horizontalLayoutLeftHipPitch.addWidget(self.doubleSpinBoxLeftHipPitch)


        self.formLayoutLeftHip.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftHipPitch)

        self.labelLeftHipRoll = QLabel(self.centralwidget)
        self.labelLeftHipRoll.setObjectName(u"labelLeftHipRoll")
        self.labelLeftHipRoll.setFont(font2)
        self.labelLeftHipRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftHip.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelLeftHipRoll)

        self.horizontalLayoutLeftHipRoll = QHBoxLayout()
        self.horizontalLayoutLeftHipRoll.setObjectName(u"horizontalLayoutLeftHipRoll")
        self.labelLeftHipRollValue = QLabel(self.centralwidget)
        self.labelLeftHipRollValue.setObjectName(u"labelLeftHipRollValue")
        self.labelLeftHipRollValue.setMinimumSize(QSize(70, 0))
        self.labelLeftHipRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftHipRollValue.setFont(font2)

        self.horizontalLayoutLeftHipRoll.addWidget(self.labelLeftHipRollValue)

        self.doubleSpinBoxLeftHipRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftHipRoll.setObjectName(u"doubleSpinBoxLeftHipRoll")
        self.doubleSpinBoxLeftHipRoll.setEnabled(False)
        self.doubleSpinBoxLeftHipRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftHipRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftHipRoll.setFont(font2)
        self.doubleSpinBoxLeftHipRoll.setReadOnly(False)
        self.doubleSpinBoxLeftHipRoll.setKeyboardTracking(False)
        self.doubleSpinBoxLeftHipRoll.setMinimum(-30.000000000000000)
        self.doubleSpinBoxLeftHipRoll.setMaximum(170.000000000000000)

        self.horizontalLayoutLeftHipRoll.addWidget(self.doubleSpinBoxLeftHipRoll)


        self.formLayoutLeftHip.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftHipRoll)

        self.labelLeftHipYaw = QLabel(self.centralwidget)
        self.labelLeftHipYaw.setObjectName(u"labelLeftHipYaw")
        self.labelLeftHipYaw.setFont(font2)
        self.labelLeftHipYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftHip.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelLeftHipYaw)

        self.horizontalLayoutLeftHipYaw = QHBoxLayout()
        self.horizontalLayoutLeftHipYaw.setObjectName(u"horizontalLayoutLeftHipYaw")
        self.labelLeftHipYawValue = QLabel(self.centralwidget)
        self.labelLeftHipYawValue.setObjectName(u"labelLeftHipYawValue")
        self.labelLeftHipYawValue.setMinimumSize(QSize(70, 0))
        self.labelLeftHipYawValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftHipYawValue.setFont(font2)

        self.horizontalLayoutLeftHipYaw.addWidget(self.labelLeftHipYawValue)

        self.doubleSpinBoxLeftHipYaw = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftHipYaw.setObjectName(u"doubleSpinBoxLeftHipYaw")
        self.doubleSpinBoxLeftHipYaw.setEnabled(False)
        self.doubleSpinBoxLeftHipYaw.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftHipYaw.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftHipYaw.setFont(font2)
        self.doubleSpinBoxLeftHipYaw.setReadOnly(False)
        self.doubleSpinBoxLeftHipYaw.setKeyboardTracking(False)
        self.doubleSpinBoxLeftHipYaw.setMinimum(-158.000000000000000)
        self.doubleSpinBoxLeftHipYaw.setMaximum(158.000000000000000)

        self.horizontalLayoutLeftHipYaw.addWidget(self.doubleSpinBoxLeftHipYaw)


        self.formLayoutLeftHip.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftHipYaw)


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

        self.formLayoutLeftKnee.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelLeftKneePitch)

        self.horizontalLayoutLeftKneePitch = QHBoxLayout()
        self.horizontalLayoutLeftKneePitch.setObjectName(u"horizontalLayoutLeftKneePitch")
        self.labelLeftKneePitchValue = QLabel(self.centralwidget)
        self.labelLeftKneePitchValue.setObjectName(u"labelLeftKneePitchValue")
        self.labelLeftKneePitchValue.setMinimumSize(QSize(70, 0))
        self.labelLeftKneePitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftKneePitchValue.setFont(font2)

        self.horizontalLayoutLeftKneePitch.addWidget(self.labelLeftKneePitchValue)

        self.doubleSpinBoxLeftKneePitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftKneePitch.setObjectName(u"doubleSpinBoxLeftKneePitch")
        self.doubleSpinBoxLeftKneePitch.setEnabled(False)
        self.doubleSpinBoxLeftKneePitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftKneePitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftKneePitch.setFont(font2)
        self.doubleSpinBoxLeftKneePitch.setReadOnly(False)
        self.doubleSpinBoxLeftKneePitch.setKeyboardTracking(False)
        self.doubleSpinBoxLeftKneePitch.setMinimum(-5.000000000000000)
        self.doubleSpinBoxLeftKneePitch.setMaximum(165.000000000000000)

        self.horizontalLayoutLeftKneePitch.addWidget(self.doubleSpinBoxLeftKneePitch)


        self.formLayoutLeftKnee.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftKneePitch)


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

        self.formLayoutLeftAnkle.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelLeftAnklePitch)

        self.horizontalLayoutLeftAnklePitch = QHBoxLayout()
        self.horizontalLayoutLeftAnklePitch.setObjectName(u"horizontalLayoutLeftAnklePitch")
        self.labelLeftAnklePitchValue = QLabel(self.centralwidget)
        self.labelLeftAnklePitchValue.setObjectName(u"labelLeftAnklePitchValue")
        self.labelLeftAnklePitchValue.setMinimumSize(QSize(70, 0))
        self.labelLeftAnklePitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftAnklePitchValue.setFont(font2)

        self.horizontalLayoutLeftAnklePitch.addWidget(self.labelLeftAnklePitchValue)

        self.doubleSpinBoxLeftAnklePitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftAnklePitch.setObjectName(u"doubleSpinBoxLeftAnklePitch")
        self.doubleSpinBoxLeftAnklePitch.setEnabled(False)
        self.doubleSpinBoxLeftAnklePitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftAnklePitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftAnklePitch.setFont(font2)
        self.doubleSpinBoxLeftAnklePitch.setReadOnly(False)
        self.doubleSpinBoxLeftAnklePitch.setKeyboardTracking(False)
        self.doubleSpinBoxLeftAnklePitch.setMinimum(-50.000000000000000)
        self.doubleSpinBoxLeftAnklePitch.setMaximum(30.000000000000000)

        self.horizontalLayoutLeftAnklePitch.addWidget(self.doubleSpinBoxLeftAnklePitch)


        self.formLayoutLeftAnkle.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftAnklePitch)

        self.labelLeftAnkleRoll = QLabel(self.centralwidget)
        self.labelLeftAnkleRoll.setObjectName(u"labelLeftAnkleRoll")
        self.labelLeftAnkleRoll.setFont(font2)
        self.labelLeftAnkleRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutLeftAnkle.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelLeftAnkleRoll)

        self.horizontalLayoutLeftAnkleRoll = QHBoxLayout()
        self.horizontalLayoutLeftAnkleRoll.setObjectName(u"horizontalLayoutLeftAnkleRoll")
        self.labelLeftAnkleRollValue = QLabel(self.centralwidget)
        self.labelLeftAnkleRollValue.setObjectName(u"labelLeftAnkleRollValue")
        self.labelLeftAnkleRollValue.setMinimumSize(QSize(70, 0))
        self.labelLeftAnkleRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelLeftAnkleRollValue.setFont(font2)

        self.horizontalLayoutLeftAnkleRoll.addWidget(self.labelLeftAnkleRollValue)

        self.doubleSpinBoxLeftAnkleRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLeftAnkleRoll.setObjectName(u"doubleSpinBoxLeftAnkleRoll")
        self.doubleSpinBoxLeftAnkleRoll.setEnabled(False)
        self.doubleSpinBoxLeftAnkleRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxLeftAnkleRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxLeftAnkleRoll.setFont(font2)
        self.doubleSpinBoxLeftAnkleRoll.setReadOnly(False)
        self.doubleSpinBoxLeftAnkleRoll.setKeyboardTracking(False)
        self.doubleSpinBoxLeftAnkleRoll.setMinimum(-15.000000000000000)
        self.doubleSpinBoxLeftAnkleRoll.setMaximum(15.000000000000000)

        self.horizontalLayoutLeftAnkleRoll.addWidget(self.doubleSpinBoxLeftAnkleRoll)


        self.formLayoutLeftAnkle.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutLeftAnkleRoll)


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

        self.formLayoutRightHip.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelRightHipPitch)

        self.labelRightHipRoll = QLabel(self.centralwidget)
        self.labelRightHipRoll.setObjectName(u"labelRightHipRoll")
        self.labelRightHipRoll.setFont(font2)
        self.labelRightHipRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightHip.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelRightHipRoll)

        self.labelRightHipYaw = QLabel(self.centralwidget)
        self.labelRightHipYaw.setObjectName(u"labelRightHipYaw")
        self.labelRightHipYaw.setFont(font2)
        self.labelRightHipYaw.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightHip.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelRightHipYaw)

        self.horizontalLayoutRightHipPitch = QHBoxLayout()
        self.horizontalLayoutRightHipPitch.setObjectName(u"horizontalLayoutRightHipPitch")
        self.labelRightHipPitchValue = QLabel(self.centralwidget)
        self.labelRightHipPitchValue.setObjectName(u"labelRightHipPitchValue")
        self.labelRightHipPitchValue.setMinimumSize(QSize(70, 0))
        self.labelRightHipPitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightHipPitchValue.setFont(font2)

        self.horizontalLayoutRightHipPitch.addWidget(self.labelRightHipPitchValue)

        self.doubleSpinBoxRightHipPitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightHipPitch.setObjectName(u"doubleSpinBoxRightHipPitch")
        self.doubleSpinBoxRightHipPitch.setEnabled(False)
        self.doubleSpinBoxRightHipPitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightHipPitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightHipPitch.setFont(font2)
        self.doubleSpinBoxRightHipPitch.setReadOnly(False)
        self.doubleSpinBoxRightHipPitch.setKeyboardTracking(False)
        self.doubleSpinBoxRightHipPitch.setMinimum(-145.000000000000000)
        self.doubleSpinBoxRightHipPitch.setMaximum(165.000000000000000)

        self.horizontalLayoutRightHipPitch.addWidget(self.doubleSpinBoxRightHipPitch)


        self.formLayoutRightHip.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightHipPitch)

        self.horizontalLayoutRightHipRoll = QHBoxLayout()
        self.horizontalLayoutRightHipRoll.setObjectName(u"horizontalLayoutRightHipRoll")
        self.labelRightHipRollValue = QLabel(self.centralwidget)
        self.labelRightHipRollValue.setObjectName(u"labelRightHipRollValue")
        self.labelRightHipRollValue.setMinimumSize(QSize(70, 0))
        self.labelRightHipRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightHipRollValue.setFont(font2)

        self.horizontalLayoutRightHipRoll.addWidget(self.labelRightHipRollValue)

        self.doubleSpinBoxRightHipRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightHipRoll.setObjectName(u"doubleSpinBoxRightHipRoll")
        self.doubleSpinBoxRightHipRoll.setEnabled(False)
        self.doubleSpinBoxRightHipRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightHipRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightHipRoll.setFont(font2)
        self.doubleSpinBoxRightHipRoll.setReadOnly(False)
        self.doubleSpinBoxRightHipRoll.setKeyboardTracking(False)
        self.doubleSpinBoxRightHipRoll.setMinimum(-170.000000000000000)
        self.doubleSpinBoxRightHipRoll.setMaximum(30.000000000000000)

        self.horizontalLayoutRightHipRoll.addWidget(self.doubleSpinBoxRightHipRoll)


        self.formLayoutRightHip.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightHipRoll)

        self.horizontalLayoutRightHipYaw = QHBoxLayout()
        self.horizontalLayoutRightHipYaw.setObjectName(u"horizontalLayoutRightHipYaw")
        self.labelRightHipYawValue = QLabel(self.centralwidget)
        self.labelRightHipYawValue.setObjectName(u"labelRightHipYawValue")
        self.labelRightHipYawValue.setMinimumSize(QSize(70, 0))
        self.labelRightHipYawValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightHipYawValue.setFont(font2)

        self.horizontalLayoutRightHipYaw.addWidget(self.labelRightHipYawValue)

        self.doubleSpinBoxRightHipYaw = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightHipYaw.setObjectName(u"doubleSpinBoxRightHipYaw")
        self.doubleSpinBoxRightHipYaw.setEnabled(False)
        self.doubleSpinBoxRightHipYaw.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightHipYaw.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightHipYaw.setFont(font2)
        self.doubleSpinBoxRightHipYaw.setReadOnly(False)
        self.doubleSpinBoxRightHipYaw.setKeyboardTracking(False)
        self.doubleSpinBoxRightHipYaw.setMinimum(-158.000000000000000)
        self.doubleSpinBoxRightHipYaw.setMaximum(158.000000000000000)

        self.horizontalLayoutRightHipYaw.addWidget(self.doubleSpinBoxRightHipYaw)


        self.formLayoutRightHip.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightHipYaw)


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

        self.formLayoutRightKnee.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelRightKneePitch)

        self.horizontalLayoutRightKneePitch = QHBoxLayout()
        self.horizontalLayoutRightKneePitch.setObjectName(u"horizontalLayoutRightKneePitch")
        self.labelRightKneePitchValue = QLabel(self.centralwidget)
        self.labelRightKneePitchValue.setObjectName(u"labelRightKneePitchValue")
        self.labelRightKneePitchValue.setMinimumSize(QSize(70, 0))
        self.labelRightKneePitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightKneePitchValue.setFont(font2)

        self.horizontalLayoutRightKneePitch.addWidget(self.labelRightKneePitchValue)

        self.doubleSpinBoxRightKneePitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightKneePitch.setObjectName(u"doubleSpinBoxRightKneePitch")
        self.doubleSpinBoxRightKneePitch.setEnabled(False)
        self.doubleSpinBoxRightKneePitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightKneePitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightKneePitch.setFont(font2)
        self.doubleSpinBoxRightKneePitch.setReadOnly(False)
        self.doubleSpinBoxRightKneePitch.setKeyboardTracking(False)
        self.doubleSpinBoxRightKneePitch.setMinimum(-5.000000000000000)
        self.doubleSpinBoxRightKneePitch.setMaximum(165.000000000000000)

        self.horizontalLayoutRightKneePitch.addWidget(self.doubleSpinBoxRightKneePitch)


        self.formLayoutRightKnee.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightKneePitch)


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

        self.formLayoutRightAnkle.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelRightAnklePitch)

        self.horizontalLayoutRightAnklePitch = QHBoxLayout()
        self.horizontalLayoutRightAnklePitch.setObjectName(u"horizontalLayoutRightAnklePitch")
        self.labelRightAnklePitchValue = QLabel(self.centralwidget)
        self.labelRightAnklePitchValue.setObjectName(u"labelRightAnklePitchValue")
        self.labelRightAnklePitchValue.setMinimumSize(QSize(70, 0))
        self.labelRightAnklePitchValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightAnklePitchValue.setFont(font2)

        self.horizontalLayoutRightAnklePitch.addWidget(self.labelRightAnklePitchValue)

        self.doubleSpinBoxRightAnklePitch = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightAnklePitch.setObjectName(u"doubleSpinBoxRightAnklePitch")
        self.doubleSpinBoxRightAnklePitch.setEnabled(False)
        self.doubleSpinBoxRightAnklePitch.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightAnklePitch.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightAnklePitch.setFont(font2)
        self.doubleSpinBoxRightAnklePitch.setReadOnly(False)
        self.doubleSpinBoxRightAnklePitch.setKeyboardTracking(False)
        self.doubleSpinBoxRightAnklePitch.setMinimum(-50.000000000000000)
        self.doubleSpinBoxRightAnklePitch.setMaximum(30.000000000000000)

        self.horizontalLayoutRightAnklePitch.addWidget(self.doubleSpinBoxRightAnklePitch)


        self.formLayoutRightAnkle.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightAnklePitch)

        self.labelRightAnkleRoll = QLabel(self.centralwidget)
        self.labelRightAnkleRoll.setObjectName(u"labelRightAnkleRoll")
        self.labelRightAnkleRoll.setFont(font2)
        self.labelRightAnkleRoll.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayoutRightAnkle.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelRightAnkleRoll)

        self.horizontalLayoutRightAnkleRoll = QHBoxLayout()
        self.horizontalLayoutRightAnkleRoll.setObjectName(u"horizontalLayoutRightAnkleRoll")
        self.labelRightAnkleRollValue = QLabel(self.centralwidget)
        self.labelRightAnkleRollValue.setObjectName(u"labelRightAnkleRollValue")
        self.labelRightAnkleRollValue.setMinimumSize(QSize(70, 0))
        self.labelRightAnkleRollValue.setMaximumSize(QSize(70, 16777215))
        self.labelRightAnkleRollValue.setFont(font2)

        self.horizontalLayoutRightAnkleRoll.addWidget(self.labelRightAnkleRollValue)

        self.doubleSpinBoxRightAnkleRoll = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRightAnkleRoll.setObjectName(u"doubleSpinBoxRightAnkleRoll")
        self.doubleSpinBoxRightAnkleRoll.setEnabled(False)
        self.doubleSpinBoxRightAnkleRoll.setMinimumSize(QSize(90, 0))
        self.doubleSpinBoxRightAnkleRoll.setMaximumSize(QSize(90, 16777215))
        self.doubleSpinBoxRightAnkleRoll.setFont(font2)
        self.doubleSpinBoxRightAnkleRoll.setReadOnly(False)
        self.doubleSpinBoxRightAnkleRoll.setKeyboardTracking(False)
        self.doubleSpinBoxRightAnkleRoll.setMinimum(-15.000000000000000)
        self.doubleSpinBoxRightAnkleRoll.setMaximum(15.000000000000000)

        self.horizontalLayoutRightAnkleRoll.addWidget(self.doubleSpinBoxRightAnkleRoll)


        self.formLayoutRightAnkle.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayoutRightAnkleRoll)


        self.verticalLayoutRightAnkle.addLayout(self.formLayoutRightAnkle)


        self.verticalLayoutRightLeg.addLayout(self.verticalLayoutRightAnkle)


        self.horizontalLayoutLegs.addLayout(self.verticalLayoutRightLeg)


        self.verticalLayoutLegs.addLayout(self.horizontalLayoutLegs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutLegs.addItem(self.verticalSpacer)


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
        self.radioButtonArms.setText(QCoreApplication.translate("G1ControlPanel", u"Arms", None))
        self.labelLeftShoulder.setText(QCoreApplication.translate("G1ControlPanel", u"Left Shoulder", None))
        self.labelLeftShoulderPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelLeftShoulderPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.doubleSpinBoxLeftShoulderPitch.setSpecialValueText("")
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
        self.radioButtonWaist.setText(QCoreApplication.translate("G1ControlPanel", u"Waist", None))
        self.labelWaist.setText(QCoreApplication.translate("G1ControlPanel", u"Waist", None))
        self.labelWaistPitch.setText(QCoreApplication.translate("G1ControlPanel", u"Pitch", None))
        self.labelWaistPitchValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelWaistRoll.setText(QCoreApplication.translate("G1ControlPanel", u"Roll", None))
        self.labelWaistRollValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.labelWaistYaw.setText(QCoreApplication.translate("G1ControlPanel", u"Yaw", None))
        self.labelWaistYawValue.setText(QCoreApplication.translate("G1ControlPanel", u"0", None))
        self.pushButtonOn.setText(QCoreApplication.translate("G1ControlPanel", u"All On", None))
        self.pushButtonOff.setText(QCoreApplication.translate("G1ControlPanel", u"All Off", None))
        self.radioButtonLegs.setText(QCoreApplication.translate("G1ControlPanel", u"Legs", None))
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

