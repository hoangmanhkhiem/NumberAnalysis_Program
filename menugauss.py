# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menugauss.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homegauss(object):
    def setupUi(self, homegauss):
        homegauss.setObjectName("homegauss")
        homegauss.resize(523, 344)
        self.menugauss = QtWidgets.QWidget(homegauss)
        self.menugauss.setObjectName("menugauss")
        self.textBrowser = QtWidgets.QTextBrowser(self.menugauss)
        self.textBrowser.setGeometry(QtCore.QRect(80, 60, 361, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.menugauss)
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
        self.ppgaussss = QtWidgets.QPushButton(self.menugauss)
        self.ppgaussss.setGeometry(QtCore.QRect(110, 100, 301, 28))
        self.ppgaussss.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ppgaussss.setObjectName("ppgaussss")
        self.back = QtWidgets.QPushButton(self.menugauss)
        self.back.setGeometry(QtCore.QRect(110, 160, 301, 28))
        self.back.setObjectName("back")
        self.label_5 = QtWidgets.QLabel(self.menugauss)
        self.label_5.setGeometry(QtCore.QRect(390, 90, 441, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.menugauss)
        self.label_6.setGeometry(QtCore.QRect(80, 70, 361, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.ausssbif = QtWidgets.QPushButton(self.menugauss)
        self.ausssbif.setGeometry(QtCore.QRect(110, 130, 301, 28))
        self.ausssbif.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ausssbif.setObjectName("ausssbif")
        homegauss.setCentralWidget(self.menugauss)
        self.menubar = QtWidgets.QMenuBar(homegauss)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
        self.menubar.setObjectName("menubar")
        homegauss.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homegauss)
        self.statusbar.setObjectName("statusbar")
        homegauss.setStatusBar(self.statusbar)

        self.retranslateUi(homegauss)
        QtCore.QMetaObject.connectSlotsByName(homegauss)

    def retranslateUi(self, homegauss):
        _translate = QtCore.QCoreApplication.translate
        homegauss.setWindowTitle(_translate("homegauss", "Hoàng Mạnh Khiêm VipPro"))
        self.label.setText(_translate("homegauss", "PHƯƠNG PHÁP GAUSS"))
        self.ppgaussss.setText(_translate("homegauss", "Phương pháp Gauss"))
        self.back.setText(_translate("homegauss", "Back"))
        self.label_5.setText(_translate("homegauss", "Copyright 2023 - SKROMNYY"))
        self.label_6.setText(_translate("homegauss", "Copyright 2023 - SKROMNYY"))
        self.ausssbif.setText(_translate("homegauss", "Phương pháp Gauss for BigData"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homegauss = QtWidgets.QMainWindow()
    ui = Ui_homegauss()
    ui.setupUi(homegauss)
    homegauss.show()
    sys.exit(app.exec_())
