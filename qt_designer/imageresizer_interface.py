# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageresizer_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 5, 7, 1, 1)
        self.linedit_image_type = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linedit_image_type.sizePolicy().hasHeightForWidth())
        self.linedit_image_type.setSizePolicy(sizePolicy)
        self.linedit_image_type.setObjectName("linedit_image_type")
        self.gridLayout.addWidget(self.linedit_image_type, 5, 3, 1, 1)
        self.label_image_type = QtWidgets.QLabel(self.centralwidget)
        self.label_image_type.setObjectName("label_image_type")
        self.gridLayout.addWidget(self.label_image_type, 5, 1, 1, 1)
        self.btn_open_image = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_image.setObjectName("btn_open_image")
        self.gridLayout.addWidget(self.btn_open_image, 1, 7, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 487))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout_2.addWidget(self.label_image, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 8)
        self.label_image_height = QtWidgets.QLabel(self.centralwidget)
        self.label_image_height.setEnabled(True)
        self.label_image_height.setObjectName("label_image_height")
        self.gridLayout.addWidget(self.label_image_height, 4, 4, 1, 1)
        self.btn_resize = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resize.setObjectName("btn_resize")
        self.gridLayout.addWidget(self.btn_resize, 4, 7, 1, 1)
        self.label_image_width = QtWidgets.QLabel(self.centralwidget)
        self.label_image_width.setObjectName("label_image_width")
        self.gridLayout.addWidget(self.label_image_width, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.linedit_image_path = QtWidgets.QLineEdit(self.centralwidget)
        self.linedit_image_path.setObjectName("linedit_image_path")
        self.gridLayout.addWidget(self.linedit_image_path, 1, 0, 1, 7)
        self.linedit_image_height = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linedit_image_height.sizePolicy().hasHeightForWidth())
        self.linedit_image_height.setSizePolicy(sizePolicy)
        self.linedit_image_height.setObjectName("linedit_image_height")
        self.gridLayout.addWidget(self.linedit_image_height, 4, 5, 1, 1)
        self.linedit_image_width = QtWidgets.QLineEdit(self.centralwidget)
        self.linedit_image_width.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linedit_image_width.sizePolicy().hasHeightForWidth())
        self.linedit_image_width.setSizePolicy(sizePolicy)
        self.linedit_image_width.setMaxLength(32725)
        self.linedit_image_width.setObjectName("linedit_image_width")
        self.gridLayout.addWidget(self.linedit_image_width, 4, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.label_image_type.setText(_translate("MainWindow", "Image type"))
        self.btn_open_image.setText(_translate("MainWindow", "Open image"))
        self.label_image_height.setText(_translate("MainWindow", "Height"))
        self.btn_resize.setText(_translate("MainWindow", "Resize"))
        self.label_image_width.setText(_translate("MainWindow", "Width"))
