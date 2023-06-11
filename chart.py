import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from vedt import show_chart
from dothipt import Ui_dothipt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_dothipt()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.show_diagram)
        
        self.index = "you can send data here"
        
    def show_diagram(self):
        if self.uic.screen.isEmpty():
            self.uic.screen.addWidget(show_chart(self.index))
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())