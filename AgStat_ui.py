# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\andre\Documents\UAAAN\PROYECTO\App\Ag_Stat\AgStat.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.stackedWidget.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"background-image: url(:/Img/Img/Bg.png);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainMe = QtWidgets.QWidget()
        self.mainMe.setStyleSheet("")
        self.mainMe.setObjectName("mainMe")
        self.mainMe_label_logo = QtWidgets.QLabel(self.mainMe)
        self.mainMe_label_logo.setGeometry(QtCore.QRect(160, 30, 470, 140))
        self.mainMe_label_logo.setObjectName("mainMe_label_logo")
        self.mainMe_frame = QtWidgets.QFrame(self.mainMe)
        self.mainMe_frame.setGeometry(QtCore.QRect(0, 176, 800, 210))
        self.mainMe_frame.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.mainMe_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainMe_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainMe_frame.setObjectName("mainMe_frame")
        self.mainMe_pushButton_an = QtWidgets.QPushButton(self.mainMe_frame)
        self.mainMe_pushButton_an.setGeometry(QtCore.QRect(40, 15, 165, 180))
        self.mainMe_pushButton_an.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_Analysis.png);\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.mainMe_pushButton_an.setText("")
        self.mainMe_pushButton_an.setObjectName("mainMe_pushButton_an")
        self.mainMe_pushButton_aq = QtWidgets.QPushButton(self.mainMe_frame)
        self.mainMe_pushButton_aq.setGeometry(QtCore.QRect(225, 15, 165, 180))
        self.mainMe_pushButton_aq.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_Aquisition.png);\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.mainMe_pushButton_aq.setText("")
        self.mainMe_pushButton_aq.setObjectName("mainMe_pushButton_aq")
        self.mainMe_pushButton_fi = QtWidgets.QPushButton(self.mainMe_frame)
        self.mainMe_pushButton_fi.setGeometry(QtCore.QRect(410, 15, 165, 180))
        self.mainMe_pushButton_fi.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_Files.png);\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.mainMe_pushButton_fi.setText("")
        self.mainMe_pushButton_fi.setObjectName("mainMe_pushButton_fi")
        self.mainMe_pushButton_se = QtWidgets.QPushButton(self.mainMe_frame)
        self.mainMe_pushButton_se.setGeometry(QtCore.QRect(595, 15, 165, 180))
        self.mainMe_pushButton_se.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_Settings.png);\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.mainMe_pushButton_se.setText("")
        self.mainMe_pushButton_se.setObjectName("mainMe_pushButton_se")
        self.mainMe_pushButton_help = QtWidgets.QPushButton(self.mainMe)
        self.mainMe_pushButton_help.setGeometry(QtCore.QRect(650, 405, 110, 50))
        self.mainMe_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_Help.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.mainMe_pushButton_help.setText("")
        self.mainMe_pushButton_help.setObjectName("mainMe_pushButton_help")
        self.stackedWidget.addWidget(self.mainMe)
        self.an_me = QtWidgets.QWidget()
        self.an_me.setObjectName("an_me")
        self.an_me_pushButton_home = QtWidgets.QPushButton(self.an_me)
        self.an_me_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.an_me_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_me_pushButton_home.setText("")
        self.an_me_pushButton_home.setObjectName("an_me_pushButton_home")
        self.an_me_pushButton_help = QtWidgets.QPushButton(self.an_me)
        self.an_me_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.an_me_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_me_pushButton_help.setText("")
        self.an_me_pushButton_help.setObjectName("an_me_pushButton_help")
        self.an_me_label_title = QtWidgets.QLabel(self.an_me)
        self.an_me_label_title.setGeometry(QtCore.QRect(290, 60, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(54)
        self.an_me_label_title.setFont(font)
        self.an_me_label_title.setStyleSheet("")
        self.an_me_label_title.setObjectName("an_me_label_title")
        self.an_me_pushButton_gRx = QtWidgets.QPushButton(self.an_me)
        self.an_me_pushButton_gRx.setGeometry(QtCore.QRect(40, 150, 340, 280))
        self.an_me_pushButton_gRx.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_GenerateRx.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_me_pushButton_gRx.setText("")
        self.an_me_pushButton_gRx.setObjectName("an_me_pushButton_gRx")
        self.an_me_pushButton_vi = QtWidgets.QPushButton(self.an_me)
        self.an_me_pushButton_vi.setGeometry(QtCore.QRect(420, 150, 340, 280))
        self.an_me_pushButton_vi.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Visualization.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_me_pushButton_vi.setText("")
        self.an_me_pushButton_vi.setObjectName("an_me_pushButton_vi")
        self.stackedWidget.addWidget(self.an_me)
        self.an_gRx1 = QtWidgets.QWidget()
        self.an_gRx1.setObjectName("an_gRx1")
        self.an_gRx1_pushButton_home = QtWidgets.QPushButton(self.an_gRx1)
        self.an_gRx1_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.an_gRx1_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx1_pushButton_home.setText("")
        self.an_gRx1_pushButton_home.setObjectName("an_gRx1_pushButton_home")
        self.an_gRx1_pushButton_help = QtWidgets.QPushButton(self.an_gRx1)
        self.an_gRx1_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.an_gRx1_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_gRx1_pushButton_help.setText("")
        self.an_gRx1_pushButton_help.setObjectName("an_gRx1_pushButton_help")
        self.an_gRx1_label_title = QtWidgets.QLabel(self.an_gRx1)
        self.an_gRx1_label_title.setGeometry(QtCore.QRect(195, 60, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.an_gRx1_label_title.setFont(font)
        self.an_gRx1_label_title.setObjectName("an_gRx1_label_title")
        self.an_gRx1_pushButton_next = QtWidgets.QPushButton(self.an_gRx1)
        self.an_gRx1_pushButton_next.setGeometry(QtCore.QRect(550, 200, 210, 70))
        self.an_gRx1_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"font: 32pt \"Calibri\";\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_gRx1_pushButton_next.setObjectName("an_gRx1_pushButton_next")
        self.an_gRx1_pushButton_previous = QtWidgets.QPushButton(self.an_gRx1)
        self.an_gRx1_pushButton_previous.setGeometry(QtCore.QRect(550, 310, 210, 70))
        self.an_gRx1_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx1_pushButton_previous.setObjectName("an_gRx1_pushButton_previous")
        self.an_gRx1_frame = QtWidgets.QFrame(self.an_gRx1)
        self.an_gRx1_frame.setGeometry(QtCore.QRect(20, 140, 501, 301))
        self.an_gRx1_frame.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.an_gRx1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx1_frame.setObjectName("an_gRx1_frame")
        self.an_gRx1_label_client = QtWidgets.QLabel(self.an_gRx1_frame)
        self.an_gRx1_label_client.setGeometry(QtCore.QRect(20, 0, 461, 60))
        self.an_gRx1_label_client.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx1_label_client.setObjectName("an_gRx1_label_client")
        self.an_gRx1_label_farm = QtWidgets.QLabel(self.an_gRx1_frame)
        self.an_gRx1_label_farm.setGeometry(QtCore.QRect(20, 80, 461, 60))
        self.an_gRx1_label_farm.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.an_gRx1_label_farm.setObjectName("an_gRx1_label_farm")
        self.an_gRx1_label_field = QtWidgets.QLabel(self.an_gRx1_frame)
        self.an_gRx1_label_field.setGeometry(QtCore.QRect(20, 160, 461, 60))
        self.an_gRx1_label_field.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.an_gRx1_label_field.setObjectName("an_gRx1_label_field")
        self.an_gRx1_label_crop = QtWidgets.QLabel(self.an_gRx1_frame)
        self.an_gRx1_label_crop.setGeometry(QtCore.QRect(20, 240, 461, 60))
        self.an_gRx1_label_crop.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx1_label_crop.setObjectName("an_gRx1_label_crop")
        self.an_gRx1_comboBox_client = QtWidgets.QComboBox(self.an_gRx1_frame)
        self.an_gRx1_comboBox_client.setGeometry(QtCore.QRect(150, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx1_comboBox_client.setFont(font)
        self.an_gRx1_comboBox_client.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx1_comboBox_client.setObjectName("an_gRx1_comboBox_client")
        self.an_gRx1_comboBox_farm = QtWidgets.QComboBox(self.an_gRx1_frame)
        self.an_gRx1_comboBox_farm.setGeometry(QtCore.QRect(150, 90, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx1_comboBox_farm.setFont(font)
        self.an_gRx1_comboBox_farm.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx1_comboBox_farm.setObjectName("an_gRx1_comboBox_farm")
        self.an_gRx1_comboBox_field = QtWidgets.QComboBox(self.an_gRx1_frame)
        self.an_gRx1_comboBox_field.setGeometry(QtCore.QRect(150, 170, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx1_comboBox_field.setFont(font)
        self.an_gRx1_comboBox_field.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx1_comboBox_field.setObjectName("an_gRx1_comboBox_field")
        self.an_gRx1_comboBox_crop = QtWidgets.QComboBox(self.an_gRx1_frame)
        self.an_gRx1_comboBox_crop.setGeometry(QtCore.QRect(150, 250, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx1_comboBox_crop.setFont(font)
        self.an_gRx1_comboBox_crop.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx1_comboBox_crop.setObjectName("an_gRx1_comboBox_crop")
        self.an_gRx1_comboBox_crop.addItem("")
        self.stackedWidget.addWidget(self.an_gRx1)
        self.an_gRx2 = QtWidgets.QWidget()
        self.an_gRx2.setObjectName("an_gRx2")
        self.an_gRx2_pushButton_previous = QtWidgets.QPushButton(self.an_gRx2)
        self.an_gRx2_pushButton_previous.setGeometry(QtCore.QRect(550, 310, 210, 70))
        self.an_gRx2_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx2_pushButton_previous.setObjectName("an_gRx2_pushButton_previous")
        self.an_gRx2_label_title = QtWidgets.QLabel(self.an_gRx2)
        self.an_gRx2_label_title.setGeometry(QtCore.QRect(195, 60, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.an_gRx2_label_title.setFont(font)
        self.an_gRx2_label_title.setObjectName("an_gRx2_label_title")
        self.an_gRx2_pushButton_home = QtWidgets.QPushButton(self.an_gRx2)
        self.an_gRx2_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.an_gRx2_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx2_pushButton_home.setText("")
        self.an_gRx2_pushButton_home.setObjectName("an_gRx2_pushButton_home")
        self.an_gRx2_pushButton_help = QtWidgets.QPushButton(self.an_gRx2)
        self.an_gRx2_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.an_gRx2_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_gRx2_pushButton_help.setText("")
        self.an_gRx2_pushButton_help.setObjectName("an_gRx2_pushButton_help")
        self.an_gRx2_pushButton_next = QtWidgets.QPushButton(self.an_gRx2)
        self.an_gRx2_pushButton_next.setGeometry(QtCore.QRect(550, 200, 210, 70))
        self.an_gRx2_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"font: 32pt \"Calibri\";\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_gRx2_pushButton_next.setObjectName("an_gRx2_pushButton_next")
        self.an_gRx2_frame = QtWidgets.QFrame(self.an_gRx2)
        self.an_gRx2_frame.setGeometry(QtCore.QRect(20, 140, 501, 301))
        self.an_gRx2_frame.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.an_gRx2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx2_frame.setObjectName("an_gRx2_frame")
        self.an_gRx2_label_cycle = QtWidgets.QLabel(self.an_gRx2_frame)
        self.an_gRx2_label_cycle.setGeometry(QtCore.QRect(20, 0, 461, 60))
        self.an_gRx2_label_cycle.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx2_label_cycle.setObjectName("an_gRx2_label_cycle")
        self.an_gRx2_label_model = QtWidgets.QLabel(self.an_gRx2_frame)
        self.an_gRx2_label_model.setGeometry(QtCore.QRect(20, 80, 461, 60))
        self.an_gRx2_label_model.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.an_gRx2_label_model.setObjectName("an_gRx2_label_model")
        self.an_gRx2_label_input = QtWidgets.QLabel(self.an_gRx2_frame)
        self.an_gRx2_label_input.setGeometry(QtCore.QRect(20, 160, 461, 60))
        self.an_gRx2_label_input.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx2_label_input.setObjectName("an_gRx2_label_input")
        self.an_gRx2_label_inputUnit = QtWidgets.QLabel(self.an_gRx2_frame)
        self.an_gRx2_label_inputUnit.setGeometry(QtCore.QRect(20, 240, 461, 60))
        self.an_gRx2_label_inputUnit.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx2_label_inputUnit.setObjectName("an_gRx2_label_inputUnit")
        self.an_gRx2_comboBox_cycle = QtWidgets.QComboBox(self.an_gRx2_frame)
        self.an_gRx2_comboBox_cycle.setGeometry(QtCore.QRect(120, 10, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx2_comboBox_cycle.setFont(font)
        self.an_gRx2_comboBox_cycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx2_comboBox_cycle.setObjectName("an_gRx2_comboBox_cycle")
        self.an_gRx2_comboBox_cycle.addItem("")
        self.an_gRx2_comboBox_cycle.addItem("")
        self.an_gRx2_comboBox_model = QtWidgets.QComboBox(self.an_gRx2_frame)
        self.an_gRx2_comboBox_model.setGeometry(QtCore.QRect(160, 90, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx2_comboBox_model.setFont(font)
        self.an_gRx2_comboBox_model.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx2_comboBox_model.setObjectName("an_gRx2_comboBox_model")
        self.an_gRx2_comboBox_model.addItem("")
        self.an_gRx2_comboBox_input = QtWidgets.QComboBox(self.an_gRx2_frame)
        self.an_gRx2_comboBox_input.setGeometry(QtCore.QRect(160, 170, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx2_comboBox_input.setFont(font)
        self.an_gRx2_comboBox_input.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx2_comboBox_input.setObjectName("an_gRx2_comboBox_input")
        self.an_gRx2_comboBox_input.addItem("")
        self.an_gRx2_comboBox_inputUnit = QtWidgets.QComboBox(self.an_gRx2_frame)
        self.an_gRx2_comboBox_inputUnit.setGeometry(QtCore.QRect(260, 250, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx2_comboBox_inputUnit.setFont(font)
        self.an_gRx2_comboBox_inputUnit.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx2_comboBox_inputUnit.setObjectName("an_gRx2_comboBox_inputUnit")
        self.an_gRx2_comboBox_inputUnit.addItem("")
        self.stackedWidget.addWidget(self.an_gRx2)
        self.an_gRx3 = QtWidgets.QWidget()
        self.an_gRx3.setObjectName("an_gRx3")
        self.an_gRx3_pushButton_previous = QtWidgets.QPushButton(self.an_gRx3)
        self.an_gRx3_pushButton_previous.setGeometry(QtCore.QRect(550, 310, 210, 70))
        self.an_gRx3_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx3_pushButton_previous.setObjectName("an_gRx3_pushButton_previous")
        self.an_gRx3_pushButton_next = QtWidgets.QPushButton(self.an_gRx3)
        self.an_gRx3_pushButton_next.setGeometry(QtCore.QRect(550, 200, 210, 70))
        self.an_gRx3_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"font: 32pt \"Calibri\";\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_gRx3_pushButton_next.setObjectName("an_gRx3_pushButton_next")
        self.an_gRx3_pushButton_home = QtWidgets.QPushButton(self.an_gRx3)
        self.an_gRx3_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.an_gRx3_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx3_pushButton_home.setText("")
        self.an_gRx3_pushButton_home.setObjectName("an_gRx3_pushButton_home")
        self.an_gRx3_label_title = QtWidgets.QLabel(self.an_gRx3)
        self.an_gRx3_label_title.setGeometry(QtCore.QRect(195, 60, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.an_gRx3_label_title.setFont(font)
        self.an_gRx3_label_title.setObjectName("an_gRx3_label_title")
        self.an_gRx3_pushButton_help = QtWidgets.QPushButton(self.an_gRx3)
        self.an_gRx3_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.an_gRx3_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_gRx3_pushButton_help.setText("")
        self.an_gRx3_pushButton_help.setObjectName("an_gRx3_pushButton_help")
        self.an_gRx3_frame = QtWidgets.QFrame(self.an_gRx3)
        self.an_gRx3_frame.setGeometry(QtCore.QRect(20, 140, 501, 301))
        self.an_gRx3_frame.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.an_gRx3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx3_frame.setObjectName("an_gRx3_frame")
        self.an_gRx3_label_inputCost = QtWidgets.QLabel(self.an_gRx3_frame)
        self.an_gRx3_label_inputCost.setGeometry(QtCore.QRect(20, 0, 461, 60))
        self.an_gRx3_label_inputCost.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx3_label_inputCost.setObjectName("an_gRx3_label_inputCost")
        self.an_gRx3_textEdit_inputCost = QtWidgets.QTextEdit(self.an_gRx3_frame)
        self.an_gRx3_textEdit_inputCost.setEnabled(True)
        self.an_gRx3_textEdit_inputCost.setGeometry(QtCore.QRect(290, 6, 171, 47))
        self.an_gRx3_textEdit_inputCost.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"background-color: rgb(64, 64, 64);\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(236, 239, 240);")
        self.an_gRx3_textEdit_inputCost.setObjectName("an_gRx3_textEdit_inputCost")
        self.an_gRx3_textEdit_yieldGoal = QtWidgets.QTextEdit(self.an_gRx3_frame)
        self.an_gRx3_textEdit_yieldGoal.setGeometry(QtCore.QRect(290, 86, 171, 47))
        self.an_gRx3_textEdit_yieldGoal.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"background-color: rgb(64, 64, 64);\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(236, 239, 240);")
        self.an_gRx3_textEdit_yieldGoal.setObjectName("an_gRx3_textEdit_yieldGoal")
        self.an_gRx3_comboBox_refCycle = QtWidgets.QComboBox(self.an_gRx3_frame)
        self.an_gRx3_comboBox_refCycle.setGeometry(QtCore.QRect(280, 169, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx3_comboBox_refCycle.setFont(font)
        self.an_gRx3_comboBox_refCycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx3_comboBox_refCycle.setObjectName("an_gRx3_comboBox_refCycle")
        self.an_gRx3_label_refCycle = QtWidgets.QLabel(self.an_gRx3_frame)
        self.an_gRx3_label_refCycle.setGeometry(QtCore.QRect(20, 160, 461, 60))
        self.an_gRx3_label_refCycle.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx3_label_refCycle.setObjectName("an_gRx3_label_refCycle")
        self.an_gRx3_label_yieldGoal = QtWidgets.QLabel(self.an_gRx3_frame)
        self.an_gRx3_label_yieldGoal.setGeometry(QtCore.QRect(20, 80, 461, 60))
        self.an_gRx3_label_yieldGoal.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx3_label_yieldGoal.setObjectName("an_gRx3_label_yieldGoal")
        self.an_gRx3_label_application = QtWidgets.QLabel(self.an_gRx3_frame)
        self.an_gRx3_label_application.setGeometry(QtCore.QRect(20, 240, 461, 60))
        self.an_gRx3_label_application.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx3_label_application.setObjectName("an_gRx3_label_application")
        self.an_gRx3_comboBox_application = QtWidgets.QComboBox(self.an_gRx3_frame)
        self.an_gRx3_comboBox_application.setGeometry(QtCore.QRect(210, 250, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.an_gRx3_comboBox_application.setFont(font)
        self.an_gRx3_comboBox_application.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_gRx3_comboBox_application.setObjectName("an_gRx3_comboBox_application")
        self.an_gRx3_comboBox_application.addItem("")
        self.an_gRx3_label_refCycle.raise_()
        self.an_gRx3_label_yieldGoal.raise_()
        self.an_gRx3_label_inputCost.raise_()
        self.an_gRx3_textEdit_inputCost.raise_()
        self.an_gRx3_textEdit_yieldGoal.raise_()
        self.an_gRx3_comboBox_refCycle.raise_()
        self.an_gRx3_label_application.raise_()
        self.an_gRx3_comboBox_application.raise_()
        self.stackedWidget.addWidget(self.an_gRx3)
        self.an_gRx4 = QtWidgets.QWidget()
        self.an_gRx4.setObjectName("an_gRx4")
        self.an_gRx4_pushButton_help = QtWidgets.QPushButton(self.an_gRx4)
        self.an_gRx4_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.an_gRx4_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_gRx4_pushButton_help.setText("")
        self.an_gRx4_pushButton_help.setObjectName("an_gRx4_pushButton_help")
        self.an_gRx4_label_title = QtWidgets.QLabel(self.an_gRx4)
        self.an_gRx4_label_title.setGeometry(QtCore.QRect(240, 60, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.an_gRx4_label_title.setFont(font)
        self.an_gRx4_label_title.setObjectName("an_gRx4_label_title")
        self.an_gRx4_pushButton_home = QtWidgets.QPushButton(self.an_gRx4)
        self.an_gRx4_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.an_gRx4_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx4_pushButton_home.setText("")
        self.an_gRx4_pushButton_home.setObjectName("an_gRx4_pushButton_home")
        self.an_gRx4_pushButton_generateRx = QtWidgets.QPushButton(self.an_gRx4)
        self.an_gRx4_pushButton_generateRx.setGeometry(QtCore.QRect(470, 360, 290, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_gRx4_pushButton_generateRx.setFont(font)
        self.an_gRx4_pushButton_generateRx.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(74, 143, 231);\n"
"background-image: url(:/Img/Img/pushButton_Action_GenerateRx.png);\n"
"color: rgb(236, 239, 240);\n"
"font: 38pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.an_gRx4_pushButton_generateRx.setObjectName("an_gRx4_pushButton_generateRx")
        self.an_gRx4_pushButton_previous = QtWidgets.QPushButton(self.an_gRx4)
        self.an_gRx4_pushButton_previous.setGeometry(QtCore.QRect(40, 370, 270, 70))
        self.an_gRx4_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx4_pushButton_previous.setObjectName("an_gRx4_pushButton_previous")
        self.an_gRx4_frame = QtWidgets.QFrame(self.an_gRx4)
        self.an_gRx4_frame.setGeometry(QtCore.QRect(40, 140, 721, 211))
        self.an_gRx4_frame.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 20px;")
        self.an_gRx4_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx4_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx4_frame.setObjectName("an_gRx4_frame")
        self.an_gRx4_label_data1 = QtWidgets.QLabel(self.an_gRx4_frame)
        self.an_gRx4_label_data1.setGeometry(QtCore.QRect(10, 8, 331, 191))
        self.an_gRx4_label_data1.setStyleSheet("font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"background-color: rgb(64, 64, 64);")
        self.an_gRx4_label_data1.setObjectName("an_gRx4_label_data1")
        self.an_gRx4_label_data2 = QtWidgets.QLabel(self.an_gRx4_frame)
        self.an_gRx4_label_data2.setGeometry(QtCore.QRect(370, 8, 341, 190))
        self.an_gRx4_label_data2.setStyleSheet("font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"background-color: rgb(64, 64, 64);")
        self.an_gRx4_label_data2.setObjectName("an_gRx4_label_data2")
        self.stackedWidget.addWidget(self.an_gRx4)
        self.an_gRx5 = QtWidgets.QWidget()
        self.an_gRx5.setObjectName("an_gRx5")
        self.an_gRx5_pushButton_home = QtWidgets.QPushButton(self.an_gRx5)
        self.an_gRx5_pushButton_home.setGeometry(QtCore.QRect(590, 60, 51, 51))
        self.an_gRx5_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/pushButton_Home2.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx5_pushButton_home.setText("")
        self.an_gRx5_pushButton_home.setObjectName("an_gRx5_pushButton_home")
        self.an_gRx5_label_title = QtWidgets.QLabel(self.an_gRx5)
        self.an_gRx5_label_title.setGeometry(QtCore.QRect(590, 120, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_gRx5_label_title.setFont(font)
        self.an_gRx5_label_title.setStyleSheet("font: 24pt \"Calibri\";")
        self.an_gRx5_label_title.setObjectName("an_gRx5_label_title")
        self.an_gRx5_pushButton_help = QtWidgets.QPushButton(self.an_gRx5)
        self.an_gRx5_pushButton_help.setGeometry(QtCore.QRect(710, 60, 50, 50))
        self.an_gRx5_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_gRx5_pushButton_help.setText("")
        self.an_gRx5_pushButton_help.setObjectName("an_gRx5_pushButton_help")
        self.an_gRx5_pushButton_back = QtWidgets.QPushButton(self.an_gRx5)
        self.an_gRx5_pushButton_back.setGeometry(QtCore.QRect(590, 340, 171, 51))
        self.an_gRx5_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx5_pushButton_back.setObjectName("an_gRx5_pushButton_back")
        self.an_gRx5_pushButton_exportRx = QtWidgets.QPushButton(self.an_gRx5)
        self.an_gRx5_pushButton_exportRx.setGeometry(QtCore.QRect(590, 250, 171, 81))
        self.an_gRx5_pushButton_exportRx.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(74, 143, 231);\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.an_gRx5_pushButton_exportRx.setObjectName("an_gRx5_pushButton_exportRx")
        self.an_gRx5_pushButton_ecEs = QtWidgets.QPushButton(self.an_gRx5)
        self.an_gRx5_pushButton_ecEs.setGeometry(QtCore.QRect(590, 180, 171, 61))
        self.an_gRx5_pushButton_ecEs.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(160, 181, 50);\n"
"font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_gRx5_pushButton_ecEs.setObjectName("an_gRx5_pushButton_ecEs")
        self.an_gRx5_plot = MplWidget(self.an_gRx5)
        self.an_gRx5_plot.setGeometry(QtCore.QRect(19, 9, 551, 451))
        self.an_gRx5_plot.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.an_gRx5_plot.setObjectName("an_gRx5_plot")
        self.stackedWidget.addWidget(self.an_gRx5)
        self.an_gRx6 = QtWidgets.QWidget()
        self.an_gRx6.setObjectName("an_gRx6")
        self.an_gRx6_pushButton_home = QtWidgets.QPushButton(self.an_gRx6)
        self.an_gRx6_pushButton_home.setGeometry(QtCore.QRect(40, 20, 75, 75))
        self.an_gRx6_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx6_pushButton_home.setText("")
        self.an_gRx6_pushButton_home.setObjectName("an_gRx6_pushButton_home")
        self.an_gRx6_label_title = QtWidgets.QLabel(self.an_gRx6)
        self.an_gRx6_label_title.setGeometry(QtCore.QRect(190, 40, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.an_gRx6_label_title.setFont(font)
        self.an_gRx6_label_title.setObjectName("an_gRx6_label_title")
        self.an_gRx6_pushButton_help = QtWidgets.QPushButton(self.an_gRx6)
        self.an_gRx6_pushButton_help.setGeometry(QtCore.QRect(710, 20, 50, 50))
        self.an_gRx6_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_gRx6_pushButton_help.setText("")
        self.an_gRx6_pushButton_help.setObjectName("an_gRx6_pushButton_help")
        self.an_gRx6_frame_input = QtWidgets.QFrame(self.an_gRx6)
        self.an_gRx6_frame_input.setGeometry(QtCore.QRect(40, 100, 340, 241))
        self.an_gRx6_frame_input.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 20px;\n"
"")
        self.an_gRx6_frame_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx6_frame_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx6_frame_input.setObjectName("an_gRx6_frame_input")
        self.an_gRx6_label_inputTitle = QtWidgets.QLabel(self.an_gRx6_frame_input)
        self.an_gRx6_label_inputTitle.setGeometry(QtCore.QRect(110, 10, 111, 31))
        self.an_gRx6_label_inputTitle.setStyleSheet("font: 28pt \"Calibri\";")
        self.an_gRx6_label_inputTitle.setObjectName("an_gRx6_label_inputTitle")
        self.an_gRx6_label_inputEstLabel = QtWidgets.QLabel(self.an_gRx6_frame_input)
        self.an_gRx6_label_inputEstLabel.setGeometry(QtCore.QRect(30, 60, 201, 20))
        self.an_gRx6_label_inputEstLabel.setStyleSheet("font: 18pt \"Calibri\";")
        self.an_gRx6_label_inputEstLabel.setObjectName("an_gRx6_label_inputEstLabel")
        self.an_gRx6_label_inputEstIndicator = QtWidgets.QLabel(self.an_gRx6_frame_input)
        self.an_gRx6_label_inputEstIndicator.setGeometry(QtCore.QRect(230, 45, 91, 51))
        self.an_gRx6_label_inputEstIndicator.setStyleSheet("font: 25pt \"Calibri\";")
        self.an_gRx6_label_inputEstIndicator.setObjectName("an_gRx6_label_inputEstIndicator")
        self.an_gRx6_frame_inputIndicators = QtWidgets.QFrame(self.an_gRx6_frame_input)
        self.an_gRx6_frame_inputIndicators.setGeometry(QtCore.QRect(19, 105, 301, 121))
        self.an_gRx6_frame_inputIndicators.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.an_gRx6_frame_inputIndicators.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx6_frame_inputIndicators.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx6_frame_inputIndicators.setObjectName("an_gRx6_frame_inputIndicators")
        self.an_gRx6_label_inputQuanIndicator = QtWidgets.QLabel(self.an_gRx6_frame_inputIndicators)
        self.an_gRx6_label_inputQuanIndicator.setGeometry(QtCore.QRect(20, 55, 271, 61))
        self.an_gRx6_label_inputQuanIndicator.setStyleSheet("font: 35pt \"Calibri\";\n"
"color: rgb(160, 181, 50);")
        self.an_gRx6_label_inputQuanIndicator.setObjectName("an_gRx6_label_inputQuanIndicator")
        self.an_gRx6_label_inputPercIndicator = QtWidgets.QLabel(self.an_gRx6_frame_inputIndicators)
        self.an_gRx6_label_inputPercIndicator.setGeometry(QtCore.QRect(20, 0, 201, 61))
        self.an_gRx6_label_inputPercIndicator.setStyleSheet("font: 35pt \"Calibri\";\n"
"color: rgb(160, 181, 50);")
        self.an_gRx6_label_inputPercIndicator.setObjectName("an_gRx6_label_inputPercIndicator")
        self.an_gRx6_pushButton_back = QtWidgets.QPushButton(self.an_gRx6)
        self.an_gRx6_pushButton_back.setGeometry(QtCore.QRect(570, 350, 191, 81))
        self.an_gRx6_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(160, 181, 50);\n"
"font: 30pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_gRx6_pushButton_back.setObjectName("an_gRx6_pushButton_back")
        self.an_gRx6_frame_yield = QtWidgets.QFrame(self.an_gRx6)
        self.an_gRx6_frame_yield.setGeometry(QtCore.QRect(420, 100, 340, 241))
        self.an_gRx6_frame_yield.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 20px;\n"
"")
        self.an_gRx6_frame_yield.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx6_frame_yield.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx6_frame_yield.setObjectName("an_gRx6_frame_yield")
        self.an_gRx6_label_yieldTitle = QtWidgets.QLabel(self.an_gRx6_frame_yield)
        self.an_gRx6_label_yieldTitle.setGeometry(QtCore.QRect(75, 10, 191, 31))
        self.an_gRx6_label_yieldTitle.setStyleSheet("font: 28pt \"Calibri\";")
        self.an_gRx6_label_yieldTitle.setObjectName("an_gRx6_label_yieldTitle")
        self.an_gRx6_label_yieldEstLabel1 = QtWidgets.QLabel(self.an_gRx6_frame_yield)
        self.an_gRx6_label_yieldEstLabel1.setGeometry(QtCore.QRect(20, 60, 201, 20))
        self.an_gRx6_label_yieldEstLabel1.setStyleSheet("font: 18pt \"Calibri\";")
        self.an_gRx6_label_yieldEstLabel1.setObjectName("an_gRx6_label_yieldEstLabel1")
        self.an_gRx6_label_yieldEstIndicator = QtWidgets.QLabel(self.an_gRx6_frame_yield)
        self.an_gRx6_label_yieldEstIndicator.setGeometry(QtCore.QRect(190, 45, 151, 51))
        self.an_gRx6_label_yieldEstIndicator.setStyleSheet("font: 25pt \"Calibri\";\n"
"backround-color: rgba(0,0,0,0)")
        self.an_gRx6_label_yieldEstIndicator.setObjectName("an_gRx6_label_yieldEstIndicator")
        self.an_gRx6_frame_yieldIndicators = QtWidgets.QFrame(self.an_gRx6_frame_yield)
        self.an_gRx6_frame_yieldIndicators.setGeometry(QtCore.QRect(19, 105, 301, 121))
        self.an_gRx6_frame_yieldIndicators.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.an_gRx6_frame_yieldIndicators.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx6_frame_yieldIndicators.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx6_frame_yieldIndicators.setObjectName("an_gRx6_frame_yieldIndicators")
        self.an_gRx6_label_yieldQuanIndicator = QtWidgets.QLabel(self.an_gRx6_frame_yieldIndicators)
        self.an_gRx6_label_yieldQuanIndicator.setGeometry(QtCore.QRect(20, 55, 271, 61))
        self.an_gRx6_label_yieldQuanIndicator.setStyleSheet("font: 35pt \"Calibri\";\n"
"color: rgb(160, 181, 50);")
        self.an_gRx6_label_yieldQuanIndicator.setObjectName("an_gRx6_label_yieldQuanIndicator")
        self.an_gRx6_label_yieldPercIndicator = QtWidgets.QLabel(self.an_gRx6_frame_yieldIndicators)
        self.an_gRx6_label_yieldPercIndicator.setGeometry(QtCore.QRect(20, 0, 201, 61))
        self.an_gRx6_label_yieldPercIndicator.setStyleSheet("font: 35pt \"Calibri\";\n"
"color: rgb(160, 181, 50);")
        self.an_gRx6_label_yieldPercIndicator.setObjectName("an_gRx6_label_yieldPercIndicator")
        self.an_gRx6_label_yieldTitle.raise_()
        self.an_gRx6_frame_yieldIndicators.raise_()
        self.an_gRx6_label_yieldEstLabel1.raise_()
        self.an_gRx6_label_yieldEstIndicator.raise_()
        self.an_gRx6_frame_total = QtWidgets.QFrame(self.an_gRx6)
        self.an_gRx6_frame_total.setGeometry(QtCore.QRect(40, 350, 521, 81))
        self.an_gRx6_frame_total.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 20px;\n"
"")
        self.an_gRx6_frame_total.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx6_frame_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx6_frame_total.setObjectName("an_gRx6_frame_total")
        self.an_gRx6_label_totalLabel = QtWidgets.QLabel(self.an_gRx6_frame_total)
        self.an_gRx6_label_totalLabel.setGeometry(QtCore.QRect(10, 10, 211, 60))
        self.an_gRx6_label_totalLabel.setStyleSheet("font: 32pt \"Calibri\";")
        self.an_gRx6_label_totalLabel.setObjectName("an_gRx6_label_totalLabel")
        self.an_gRx6_label_totalIndicator = QtWidgets.QLabel(self.an_gRx6_frame_total)
        self.an_gRx6_label_totalIndicator.setGeometry(QtCore.QRect(210, 10, 301, 61))
        self.an_gRx6_label_totalIndicator.setStyleSheet("font: 44pt \"Calibri\";\n"
"background-color: rgb(64, 64, 64);\n"
"color: rgb(160, 181, 50);")
        self.an_gRx6_label_totalIndicator.setObjectName("an_gRx6_label_totalIndicator")
        self.an_gRx6_label_referenceCycle = QtWidgets.QLabel(self.an_gRx6)
        self.an_gRx6_label_referenceCycle.setGeometry(QtCore.QRect(40, 430, 441, 30))
        self.an_gRx6_label_referenceCycle.setStyleSheet("font: 18pt \"Calibri\";")
        self.an_gRx6_label_referenceCycle.setObjectName("an_gRx6_label_referenceCycle")
        self.stackedWidget.addWidget(self.an_gRx6)
        self.an_gRx7 = QtWidgets.QWidget()
        self.an_gRx7.setObjectName("an_gRx7")
        self.an_gRx7_label_title = QtWidgets.QLabel(self.an_gRx7)
        self.an_gRx7_label_title.setGeometry(QtCore.QRect(190, 60, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.an_gRx7_label_title.setFont(font)
        self.an_gRx7_label_title.setObjectName("an_gRx7_label_title")
        self.an_gRx7_pushButton_home = QtWidgets.QPushButton(self.an_gRx7)
        self.an_gRx7_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.an_gRx7_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx7_pushButton_home.setText("")
        self.an_gRx7_pushButton_home.setObjectName("an_gRx7_pushButton_home")
        self.an_gRx7_pushButton_help = QtWidgets.QPushButton(self.an_gRx7)
        self.an_gRx7_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.an_gRx7_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_gRx7_pushButton_help.setText("")
        self.an_gRx7_pushButton_help.setObjectName("an_gRx7_pushButton_help")
        self.an_gRx7_frame_fileLocation = QtWidgets.QFrame(self.an_gRx7)
        self.an_gRx7_frame_fileLocation.setGeometry(QtCore.QRect(40, 150, 720, 121))
        self.an_gRx7_frame_fileLocation.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px")
        self.an_gRx7_frame_fileLocation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_gRx7_frame_fileLocation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_gRx7_frame_fileLocation.setObjectName("an_gRx7_frame_fileLocation")
        self.an_gRx7_textEdit_fileLocation = QtWidgets.QTextEdit(self.an_gRx7_frame_fileLocation)
        self.an_gRx7_textEdit_fileLocation.setGeometry(QtCore.QRect(10, 55, 701, 51))
        self.an_gRx7_textEdit_fileLocation.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(236, 239, 240);\n"
"font: 24pt \"Calibri\";")
        self.an_gRx7_textEdit_fileLocation.setObjectName("an_gRx7_textEdit_fileLocation")
        self.an_gRx7_label_fileLocation = QtWidgets.QLabel(self.an_gRx7_frame_fileLocation)
        self.an_gRx7_label_fileLocation.setGeometry(QtCore.QRect(10, 15, 341, 31))
        self.an_gRx7_label_fileLocation.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 28pt \"Calibri\";\n"
"color: rgb(0, 0, 0);")
        self.an_gRx7_label_fileLocation.setObjectName("an_gRx7_label_fileLocation")
        self.an_gRx7_checkBox_eraseUSB = QtWidgets.QCheckBox(self.an_gRx7)
        self.an_gRx7_checkBox_eraseUSB.setGeometry(QtCore.QRect(40, 300, 311, 61))
        self.an_gRx7_checkBox_eraseUSB.setStyleSheet("QCheckBox\n"
"{\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QCheckBox::indicator::checked\n"
"{\n"
"image: url(:/Img/Img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"image: url(:/Img/Img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed\n"
"{\n"
"image: url(:/Img/Img/checkbox_checked_pressed.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed\n"
"{\n"
"image: url(:/Img/Img/checkbox_unchecked_pressed.png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.an_gRx7_checkBox_eraseUSB.setIconSize(QtCore.QSize(16, 16))
        self.an_gRx7_checkBox_eraseUSB.setChecked(False)
        self.an_gRx7_checkBox_eraseUSB.setTristate(False)
        self.an_gRx7_checkBox_eraseUSB.setObjectName("an_gRx7_checkBox_eraseUSB")
        self.an_gRx7_pushButton_back = QtWidgets.QPushButton(self.an_gRx7)
        self.an_gRx7_pushButton_back.setGeometry(QtCore.QRect(40, 390, 301, 51))
        self.an_gRx7_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_gRx7_pushButton_back.setObjectName("an_gRx7_pushButton_back")
        self.an_gRx7_pushButton_exportRx = QtWidgets.QPushButton(self.an_gRx7)
        self.an_gRx7_pushButton_exportRx.setGeometry(QtCore.QRect(400, 299, 360, 141))
        self.an_gRx7_pushButton_exportRx.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(74, 143, 231);\n"
"background-image: url(:/Img/Img/pushButton_ExportRx.png);\n"
"color: rgb(236, 239, 240);\n"
"font: 38pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.an_gRx7_pushButton_exportRx.setText("")
        self.an_gRx7_pushButton_exportRx.setObjectName("an_gRx7_pushButton_exportRx")
        self.stackedWidget.addWidget(self.an_gRx7)
        self.an_vi_me = QtWidgets.QWidget()
        self.an_vi_me.setObjectName("an_vi_me")
        self.an_vi_me_pushButton_home = QtWidgets.QPushButton(self.an_vi_me)
        self.an_vi_me_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.an_vi_me_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_me_pushButton_home.setText("")
        self.an_vi_me_pushButton_home.setObjectName("an_vi_me_pushButton_home")
        self.an_vi_me_label_title = QtWidgets.QLabel(self.an_vi_me)
        self.an_vi_me_label_title.setGeometry(QtCore.QRect(280, 60, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.an_vi_me_label_title.setFont(font)
        self.an_vi_me_label_title.setStyleSheet("font: 36pt \"Calibri\";")
        self.an_vi_me_label_title.setObjectName("an_vi_me_label_title")
        self.an_vi_me_pushButton_help = QtWidgets.QPushButton(self.an_vi_me)
        self.an_vi_me_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.an_vi_me_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_vi_me_pushButton_help.setText("")
        self.an_vi_me_pushButton_help.setObjectName("an_vi_me_pushButton_help")
        self.an_vi_me_pushButton_diagnosisMaps = QtWidgets.QPushButton(self.an_vi_me)
        self.an_vi_me_pushButton_diagnosisMaps.setGeometry(QtCore.QRect(40, 139, 350, 140))
        self.an_vi_me_pushButton_diagnosisMaps.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_DiagnosisMaps.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_me_pushButton_diagnosisMaps.setText("")
        self.an_vi_me_pushButton_diagnosisMaps.setObjectName("an_vi_me_pushButton_diagnosisMaps")
        self.an_vi_me_pushButton_scatter = QtWidgets.QPushButton(self.an_vi_me)
        self.an_vi_me_pushButton_scatter.setGeometry(QtCore.QRect(40, 300, 350, 140))
        self.an_vi_me_pushButton_scatter.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Scatter.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_me_pushButton_scatter.setText("")
        self.an_vi_me_pushButton_scatter.setObjectName("an_vi_me_pushButton_scatter")
        self.an_vi_me_pushButton_regression = QtWidgets.QPushButton(self.an_vi_me)
        self.an_vi_me_pushButton_regression.setGeometry(QtCore.QRect(409, 300, 350, 140))
        self.an_vi_me_pushButton_regression.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Regression.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_me_pushButton_regression.setText("")
        self.an_vi_me_pushButton_regression.setObjectName("an_vi_me_pushButton_regression")
        self.an_vi_me_pushButton_distribution = QtWidgets.QPushButton(self.an_vi_me)
        self.an_vi_me_pushButton_distribution.setGeometry(QtCore.QRect(409, 139, 350, 140))
        self.an_vi_me_pushButton_distribution.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Distribution.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_me_pushButton_distribution.setText("")
        self.an_vi_me_pushButton_distribution.setObjectName("an_vi_me_pushButton_distribution")
        self.stackedWidget.addWidget(self.an_vi_me)
        self.an_vi_dMa = QtWidgets.QWidget()
        self.an_vi_dMa.setObjectName("an_vi_dMa")
        self.an_vi_dMa_label_title = QtWidgets.QLabel(self.an_vi_dMa)
        self.an_vi_dMa_label_title.setGeometry(QtCore.QRect(645, 10, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_dMa_label_title.setFont(font)
        self.an_vi_dMa_label_title.setStyleSheet("font: 20pt \"Calibri\";")
        self.an_vi_dMa_label_title.setObjectName("an_vi_dMa_label_title")
        self.an_vi_dMa_pushButton_home = QtWidgets.QPushButton(self.an_vi_dMa)
        self.an_vi_dMa_pushButton_home.setGeometry(QtCore.QRect(570, 10, 50, 50))
        self.an_vi_dMa_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 13px;\n"
"background-image: url(:/Img/Img/pushButton_Home2.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_dMa_pushButton_home.setText("")
        self.an_vi_dMa_pushButton_home.setObjectName("an_vi_dMa_pushButton_home")
        self.an_vi_dMa_pushButton_help = QtWidgets.QPushButton(self.an_vi_dMa)
        self.an_vi_dMa_pushButton_help.setGeometry(QtCore.QRect(733, 6, 50, 50))
        self.an_vi_dMa_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_vi_dMa_pushButton_help.setText("")
        self.an_vi_dMa_pushButton_help.setObjectName("an_vi_dMa_pushButton_help")
        self.an_vi_dMa_pushButton_save = QtWidgets.QPushButton(self.an_vi_dMa)
        self.an_vi_dMa_pushButton_save.setGeometry(QtCore.QRect(730, 400, 50, 50))
        self.an_vi_dMa_pushButton_save.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(160, 181, 50);\n"
"background-image: url(:/Img/Img/pushButton_Save.png);\n"
"font: 17pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_vi_dMa_pushButton_save.setText("")
        self.an_vi_dMa_pushButton_save.setObjectName("an_vi_dMa_pushButton_save")
        self.an_vi_dMa_pushButton_back = QtWidgets.QPushButton(self.an_vi_dMa)
        self.an_vi_dMa_pushButton_back.setGeometry(QtCore.QRect(570, 400, 141, 51))
        self.an_vi_dMa_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 20pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_dMa_pushButton_back.setObjectName("an_vi_dMa_pushButton_back")
        self.an_vi_dMa_frame_parameters = QtWidgets.QFrame(self.an_vi_dMa)
        self.an_vi_dMa_frame_parameters.setGeometry(QtCore.QRect(560, 70, 241, 321))
        self.an_vi_dMa_frame_parameters.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.an_vi_dMa_frame_parameters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_vi_dMa_frame_parameters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_vi_dMa_frame_parameters.setObjectName("an_vi_dMa_frame_parameters")
        self.an_vi_dMa_comboBox_client = QtWidgets.QComboBox(self.an_vi_dMa_frame_parameters)
        self.an_vi_dMa_comboBox_client.setGeometry(QtCore.QRect(10, 10, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_dMa_comboBox_client.setFont(font)
        self.an_vi_dMa_comboBox_client.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_dMa_comboBox_client.setObjectName("an_vi_dMa_comboBox_client")
        self.an_vi_dMa_comboBox_farm = QtWidgets.QComboBox(self.an_vi_dMa_frame_parameters)
        self.an_vi_dMa_comboBox_farm.setGeometry(QtCore.QRect(10, 60, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_dMa_comboBox_farm.setFont(font)
        self.an_vi_dMa_comboBox_farm.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_dMa_comboBox_farm.setObjectName("an_vi_dMa_comboBox_farm")
        self.an_vi_dMa_comboBox_field = QtWidgets.QComboBox(self.an_vi_dMa_frame_parameters)
        self.an_vi_dMa_comboBox_field.setGeometry(QtCore.QRect(10, 110, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_dMa_comboBox_field.setFont(font)
        self.an_vi_dMa_comboBox_field.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_dMa_comboBox_field.setObjectName("an_vi_dMa_comboBox_field")
        self.an_vi_dMa_pushButton_generate = QtWidgets.QPushButton(self.an_vi_dMa_frame_parameters)
        self.an_vi_dMa_pushButton_generate.setGeometry(QtCore.QRect(10, 260, 211, 51))
        self.an_vi_dMa_pushButton_generate.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(74, 143, 231);\n"
"font: 28pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.an_vi_dMa_pushButton_generate.setObjectName("an_vi_dMa_pushButton_generate")
        self.an_vi_dMa_label_cycle = QtWidgets.QLabel(self.an_vi_dMa_frame_parameters)
        self.an_vi_dMa_label_cycle.setGeometry(QtCore.QRect(10, 160, 201, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_dMa_label_cycle.setFont(font)
        self.an_vi_dMa_label_cycle.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_dMa_label_cycle.setObjectName("an_vi_dMa_label_cycle")
        self.an_vi_dMa_comboBox_cycle = QtWidgets.QComboBox(self.an_vi_dMa_frame_parameters)
        self.an_vi_dMa_comboBox_cycle.setGeometry(QtCore.QRect(80, 160, 141, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_dMa_comboBox_cycle.setFont(font)
        self.an_vi_dMa_comboBox_cycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_dMa_comboBox_cycle.setObjectName("an_vi_dMa_comboBox_cycle")
        self.an_vi_dMa_comboBox_variable = QtWidgets.QComboBox(self.an_vi_dMa_frame_parameters)
        self.an_vi_dMa_comboBox_variable.setGeometry(QtCore.QRect(10, 210, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_dMa_comboBox_variable.setFont(font)
        self.an_vi_dMa_comboBox_variable.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_dMa_comboBox_variable.setObjectName("an_vi_dMa_comboBox_variable")
        self.an_vi_dMa_label_cycle.raise_()
        self.an_vi_dMa_comboBox_client.raise_()
        self.an_vi_dMa_comboBox_farm.raise_()
        self.an_vi_dMa_comboBox_field.raise_()
        self.an_vi_dMa_pushButton_generate.raise_()
        self.an_vi_dMa_comboBox_cycle.raise_()
        self.an_vi_dMa_comboBox_variable.raise_()
        self.an_vi_dMa_plot = MplWidget(self.an_vi_dMa)
        self.an_vi_dMa_plot.setGeometry(QtCore.QRect(9, -1, 541, 461))
        self.an_vi_dMa_plot.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.an_vi_dMa_plot.setObjectName("an_vi_dMa_plot")
        self.stackedWidget.addWidget(self.an_vi_dMa)
        self.an_vi_di = QtWidgets.QWidget()
        self.an_vi_di.setObjectName("an_vi_di")
        self.an_vi_di_pushButton_help = QtWidgets.QPushButton(self.an_vi_di)
        self.an_vi_di_pushButton_help.setGeometry(QtCore.QRect(710, 20, 50, 50))
        self.an_vi_di_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_vi_di_pushButton_help.setText("")
        self.an_vi_di_pushButton_help.setObjectName("an_vi_di_pushButton_help")
        self.an_vi_di_label_title = QtWidgets.QLabel(self.an_vi_di)
        self.an_vi_di_label_title.setGeometry(QtCore.QRect(300, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_label_title.setFont(font)
        self.an_vi_di_label_title.setStyleSheet("font: 30pt \"Calibri\";")
        self.an_vi_di_label_title.setObjectName("an_vi_di_label_title")
        self.an_vi_di_pushButton_home = QtWidgets.QPushButton(self.an_vi_di)
        self.an_vi_di_pushButton_home.setGeometry(QtCore.QRect(40, 20, 50, 50))
        self.an_vi_di_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 13px;\n"
"background-image: url(:/Img/Img/pushButton_Home2.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_di_pushButton_home.setText("")
        self.an_vi_di_pushButton_home.setObjectName("an_vi_di_pushButton_home")
        self.an_vi_di_pushButton_save = QtWidgets.QPushButton(self.an_vi_di)
        self.an_vi_di_pushButton_save.setGeometry(QtCore.QRect(710, 400, 50, 50))
        self.an_vi_di_pushButton_save.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(160, 181, 50);\n"
"background-image: url(:/Img/Img/pushButton_Save.png);\n"
"font: 17pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_vi_di_pushButton_save.setText("")
        self.an_vi_di_pushButton_save.setObjectName("an_vi_di_pushButton_save")
        self.an_vi_di_pushButton_back = QtWidgets.QPushButton(self.an_vi_di)
        self.an_vi_di_pushButton_back.setGeometry(QtCore.QRect(550, 400, 141, 51))
        self.an_vi_di_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 20pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_di_pushButton_back.setObjectName("an_vi_di_pushButton_back")
        self.an_vi_di_frame_parameters = QtWidgets.QFrame(self.an_vi_di)
        self.an_vi_di_frame_parameters.setGeometry(QtCore.QRect(540, 70, 241, 321))
        self.an_vi_di_frame_parameters.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.an_vi_di_frame_parameters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_vi_di_frame_parameters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_vi_di_frame_parameters.setObjectName("an_vi_di_frame_parameters")
        self.an_vi_di_comboBox_client = QtWidgets.QComboBox(self.an_vi_di_frame_parameters)
        self.an_vi_di_comboBox_client.setGeometry(QtCore.QRect(10, 10, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_comboBox_client.setFont(font)
        self.an_vi_di_comboBox_client.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_di_comboBox_client.setObjectName("an_vi_di_comboBox_client")
        self.an_vi_di_comboBox_farm = QtWidgets.QComboBox(self.an_vi_di_frame_parameters)
        self.an_vi_di_comboBox_farm.setGeometry(QtCore.QRect(10, 51, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_comboBox_farm.setFont(font)
        self.an_vi_di_comboBox_farm.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_di_comboBox_farm.setObjectName("an_vi_di_comboBox_farm")
        self.an_vi_di_comboBox_field = QtWidgets.QComboBox(self.an_vi_di_frame_parameters)
        self.an_vi_di_comboBox_field.setGeometry(QtCore.QRect(10, 92, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_comboBox_field.setFont(font)
        self.an_vi_di_comboBox_field.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_di_comboBox_field.setObjectName("an_vi_di_comboBox_field")
        self.an_vi_di_pushButton_generate = QtWidgets.QPushButton(self.an_vi_di_frame_parameters)
        self.an_vi_di_pushButton_generate.setGeometry(QtCore.QRect(10, 260, 211, 51))
        self.an_vi_di_pushButton_generate.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(74, 143, 231);\n"
"font: 28pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.an_vi_di_pushButton_generate.setObjectName("an_vi_di_pushButton_generate")
        self.an_vi_di_label_cycle = QtWidgets.QLabel(self.an_vi_di_frame_parameters)
        self.an_vi_di_label_cycle.setGeometry(QtCore.QRect(10, 133, 111, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_label_cycle.setFont(font)
        self.an_vi_di_label_cycle.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_di_label_cycle.setObjectName("an_vi_di_label_cycle")
        self.an_vi_di_label_nBins = QtWidgets.QLabel(self.an_vi_di_frame_parameters)
        self.an_vi_di_label_nBins.setGeometry(QtCore.QRect(10, 215, 201, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_label_nBins.setFont(font)
        self.an_vi_di_label_nBins.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_di_label_nBins.setObjectName("an_vi_di_label_nBins")
        self.an_vi_di_comboBox_nBins = QtWidgets.QComboBox(self.an_vi_di_frame_parameters)
        self.an_vi_di_comboBox_nBins.setGeometry(QtCore.QRect(140, 215, 81, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_comboBox_nBins.setFont(font)
        self.an_vi_di_comboBox_nBins.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_di_comboBox_nBins.setObjectName("an_vi_di_comboBox_nBins")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_nBins.addItem("")
        self.an_vi_di_comboBox_cycle = QtWidgets.QComboBox(self.an_vi_di_frame_parameters)
        self.an_vi_di_comboBox_cycle.setGeometry(QtCore.QRect(80, 133, 141, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_comboBox_cycle.setFont(font)
        self.an_vi_di_comboBox_cycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_di_comboBox_cycle.setObjectName("an_vi_di_comboBox_cycle")
        self.an_vi_di_comboBox_variable = QtWidgets.QComboBox(self.an_vi_di_frame_parameters)
        self.an_vi_di_comboBox_variable.setGeometry(QtCore.QRect(10, 174, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_di_comboBox_variable.setFont(font)
        self.an_vi_di_comboBox_variable.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_di_comboBox_variable.setObjectName("an_vi_di_comboBox_variable")
        self.an_vi_di_plot = MplWidget(self.an_vi_di)
        self.an_vi_di_plot.setGeometry(QtCore.QRect(29, 69, 501, 391))
        self.an_vi_di_plot.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.an_vi_di_plot.setObjectName("an_vi_di_plot")
        self.stackedWidget.addWidget(self.an_vi_di)
        self.an_vi_sc = QtWidgets.QWidget()
        self.an_vi_sc.setObjectName("an_vi_sc")
        self.an_vi_sc_pushButton_back = QtWidgets.QPushButton(self.an_vi_sc)
        self.an_vi_sc_pushButton_back.setGeometry(QtCore.QRect(550, 400, 141, 51))
        self.an_vi_sc_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 20pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_sc_pushButton_back.setObjectName("an_vi_sc_pushButton_back")
        self.an_vi_sc_pushButton_save = QtWidgets.QPushButton(self.an_vi_sc)
        self.an_vi_sc_pushButton_save.setGeometry(QtCore.QRect(710, 400, 50, 50))
        self.an_vi_sc_pushButton_save.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(160, 181, 50);\n"
"background-image: url(:/Img/Img/pushButton_Save.png);\n"
"font: 17pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_vi_sc_pushButton_save.setText("")
        self.an_vi_sc_pushButton_save.setObjectName("an_vi_sc_pushButton_save")
        self.an_vi_sc_pushButton_home = QtWidgets.QPushButton(self.an_vi_sc)
        self.an_vi_sc_pushButton_home.setGeometry(QtCore.QRect(40, 20, 50, 50))
        self.an_vi_sc_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 13px;\n"
"background-image: url(:/Img/Img/pushButton_Home2.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_sc_pushButton_home.setText("")
        self.an_vi_sc_pushButton_home.setObjectName("an_vi_sc_pushButton_home")
        self.an_vi_sc_label_title = QtWidgets.QLabel(self.an_vi_sc)
        self.an_vi_sc_label_title.setGeometry(QtCore.QRect(310, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_label_title.setFont(font)
        self.an_vi_sc_label_title.setStyleSheet("font: 30pt \"Calibri\";")
        self.an_vi_sc_label_title.setObjectName("an_vi_sc_label_title")
        self.an_vi_sc_pushButton_help = QtWidgets.QPushButton(self.an_vi_sc)
        self.an_vi_sc_pushButton_help.setGeometry(QtCore.QRect(710, 20, 50, 50))
        self.an_vi_sc_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_vi_sc_pushButton_help.setText("")
        self.an_vi_sc_pushButton_help.setObjectName("an_vi_sc_pushButton_help")
        self.an_vi_sc_frame_parameters = QtWidgets.QFrame(self.an_vi_sc)
        self.an_vi_sc_frame_parameters.setGeometry(QtCore.QRect(540, 70, 241, 321))
        self.an_vi_sc_frame_parameters.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.an_vi_sc_frame_parameters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_vi_sc_frame_parameters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_vi_sc_frame_parameters.setObjectName("an_vi_sc_frame_parameters")
        self.an_vi_sc_comboBox_client = QtWidgets.QComboBox(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_comboBox_client.setGeometry(QtCore.QRect(10, 10, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_comboBox_client.setFont(font)
        self.an_vi_sc_comboBox_client.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_sc_comboBox_client.setObjectName("an_vi_sc_comboBox_client")
        self.an_vi_sc_comboBox_farm = QtWidgets.QComboBox(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_comboBox_farm.setGeometry(QtCore.QRect(10, 51, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_comboBox_farm.setFont(font)
        self.an_vi_sc_comboBox_farm.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_sc_comboBox_farm.setObjectName("an_vi_sc_comboBox_farm")
        self.an_vi_sc_comboBox_field = QtWidgets.QComboBox(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_comboBox_field.setGeometry(QtCore.QRect(10, 92, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_comboBox_field.setFont(font)
        self.an_vi_sc_comboBox_field.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_sc_comboBox_field.setObjectName("an_vi_sc_comboBox_field")
        self.an_vi_sc_comboBox_variableX = QtWidgets.QComboBox(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_comboBox_variableX.setGeometry(QtCore.QRect(40, 174, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_comboBox_variableX.setFont(font)
        self.an_vi_sc_comboBox_variableX.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_sc_comboBox_variableX.setObjectName("an_vi_sc_comboBox_variableX")
        self.an_vi_sc_pushButton_generate = QtWidgets.QPushButton(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_pushButton_generate.setGeometry(QtCore.QRect(10, 260, 211, 51))
        self.an_vi_sc_pushButton_generate.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(74, 143, 231);\n"
"font: 28pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.an_vi_sc_pushButton_generate.setObjectName("an_vi_sc_pushButton_generate")
        self.an_vi_sc_label_variableX = QtWidgets.QLabel(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_label_variableX.setGeometry(QtCore.QRect(10, 174, 101, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_label_variableX.setFont(font)
        self.an_vi_sc_label_variableX.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_sc_label_variableX.setObjectName("an_vi_sc_label_variableX")
        self.an_vi_sc_label_variableY = QtWidgets.QLabel(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_label_variableY.setGeometry(QtCore.QRect(10, 215, 101, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_label_variableY.setFont(font)
        self.an_vi_sc_label_variableY.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_sc_label_variableY.setObjectName("an_vi_sc_label_variableY")
        self.an_vi_sc_comboBox_variableY = QtWidgets.QComboBox(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_comboBox_variableY.setGeometry(QtCore.QRect(40, 215, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_comboBox_variableY.setFont(font)
        self.an_vi_sc_comboBox_variableY.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_sc_comboBox_variableY.setObjectName("an_vi_sc_comboBox_variableY")
        self.an_vi_sc_comboBox_cycle = QtWidgets.QComboBox(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_comboBox_cycle.setGeometry(QtCore.QRect(80, 133, 141, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_comboBox_cycle.setFont(font)
        self.an_vi_sc_comboBox_cycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_sc_comboBox_cycle.setObjectName("an_vi_sc_comboBox_cycle")
        self.an_vi_sc_label_cycle = QtWidgets.QLabel(self.an_vi_sc_frame_parameters)
        self.an_vi_sc_label_cycle.setGeometry(QtCore.QRect(10, 133, 111, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_sc_label_cycle.setFont(font)
        self.an_vi_sc_label_cycle.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_sc_label_cycle.setObjectName("an_vi_sc_label_cycle")
        self.an_vi_sc_label_cycle.raise_()
        self.an_vi_sc_label_variableX.raise_()
        self.an_vi_sc_comboBox_client.raise_()
        self.an_vi_sc_comboBox_farm.raise_()
        self.an_vi_sc_comboBox_field.raise_()
        self.an_vi_sc_comboBox_variableX.raise_()
        self.an_vi_sc_pushButton_generate.raise_()
        self.an_vi_sc_label_variableY.raise_()
        self.an_vi_sc_comboBox_variableY.raise_()
        self.an_vi_sc_comboBox_cycle.raise_()
        self.an_vi_sc_plot = MplWidget(self.an_vi_sc)
        self.an_vi_sc_plot.setGeometry(QtCore.QRect(29, 69, 501, 391))
        self.an_vi_sc_plot.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.an_vi_sc_plot.setObjectName("an_vi_sc_plot")
        self.stackedWidget.addWidget(self.an_vi_sc)
        self.an_vi_re = QtWidgets.QWidget()
        self.an_vi_re.setObjectName("an_vi_re")
        self.an_vi_re_frame_parameters = QtWidgets.QFrame(self.an_vi_re)
        self.an_vi_re_frame_parameters.setGeometry(QtCore.QRect(540, 70, 241, 321))
        self.an_vi_re_frame_parameters.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.an_vi_re_frame_parameters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.an_vi_re_frame_parameters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.an_vi_re_frame_parameters.setObjectName("an_vi_re_frame_parameters")
        self.an_vi_re_comboBox_client = QtWidgets.QComboBox(self.an_vi_re_frame_parameters)
        self.an_vi_re_comboBox_client.setGeometry(QtCore.QRect(10, 10, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_comboBox_client.setFont(font)
        self.an_vi_re_comboBox_client.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_re_comboBox_client.setObjectName("an_vi_re_comboBox_client")
        self.an_vi_re_comboBox_farm = QtWidgets.QComboBox(self.an_vi_re_frame_parameters)
        self.an_vi_re_comboBox_farm.setGeometry(QtCore.QRect(10, 51, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_comboBox_farm.setFont(font)
        self.an_vi_re_comboBox_farm.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_re_comboBox_farm.setObjectName("an_vi_re_comboBox_farm")
        self.an_vi_re_comboBox_field = QtWidgets.QComboBox(self.an_vi_re_frame_parameters)
        self.an_vi_re_comboBox_field.setGeometry(QtCore.QRect(10, 92, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_comboBox_field.setFont(font)
        self.an_vi_re_comboBox_field.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_re_comboBox_field.setObjectName("an_vi_re_comboBox_field")
        self.an_vi_re_comboBox_variableX = QtWidgets.QComboBox(self.an_vi_re_frame_parameters)
        self.an_vi_re_comboBox_variableX.setGeometry(QtCore.QRect(40, 174, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_comboBox_variableX.setFont(font)
        self.an_vi_re_comboBox_variableX.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_re_comboBox_variableX.setObjectName("an_vi_re_comboBox_variableX")
        self.an_vi_re_pushButton_generate = QtWidgets.QPushButton(self.an_vi_re_frame_parameters)
        self.an_vi_re_pushButton_generate.setGeometry(QtCore.QRect(100, 256, 121, 54))
        self.an_vi_re_pushButton_generate.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(74, 143, 231);\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.an_vi_re_pushButton_generate.setObjectName("an_vi_re_pushButton_generate")
        self.an_vi_re_label_variableX = QtWidgets.QLabel(self.an_vi_re_frame_parameters)
        self.an_vi_re_label_variableX.setGeometry(QtCore.QRect(10, 174, 101, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_label_variableX.setFont(font)
        self.an_vi_re_label_variableX.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_re_label_variableX.setObjectName("an_vi_re_label_variableX")
        self.an_vi_re_label_variableY = QtWidgets.QLabel(self.an_vi_re_frame_parameters)
        self.an_vi_re_label_variableY.setGeometry(QtCore.QRect(10, 215, 101, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_label_variableY.setFont(font)
        self.an_vi_re_label_variableY.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_re_label_variableY.setObjectName("an_vi_re_label_variableY")
        self.an_vi_re_comboBox_variableY = QtWidgets.QComboBox(self.an_vi_re_frame_parameters)
        self.an_vi_re_comboBox_variableY.setGeometry(QtCore.QRect(40, 215, 181, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_comboBox_variableY.setFont(font)
        self.an_vi_re_comboBox_variableY.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_re_comboBox_variableY.setObjectName("an_vi_re_comboBox_variableY")
        self.an_vi_re_comboBox_cycle = QtWidgets.QComboBox(self.an_vi_re_frame_parameters)
        self.an_vi_re_comboBox_cycle.setGeometry(QtCore.QRect(80, 133, 141, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_comboBox_cycle.setFont(font)
        self.an_vi_re_comboBox_cycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_re_comboBox_cycle.setObjectName("an_vi_re_comboBox_cycle")
        self.an_vi_re_label_cycle = QtWidgets.QLabel(self.an_vi_re_frame_parameters)
        self.an_vi_re_label_cycle.setGeometry(QtCore.QRect(10, 133, 111, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_label_cycle.setFont(font)
        self.an_vi_re_label_cycle.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_re_label_cycle.setObjectName("an_vi_re_label_cycle")
        self.an_vi_re_label_order = QtWidgets.QLabel(self.an_vi_re_frame_parameters)
        self.an_vi_re_label_order.setGeometry(QtCore.QRect(10, 256, 81, 54))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_label_order.setFont(font)
        self.an_vi_re_label_order.setStyleSheet("font: 18pt \"Calibri\";\n"
"background-color: rgb(217, 217, 217);\n"
"border-radius: 10px;")
        self.an_vi_re_label_order.setObjectName("an_vi_re_label_order")
        self.an_vi_re_comboBox_order = QtWidgets.QComboBox(self.an_vi_re_frame_parameters)
        self.an_vi_re_comboBox_order.setGeometry(QtCore.QRect(30, 282, 51, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_comboBox_order.setFont(font)
        self.an_vi_re_comboBox_order.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow2_on.png);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:35px;\n"
"/*height:50px;*/\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.an_vi_re_comboBox_order.setObjectName("an_vi_re_comboBox_order")
        self.an_vi_re_comboBox_order.addItem("")
        self.an_vi_re_comboBox_order.addItem("")
        self.an_vi_re_comboBox_order.addItem("")
        self.an_vi_re_comboBox_order.addItem("")
        self.an_vi_re_comboBox_order.addItem("")
        self.an_vi_re_label_cycle.raise_()
        self.an_vi_re_label_variableX.raise_()
        self.an_vi_re_comboBox_client.raise_()
        self.an_vi_re_comboBox_farm.raise_()
        self.an_vi_re_comboBox_field.raise_()
        self.an_vi_re_comboBox_variableX.raise_()
        self.an_vi_re_pushButton_generate.raise_()
        self.an_vi_re_label_variableY.raise_()
        self.an_vi_re_comboBox_variableY.raise_()
        self.an_vi_re_comboBox_cycle.raise_()
        self.an_vi_re_label_order.raise_()
        self.an_vi_re_comboBox_order.raise_()
        self.an_vi_re_pushButton_back = QtWidgets.QPushButton(self.an_vi_re)
        self.an_vi_re_pushButton_back.setGeometry(QtCore.QRect(550, 400, 141, 51))
        self.an_vi_re_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 20pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_re_pushButton_back.setObjectName("an_vi_re_pushButton_back")
        self.an_vi_re_label_title = QtWidgets.QLabel(self.an_vi_re)
        self.an_vi_re_label_title.setGeometry(QtCore.QRect(320, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.an_vi_re_label_title.setFont(font)
        self.an_vi_re_label_title.setStyleSheet("font: 30pt \"Calibri\";")
        self.an_vi_re_label_title.setObjectName("an_vi_re_label_title")
        self.an_vi_re_pushButton_help = QtWidgets.QPushButton(self.an_vi_re)
        self.an_vi_re_pushButton_help.setGeometry(QtCore.QRect(710, 20, 50, 50))
        self.an_vi_re_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.an_vi_re_pushButton_help.setText("")
        self.an_vi_re_pushButton_help.setObjectName("an_vi_re_pushButton_help")
        self.an_vi_re_pushButton_home = QtWidgets.QPushButton(self.an_vi_re)
        self.an_vi_re_pushButton_home.setGeometry(QtCore.QRect(40, 20, 50, 50))
        self.an_vi_re_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 13px;\n"
"background-image: url(:/Img/Img/pushButton_Home2.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.an_vi_re_pushButton_home.setText("")
        self.an_vi_re_pushButton_home.setObjectName("an_vi_re_pushButton_home")
        self.an_vi_re_pushButton_save = QtWidgets.QPushButton(self.an_vi_re)
        self.an_vi_re_pushButton_save.setGeometry(QtCore.QRect(710, 400, 50, 50))
        self.an_vi_re_pushButton_save.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(160, 181, 50);\n"
"background-image: url(:/Img/Img/pushButton_Save.png);\n"
"font: 17pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.an_vi_re_pushButton_save.setText("")
        self.an_vi_re_pushButton_save.setObjectName("an_vi_re_pushButton_save")
        self.an_vi_re_plot = MplWidget(self.an_vi_re)
        self.an_vi_re_plot.setGeometry(QtCore.QRect(29, 69, 501, 391))
        self.an_vi_re_plot.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.an_vi_re_plot.setObjectName("an_vi_re_plot")
        self.stackedWidget.addWidget(self.an_vi_re)
        self.su1 = QtWidgets.QWidget()
        self.su1.setObjectName("su1")
        self.su1_pushButton_home = QtWidgets.QPushButton(self.su1)
        self.su1_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.su1_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su1_pushButton_home.setText("")
        self.su1_pushButton_home.setObjectName("su1_pushButton_home")
        self.su1_frame = QtWidgets.QFrame(self.su1)
        self.su1_frame.setGeometry(QtCore.QRect(20, 140, 501, 301))
        self.su1_frame.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.su1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.su1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.su1_frame.setObjectName("su1_frame")
        self.su1_label_client = QtWidgets.QLabel(self.su1_frame)
        self.su1_label_client.setGeometry(QtCore.QRect(20, 0, 391, 60))
        self.su1_label_client.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.su1_label_client.setObjectName("su1_label_client")
        self.su1_label_farm = QtWidgets.QLabel(self.su1_frame)
        self.su1_label_farm.setGeometry(QtCore.QRect(20, 80, 391, 60))
        self.su1_label_farm.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.su1_label_farm.setObjectName("su1_label_farm")
        self.su1_label_field = QtWidgets.QLabel(self.su1_frame)
        self.su1_label_field.setGeometry(QtCore.QRect(20, 160, 391, 60))
        self.su1_label_field.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.su1_label_field.setObjectName("su1_label_field")
        self.su1_label_cycle = QtWidgets.QLabel(self.su1_frame)
        self.su1_label_cycle.setGeometry(QtCore.QRect(20, 240, 391, 60))
        self.su1_label_cycle.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.su1_label_cycle.setObjectName("su1_label_cycle")
        self.su1_comboBox_client = QtWidgets.QComboBox(self.su1_frame)
        self.su1_comboBox_client.setGeometry(QtCore.QRect(150, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.su1_comboBox_client.setFont(font)
        self.su1_comboBox_client.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.su1_comboBox_client.setObjectName("su1_comboBox_client")
        self.su1_comboBox_farm = QtWidgets.QComboBox(self.su1_frame)
        self.su1_comboBox_farm.setGeometry(QtCore.QRect(150, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.su1_comboBox_farm.setFont(font)
        self.su1_comboBox_farm.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.su1_comboBox_farm.setObjectName("su1_comboBox_farm")
        self.su1_comboBox_field = QtWidgets.QComboBox(self.su1_frame)
        self.su1_comboBox_field.setGeometry(QtCore.QRect(150, 170, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.su1_comboBox_field.setFont(font)
        self.su1_comboBox_field.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.su1_comboBox_field.setObjectName("su1_comboBox_field")
        self.su1_comboBox_cycle = QtWidgets.QComboBox(self.su1_frame)
        self.su1_comboBox_cycle.setGeometry(QtCore.QRect(150, 250, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.su1_comboBox_cycle.setFont(font)
        self.su1_comboBox_cycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.su1_comboBox_cycle.setObjectName("su1_comboBox_cycle")
        self.su1_pushButton_addClient = QtWidgets.QPushButton(self.su1_frame)
        self.su1_pushButton_addClient.setGeometry(QtCore.QRect(420, 0, 60, 60))
        self.su1_pushButton_addClient.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su1_pushButton_addClient.setText("")
        self.su1_pushButton_addClient.setObjectName("su1_pushButton_addClient")
        self.su1_pushButton_addFarm = QtWidgets.QPushButton(self.su1_frame)
        self.su1_pushButton_addFarm.setGeometry(QtCore.QRect(420, 80, 60, 60))
        self.su1_pushButton_addFarm.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su1_pushButton_addFarm.setText("")
        self.su1_pushButton_addFarm.setObjectName("su1_pushButton_addFarm")
        self.su1_pushButton_addField = QtWidgets.QPushButton(self.su1_frame)
        self.su1_pushButton_addField.setGeometry(QtCore.QRect(420, 160, 60, 60))
        self.su1_pushButton_addField.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su1_pushButton_addField.setText("")
        self.su1_pushButton_addField.setObjectName("su1_pushButton_addField")
        self.su1_pushButton_addCycle = QtWidgets.QPushButton(self.su1_frame)
        self.su1_pushButton_addCycle.setGeometry(QtCore.QRect(420, 240, 60, 60))
        self.su1_pushButton_addCycle.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su1_pushButton_addCycle.setText("")
        self.su1_pushButton_addCycle.setObjectName("su1_pushButton_addCycle")
        self.su1_label_title = QtWidgets.QLabel(self.su1)
        self.su1_label_title.setGeometry(QtCore.QRect(230, 60, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.su1_label_title.setFont(font)
        self.su1_label_title.setObjectName("su1_label_title")
        self.su1_pushButton_help = QtWidgets.QPushButton(self.su1)
        self.su1_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.su1_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.su1_pushButton_help.setText("")
        self.su1_pushButton_help.setObjectName("su1_pushButton_help")
        self.su1_pushButton_previous = QtWidgets.QPushButton(self.su1)
        self.su1_pushButton_previous.setGeometry(QtCore.QRect(550, 310, 210, 70))
        self.su1_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su1_pushButton_previous.setObjectName("su1_pushButton_previous")
        self.su1_pushButton_next = QtWidgets.QPushButton(self.su1)
        self.su1_pushButton_next.setGeometry(QtCore.QRect(550, 200, 210, 70))
        self.su1_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"font: 32pt \"Calibri\";\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.su1_pushButton_next.setObjectName("su1_pushButton_next")
        self.stackedWidget.addWidget(self.su1)
        self.su2 = QtWidgets.QWidget()
        self.su2.setObjectName("su2")
        self.su2_pushButton_home = QtWidgets.QPushButton(self.su2)
        self.su2_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.su2_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su2_pushButton_home.setText("")
        self.su2_pushButton_home.setObjectName("su2_pushButton_home")
        self.su1_frame_2 = QtWidgets.QFrame(self.su2)
        self.su1_frame_2.setGeometry(QtCore.QRect(20, 140, 501, 301))
        self.su1_frame_2.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.su1_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.su1_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.su1_frame_2.setObjectName("su1_frame_2")
        self.su2_label_variable = QtWidgets.QLabel(self.su1_frame_2)
        self.su2_label_variable.setGeometry(QtCore.QRect(20, 0, 391, 60))
        self.su2_label_variable.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.su2_label_variable.setObjectName("su2_label_variable")
        self.su2_label_instrument = QtWidgets.QLabel(self.su1_frame_2)
        self.su2_label_instrument.setGeometry(QtCore.QRect(20, 80, 391, 60))
        self.su2_label_instrument.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.su2_label_instrument.setObjectName("su2_label_instrument")
        self.su2_label_mode = QtWidgets.QLabel(self.su1_frame_2)
        self.su2_label_mode.setGeometry(QtCore.QRect(20, 160, 391, 60))
        self.su2_label_mode.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.su2_label_mode.setObjectName("su2_label_mode")
        self.su2_label_interval = QtWidgets.QLabel(self.su1_frame_2)
        self.su2_label_interval.setGeometry(QtCore.QRect(20, 240, 391, 60))
        self.su2_label_interval.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.su2_label_interval.setObjectName("su2_label_interval")
        self.su2_comboBox_variable = QtWidgets.QComboBox(self.su1_frame_2)
        self.su2_comboBox_variable.setGeometry(QtCore.QRect(170, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.su2_comboBox_variable.setFont(font)
        self.su2_comboBox_variable.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.su2_comboBox_variable.setObjectName("su2_comboBox_variable")
        self.su2_comboBox_instrument = QtWidgets.QComboBox(self.su1_frame_2)
        self.su2_comboBox_instrument.setGeometry(QtCore.QRect(220, 90, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.su2_comboBox_instrument.setFont(font)
        self.su2_comboBox_instrument.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.su2_comboBox_instrument.setObjectName("su2_comboBox_instrument")
        self.su2_comboBox_instrument.addItem("")
        self.su2_comboBox_instrument.addItem("")
        self.su2_comboBox_instrument.addItem("")
        self.su2_comboBox_mode = QtWidgets.QComboBox(self.su1_frame_2)
        self.su2_comboBox_mode.setGeometry(QtCore.QRect(220, 170, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.su2_comboBox_mode.setFont(font)
        self.su2_comboBox_mode.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.su2_comboBox_mode.setObjectName("su2_comboBox_mode")
        self.su2_comboBox_mode.addItem("")
        self.su2_comboBox_mode.addItem("")
        self.su2_textEdit_interval = QtWidgets.QTextEdit(self.su1_frame_2)
        self.su2_textEdit_interval.setEnabled(True)
        self.su2_textEdit_interval.setGeometry(QtCore.QRect(220, 247, 171, 47))
        self.su2_textEdit_interval.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(236, 239, 240);")
        self.su2_textEdit_interval.setObjectName("su2_textEdit_interval")
        self.su2_pushButton_addVariable = QtWidgets.QPushButton(self.su1_frame_2)
        self.su2_pushButton_addVariable.setGeometry(QtCore.QRect(420, 0, 60, 60))
        self.su2_pushButton_addVariable.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su2_pushButton_addVariable.setText("")
        self.su2_pushButton_addVariable.setObjectName("su2_pushButton_addVariable")
        self.su2_pushButton_addInstrument = QtWidgets.QPushButton(self.su1_frame_2)
        self.su2_pushButton_addInstrument.setGeometry(QtCore.QRect(420, 80, 60, 60))
        self.su2_pushButton_addInstrument.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su2_pushButton_addInstrument.setText("")
        self.su2_pushButton_addInstrument.setObjectName("su2_pushButton_addInstrument")
        self.su2_label_title = QtWidgets.QLabel(self.su2)
        self.su2_label_title.setGeometry(QtCore.QRect(230, 60, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.su2_label_title.setFont(font)
        self.su2_label_title.setObjectName("su2_label_title")
        self.su2_pushButton_help = QtWidgets.QPushButton(self.su2)
        self.su2_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.su2_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.su2_pushButton_help.setText("")
        self.su2_pushButton_help.setObjectName("su2_pushButton_help")
        self.su2_pushButton_previous = QtWidgets.QPushButton(self.su2)
        self.su2_pushButton_previous.setGeometry(QtCore.QRect(550, 310, 210, 70))
        self.su2_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su2_pushButton_previous.setObjectName("su2_pushButton_previous")
        self.su2_pushButton_next = QtWidgets.QPushButton(self.su2)
        self.su2_pushButton_next.setGeometry(QtCore.QRect(550, 200, 210, 70))
        self.su2_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"font: 32pt \"Calibri\";\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.su2_pushButton_next.setObjectName("su2_pushButton_next")
        self.stackedWidget.addWidget(self.su2)
        self.su3 = QtWidgets.QWidget()
        self.su3.setObjectName("su3")
        self.su3_label_title = QtWidgets.QLabel(self.su3)
        self.su3_label_title.setGeometry(QtCore.QRect(230, 60, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.su3_label_title.setFont(font)
        self.su3_label_title.setObjectName("su3_label_title")
        self.su3_checkBox_eraseUSB = QtWidgets.QCheckBox(self.su3)
        self.su3_checkBox_eraseUSB.setGeometry(QtCore.QRect(40, 300, 311, 61))
        self.su3_checkBox_eraseUSB.setStyleSheet("QCheckBox\n"
"{\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QCheckBox::indicator::checked\n"
"{\n"
"image: url(:/Img/Img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"image: url(:/Img/Img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed\n"
"{\n"
"image: url(:/Img/Img/checkbox_checked_pressed.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed\n"
"{\n"
"image: url(:/Img/Img/checkbox_unchecked_pressed.png);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.su3_checkBox_eraseUSB.setIconSize(QtCore.QSize(16, 16))
        self.su3_checkBox_eraseUSB.setChecked(False)
        self.su3_checkBox_eraseUSB.setTristate(False)
        self.su3_checkBox_eraseUSB.setObjectName("su3_checkBox_eraseUSB")
        self.su3_pushButton_back = QtWidgets.QPushButton(self.su3)
        self.su3_pushButton_back.setGeometry(QtCore.QRect(40, 390, 301, 51))
        self.su3_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su3_pushButton_back.setObjectName("su3_pushButton_back")
        self.su3_pushButton_help = QtWidgets.QPushButton(self.su3)
        self.su3_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.su3_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.su3_pushButton_help.setText("")
        self.su3_pushButton_help.setObjectName("su3_pushButton_help")
        self.su3_pushButton_home = QtWidgets.QPushButton(self.su3)
        self.su3_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.su3_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.su3_pushButton_home.setText("")
        self.su3_pushButton_home.setObjectName("su3_pushButton_home")
        self.su3_pushButton_goToCapture = QtWidgets.QPushButton(self.su3)
        self.su3_pushButton_goToCapture.setGeometry(QtCore.QRect(400, 300, 360, 140))
        self.su3_pushButton_goToCapture.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(74, 143, 231);\n"
"background-image: url(:/Img/Img/pushButton_GoToCapture.png);\n"
"color: rgb(236, 239, 240);\n"
"font: 38pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.su3_pushButton_goToCapture.setText("")
        self.su3_pushButton_goToCapture.setObjectName("su3_pushButton_goToCapture")
        self.su3_frame_fileLocation = QtWidgets.QFrame(self.su3)
        self.su3_frame_fileLocation.setGeometry(QtCore.QRect(40, 150, 720, 121))
        self.su3_frame_fileLocation.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px")
        self.su3_frame_fileLocation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.su3_frame_fileLocation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.su3_frame_fileLocation.setObjectName("su3_frame_fileLocation")
        self.su3_textEdit_fileLocation = QtWidgets.QTextEdit(self.su3_frame_fileLocation)
        self.su3_textEdit_fileLocation.setGeometry(QtCore.QRect(10, 55, 701, 51))
        self.su3_textEdit_fileLocation.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(236, 239, 240);\n"
"font: 24pt \"Calibri\";")
        self.su3_textEdit_fileLocation.setObjectName("su3_textEdit_fileLocation")
        self.su3_label_fileLocation = QtWidgets.QLabel(self.su3_frame_fileLocation)
        self.su3_label_fileLocation.setGeometry(QtCore.QRect(10, 15, 341, 31))
        self.su3_label_fileLocation.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 28pt \"Calibri\";\n"
"color: rgb(0, 0, 0);")
        self.su3_label_fileLocation.setObjectName("su3_label_fileLocation")
        self.stackedWidget.addWidget(self.su3)
        self.suC = QtWidgets.QWidget()
        self.suC.setObjectName("suC")
        self.suC_frame_map = QtWidgets.QFrame(self.suC)
        self.suC_frame_map.setGeometry(QtCore.QRect(20, 60, 551, 321))
        self.suC_frame_map.setStyleSheet("background-color: rgb(160, 181, 50);\n"
"border: 10px rgb(64, 64, 64);\n"
"border-radius:20px;")
        self.suC_frame_map.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suC_frame_map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suC_frame_map.setObjectName("suC_frame_map")
        self.suC_label_cursor = QtWidgets.QLabel(self.suC_frame_map)
        self.suC_label_cursor.setGeometry(QtCore.QRect(260, 260, 34, 44))
        self.suC_label_cursor.setStyleSheet("background-image: url(:/Img/Img/cursorGPS.png);\n"
"border-radius:0px;")
        self.suC_label_cursor.setText("")
        self.suC_label_cursor.setObjectName("suC_label_cursor")
        self.suC_frame_zoom = QtWidgets.QFrame(self.suC_frame_map)
        self.suC_frame_zoom.setGeometry(QtCore.QRect(480, 120, 48, 91))
        self.suC_frame_zoom.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius:20px;")
        self.suC_frame_zoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suC_frame_zoom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suC_frame_zoom.setObjectName("suC_frame_zoom")
        self.suC_pushButton_zoomIn = QtWidgets.QPushButton(self.suC_frame_zoom)
        self.suC_pushButton_zoomIn.setGeometry(QtCore.QRect(7, 10, 33, 32))
        self.suC_pushButton_zoomIn.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(64, 64, 64);\n"
"    background-image: url(:/Img/Img/ZoomIn.png);\n"
"font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(126, 126, 126);\n"
"}")
        self.suC_pushButton_zoomIn.setText("")
        self.suC_pushButton_zoomIn.setObjectName("suC_pushButton_zoomIn")
        self.suC_pushButton_zoomOut = QtWidgets.QPushButton(self.suC_frame_zoom)
        self.suC_pushButton_zoomOut.setGeometry(QtCore.QRect(7, 50, 33, 32))
        self.suC_pushButton_zoomOut.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(64, 64, 64);\n"
"    background-image: url(:/Img/Img/ZoomOut.png);\n"
"font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(126, 126, 126);\n"
"}")
        self.suC_pushButton_zoomOut.setText("")
        self.suC_pushButton_zoomOut.setObjectName("suC_pushButton_zoomOut")
        self.suC_label_compass = QtWidgets.QLabel(self.suC_frame_map)
        self.suC_label_compass.setGeometry(QtCore.QRect(480, 20, 48, 48))
        self.suC_label_compass.setStyleSheet("background-image: url(:/Img/Img/compassGPS.png);\n"
"border-radius:0px;")
        self.suC_label_compass.setText("")
        self.suC_label_compass.setObjectName("suC_label_compass")
        self.suC_pushButton_back = QtWidgets.QPushButton(self.suC)
        self.suC_pushButton_back.setGeometry(QtCore.QRect(19, 400, 201, 50))
        self.suC_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.suC_pushButton_back.setObjectName("suC_pushButton_back")
        self.suC_checkbox_toggleStart = QtWidgets.QCheckBox(self.suC)
        self.suC_checkbox_toggleStart.setGeometry(QtCore.QRect(290, 400, 230, 50))
        self.suC_checkbox_toggleStart.setStyleSheet("QCheckBox\n"
"{\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QCheckBox:indicator\n"
"{\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator::checked\n"
"{\n"
"image: url(:/Img/Img/toggle_endCapture.png);\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked\n"
"{\n"
"image: url(:/Img/Img/toggle_startCapture.png);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed\n"
"{\n"
"image: url(:/Img/Img/toggle_endCapture_pressed.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed\n"
"{\n"
"image: url(:/Img/Img/toggle_startCapture_pressed.png);\n"
"}\n"
"\n"
"")
        self.suC_checkbox_toggleStart.setObjectName("suC_checkbox_toggleStart")
        self.suC_frame_sampleInfo = QtWidgets.QFrame(self.suC)
        self.suC_frame_sampleInfo.setGeometry(QtCore.QRect(590, 140, 191, 241))
        self.suC_frame_sampleInfo.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.suC_frame_sampleInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suC_frame_sampleInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suC_frame_sampleInfo.setObjectName("suC_frame_sampleInfo")
        self.suC_label_sampleValueLabel = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_sampleValueLabel.setGeometry(QtCore.QRect(35, 10, 131, 41))
        self.suC_label_sampleValueLabel.setStyleSheet("font: 16pt \"Calibri\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(236, 239, 240);")
        self.suC_label_sampleValueLabel.setObjectName("suC_label_sampleValueLabel")
        self.suC_label_sampleNoLabel = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_sampleNoLabel.setGeometry(QtCore.QRect(50, 100, 91, 20))
        self.suC_label_sampleNoLabel.setStyleSheet("font: 16pt \"Calibri\";")
        self.suC_label_sampleNoLabel.setObjectName("suC_label_sampleNoLabel")
        self.suC_label_latLabel = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_latLabel.setGeometry(QtCore.QRect(20, 190, 41, 41))
        self.suC_label_latLabel.setStyleSheet("font: 16pt \"Calibri\";\n"
"")
        self.suC_label_latLabel.setObjectName("suC_label_latLabel")
        self.suC_label_lonLabel = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_lonLabel.setGeometry(QtCore.QRect(20, 160, 51, 41))
        self.suC_label_lonLabel.setStyleSheet("font: 16pt \"Calibri\";")
        self.suC_label_lonLabel.setObjectName("suC_label_lonLabel")
        self.suC_label_sampleValueIndicator = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_sampleValueIndicator.setGeometry(QtCore.QRect(25, 42, 141, 41))
        self.suC_label_sampleValueIndicator.setStyleSheet("font: 32pt \"Calibri\";\n"
"color: rgb(232, 68, 68);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.suC_label_sampleValueIndicator.setObjectName("suC_label_sampleValueIndicator")
        self.suC_label_sampleNoIndicator = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_sampleNoIndicator.setGeometry(QtCore.QRect(90, 115, 31, 41))
        self.suC_label_sampleNoIndicator.setStyleSheet("font: 20pt \"Calibri\";\n"
"")
        self.suC_label_sampleNoIndicator.setObjectName("suC_label_sampleNoIndicator")
        self.suC_label_lonIndicator = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_lonIndicator.setGeometry(QtCore.QRect(60, 160, 121, 41))
        self.suC_label_lonIndicator.setStyleSheet("font: 16pt \"Calibri\";")
        self.suC_label_lonIndicator.setObjectName("suC_label_lonIndicator")
        self.suC_label_latIndicator = QtWidgets.QLabel(self.suC_frame_sampleInfo)
        self.suC_label_latIndicator.setGeometry(QtCore.QRect(60, 190, 121, 41))
        self.suC_label_latIndicator.setStyleSheet("font: 16pt \"Calibri\";")
        self.suC_label_latIndicator.setObjectName("suC_label_latIndicator")
        self.suC_frame_sample = QtWidgets.QFrame(self.suC_frame_sampleInfo)
        self.suC_frame_sample.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.suC_frame_sample.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"")
        self.suC_frame_sample.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suC_frame_sample.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suC_frame_sample.setObjectName("suC_frame_sample")
        self.suC_frame_sample.raise_()
        self.suC_label_sampleNoIndicator.raise_()
        self.suC_label_sampleValueLabel.raise_()
        self.suC_label_sampleNoLabel.raise_()
        self.suC_label_latLabel.raise_()
        self.suC_label_lonLabel.raise_()
        self.suC_label_sampleValueIndicator.raise_()
        self.suC_label_lonIndicator.raise_()
        self.suC_label_latIndicator.raise_()
        self.suC_pushButton_next = QtWidgets.QPushButton(self.suC)
        self.suC_pushButton_next.setGeometry(QtCore.QRect(589, 400, 191, 50))
        self.suC_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.suC_pushButton_next.setObjectName("suC_pushButton_next")
        self.suC_pushButton_help = QtWidgets.QPushButton(self.suC)
        self.suC_pushButton_help.setGeometry(QtCore.QRect(735, 15, 50, 50))
        self.suC_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.suC_pushButton_help.setText("")
        self.suC_pushButton_help.setObjectName("suC_pushButton_help")
        self.suC_pushButton_lockRef = QtWidgets.QPushButton(self.suC)
        self.suC_pushButton_lockRef.setGeometry(QtCore.QRect(590, 20, 141, 41))
        self.suC_pushButton_lockRef.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(64, 64, 64);\n"
"font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(126, 126, 126);\n"
"}")
        self.suC_pushButton_lockRef.setObjectName("suC_pushButton_lockRef")
        self.suC_frame_gpsInfo = QtWidgets.QFrame(self.suC)
        self.suC_frame_gpsInfo.setGeometry(QtCore.QRect(590, 70, 191, 60))
        self.suC_frame_gpsInfo.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.suC_frame_gpsInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suC_frame_gpsInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suC_frame_gpsInfo.setObjectName("suC_frame_gpsInfo")
        self.suC_label_satNoIcon = QtWidgets.QLabel(self.suC_frame_gpsInfo)
        self.suC_label_satNoIcon.setGeometry(QtCore.QRect(25, 15, 31, 30))
        self.suC_label_satNoIcon.setStyleSheet("image: url(:/Img/Img/GPSsatellite.png);\n"
"border-radius:0px;")
        self.suC_label_satNoIcon.setText("")
        self.suC_label_satNoIcon.setObjectName("suC_label_satNoIcon")
        self.suC_label_satNoIndicator = QtWidgets.QLabel(self.suC_frame_gpsInfo)
        self.suC_label_satNoIndicator.setGeometry(QtCore.QRect(60, 7, 31, 41))
        self.suC_label_satNoIndicator.setStyleSheet("font: 40pt \"Calibri\";\n"
"")
        self.suC_label_satNoIndicator.setObjectName("suC_label_satNoIndicator")
        self.suC_label_rtkLabel = QtWidgets.QLabel(self.suC_frame_gpsInfo)
        self.suC_label_rtkLabel.setGeometry(QtCore.QRect(100, 10, 71, 20))
        self.suC_label_rtkLabel.setStyleSheet("font: 16pt \"Calibri\";")
        self.suC_label_rtkLabel.setObjectName("suC_label_rtkLabel")
        self.suC_label_rtkIndicator = QtWidgets.QLabel(self.suC_frame_gpsInfo)
        self.suC_label_rtkIndicator.setGeometry(QtCore.QRect(100, 30, 71, 20))
        self.suC_label_rtkIndicator.setStyleSheet("font: 16pt \"Calibri\";")
        self.suC_label_rtkIndicator.setObjectName("suC_label_rtkIndicator")
        self.suC_label_fieldData = QtWidgets.QLabel(self.suC)
        self.suC_label_fieldData.setGeometry(QtCore.QRect(20, 20, 551, 31))
        self.suC_label_fieldData.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";")
        self.suC_label_fieldData.setObjectName("suC_label_fieldData")
        self.stackedWidget.addWidget(self.suC)
        self.suP = QtWidgets.QWidget()
        self.suP.setObjectName("suP")
        self.suP_frame_sampleInfo = QtWidgets.QFrame(self.suP)
        self.suP_frame_sampleInfo.setGeometry(QtCore.QRect(590, 140, 191, 241))
        self.suP_frame_sampleInfo.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.suP_frame_sampleInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suP_frame_sampleInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suP_frame_sampleInfo.setObjectName("suP_frame_sampleInfo")
        self.suP_label_sampleValueLabel = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_sampleValueLabel.setGeometry(QtCore.QRect(35, 10, 131, 41))
        self.suP_label_sampleValueLabel.setStyleSheet("font: 16pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"background-color: rgba(232, 68, 68,0);")
        self.suP_label_sampleValueLabel.setObjectName("suP_label_sampleValueLabel")
        self.suP_label_sampleNoLabel = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_sampleNoLabel.setGeometry(QtCore.QRect(50, 100, 91, 20))
        self.suP_label_sampleNoLabel.setStyleSheet("font: 16pt \"Calibri\";")
        self.suP_label_sampleNoLabel.setObjectName("suP_label_sampleNoLabel")
        self.suP_label_latLabel = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_latLabel.setGeometry(QtCore.QRect(20, 190, 41, 41))
        self.suP_label_latLabel.setStyleSheet("font: 16pt \"Calibri\";\n"
"")
        self.suP_label_latLabel.setObjectName("suP_label_latLabel")
        self.suP_label_lonLabel = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_lonLabel.setGeometry(QtCore.QRect(20, 160, 51, 41))
        self.suP_label_lonLabel.setStyleSheet("font: 16pt \"Calibri\";")
        self.suP_label_lonLabel.setObjectName("suP_label_lonLabel")
        self.suP_label_sampleValueIndicator = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_sampleValueIndicator.setGeometry(QtCore.QRect(25, 42, 141, 41))
        self.suP_label_sampleValueIndicator.setStyleSheet("font: 32pt \"Calibri\";\n"
"color: rgb(232, 68, 68);\n"
"background-color: rgba(232, 68, 68,0);")
        self.suP_label_sampleValueIndicator.setObjectName("suP_label_sampleValueIndicator")
        self.suP_label_sampleNoIndicator = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_sampleNoIndicator.setGeometry(QtCore.QRect(90, 125, 31, 20))
        self.suP_label_sampleNoIndicator.setStyleSheet("font: 20pt \"Calibri\";\n"
"")
        self.suP_label_sampleNoIndicator.setObjectName("suP_label_sampleNoIndicator")
        self.suP_label_lonIndicator = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_lonIndicator.setGeometry(QtCore.QRect(60, 160, 121, 41))
        self.suP_label_lonIndicator.setStyleSheet("font: 16pt \"Calibri\";")
        self.suP_label_lonIndicator.setObjectName("suP_label_lonIndicator")
        self.suP_label_latIndicator = QtWidgets.QLabel(self.suP_frame_sampleInfo)
        self.suP_label_latIndicator.setGeometry(QtCore.QRect(60, 190, 121, 41))
        self.suP_label_latIndicator.setStyleSheet("font: 16pt \"Calibri\";")
        self.suP_label_latIndicator.setObjectName("suP_label_latIndicator")
        self.suP_frame_sample = QtWidgets.QFrame(self.suP_frame_sampleInfo)
        self.suP_frame_sample.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.suP_frame_sample.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"")
        self.suP_frame_sample.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suP_frame_sample.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suP_frame_sample.setObjectName("suP_frame_sample")
        self.suP_frame_sample.raise_()
        self.suP_label_sampleValueLabel.raise_()
        self.suP_label_sampleNoLabel.raise_()
        self.suP_label_latLabel.raise_()
        self.suP_label_lonLabel.raise_()
        self.suP_label_sampleValueIndicator.raise_()
        self.suP_label_sampleNoIndicator.raise_()
        self.suP_label_lonIndicator.raise_()
        self.suP_label_latIndicator.raise_()
        self.suP_pushButton_next = QtWidgets.QPushButton(self.suP)
        self.suP_pushButton_next.setGeometry(QtCore.QRect(589, 400, 191, 50))
        self.suP_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"font: 24pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.suP_pushButton_next.setObjectName("suP_pushButton_next")
        self.suP_frame_map = QtWidgets.QFrame(self.suP)
        self.suP_frame_map.setGeometry(QtCore.QRect(20, 60, 551, 321))
        self.suP_frame_map.setStyleSheet("background-color: rgb(160, 181, 50);\n"
"border: 10px rgb(64, 64, 64);\n"
"border-radius:20px;")
        self.suP_frame_map.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suP_frame_map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suP_frame_map.setObjectName("suP_frame_map")
        self.suP_label_cursor = QtWidgets.QLabel(self.suP_frame_map)
        self.suP_label_cursor.setGeometry(QtCore.QRect(260, 260, 34, 44))
        self.suP_label_cursor.setStyleSheet("background-image: url(:/Img/Img/cursorGPS.png);\n"
"border-radius:0px;")
        self.suP_label_cursor.setText("")
        self.suP_label_cursor.setObjectName("suP_label_cursor")
        self.suP_frame_zoom = QtWidgets.QFrame(self.suP_frame_map)
        self.suP_frame_zoom.setGeometry(QtCore.QRect(480, 120, 48, 91))
        self.suP_frame_zoom.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius:20px;")
        self.suP_frame_zoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suP_frame_zoom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suP_frame_zoom.setObjectName("suP_frame_zoom")
        self.suP_pushButton_zoomIn = QtWidgets.QPushButton(self.suP_frame_zoom)
        self.suP_pushButton_zoomIn.setGeometry(QtCore.QRect(7, 10, 33, 32))
        self.suP_pushButton_zoomIn.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(64, 64, 64);\n"
"    background-image: url(:/Img/Img/ZoomIn.png);\n"
"font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(126, 126, 126);\n"
"}")
        self.suP_pushButton_zoomIn.setText("")
        self.suP_pushButton_zoomIn.setObjectName("suP_pushButton_zoomIn")
        self.suP_pushButton_zoomOut = QtWidgets.QPushButton(self.suP_frame_zoom)
        self.suP_pushButton_zoomOut.setGeometry(QtCore.QRect(7, 50, 33, 32))
        self.suP_pushButton_zoomOut.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(64, 64, 64);\n"
"    background-image: url(:/Img/Img/ZoomOut.png);\n"
"font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(126, 126, 126);\n"
"}")
        self.suP_pushButton_zoomOut.setText("")
        self.suP_pushButton_zoomOut.setObjectName("suP_pushButton_zoomOut")
        self.suP_label_compass = QtWidgets.QLabel(self.suP_frame_map)
        self.suP_label_compass.setGeometry(QtCore.QRect(480, 20, 48, 48))
        self.suP_label_compass.setStyleSheet("background-image: url(:/Img/Img/compassGPS.png);\n"
"border-radius:0px;")
        self.suP_label_compass.setText("")
        self.suP_label_compass.setObjectName("suP_label_compass")
        self.suP_label_fieldData = QtWidgets.QLabel(self.suP)
        self.suP_label_fieldData.setGeometry(QtCore.QRect(20, 20, 551, 31))
        self.suP_label_fieldData.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 18pt \"Calibri\";")
        self.suP_label_fieldData.setObjectName("suP_label_fieldData")
        self.suP_pushButton_back = QtWidgets.QPushButton(self.suP)
        self.suP_pushButton_back.setGeometry(QtCore.QRect(19, 400, 201, 50))
        self.suP_pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.suP_pushButton_back.setObjectName("suP_pushButton_back")
        self.suP_pushButton_lockRef = QtWidgets.QPushButton(self.suP)
        self.suP_pushButton_lockRef.setGeometry(QtCore.QRect(590, 20, 141, 41))
        self.suP_pushButton_lockRef.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(64, 64, 64);\n"
"font: 18pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(126, 126, 126);\n"
"}")
        self.suP_pushButton_lockRef.setObjectName("suP_pushButton_lockRef")
        self.suP_pushButton_help = QtWidgets.QPushButton(self.suP)
        self.suP_pushButton_help.setGeometry(QtCore.QRect(735, 15, 50, 50))
        self.suP_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.suP_pushButton_help.setText("")
        self.suP_pushButton_help.setObjectName("suP_pushButton_help")
        self.suP_frame_gpsInfo = QtWidgets.QFrame(self.suP)
        self.suP_frame_gpsInfo.setGeometry(QtCore.QRect(590, 70, 191, 60))
        self.suP_frame_gpsInfo.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.suP_frame_gpsInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.suP_frame_gpsInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.suP_frame_gpsInfo.setObjectName("suP_frame_gpsInfo")
        self.suP_label_satNoIcon = QtWidgets.QLabel(self.suP_frame_gpsInfo)
        self.suP_label_satNoIcon.setGeometry(QtCore.QRect(25, 15, 31, 30))
        self.suP_label_satNoIcon.setStyleSheet("image: url(:/Img/Img/GPSsatellite.png);\n"
"border-radius:0px;")
        self.suP_label_satNoIcon.setText("")
        self.suP_label_satNoIcon.setObjectName("suP_label_satNoIcon")
        self.suP_label_satNoIndicator = QtWidgets.QLabel(self.suP_frame_gpsInfo)
        self.suP_label_satNoIndicator.setGeometry(QtCore.QRect(60, 7, 31, 41))
        self.suP_label_satNoIndicator.setStyleSheet("font: 40pt \"Calibri\";\n"
"")
        self.suP_label_satNoIndicator.setObjectName("suP_label_satNoIndicator")
        self.suP_label_rtkLabel = QtWidgets.QLabel(self.suP_frame_gpsInfo)
        self.suP_label_rtkLabel.setGeometry(QtCore.QRect(100, 10, 71, 20))
        self.suP_label_rtkLabel.setStyleSheet("font: 16pt \"Calibri\";")
        self.suP_label_rtkLabel.setObjectName("suP_label_rtkLabel")
        self.suP_label_rtkIndicator = QtWidgets.QLabel(self.suP_frame_gpsInfo)
        self.suP_label_rtkIndicator.setGeometry(QtCore.QRect(100, 30, 71, 20))
        self.suP_label_rtkIndicator.setStyleSheet("font: 16pt \"Calibri\";")
        self.suP_label_rtkIndicator.setObjectName("suP_label_rtkIndicator")
        self.suP_pushButton_sample = QtWidgets.QPushButton(self.suP)
        self.suP_pushButton_sample.setGeometry(QtCore.QRect(270, 400, 271, 50))
        self.suP_pushButton_sample.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(74, 143, 231);\n"
"font: 28pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"\n"
"")
        self.suP_pushButton_sample.setObjectName("suP_pushButton_sample")
        self.stackedWidget.addWidget(self.suP)
        self.aq_menu = QtWidgets.QWidget()
        self.aq_menu.setObjectName("aq_menu")
        self.aq_menu_pushButton_field = QtWidgets.QPushButton(self.aq_menu)
        self.aq_menu_pushButton_field.setGeometry(QtCore.QRect(40, 140, 224, 297))
        self.aq_menu_pushButton_field.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/Img/Img/AqField.png);\n"
"font: 24pt \"Calibri\";\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_menu_pushButton_field.setText("")
        self.aq_menu_pushButton_field.setObjectName("aq_menu_pushButton_field")
        self.aq_menu_pushButton_help = QtWidgets.QPushButton(self.aq_menu)
        self.aq_menu_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.aq_menu_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.aq_menu_pushButton_help.setText("")
        self.aq_menu_pushButton_help.setObjectName("aq_menu_pushButton_help")
        self.aq_menu_pushButton_home = QtWidgets.QPushButton(self.aq_menu)
        self.aq_menu_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.aq_menu_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_menu_pushButton_home.setText("")
        self.aq_menu_pushButton_home.setObjectName("aq_menu_pushButton_home")
        self.aq_menu_label_title = QtWidgets.QLabel(self.aq_menu)
        self.aq_menu_label_title.setGeometry(QtCore.QRect(190, 50, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.aq_menu_label_title.setFont(font)
        self.aq_menu_label_title.setObjectName("aq_menu_label_title")
        self.aq_menu_pushButton_interpolated = QtWidgets.QPushButton(self.aq_menu)
        self.aq_menu_pushButton_interpolated.setGeometry(QtCore.QRect(540, 140, 224, 297))
        self.aq_menu_pushButton_interpolated.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"background-image: url(:/Img/Img/AqInterpolated.png);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_menu_pushButton_interpolated.setText("")
        self.aq_menu_pushButton_interpolated.setObjectName("aq_menu_pushButton_interpolated")
        self.aq_menu_pushButton_scattered = QtWidgets.QPushButton(self.aq_menu)
        self.aq_menu_pushButton_scattered.setGeometry(QtCore.QRect(290, 140, 224, 297))
        self.aq_menu_pushButton_scattered.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"background-image: url(:/Img/Img/AqScatter.png);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_menu_pushButton_scattered.setText("")
        self.aq_menu_pushButton_scattered.setObjectName("aq_menu_pushButton_scattered")
        self.stackedWidget.addWidget(self.aq_menu)
        self.aq_sc1 = QtWidgets.QWidget()
        self.aq_sc1.setObjectName("aq_sc1")
        self.aq_sc1_pushButton_next = QtWidgets.QPushButton(self.aq_sc1)
        self.aq_sc1_pushButton_next.setGeometry(QtCore.QRect(550, 200, 210, 70))
        self.aq_sc1_pushButton_next.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"font: 32pt \"Calibri\";\n"
"background-color: rgb(160, 181, 50);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(172, 196, 54);\n"
"}")
        self.aq_sc1_pushButton_next.setObjectName("aq_sc1_pushButton_next")
        self.aq_sc1_pushButton_home = QtWidgets.QPushButton(self.aq_sc1)
        self.aq_sc1_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.aq_sc1_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc1_pushButton_home.setText("")
        self.aq_sc1_pushButton_home.setObjectName("aq_sc1_pushButton_home")
        self.aq_sc1_label_title_2 = QtWidgets.QLabel(self.aq_sc1)
        self.aq_sc1_label_title_2.setGeometry(QtCore.QRect(230, 60, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.aq_sc1_label_title_2.setFont(font)
        self.aq_sc1_label_title_2.setObjectName("aq_sc1_label_title_2")
        self.aq_sc1_pushButton_previous = QtWidgets.QPushButton(self.aq_sc1)
        self.aq_sc1_pushButton_previous.setGeometry(QtCore.QRect(550, 310, 210, 70))
        self.aq_sc1_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc1_pushButton_previous.setObjectName("aq_sc1_pushButton_previous")
        self.aq_sc1_pushButton_help = QtWidgets.QPushButton(self.aq_sc1)
        self.aq_sc1_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.aq_sc1_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.aq_sc1_pushButton_help.setText("")
        self.aq_sc1_pushButton_help.setObjectName("aq_sc1_pushButton_help")
        self.aq_sc1_frame = QtWidgets.QFrame(self.aq_sc1)
        self.aq_sc1_frame.setGeometry(QtCore.QRect(20, 140, 501, 301))
        self.aq_sc1_frame.setStyleSheet("background-color: rgb(236, 239, 240);\n"
"border-radius: 10px;")
        self.aq_sc1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aq_sc1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aq_sc1_frame.setObjectName("aq_sc1_frame")
        self.aq_sc1_label_client = QtWidgets.QLabel(self.aq_sc1_frame)
        self.aq_sc1_label_client.setGeometry(QtCore.QRect(20, 0, 391, 60))
        self.aq_sc1_label_client.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.aq_sc1_label_client.setObjectName("aq_sc1_label_client")
        self.aq_sc1_label_farm = QtWidgets.QLabel(self.aq_sc1_frame)
        self.aq_sc1_label_farm.setGeometry(QtCore.QRect(20, 80, 391, 60))
        self.aq_sc1_label_farm.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.aq_sc1_label_farm.setObjectName("aq_sc1_label_farm")
        self.aq_sc1_label_field = QtWidgets.QLabel(self.aq_sc1_frame)
        self.aq_sc1_label_field.setGeometry(QtCore.QRect(20, 160, 391, 60))
        self.aq_sc1_label_field.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"")
        self.aq_sc1_label_field.setObjectName("aq_sc1_label_field")
        self.aq_sc1_label_cycle = QtWidgets.QLabel(self.aq_sc1_frame)
        self.aq_sc1_label_cycle.setGeometry(QtCore.QRect(20, 240, 391, 60))
        self.aq_sc1_label_cycle.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";")
        self.aq_sc1_label_cycle.setObjectName("aq_sc1_label_cycle")
        self.aq_sc1_comboBox_client = QtWidgets.QComboBox(self.aq_sc1_frame)
        self.aq_sc1_comboBox_client.setGeometry(QtCore.QRect(150, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.aq_sc1_comboBox_client.setFont(font)
        self.aq_sc1_comboBox_client.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.aq_sc1_comboBox_client.setObjectName("aq_sc1_comboBox_client")
        self.aq_sc1_comboBox_farm = QtWidgets.QComboBox(self.aq_sc1_frame)
        self.aq_sc1_comboBox_farm.setGeometry(QtCore.QRect(150, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.aq_sc1_comboBox_farm.setFont(font)
        self.aq_sc1_comboBox_farm.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.aq_sc1_comboBox_farm.setObjectName("aq_sc1_comboBox_farm")
        self.aq_sc1_comboBox_field = QtWidgets.QComboBox(self.aq_sc1_frame)
        self.aq_sc1_comboBox_field.setGeometry(QtCore.QRect(150, 170, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.aq_sc1_comboBox_field.setFont(font)
        self.aq_sc1_comboBox_field.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.aq_sc1_comboBox_field.setObjectName("aq_sc1_comboBox_field")
        self.aq_sc1_comboBox_cycle = QtWidgets.QComboBox(self.aq_sc1_frame)
        self.aq_sc1_comboBox_cycle.setGeometry(QtCore.QRect(150, 250, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.aq_sc1_comboBox_cycle.setFont(font)
        self.aq_sc1_comboBox_cycle.setStyleSheet("QComboBox\n"
"{\n"
"background-color: rgb(217, 217, 217);\n"
"font: 24pt \"Calibri\";\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow.png)\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on\n"
"{\n"
"image: url(:/Img/Img/combobox_downarrow_on.png)\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width:23px;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.aq_sc1_comboBox_cycle.setObjectName("aq_sc1_comboBox_cycle")
        self.aq_sc1_pushButton_addClient = QtWidgets.QPushButton(self.aq_sc1_frame)
        self.aq_sc1_pushButton_addClient.setGeometry(QtCore.QRect(420, 0, 60, 60))
        self.aq_sc1_pushButton_addClient.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc1_pushButton_addClient.setText("")
        self.aq_sc1_pushButton_addClient.setObjectName("aq_sc1_pushButton_addClient")
        self.aq_sc1_pushButton_addFarm = QtWidgets.QPushButton(self.aq_sc1_frame)
        self.aq_sc1_pushButton_addFarm.setGeometry(QtCore.QRect(420, 80, 60, 60))
        self.aq_sc1_pushButton_addFarm.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc1_pushButton_addFarm.setText("")
        self.aq_sc1_pushButton_addFarm.setObjectName("aq_sc1_pushButton_addFarm")
        self.aq_sc1_pushButton_addField = QtWidgets.QPushButton(self.aq_sc1_frame)
        self.aq_sc1_pushButton_addField.setGeometry(QtCore.QRect(420, 160, 60, 60))
        self.aq_sc1_pushButton_addField.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc1_pushButton_addField.setText("")
        self.aq_sc1_pushButton_addField.setObjectName("aq_sc1_pushButton_addField")
        self.aq_sc1_pushButton_addCycle = QtWidgets.QPushButton(self.aq_sc1_frame)
        self.aq_sc1_pushButton_addCycle.setGeometry(QtCore.QRect(420, 240, 60, 60))
        self.aq_sc1_pushButton_addCycle.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/AddNew.png);\n"
"background-color: rgb(217, 217    , 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc1_pushButton_addCycle.setText("")
        self.aq_sc1_pushButton_addCycle.setObjectName("aq_sc1_pushButton_addCycle")
        self.stackedWidget.addWidget(self.aq_sc1)
        self.aq_sc2 = QtWidgets.QWidget()
        self.aq_sc2.setObjectName("aq_sc2")
        self.aq_sc2_pushButton_home = QtWidgets.QPushButton(self.aq_sc2)
        self.aq_sc2_pushButton_home.setGeometry(QtCore.QRect(40, 40, 75, 75))
        self.aq_sc2_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 20px;\n"
"background-image: url(:/Img/Img/pushButton_Home.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc2_pushButton_home.setText("")
        self.aq_sc2_pushButton_home.setObjectName("aq_sc2_pushButton_home")
        self.aq_sc2_pushButton_help = QtWidgets.QPushButton(self.aq_sc2)
        self.aq_sc2_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.aq_sc2_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.aq_sc2_pushButton_help.setText("")
        self.aq_sc2_pushButton_help.setObjectName("aq_sc2_pushButton_help")
        self.aq_sc2_label_title = QtWidgets.QLabel(self.aq_sc2)
        self.aq_sc2_label_title.setGeometry(QtCore.QRect(230, 60, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.aq_sc2_label_title.setFont(font)
        self.aq_sc2_label_title.setObjectName("aq_sc2_label_title")
        self.aq_sc2_pushButton_previous = QtWidgets.QPushButton(self.aq_sc2)
        self.aq_sc2_pushButton_previous.setGeometry(QtCore.QRect(40, 350, 241, 70))
        self.aq_sc2_pushButton_previous.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 32pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.aq_sc2_pushButton_previous.setObjectName("aq_sc2_pushButton_previous")
        self.aq_sc2_pushButton_add = QtWidgets.QPushButton(self.aq_sc2)
        self.aq_sc2_pushButton_add.setGeometry(QtCore.QRect(520, 330, 241, 91))
        self.aq_sc2_pushButton_add.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 8px;\n"
"background-color: rgb(74, 143, 231);\n"
"font: 34pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(115, 167, 237);\n"
"}\n"
"")
        self.aq_sc2_pushButton_add.setObjectName("aq_sc2_pushButton_add")
        self.ac_sc2_frame_fileLocation = QtWidgets.QFrame(self.aq_sc2)
        self.ac_sc2_frame_fileLocation.setGeometry(QtCore.QRect(40, 180, 720, 121))
        self.ac_sc2_frame_fileLocation.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"border-radius: 10px")
        self.ac_sc2_frame_fileLocation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ac_sc2_frame_fileLocation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ac_sc2_frame_fileLocation.setObjectName("ac_sc2_frame_fileLocation")
        self.ac_sc2_textEdit_fileLocation = QtWidgets.QTextEdit(self.ac_sc2_frame_fileLocation)
        self.ac_sc2_textEdit_fileLocation.setGeometry(QtCore.QRect(10, 55, 701, 51))
        self.ac_sc2_textEdit_fileLocation.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(236, 239, 240);\n"
"font: 24pt \"Calibri\";")
        self.ac_sc2_textEdit_fileLocation.setObjectName("ac_sc2_textEdit_fileLocation")
        self.ac_sc2_label_fileLocation = QtWidgets.QLabel(self.ac_sc2_frame_fileLocation)
        self.ac_sc2_label_fileLocation.setGeometry(QtCore.QRect(10, 15, 341, 31))
        self.ac_sc2_label_fileLocation.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 28pt \"Calibri\";\n"
"color: rgb(0, 0, 0);")
        self.ac_sc2_label_fileLocation.setObjectName("ac_sc2_label_fileLocation")
        self.stackedWidget.addWidget(self.aq_sc2)
        self.files = QtWidgets.QWidget()
        self.files.setObjectName("files")
        self.files_pushButton_home = QtWidgets.QPushButton(self.files)
        self.files_pushButton_home.setGeometry(QtCore.QRect(40, 30, 51, 51))
        self.files_pushButton_home.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"background-image: url(:/Img/Img/pushButton_Home2.png);\n"
"background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(225, 225, 225);\n"
"}")
        self.files_pushButton_home.setText("")
        self.files_pushButton_home.setObjectName("files_pushButton_home")
        self.files_pushButton_help = QtWidgets.QPushButton(self.files)
        self.files_pushButton_help.setGeometry(QtCore.QRect(710, 40, 50, 50))
        self.files_pushButton_help.setStyleSheet("QPushButton\n"
"{\n"
"border-radius: 25px;\n"
"background-image: url(:/Img/Img/pushButton_HelpCircle.png);\n"
"background-color: rgb(236, 239, 240);\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(242, 244, 245);\n"
"}")
        self.files_pushButton_help.setText("")
        self.files_pushButton_help.setObjectName("files_pushButton_help")
        self.files_label_title = QtWidgets.QLabel(self.files)
        self.files_label_title.setGeometry(QtCore.QRect(330, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.files_label_title.setFont(font)
        self.files_label_title.setStyleSheet("font: 30pt \"Calibri\";")
        self.files_label_title.setObjectName("files_label_title")
        self.files_frame_L = QtWidgets.QFrame(self.files)
        self.files_frame_L.setGeometry(QtCore.QRect(40, 90, 301, 361))
        self.files_frame_L.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius: 20px;")
        self.files_frame_L.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_frame_L.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_frame_L.setObjectName("files_frame_L")
        self.files_scrollArea_L = QtWidgets.QScrollArea(self.files_frame_L)
        self.files_scrollArea_L.setGeometry(QtCore.QRect(10, 10, 261, 341))
        self.files_scrollArea_L.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius: 20px;")
        self.files_scrollArea_L.setWidgetResizable(True)
        self.files_scrollArea_L.setObjectName("files_scrollArea_L")
        self.files_scrollAreaWidgetContents_L = QtWidgets.QWidget()
        self.files_scrollAreaWidgetContents_L.setGeometry(QtCore.QRect(0, 0, 261, 341))
        self.files_scrollAreaWidgetContents_L.setObjectName("files_scrollAreaWidgetContents_L")
        self.files_scrollArea_L.setWidget(self.files_scrollAreaWidgetContents_L)
        self.files_verticalScrollBar_L = QtWidgets.QScrollBar(self.files_frame_L)
        self.files_verticalScrollBar_L.setGeometry(QtCore.QRect(280, 30, 20, 311))
        self.files_verticalScrollBar_L.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius:10px;")
        self.files_verticalScrollBar_L.setOrientation(QtCore.Qt.Vertical)
        self.files_verticalScrollBar_L.setObjectName("files_verticalScrollBar_L")
        self.files_frame_R = QtWidgets.QFrame(self.files)
        self.files_frame_R.setGeometry(QtCore.QRect(460, 90, 301, 361))
        self.files_frame_R.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius: 20px;")
        self.files_frame_R.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_frame_R.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_frame_R.setObjectName("files_frame_R")
        self.files_scrollArea_R = QtWidgets.QScrollArea(self.files_frame_R)
        self.files_scrollArea_R.setGeometry(QtCore.QRect(10, 10, 261, 341))
        self.files_scrollArea_R.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius: 20px;")
        self.files_scrollArea_R.setWidgetResizable(True)
        self.files_scrollArea_R.setObjectName("files_scrollArea_R")
        self.files_scrollAreaWidgetContents_R = QtWidgets.QWidget()
        self.files_scrollAreaWidgetContents_R.setGeometry(QtCore.QRect(0, 0, 261, 341))
        self.files_scrollAreaWidgetContents_R.setObjectName("files_scrollAreaWidgetContents_R")
        self.files_scrollArea_R.setWidget(self.files_scrollAreaWidgetContents_R)
        self.files_verticalScrollBar_R = QtWidgets.QScrollBar(self.files_frame_R)
        self.files_verticalScrollBar_R.setGeometry(QtCore.QRect(280, 30, 20, 311))
        self.files_verticalScrollBar_R.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"border-radius:10px;")
        self.files_verticalScrollBar_R.setOrientation(QtCore.Qt.Vertical)
        self.files_verticalScrollBar_R.setObjectName("files_verticalScrollBar_R")
        self.files_pushButton_copy = QtWidgets.QPushButton(self.files)
        self.files_pushButton_copy.setGeometry(QtCore.QRect(360, 240, 81, 81))
        self.files_pushButton_copy.setStyleSheet("\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(64, 64, 64);\n"
"font: 36pt \"Calibri\";\n"
"color: rgb(236, 239, 240);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"background-color: rgb(120, 120, 120);\n"
"}")
        self.files_pushButton_copy.setObjectName("files_pushButton_copy")
        self.stackedWidget.addWidget(self.files)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(22)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainMe_label_logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Img/Img/LogoWText.png\"/></p></body></html>"))
        self.an_me_label_title.setText(_translate("MainWindow", "Análisis"))
        self.an_gRx1_label_title.setText(_translate("MainWindow", "Generar prescripción"))
        self.an_gRx1_pushButton_next.setText(_translate("MainWindow", "Siguiente"))
        self.an_gRx1_pushButton_previous.setText(_translate("MainWindow", "Anterior"))
        self.an_gRx1_label_client.setText(_translate("MainWindow", "   Cliente:"))
        self.an_gRx1_label_farm.setText(_translate("MainWindow", "   Rancho:"))
        self.an_gRx1_label_field.setText(_translate("MainWindow", "   Campo:"))
        self.an_gRx1_label_crop.setText(_translate("MainWindow", "   Cultivo:"))
        self.an_gRx1_comboBox_crop.setItemText(0, _translate("MainWindow", "Maíz Forrajero"))
        self.an_gRx2_pushButton_previous.setText(_translate("MainWindow", "Anterior"))
        self.an_gRx2_label_title.setText(_translate("MainWindow", "Generar prescripción"))
        self.an_gRx2_pushButton_next.setText(_translate("MainWindow", "Siguiente"))
        self.an_gRx2_label_cycle.setText(_translate("MainWindow", "   Ciclo:"))
        self.an_gRx2_label_model.setText(_translate("MainWindow", "   Modelo:"))
        self.an_gRx2_label_input.setText(_translate("MainWindow", "   Insumo:"))
        self.an_gRx2_label_inputUnit.setText(_translate("MainWindow", "   Unidad insumo:"))
        self.an_gRx2_comboBox_cycle.setItemText(0, _translate("MainWindow", "OI-2021"))
        self.an_gRx2_comboBox_cycle.setItemText(1, _translate("MainWindow", "PV-2022"))
        self.an_gRx2_comboBox_model.setItemText(0, _translate("MainWindow", "Right Rate N"))
        self.an_gRx2_comboBox_input.setItemText(0, _translate("MainWindow", "Urea"))
        self.an_gRx2_comboBox_inputUnit.setItemText(0, _translate("MainWindow", "kg/ha"))
        self.an_gRx3_pushButton_previous.setText(_translate("MainWindow", "Anterior"))
        self.an_gRx3_pushButton_next.setText(_translate("MainWindow", "Siguiente"))
        self.an_gRx3_label_title.setText(_translate("MainWindow", "Generar prescripción"))
        self.an_gRx3_label_inputCost.setText(_translate("MainWindow", "  Costo ud. insumo:$"))
        self.an_gRx3_label_refCycle.setText(_translate("MainWindow", "   Ciclo referencia:"))
        self.an_gRx3_label_yieldGoal.setText(_translate("MainWindow", "  Meta Rend (t/ha):   "))
        self.an_gRx3_label_application.setText(_translate("MainWindow", "   Aplicación :"))
        self.an_gRx3_comboBox_application.setItemText(0, _translate("MainWindow", "Fertirriego"))
        self.an_gRx4_label_title.setText(_translate("MainWindow", "Confirmar datos"))
        self.an_gRx4_pushButton_generateRx.setText(_translate("MainWindow", "   Generar"))
        self.an_gRx4_pushButton_previous.setText(_translate("MainWindow", "Volver"))
        self.an_gRx4_label_data1.setText(_translate("MainWindow", "  Cliente: Nombre cliente\n"
"  Rancho: Nombre rancho\n"
"  Campo: Nombre Campo\n"
"  Cultivo: Nombre cultivo\n"
"  Ciclo: Nombre ciclo\n"
"  Modelo: Nom modelo"))
        self.an_gRx4_label_data2.setText(_translate("MainWindow", "  Insumo a prescribir: Insumo\n"
"  Unidad de insumo: unidad\n"
"  Costo ud. de insumo: $Costo\n"
"  Precio t de cultivo: $Precio\n"
"  Ciclo referencia: Ciclo ref\n"
"  Aplicación: 20"))
        self.an_gRx5_label_title.setText(_translate("MainWindow", "Prescripción"))
        self.an_gRx5_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.an_gRx5_pushButton_exportRx.setText(_translate("MainWindow", "Exportar"))
        self.an_gRx5_pushButton_ecEs.setText(_translate("MainWindow", "Estimación\n"
" económica"))
        self.an_gRx6_label_title.setText(_translate("MainWindow", "Estimación económica"))
        self.an_gRx6_label_inputTitle.setText(_translate("MainWindow", "Insumo"))
        self.an_gRx6_label_inputEstLabel.setText(_translate("MainWindow", "Cantidad estimada:"))
        self.an_gRx6_label_inputEstIndicator.setText(_translate("MainWindow", "200 t "))
        self.an_gRx6_label_inputQuanIndicator.setText(_translate("MainWindow", "-$104,400*"))
        self.an_gRx6_label_inputPercIndicator.setText(_translate("MainWindow", "-0.87%*"))
        self.an_gRx6_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.an_gRx6_label_yieldTitle.setText(_translate("MainWindow", "Rendimiento"))
        self.an_gRx6_label_yieldEstLabel1.setText(_translate("MainWindow", "Media estimada:"))
        self.an_gRx6_label_yieldEstIndicator.setText(_translate("MainWindow", "--.-- t/ha"))
        self.an_gRx6_label_yieldQuanIndicator.setText(_translate("MainWindow", "$ --- . -- *"))
        self.an_gRx6_label_yieldPercIndicator.setText(_translate("MainWindow", "-.-- %*"))
        self.an_gRx6_label_totalLabel.setText(_translate("MainWindow", "DIF. TOTAL:"))
        self.an_gRx6_label_totalIndicator.setText(_translate("MainWindow", "  $904,400*"))
        self.an_gRx6_label_referenceCycle.setText(_translate("MainWindow", "*Cantidades con respecto a ciclo referencia"))
        self.an_gRx7_label_title.setText(_translate("MainWindow", "Exportar prescripción"))
        self.an_gRx7_textEdit_fileLocation.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E:\\AgStat\\Rx</p></body></html>"))
        self.an_gRx7_label_fileLocation.setText(_translate("MainWindow", "Ubicación del archivo:"))
        self.an_gRx7_checkBox_eraseUSB.setText(_translate("MainWindow", " Borrar contenido \n"
" de unidad USB"))
        self.an_gRx7_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.an_vi_me_label_title.setText(_translate("MainWindow", "Visualización"))
        self.an_vi_dMa_label_title.setText(_translate("MainWindow", "Mapa"))
        self.an_vi_dMa_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.an_vi_dMa_pushButton_generate.setText(_translate("MainWindow", "Generar"))
        self.an_vi_dMa_label_cycle.setText(_translate("MainWindow", " Ciclo:"))
        self.an_vi_di_label_title.setText(_translate("MainWindow", "Distribución"))
        self.an_vi_di_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.an_vi_di_pushButton_generate.setText(_translate("MainWindow", "Generar"))
        self.an_vi_di_label_cycle.setText(_translate("MainWindow", " Ciclo:"))
        self.an_vi_di_label_nBins.setText(_translate("MainWindow", " N de clases:"))
        self.an_vi_di_comboBox_nBins.setItemText(0, _translate("MainWindow", "4"))
        self.an_vi_di_comboBox_nBins.setItemText(1, _translate("MainWindow", "5"))
        self.an_vi_di_comboBox_nBins.setItemText(2, _translate("MainWindow", "6"))
        self.an_vi_di_comboBox_nBins.setItemText(3, _translate("MainWindow", "7"))
        self.an_vi_di_comboBox_nBins.setItemText(4, _translate("MainWindow", "8"))
        self.an_vi_di_comboBox_nBins.setItemText(5, _translate("MainWindow", "9"))
        self.an_vi_di_comboBox_nBins.setItemText(6, _translate("MainWindow", "10"))
        self.an_vi_di_comboBox_nBins.setItemText(7, _translate("MainWindow", "12"))
        self.an_vi_di_comboBox_nBins.setItemText(8, _translate("MainWindow", "14"))
        self.an_vi_di_comboBox_nBins.setItemText(9, _translate("MainWindow", "18"))
        self.an_vi_di_comboBox_nBins.setItemText(10, _translate("MainWindow", "20"))
        self.an_vi_di_comboBox_nBins.setItemText(11, _translate("MainWindow", "25"))
        self.an_vi_di_comboBox_nBins.setItemText(12, _translate("MainWindow", "30"))
        self.an_vi_di_comboBox_nBins.setItemText(13, _translate("MainWindow", "40"))
        self.an_vi_di_comboBox_nBins.setItemText(14, _translate("MainWindow", "60"))
        self.an_vi_di_comboBox_nBins.setItemText(15, _translate("MainWindow", "80"))
        self.an_vi_di_comboBox_nBins.setItemText(16, _translate("MainWindow", "100"))
        self.an_vi_sc_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.an_vi_sc_label_title.setText(_translate("MainWindow", "Dispersión"))
        self.an_vi_sc_pushButton_generate.setText(_translate("MainWindow", "Generar"))
        self.an_vi_sc_label_variableX.setText(_translate("MainWindow", " X:"))
        self.an_vi_sc_label_variableY.setText(_translate("MainWindow", " Y:"))
        self.an_vi_sc_label_cycle.setText(_translate("MainWindow", " Ciclo:"))
        self.an_vi_re_pushButton_generate.setText(_translate("MainWindow", "Generar"))
        self.an_vi_re_label_variableX.setText(_translate("MainWindow", " X:"))
        self.an_vi_re_label_variableY.setText(_translate("MainWindow", " Y:"))
        self.an_vi_re_label_cycle.setText(_translate("MainWindow", " Ciclo:"))
        self.an_vi_re_label_order.setText(_translate("MainWindow", " Orden: \n"
""))
        self.an_vi_re_comboBox_order.setItemText(0, _translate("MainWindow", "1"))
        self.an_vi_re_comboBox_order.setItemText(1, _translate("MainWindow", "2"))
        self.an_vi_re_comboBox_order.setItemText(2, _translate("MainWindow", "3"))
        self.an_vi_re_comboBox_order.setItemText(3, _translate("MainWindow", "4"))
        self.an_vi_re_comboBox_order.setItemText(4, _translate("MainWindow", "5"))
        self.an_vi_re_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.an_vi_re_label_title.setText(_translate("MainWindow", "Regresión"))
        self.su1_label_client.setText(_translate("MainWindow", "   Cliente:"))
        self.su1_label_farm.setText(_translate("MainWindow", "   Rancho:"))
        self.su1_label_field.setText(_translate("MainWindow", "   Campo:"))
        self.su1_label_cycle.setText(_translate("MainWindow", "   Ciclo:"))
        self.su1_label_title.setText(_translate("MainWindow", "Datos en campo"))
        self.su1_pushButton_previous.setText(_translate("MainWindow", "Anterior"))
        self.su1_pushButton_next.setText(_translate("MainWindow", "Siguiente"))
        self.su2_label_variable.setText(_translate("MainWindow", "   Variable:"))
        self.su2_label_instrument.setText(_translate("MainWindow", "   Instrumento:"))
        self.su2_label_mode.setText(_translate("MainWindow", "   Modalidad:"))
        self.su2_label_interval.setText(_translate("MainWindow", "   Intervalo (s):"))
        self.su2_comboBox_instrument.setItemText(0, _translate("MainWindow", "Veris 3100"))
        self.su2_comboBox_instrument.setItemText(1, _translate("MainWindow", "Sistema HGF "))
        self.su2_comboBox_instrument.setItemText(2, _translate("MainWindow", "Penentrómetro"))
        self.su2_comboBox_mode.setItemText(0, _translate("MainWindow", "Puntual"))
        self.su2_comboBox_mode.setItemText(1, _translate("MainWindow", "Continuo"))
        self.su2_label_title.setText(_translate("MainWindow", "Datos en campo"))
        self.su2_pushButton_previous.setText(_translate("MainWindow", "Anterior"))
        self.su2_pushButton_next.setText(_translate("MainWindow", "Siguiente"))
        self.su3_label_title.setText(_translate("MainWindow", "Datos en campo"))
        self.su3_checkBox_eraseUSB.setText(_translate("MainWindow", " Borrar contenido \n"
" de unidad USB"))
        self.su3_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.su3_textEdit_fileLocation.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">H:/Cliente/Granja/Campo1/VariableX.csv</span></p></body></html>"))
        self.su3_label_fileLocation.setText(_translate("MainWindow", "Ubicación del archivo:"))
        self.suC_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.suC_checkbox_toggleStart.setText(_translate("MainWindow", "INICIAR"))
        self.suC_label_sampleValueLabel.setText(_translate("MainWindow", "Lectura actual:"))
        self.suC_label_sampleNoLabel.setText(_translate("MainWindow", "Lectura #:"))
        self.suC_label_latLabel.setText(_translate("MainWindow", "Lat:"))
        self.suC_label_lonLabel.setText(_translate("MainWindow", "Lon:"))
        self.suC_label_sampleValueIndicator.setText(_translate("MainWindow", "00.0000"))
        self.suC_label_sampleNoIndicator.setText(_translate("MainWindow", "0"))
        self.suC_label_lonIndicator.setText(_translate("MainWindow", "101.548654"))
        self.suC_label_latIndicator.setText(_translate("MainWindow", "24.5487896"))
        self.suC_pushButton_next.setText(_translate("MainWindow", "Reiniciar"))
        self.suC_pushButton_lockRef.setText(_translate("MainWindow", "Fijar Ref."))
        self.suC_label_satNoIndicator.setText(_translate("MainWindow", "5"))
        self.suC_label_rtkLabel.setText(_translate("MainWindow", "   RTK:"))
        self.suC_label_rtkIndicator.setText(_translate("MainWindow", "NO FIJO"))
        self.suC_label_fieldData.setText(_translate("MainWindow", "    \"Cliente\"        \"Rancho\"         \"Campo\"        \"Variable\""))
        self.suP_label_sampleValueLabel.setText(_translate("MainWindow", "Lectura actual:"))
        self.suP_label_sampleNoLabel.setText(_translate("MainWindow", "Lectura #:"))
        self.suP_label_latLabel.setText(_translate("MainWindow", "Lat:"))
        self.suP_label_lonLabel.setText(_translate("MainWindow", "Lon:"))
        self.suP_label_sampleValueIndicator.setText(_translate("MainWindow", "00.0000"))
        self.suP_label_sampleNoIndicator.setText(_translate("MainWindow", "0"))
        self.suP_label_lonIndicator.setText(_translate("MainWindow", "101.548654"))
        self.suP_label_latIndicator.setText(_translate("MainWindow", "24.5487896"))
        self.suP_pushButton_next.setText(_translate("MainWindow", "Reiniciar"))
        self.suP_label_fieldData.setText(_translate("MainWindow", "    \"Cliente\"        \"Rancho\"         \"Campo\"        \"Variable\""))
        self.suP_pushButton_back.setText(_translate("MainWindow", "Volver"))
        self.suP_pushButton_lockRef.setText(_translate("MainWindow", "Fijar Ref."))
        self.suP_label_satNoIndicator.setText(_translate("MainWindow", "5"))
        self.suP_label_rtkLabel.setText(_translate("MainWindow", "   RTK:"))
        self.suP_label_rtkIndicator.setText(_translate("MainWindow", "NO FIJO"))
        self.suP_pushButton_sample.setText(_translate("MainWindow", "Tomar muestra"))
        self.aq_menu_label_title.setText(_translate("MainWindow", "Adquisición de datos"))
        self.aq_sc1_pushButton_next.setText(_translate("MainWindow", "Siguiente"))
        self.aq_sc1_label_title_2.setText(_translate("MainWindow", "Datos dispersos"))
        self.aq_sc1_pushButton_previous.setText(_translate("MainWindow", "Anterior"))
        self.aq_sc1_label_client.setText(_translate("MainWindow", "   Cliente:"))
        self.aq_sc1_label_farm.setText(_translate("MainWindow", "   Rancho:"))
        self.aq_sc1_label_field.setText(_translate("MainWindow", "   Campo:"))
        self.aq_sc1_label_cycle.setText(_translate("MainWindow", "   Ciclo:"))
        self.aq_sc2_label_title.setText(_translate("MainWindow", "Datos dispersos"))
        self.aq_sc2_pushButton_previous.setText(_translate("MainWindow", "Anterior"))
        self.aq_sc2_pushButton_add.setText(_translate("MainWindow", "Agregar +"))
        self.ac_sc2_textEdit_fileLocation.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">H:/Cliente/Granja/Campo1/VariableX.csv</span></p></body></html>"))
        self.ac_sc2_label_fileLocation.setText(_translate("MainWindow", "Ubicación del archivo:"))
        self.files_label_title.setText(_translate("MainWindow", "Archivos"))
        self.files_pushButton_copy.setText(_translate("MainWindow", "->"))

from mplwidget import MplWidget
import AgStatResources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

