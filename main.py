
import sys
import os
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_data()
        self.init_UI()
        self.init_connect()

        self.installEventFilter(self)


    def init_data(self):
        pass

    def init_UI(self):
        self.setStyleSheet("background-color:black")
        # self.setFixedSize(1920, 1080)
        self.setFixedSize(640, 480)



    def init_connect(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)

    cpp = MainWindow()
    cpp.show()


    sys.exit(app.exec_())
