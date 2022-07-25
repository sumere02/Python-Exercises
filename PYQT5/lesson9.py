import sys
from PyQt5.QtWidgets import QPushButton,QLabel,QWidget,QHBoxLayout,QVBoxLayout,QRadioButton,QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__init__ui()
    def __init__ui(self):
        self.label = QLabel("Which language do you prefer ?")
        self.button = QPushButton("Send")
        self.c = QRadioButton("C")
        self.cpp = QRadioButton("C++")
        self.python = QRadioButton("Python")
        self.java = QRadioButton("Java")
        self.label_result = QLabel("")
        v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.c)
        v_box.addWidget(self.cpp)
        v_box.addWidget(self.python)
        v_box.addWidget(self.java)
        v_box.addWidget(self.label_result)
        v_box.addStretch()
        v_box.addWidget(self.button)
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.button.clicked.connect(lambda : self.click(self.c.isChecked(),self.cpp.isChecked(),self.python.isChecked(),self.java.isChecked()))
        self.setWindowTitle("Lesson 9")
        self.show()
    def click(self,c,cpp,python,java):
        if c:
            self.label_result.setText("C")
        elif cpp:
            self.label_result.setText("C++")
        elif python:
            self.label_result.setText("Python")
        elif java:
            self.label_result.setText("Java")
        else:
            self.label_result.setText("Choose language")
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())