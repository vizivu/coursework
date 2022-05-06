from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import pyqtgraph as pg

class Ui_GistoWindow(object):

    def openMainWindow(self):
        from main import Ui_MainWindow
        self.mWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mWindow)
        self.mWindow.show()

    def setupUi(self, GistoWindow):
        GistoWindow.setObjectName("GistoWindow")
        GistoWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(GistoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(5, 5, 790, 660))
        self.widget.setObjectName("widget")

        df = pd.read_csv('data.csv', delimiter=",", encoding="utf-8")
        self.bargraph = pg.BarGraphItem(x=df.white_rating, height=df.turns, width=0.6, brush='g')
        self.widget.addItem(self.bargraph)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 700, 200, 60))

        self.pushButton.clicked.connect(self.openMainWindow)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        GistoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GistoWindow)
        QtCore.QMetaObject.connectSlotsByName(GistoWindow)

    def retranslateUi(self, GistoWindow):
        _translate = QtCore.QCoreApplication.translate
        GistoWindow.setWindowTitle(_translate("GistoWindow", "Гистограмма"))
        self.pushButton.setText(_translate("GistoWindow", "Назад"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GistoWindow = QtWidgets.QMainWindow()
    ui = Ui_GistoWindow()
    ui.setupUi(GistoWindow)
    GistoWindow.show()
    sys.exit(app.exec_())
