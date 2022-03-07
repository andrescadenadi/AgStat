# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\andre\Documents\UAAAN\PROYECTO\App\Ag_Stat\InfoDlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        Dialog.setStyleSheet("background-color: rgba(64, 64, 64,0.3);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(175, 110, 450, 260))
        self.label.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius: 20px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_icon = QtWidgets.QLabel(Dialog)
        self.label_icon.setGeometry(QtCore.QRect(215, 155, 78, 77))
        self.label_icon.setStyleSheet("background-image: url(:/Img/Img/info.png);")
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        self.label_message = QtWidgets.QLabel(Dialog)
        self.label_message.setGeometry(QtCore.QRect(315, 145, 291, 101))
        self.label_message.setStyleSheet("font: 28pt \"Calibri\";\n"
"color: rgb(236, 239, 240);")
        self.label_message.setObjectName("label_message")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 280, 220, 55))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(64,64,64);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_message.setText(_translate("Dialog", "Texto"))
        self.pushButton.setText(_translate("Dialog", "Aceptar"))

import AgStatResources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

