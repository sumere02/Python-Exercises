import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QPushButton,QHBoxLayout,QVBoxLayout,QFileDialog,QMainWindow,QMenuBar,QAction,qApp
import os

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__init__ui()
    def __init__ui(self):
        self.button_save = QPushButton("Save")
        self.button_clear = QPushButton("Clear")
        self.button_open = QPushButton("Open")
        self.area = QTextEdit()
        v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        v_box.addWidget(self.area)
        v_box.addStretch()
        h_box.addWidget(self.button_clear)
        h_box.addWidget(self.button_save)
        h_box.addWidget(self.button_open)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("Sumerpad")
        self.button_save.clicked.connect(self.click)
        self.button_clear.clicked.connect(self.click)
        self.button_open.clicked.connect(self.click)
    def click(self):
        sent_button = self.sender().text()
        if sent_button == "Clear":
            self.area.clear()
        elif sent_button == "Open":
            file_path = QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
            with open(file_path[0],"r",encoding="UTF-8") as file:
                self.area.setText(file.read())
        else:
            file_path = QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
            with open(file_path[0],"w",encoding="UTF-8") as file:
                file.write(self.area.toPlainText())

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = Window()
        self.setCentralWidget(self.window)
        
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        open = QAction("Open",self)
        open.setShortcut("Ctrl+O")
        file.addAction(open)

        save = QAction("Save",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")
        file.addAction(exit)

        search = menubar.addMenu("Edit")
        search_and_change = search.addMenu("Search and change")
        search = QAction("Search",self)
        search.setShortcut("Ctrl+F")
        search_and_change.addAction(search)
        change = QAction("Change",self)
        change.setShortcut("Ctrl+E")
        search_and_change.addAction(change)
        clear = QAction("Clear",self)
        clear.setShortcut("Ctrl+0")
        menubar.addAction(clear)
        file.triggered.connect(self.click_file)
        clear.triggered.connect(self.clear)
        self.setWindowTitle("Sumerpad")
        self.show()
    def click_file(self,action):
        if action.text()=="Open":
            file_path = QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
            with open(file_path[0],"r",encoding="UTF-8") as file:
                self.window.area.setText(file.read())
        elif action.text() == "Save":
            file_path = QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
            with open(file_path[0],"w",encoding="UTF-8") as file:
                file.write(self.window.area.toPlainText())
        else:
            qApp.exit()
    def clear(self,action):
        self.window.area.clear()
        
app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())


