# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(985, 785)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(200, 90, 511, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 630, 136, 34))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(13, 13, 249, 19))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(270, 10, 107, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 720, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Test1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Humidity"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Temperature"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Time"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "Val1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "Toggle Start/Stop"))
        self.label.setText(_translate("Dialog", "Enter number of values to be taken"))
        self.pushButton_2.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

