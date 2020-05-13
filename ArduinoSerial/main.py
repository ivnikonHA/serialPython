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
        self.ConnectButton.clicked.connect(self.connect)
        self.DisconnectBtn.clicked.connect(self.disconnect)

    def connect(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(),int(self.Speed.currentText()))
            # self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectButton.setDisabled(True)
            self.DisconnectBtn.setDisabled(False)
        except Exception as e:
            print(e)
    def disconnect(self):
        try:
            self.realport.close()
            self.ConnectButton.setDisabled(False)
            self.DisconnectBtn.setDisabled(True)
        except Exception as e:
            print(e)

    def send(self):
        if self.realport:
            self.realport.write(b'b')



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LedApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()