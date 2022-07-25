import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Lesson 3")
    button = QtWidgets.QPushButton(window)
    button.setText("Continue")
    label1 = QtWidgets.QLabel(window)
    label1.setText("Hello World")
    label1.move(200,30)
    button.move(190,50)
    window.setGeometry(100,100,500,500)
    window.show()
    sys.exit(app.exec_())
window()