# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calclap.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calclappp(object):
    def setupUi(self, calclappp):
        calclappp.setObjectName("calclappp")
        calclappp.resize(601, 474)
        self.menucalclap = QtWidgets.QWidget(calclappp)
        self.menucalclap.setObjectName("menucalclap")
        self.label = QtWidgets.QLabel(self.menucalclap)
        self.label.setGeometry(QtCore.QRect(0, 20, 601, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.menucalclap)
        self.textBrowser.setGeometry(QtCore.QRect(80, 60, 441, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.menucalclap)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.menucalclap)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 201, 16))
        self.label_3.setObjectName("label_3")
        self.tinh = QtWidgets.QPushButton(self.menucalclap)
        self.tinh.setGeometry(QtCore.QRect(350, 280, 141, 28))
        self.tinh.setObjectName("tinh")
        self.back = QtWidgets.QPushButton(self.menucalclap)
        self.back.setGeometry(QtCore.QRect(410, 370, 93, 28))
        self.back.setObjectName("back")
        self.label_5 = QtWidgets.QLabel(self.menucalclap)
        self.label_5.setGeometry(QtCore.QRect(80, 70, 441, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.menucalclap)
        self.comboBox.setGeometry(QtCore.QRect(360, 190, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.giatrilap = QtWidgets.QTextEdit(self.menucalclap)
        self.giatrilap.setGeometry(QtCore.QRect(110, 220, 141, 21))
        self.giatrilap.setObjectName("giatrilap")
        self.imputhamso = QtWidgets.QTextEdit(self.menucalclap)
        self.imputhamso.setGeometry(QtCore.QRect(110, 120, 381, 21))
        self.imputhamso.setObjectName("imputhamso")
        self.valuebombobox = QtWidgets.QTextEdit(self.menucalclap)
        self.valuebombobox.setGeometry(QtCore.QRect(350, 220, 141, 21))
        self.valuebombobox.setObjectName("valuebombobox")
        self.label_4 = QtWidgets.QLabel(self.menucalclap)
        self.label_4.setGeometry(QtCore.QRect(110, 290, 211, 16))
        self.label_4.setObjectName("label_4")
        self.output = QtWidgets.QTextEdit(self.menucalclap)
        self.output.setGeometry(QtCore.QRect(110, 320, 381, 41))
        self.output.setObjectName("output")
        calclappp.setCentralWidget(self.menucalclap)
        self.menubar = QtWidgets.QMenuBar(calclappp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 26))
        self.menubar.setObjectName("menubar")
        calclappp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(calclappp)
        self.statusbar.setObjectName("statusbar")
        calclappp.setStatusBar(self.statusbar)

        self.retranslateUi(calclappp)
        QtCore.QMetaObject.connectSlotsByName(calclappp)

    def retranslateUi(self, calclappp):
        _translate = QtCore.QCoreApplication.translate
        calclappp.setWindowTitle(_translate("calclappp", "Hoàng Mạnh Khiêm VipPro"))
        self.label.setText(_translate("calclappp", "PHƯƠNG PHÁP LẶP"))
        self.label_2.setText(_translate("calclappp", "Nhập hàm f(x) đã chuyển đổi"))
        self.label_3.setText(_translate("calclappp", "Nhập giá trị x0"))
        self.tinh.setText(_translate("calclappp", "Tính"))
        self.back.setText(_translate("calclappp", "Back"))
        self.label_5.setText(_translate("calclappp", "Copyright 2023 - SKROMNYY"))
        self.comboBox.setItemText(0, _translate("calclappp", "Nhập giá trị sai số"))
        self.comboBox.setItemText(1, _translate("calclappp", "Nhập số lần"))
        self.label_4.setText(_translate("calclappp", "Nghiệm gần đúng của phương trình"))
        self.output.setHtml(_translate("calclappp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Đáp án sẽ hiện ở đây</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calclappp = QtWidgets.QMainWindow()
    ui = Ui_calclappp()
    ui.setupUi(calclappp)
    calclappp.show()
    sys.exit(app.exec_())