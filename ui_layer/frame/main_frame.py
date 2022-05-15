
import os
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *





class MainFrame(QFrame):
    def __init__(self):
        super(MainFrame, self).__init__()

        self.init_data()
        self.init_UI()
        self.init_connect()


    def init_data(self):
        pass

    def init_UI(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        ui_path = os.path.join(dir_path, "../../UI/main_frame.ui")
        uic.loadUi(ui_path, self)



    def init_connect(self):
        pass




