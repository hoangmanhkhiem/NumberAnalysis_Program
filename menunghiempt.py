# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menunghiemgandungpt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menunoghiempt(object):
    def setupUi(self, menunoghiempt):
        menunoghiempt.setObjectName("menunoghiempt")
        menunoghiempt.resize(523, 346)
        self.menupt = QtWidgets.QWidget(menunoghiempt)
        self.menupt.setObjectName("menupt")
        self.textBrowser = QtWidgets.QTextBrowser(self.menupt)
        self.textBrowser.setGeometry(QtCore.QRect(80, 60, 361, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.menupt)
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
        self.ppchiadoi = QtWidgets.QPushButton(self.menupt)
        self.ppchiadoi.setGeometry(QtCore.QRect(110, 90, 301, 28))
        self.ppchiadoi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ppchiadoi.setObjectName("ppchiadoi")
        self.pplap = QtWidgets.QPushButton(self.menupt)
        self.pplap.setGeometry(QtCore.QRect(110, 120, 301, 28))
        self.pplap.setObjectName("pplap")
        self.ppdaycung = QtWidgets.QPushButton(self.menupt)
        self.ppdaycung.setGeometry(QtCore.QRect(110, 150, 301, 28))
        self.ppdaycung.setObjectName("ppdaycung")
        self.back = QtWidgets.QPushButton(self.menupt)
        self.back.setGeometry(QtCore.QRect(110, 210, 301, 28))
        self.back.setObjectName("back")
        self.pptieptuyen = QtWidgets.QPushButton(self.menupt)
        self.pptieptuyen.setGeometry(QtCore.QRect(110, 180, 301, 28))
        self.pptieptuyen.setObjectName("pptieptuyen")
        menunoghiempt.setCentralWidget(self.menupt)
        self.menubar = QtWidgets.QMenuBar(menunoghiempt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
        self.menubar.setObjectName("menubar")
        menunoghiempt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menunoghiempt)
        self.statusbar.setObjectName("statusbar")
        menunoghiempt.setStatusBar(self.statusbar)

        self.retranslateUi(menunoghiempt)
        QtCore.QMetaObject.connectSlotsByName(menunoghiempt)

    def retranslateUi(self, menunoghiempt):
        _translate = QtCore.QCoreApplication.translate
        menunoghiempt.setWindowTitle(_translate("menunoghiempt", "Hoàng Mạnh Khiêm VipPro"))
        self.label.setText(_translate("menunoghiempt", "NGHIỆM GẦN ĐÚNG PHƯƠNG TRÌNH"))
        self.ppchiadoi.setText(_translate("menunoghiempt", "Phương pháp chia đôi"))
        self.pplap.setText(_translate("menunoghiempt", "Phương pháp lặp"))
        self.ppdaycung.setText(_translate("menunoghiempt", "Phương pháp dây cung"))
        self.back.setText(_translate("menunoghiempt", "Back"))
        self.pptieptuyen.setText(_translate("menunoghiempt", "Phương pháp tiếp tuyến"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menunoghiempt = QtWidgets.QMainWindow()
    ui = Ui_menunoghiempt()
    ui.setupUi(menunoghiempt)
    menunoghiempt.show()
    sys.exit(app.exec_())