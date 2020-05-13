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
        Form.resize(416, 553)
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
        self.OutputListView = QtWidgets.QListView(Form)
        self.OutputListView.setGeometry(QtCore.QRect(10, 220, 391, 291))
        self.OutputListView.setObjectName("OutputListView")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 100, 271, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ConnectBtn = QtWidgets.QPushButton(self.widget)
        self.ConnectBtn.setObjectName("ConnectBtn")
        self.gridLayout.addWidget(self.ConnectBtn, 0, 0, 1, 1)
        self.DisconnectBtn = QtWidgets.QPushButton(self.widget)
        self.DisconnectBtn.setObjectName("DisconnectBtn")
        self.gridLayout.addWidget(self.DisconnectBtn, 0, 1, 1, 1)
        self.StartBtn = QtWidgets.QPushButton(self.widget)
        self.StartBtn.setObjectName("StartBtn")
        self.gridLayout.addWidget(self.StartBtn, 1, 0, 1, 1)
        self.StopBtn = QtWidgets.QPushButton(self.widget)
        self.StopBtn.setObjectName("StopBtn")
        self.gridLayout.addWidget(self.StopBtn, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Управление подсветкой"))
        self.label.setText(_translate("Form", "Порт"))
        self.label_2.setText(_translate("Form", "Скорость"))
        self.ConnectBtn.setText(_translate("Form", "Подключиться"))
        self.DisconnectBtn.setText(_translate("Form", "Отключиться"))
        self.StartBtn.setText(_translate("Form", "Старт"))
        self.StopBtn.setText(_translate("Form", "Стоп"))
