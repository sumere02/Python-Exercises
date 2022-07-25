import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        open = QAction("Open",self)
        open.setShortcut("Ctrl+O")
        save = QAction("Save",self)
        save.setShortcut("Ctrl+S")
        exit = QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")
        exit.triggered.connect(self.click_exit)
        file.addAction(open)
        file.addAction(save)
        file.addAction(exit)
        file.triggered.connect(self.response)
        search_and_edit = edit.addMenu("Search and edit")
        search = QAction("Search",self)
        search.setShortcut("Ctrl+R")
        sub_edit = QAction("Edit",self)
        sub_edit.setShortcut("Ctrl+E")
        search_and_edit.addAction(search)
        search_and_edit.addAction(sub_edit)
        clear = QAction("Clear",self)
        clear.setShortcut("Ctrl+Z")
        menubar.addAction(clear)
        self.setWindowTitle("Menus")
        self.show()
    def click_exit(self):
        qApp.quit()
    def response(self,action):
        if action.text() == "Open":
            print("Open")
        elif action.text() == "Save":
            print("Save")
        else:
            print("Exit")
     
app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())