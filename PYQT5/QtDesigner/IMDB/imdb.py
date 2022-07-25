# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(592, 543)
        Form.setStyleSheet("QWidget\n"
"{\n"
"    background-color: #282936;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 551, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setMouseTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: #ffc80b;\n"
"    \n"
"    border-color: #000000;\n"
"\n"
"    \n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"}")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 60, 551, 461))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit\n"
"{\n"
"    background-color:#D3D3D3;\n"
"    color: #000;\n"
"    border-color: #000000;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: #ffc80b;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #ffe152;  \n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #e5c010;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: #e5c010;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.getdata)
    def getdata(self):
        count = 0
        for i in parsed_information.find_all("tbody",{"class":"lister-list"}):
            for j in i.find_all("a"):
                if count:
                        self.plainTextEdit.insertPlainText(str(count)+". "+j.text)
                        count +=1
                if count == 0:
                        count += 1
                

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "IMDB TOP 250"))
        self.pushButton.setText(_translate("Form", "GET"))
class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.m_ui = Ui_Form()
        self.m_ui.setupUi(self)
        self.show() 

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
html_information = response.content
parsed_information = BeautifulSoup(html_information,"html.parser")

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())