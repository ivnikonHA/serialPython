# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 310)
        self.Port = QtWidgets.QComboBox(Form)
        self.Port.setGeometry(QtCore.QRect(10, 50, 231, 31))
        self.Port.setObjectName("Port")
        self.Speed = QtWidgets.QComboBox(Form)
        self.Speed.setGeometry(QtCore.QRect(260, 50, 141, 32))
        self.Speed.setObjectName("Speed")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ConnectButton = QtWidgets.QPushButton(Form)
        self.ConnectButton.setGeometry(QtCore.QRect(110, 100, 101, 41))
        self.ConnectButton.setObjectName("ConnectButton")
        self.DisconnectBtn = QtWidgets.QPushButton(Form)
        self.DisconnectBtn.setGeometry(QtCore.QRect(230, 100, 101, 41))
        self.DisconnectBtn.setObjectName("DisconnectBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Управление подсветкой"))
        self.label.setText(_translate("Form", "Порт"))
        self.label_2.setText(_translate("Form", "Скорость"))
        self.ConnectButton.setText(_translate("Form", "Подключиться"))
        self.DisconnectBtn.setText(_translate("Form", "Отключиться"))
