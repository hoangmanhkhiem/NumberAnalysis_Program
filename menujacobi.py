# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menujacobi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homejacobi(object):
    def setupUi(self, homejacobi):
        homejacobi.setObjectName("homejacobi")
        homejacobi.resize(523, 344)
        self.menujacobi = QtWidgets.QWidget(homejacobi)
        self.menujacobi.setObjectName("menujacobi")
        self.textBrowser = QtWidgets.QTextBrowser(self.menujacobi)
        self.textBrowser.setGeometry(QtCore.QRect(80, 80, 361, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.menujacobi)
        self.label.setGeometry(QtCore.QRect(0, 30, 521, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ppjacobi = QtWidgets.QPushButton(self.menujacobi)
        self.ppjacobi.setGeometry(QtCore.QRect(110, 120, 301, 28))
        self.ppjacobi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ppjacobi.setObjectName("ppjacobi")
        self.back = QtWidgets.QPushButton(self.menujacobi)
        self.back.setGeometry(QtCore.QRect(110, 150, 301, 28))
        self.back.setObjectName("back")
        homejacobi.setCentralWidget(self.menujacobi)
        self.menubar = QtWidgets.QMenuBar(homejacobi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
        self.menubar.setObjectName("menubar")
        homejacobi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homejacobi)
        self.statusbar.setObjectName("statusbar")
        homejacobi.setStatusBar(self.statusbar)

        self.retranslateUi(homejacobi)
        QtCore.QMetaObject.connectSlotsByName(homejacobi)

    def retranslateUi(self, homejacobi):
        _translate = QtCore.QCoreApplication.translate
        homejacobi.setWindowTitle(_translate("homejacobi", "Hoàng Mạnh Khiêm VipPro"))
        self.label.setText(_translate("homejacobi", "PHƯƠNG PHÁP JACOBI"))
        self.ppjacobi.setText(_translate("homejacobi", "Phương pháp Jacobi"))
        self.back.setText(_translate("homejacobi", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homejacobi = QtWidgets.QMainWindow()
    ui = Ui_homejacobi()
    ui.setupUi(homejacobi)
    homejacobi.show()
    sys.exit(app.exec_())
