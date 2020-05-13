import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design
from port import serial_ports,speeds
import serial



class LedApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Port.addItems(serial_ports())
        self.Speed.addItems(speeds)
        self.realport = None
        self.DisconnectBtn.setDisabled(True)
        self.StartBtn.setDisabled(True)
        self.StopBtn.setDisabled(True)
        self.ConnectBtn.clicked.connect(self.connect)
        self.DisconnectBtn.clicked.connect(self.disconnect)
        self.StartBtn.clicked.connect(self.read)

    def connect(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(),int(self.Speed.currentText()),timeout=1)
            # self.realport.open()
            # self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectBtn.setDisabled(True)
            self.DisconnectBtn.setDisabled(False)
            self.StartBtn.setDisabled(False)
            self.StopBtn.setDisabled(False)
            self.Port.setDisabled(True)
            self.Speed.setDisabled(True)
        except Exception as e:
            print(e)
    def disconnect(self):
        try:
            self.realport.close()
            self.ConnectBtn.setDisabled(False)
            self.DisconnectBtn.setDisabled(True)
            self.StartBtn.setDisabled(True)
            self.StopBtn.setDisabled(True)
            self.Port.setDisabled(False)
            self.Speed.setDisabled(False)
        except Exception as e:
            print(e)

    def read(self):
        if self.realport:
            line = self.realport.readline()
            # self.OutputListView.ad
            print(str(line))



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LedApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()