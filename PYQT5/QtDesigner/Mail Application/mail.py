# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_Form(QtWidgets.QWidget):
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
"    background-color: #282936;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_1.setStyleSheet("QLabel\n"
"{\n"
"    background-color: #282936;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}")
        self.label_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: white;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"    selection-background-color: #0949ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::focus\n"
"{\n"
"    padding: 3px;\n"
"    border: 1px solid #0949ff;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout_2.addWidget(self.lineEdit_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    background-color: #282936;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: white;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"    selection-background-color: #0949ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::focus\n"
"{\n"
"    padding: 3px;\n"
"    border: 1px solid #0949ff;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit\n"
"{\n"
"    background-color: white;\n"
"    color: #000;\n"
"    border-color: #000000;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setStyleSheet("QPushButton\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setStyleSheet("QPushButton\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.click_send)
        self.pushButton_3.clicked.connect(self.click_clear)
        
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SumerMail"))
        self.label_1.setText(_translate("Form", "From:"))
        self.label_2.setText(_translate("Form", "To   :"))
        self.pushButton_2.setText(_translate("Form", "Send"))
        self.pushButton_3.setText(_translate("Form", "Clear"))
    def click_send(self):
            file_path = QtWidgets.QFileDialog.getSaveFileName(self,"Save Template",os.getenv("HOME"))
            with open (file_path[0],"w",encoding="utf-8") as file:
                file.write(self.plainTextEdit.text())
    def click_clear(self):
            self.lineEdit_1.clear()
            self.lineEdit_2.clear()
            self.plainTextEdit.clear()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.m_ui = Ui_Form()
        self.m_ui.setupUi(self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
