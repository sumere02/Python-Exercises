import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    continue_button = QtWidgets.QPushButton("Continue")
    exit = QtWidgets.QPushButton("Cancel")
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(continue_button)
    h_box.addWidget(exit)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Lesson 4")
    window.setLayout(v_box)
    window.setGeometry(100,100,500,500)

    window.show()
    sys.exit(app.exec_())
window()