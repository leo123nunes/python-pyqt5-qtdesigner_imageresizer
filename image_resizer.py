from PyQt5.QtWidgets import QMainWindow
from qt_designer.imageresizer_interface import *

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)