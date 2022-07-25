import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.writing_area = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("Clear")
        self.write = QtWidgets.QPushButton("Write")
        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        v_box.addWidget(self.writing_area)
        v_box.addWidget(self.write)
        v_box.addWidget(self.clear)
        v_box.addStretch()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        """
        self.clear.clicked.connect(self.clear_click)
        self.write.clicked.connect(self.write_click)
        """
        self.clear.clicked.connect(self.click)
        self.write.clicked.connect(self.click)
        self.setWindowTitle("Lesson 6")
        self.show()
    def click(self):
        sender = self.sender()
        if sender.text() == "Clear":
            self.writing_area.clear()   
        elif sender.text() == "Write":
            print(self.writing_area.text())
        else:
            pass
    """
    def clear_click(self):
        self.writing_area.setText("")
    def write_click(self):
        pass
    """
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())