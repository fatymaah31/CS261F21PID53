# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1043, 586)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1051, 591))
        self.frame.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1051, 31))
        self.frame_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 0, 47, 31))
        self.label.setStyleSheet("image: url(:/newPrefix/ok.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 47, 31))
        self.label_2.setStyleSheet("image: url(:/newPrefix/ok.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(90, 0, 47, 31))
        self.label_3.setStyleSheet("image: url(:/newPrefix/ok.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(360, 50, 341, 61))
        self.widget.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"border-radius: 29px")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 0, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 8, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 100 25pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(200, 0, 91, 61))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(40, 140, 981, 51))
        self.widget_2.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 18px")
        self.widget_2.setObjectName("widget_2")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(6, 2, 61, 51))
        self.label_8.setStyleSheet("image: url(:/newPrefix/loading.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(70, 10, 691, 31))
        self.progressBar.setStyleSheet("\n"
"QProgressBar{\n"
"color: rgb(255, 1, 1);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 12px\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius: 10px\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.progressBar.setProperty("value", 60)
        self.progressBar.setObjectName("progressBar")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(800, 10, 151, 31))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(10, -10, 41, 51))
        self.label_9.setStyleSheet("image: url(:/newPrefix/pause.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(50, 0, 41, 31))
        self.label_10.setStyleSheet("image: url(:/newPrefix/stop.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(90, 0, 47, 31))
        self.label_11.setStyleSheet("image: url(:/newPrefix/play.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setGeometry(QtCore.QRect(40, 210, 301, 351))
        self.widget_4.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 18px")
        self.widget_4.setObjectName("widget_4")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setGeometry(QtCore.QRect(20, 20, 261, 151))
        self.widget_6.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"background-color: rgb(6, 6, 6);\n"
"border-radius: 18px")
        self.widget_6.setObjectName("widget_6")
        self.label_17 = QtWidgets.QLabel(self.widget_6)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 101, 101))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget_6)
        self.label_18.setGeometry(QtCore.QRect(160, 50, 51, 20))
        self.label_18.setStyleSheet("font: 10pt \"Arial\";\n"
"")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_6)
        self.label_19.setGeometry(QtCore.QRect(150, 70, 71, 21))
        self.label_19.setStyleSheet("font: 10pt \"Arial\";\n"
"")
        self.label_19.setObjectName("label_19")
        self.comboBox = QtWidgets.QComboBox(self.widget_6)
        self.comboBox.setGeometry(QtCore.QRect(30, 122, 191, 20))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 18px")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setGeometry(QtCore.QRect(20, 180, 261, 151))
        self.widget_8.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"background-color: rgb(6, 6, 6);\n"
"border-radius: 18px")
        self.widget_8.setObjectName("widget_8")
        self.label_16 = QtWidgets.QLabel(self.widget_8)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 101, 101))
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.widget_8)
        self.label_20.setGeometry(QtCore.QRect(160, 40, 51, 20))
        self.label_20.setStyleSheet("font: 10pt \"Arial\";\n"
"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_8)
        self.label_21.setGeometry(QtCore.QRect(150, 60, 71, 21))
        self.label_21.setStyleSheet("font: 10pt \"Arial\";\n"
"")
        self.label_21.setObjectName("label_21")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_8)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 120, 191, 20))
        self.comboBox_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);\n"
"border-radius: 18px")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.widget_5 = QtWidgets.QWidget(self.frame)
        self.widget_5.setGeometry(QtCore.QRect(360, 210, 661, 351))
        self.widget_5.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 18px")
        self.widget_5.setObjectName("widget_5")
        self.widget_10 = QtWidgets.QWidget(self.widget_5)
        self.widget_10.setGeometry(QtCore.QRect(20, 20, 621, 311))
        self.widget_10.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border-radius: 18px")
        self.widget_10.setObjectName("widget_10")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_10)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 621, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 30px")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.widget_9 = QtWidgets.QWidget(self.widget_10)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 621, 31))
        self.widget_9.setStyleSheet("\n"
"background-color: rgb(255, 7, 7);\n"
"border-radius: 10px\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.label_22 = QtWidgets.QLabel(self.widget_9)
        self.label_22.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.label_22.setStyleSheet("image: url(:/newPrefix/pause.png);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_9)
        self.label_23.setGeometry(QtCore.QRect(40, 3, 47, 20))
        self.label_23.setObjectName("label_23")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">S O U N D</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">H U T</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/module_100px.png\"/></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">Select</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#f4f4f4;\">Algorithm</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "Insertion Sort"))
        self.comboBox.setItemText(1, _translate("Form", "Merge Sort"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/up_down_arrow_100px.png\"/></p></body></html>"))
        self.label_20.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">  Sorting</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_21.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#f4f4f4;\">Algorithm</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "Ascending Order"))
        self.comboBox_2.setItemText(1, _translate("Form", "Descending Order"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Song Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Genre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sub-Genre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Artist Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Album Price"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Tags"))
        self.label_22.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/search_20px.png\"/></p></body></html>"))
        self.label_23.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Search</span></p></body></html>"))

import ok_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

