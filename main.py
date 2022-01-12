from PyQt5.QtWidgets import QApplication
from image_resizer import App
import sys

q_app = QApplication(sys.argv)
app = App()

app.show()
q_app.exec_()