
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
        self.load_map_file_bt.clicked.connect(self.slot_load_map_file_bt)
        self.generate_random_maps_bt.clicked.connect(self.slot_generate_random_maps_bt)

    def slot_load_map_file_bt(self):

        files, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "choose multi files",
                                                  "./",
                                                  "All Files (*);;Text Files (*.txt)")
        print(files, ok1)



    def slot_generate_random_maps_bt(self):
        pass




