# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alererror.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homedothi(object):
    def setupUi(self, homedothi):
        homedothi.setObjectName("homedothi")
        homedothi.resize(351, 325)
        self.dothi = QtWidgets.QWidget(homedothi)
        self.dothi.setObjectName("dothi")
        self.label = QtWidgets.QLabel(self.dothi)
        self.label.setGeometry(QtCore.QRect(0, 20, 351, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.dothi)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 291, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.ok = QtWidgets.QPushButton(self.dothi)
        self.ok.setGeometry(QtCore.QRect(130, 200, 93, 28))
        self.ok.setObjectName("ok")
        self.label_5 = QtWidgets.QLabel(self.dothi)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 291, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.dothi)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dothi)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.dothi)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        homedothi.setCentralWidget(self.dothi)
        self.menubar = QtWidgets.QMenuBar(homedothi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 26))
        self.menubar.setObjectName("menubar")
        homedothi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homedothi)
        self.statusbar.setObjectName("statusbar")
        homedothi.setStatusBar(self.statusbar)

        self.retranslateUi(homedothi)
        QtCore.QMetaObject.connectSlotsByName(homedothi)

    def retranslateUi(self, homedothi):
        _translate = QtCore.QCoreApplication.translate
        homedothi.setWindowTitle(_translate("homedothi", "MainWindow"))
        self.label.setText(_translate("homedothi", "HI ! KHIÊM ĐÂY !!!!"))
        self.ok.setText(_translate("homedothi", "OK"))
        self.label_5.setText(_translate("homedothi", "Copyright 2023 - SKROMNYY"))
        self.label_2.setText(_translate("homedothi", "NHỚ ĐỌC KĨ HDSD"))
        self.label_3.setText(_translate("homedothi", "TRƯỚC KHI RA KẾT QUẢ"))
        self.label_4.setText(_translate("homedothi", "THÌ NOT RESPONDING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homedothi = QtWidgets.QMainWindow()
    ui = Ui_homedothi()
    ui.setupUi(homedothi)
    homedothi.show()
    sys.exit(app.exec_())
