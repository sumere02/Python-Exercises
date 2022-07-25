# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication 
import requests
from bs4 import BeautifulSoup
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(473, 386)
        Form.setStyleSheet("QWidget\n"
"{\n"
"    background-color: #282936;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 10, 91, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setMouseTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QFrame, QLabel, QToolTip {\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    background-image: url(images/welcome.png);\n"
"}")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 60, 333, 301))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox.setStyleSheet("QComboBox\n"
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
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    background-color: #282936;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_2.setStyleSheet("QComboBox\n"
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
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit.setStyleSheet("QLineEdit\n"
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
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
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
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    background-color: #282936;\n"
"    color: #ffffff;\n"
"    border-color: #000000;\n"
"\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
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
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(lambda : self.click(self.lineEdit.text()))
    def click(self,amount):
        if self.comboBox_2.currentText() == "TL":
                result = str(float(amount)*float(currency[self.comboBox.currentText()]))
        elif self.comboBox.currentText() != "TL":
                result = str(float(amount)*(float(currency[self.comboBox.currentText()]))/float(currency[self.comboBox_2.currentText()]))
        else:
                result = str(float(amount)*(1/float(currency[self.comboBox_2.currentText()])))
        self.lineEdit_2.setText(result)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IS BANK"))
        self.pushButton.setText(_translate("Form", "Contact"))
        self.label.setText(_translate("Form", "Currency Converter"))
        self.label_2.setText(_translate("Form", "From:"))
        self.comboBox.setItemText(0, _translate("Form", "Currency"))
        self.comboBox.setItemText(1, _translate("Form", "DOLAR"))
        self.comboBox.setItemText(2, _translate("Form", "TL"))
        self.comboBox.setItemText(3, _translate("Form", "EURO"))
        self.comboBox.setItemText(4, _translate("Form", "GRAM ALTIN"))
        self.label_3.setText(_translate("Form", "To:"))
        self.comboBox_2.setItemText(0, _translate("Form", "Currency"))
        self.comboBox_2.setItemText(1, _translate("Form", "DOLAR"))
        self.comboBox_2.setItemText(2, _translate("Form", "TL"))
        self.comboBox_2.setItemText(3, _translate("Form", "EURO"))
        self.comboBox_2.setItemText(4, _translate("Form", "GRAM ALTIN"))
        self.lineEdit.setText(_translate("Form", "Amount"))
        self.pushButton_2.setText(_translate("Form", "Convert"))
        self.label_4.setText(_translate("Form", "Result:"))
        self.lineEdit_2.setText(_translate("Form", "Result"))
class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.m_ui = Ui_Form()
        self.m_ui.setupUi(self)
        self.show()    


url = "https://www.doviz.com"

response = requests.get(url)

html_information = response.content

parsed = BeautifulSoup(html_information,"html.parser")

list_currency = list()
list_currency_name = list()
currency = parsed.find_all("span",{"class":"value"})
currency_name = parsed.find_all("span",{"class":"name"})
for i in currency:
    list_currency.append(i.text.replace("$","").replace(",","."))
for i in currency_name:
    list_currency_name.append(i.text)
currency = dict(zip(list_currency_name,list_currency))
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())