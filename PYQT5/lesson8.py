import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QPushButton,QLabel,QVBoxLayout,QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__init__ui()
    def __init__ui(self):
        self.check_box = QCheckBox("Do you like python ?")
        self.button = QPushButton("Click")
        self.label = QLabel("")
        v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        v_box.addWidget(self.check_box)
        v_box.addWidget(self.label)
        v_box.addStretch()
        v_box.addWidget(self.button)
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Lesson 8")
        self.button.clicked.connect(lambda : self.click(self.check_box.isChecked()))
        self.show()
    def click(self,check):
        if check:
            self.label.setText("Good")
        else:
            self.label.setText(":(")
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
        
