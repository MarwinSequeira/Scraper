from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 807)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchText = QtWidgets.QLineEdit(self.centralwidget)
        self.searchText.setGeometry(QtCore.QRect(110, 50, 531, 51))
        self.searchText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.searchText.setObjectName("searchText")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(680, 60, 111, 31))
        self.searchButton.setObjectName("searchButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(180, 140, 161, 41))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(430, 150, 171, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.searchButton.clicked.connect(self.search)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchText.setPlaceholderText(_translate("MainWindow", "Emter text for search"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.radioButton.setText(_translate("MainWindow", "Search only in Amazon"))
        self.radioButton_2.setText(_translate("MainWindow", "Search only in Flipkart"))

    def search(self):
        if self.radioButton.isChecked():
            # call amzon function
            pass
        elif self.radioButton_2.isChecked():
            # call flipkart function
            pass
        else:
            # call bith funtions
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())