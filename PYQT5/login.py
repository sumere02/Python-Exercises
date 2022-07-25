import sys
from PyQt5 import QtWidgets
import sqlite3

"""
connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("INSERT INTO INFO VALUES (?,?)",("sumere20","51259363712Es."))
connection.commit()
connection.close()
"""

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.id = QtWidgets.QLineEdit("ID")
        self.password = QtWidgets.QLineEdit("Password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.clear = QtWidgets.QPushButton("Clear")
        self.info = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        v_box.addWidget(self.id)
        v_box.addWidget(self.password)
        v_box.addWidget(self.info)
        v_box.addStretch()
        v_box.addWidget(self.login)
        v_box.addWidget(self.clear)
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.login.clicked.connect(self.click)
        self.clear.clicked.connect(self.click)
        self.setWindowTitle("SumerBook")
        self.show()
    def click(self):
        sent_button = self.sender()
        sent_button = sent_button.text()
        if sent_button == "Clear":
            self.id.clear()
            self.password.clear()
        else:
            self.connection = sqlite3.connect("database.db")
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * From INFO")
            data = self.cursor.fetchall()
            flag = 0
            for person in data:
                if person[0] == self.id.text() and person[1] == self.password.text():
                    flag = 1
                    break
            if flag:
                self.info.setText("Welcome {}".format(self.id.text()))
            else:
                self.info.setText("Wrong ID or PASSWORD")
            self.connection.close()
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

