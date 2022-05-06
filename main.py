from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def openGistoWindow(self):
        from gisto import Ui_GistoWindow
        self.gWindow = QtWidgets.QMainWindow()
        self.ui = Ui_GistoWindow()
        self.ui.setupUi(self.gWindow)
        self.gWindow.show()

    def openTableWindow(self):
        from table import Ui_TableWindow
        self.tWindow = QtWidgets.QMainWindow()
        self.ui = Ui_TableWindow(self.tWindow)
        self.ui.setupUi(self.tWindow)
        self.tWindow.show()

    def openTWSWindow(self):
        from tws import Ui_TWSWindow
        self.twsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_TWSWindow(self.twsWindow)
        self.ui.setupUi(self.twsWindow)
        self.twsWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 380)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnTable = QtWidgets.QPushButton(self.centralwidget)
        self.btnTable.setGeometry(QtCore.QRect(60, 160, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTable.setFont(font)
        self.btnTable.setObjectName("btnTable")

        self.btnTable.clicked.connect(self.openTableWindow)

        self.btnTWS = QtWidgets.QPushButton(self.centralwidget)
        self.btnTWS.setGeometry(QtCore.QRect(340, 160, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTWS.setFont(font)
        self.btnTWS.setObjectName("btnTWS")

        self.btnTWS.clicked.connect(self.openTWSWindow)

        self.btnGisto = QtWidgets.QPushButton(self.centralwidget)
        self.btnGisto.setGeometry(QtCore.QRect(200, 260, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGisto.setFont(font)
        self.btnGisto.setObjectName("btnGisto")

        self.btnGisto.clicked.connect(self.openGistoWindow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 500, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Набор данных для шахматных игр (Lichess)"))
        self.btnTable.setText(_translate("MainWindow", "Таблица"))
        self.btnTWS.setText(_translate("MainWindow", "Таблица с поиском"))
        self.btnGisto.setText(_translate("MainWindow", "Гистограмма"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать в программу. Выберите интересующую вас функцию"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
