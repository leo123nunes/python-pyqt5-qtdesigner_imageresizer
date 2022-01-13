from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from qt_designer.imageresizer_interface import *
import imghdr

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Image resizer')

        self.image = None

        self.new_image = None
        
        self.linedit_image_path.setReadOnly(True)

        self.linedit_image_type.setReadOnly(True)

        self.btn_open_image.clicked.connect(self.open_input_image)

        self.btn_resize.clicked.connect(self.resize_image)

        self.btn_save.clicked.connect(self.save_image)

    def open_input_image(self):

        image_input = QFileDialog()

        image_path = image_input.getOpenFileName()[0]

        if not image_path:
            return

        self.new_image = None

        image_type = imghdr.what(image_path)

        self.linedit_image_path.setText(image_path)

        self.linedit_image_type.setText(image_type)

        self.image = QPixmap(image_path)

        self.label_image.setPixmap(self.image)

        self.linedit_image_width.setText(str(self.image.width()))

        self.linedit_image_height.setText(str(self.image.height()))

    def resize_image(self):
        try:
            new_width = self.linedit_image_width.text()

            self.new_image = self.image.scaledToWidth(int(new_width))

            self.linedit_image_width.setText(str(self.new_image.width()))

            self.linedit_image_height.setText(str(self.new_image.height()))

            self.label_image.setPixmap(self.new_image)

        except Exception as e:
            self.show_error_msg('Select an image.')

    def save_image(self):

        if not self.new_image:
            self.show_error_msg('No resized image.')
            return

        try:
            image_save_path = QFileDialog().getSaveFileName()[0]

            if not image_save_path:
                return

            image_to_save = self.new_image.toImage()

            image_to_save.save(image_save_path, imghdr.what(self.linedit_image_path.text()), -1)

            self.new_image = None

            self.show_success_msg('Image sucessfully saved.')


        except Exception as e:

            print(e)

    def show_error_msg(self, msg):
        message_box = QMessageBox()
        message_box.setText(msg)
        message_box.setStandardButtons(QMessageBox.StandardButton.Close)
        message_box.exec()

    def show_success_msg(self, msg):
        message_box = QMessageBox()
        message_box.setText(msg)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        message_box.exec()

