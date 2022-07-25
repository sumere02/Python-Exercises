import sys
from PyQt5 import QtWidgets,QtGui
def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Lesson 2")
    label1 = QtWidgets.QLabel(window)
    label1.setText("TEXT")
    label1.move(400,400)
    label2 = QtWidgets.QLabel
    label2.setPixmap(QtGui.QPixmap("python.png")) 
    window.setGeometry(100,100,500,500)
    window.show()
    sys.exit(app.exec_())
window()