from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class Ui_TableWindow(object):
    TableWindow = None

    def openMainWindow(self):
        from main import Ui_MainWindow
        self.mWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mWindow)
        self.TableWindow.hide()
        self.mWindow.show()

    def __init__(self, tw, parent=None):
        self.TableWindow = tw
        self.model = QtGui.QStandardItemModel(self.TableWindow)
        self.setupUi(self.TableWindow)

    def setupUi(self, TableWindow):
        TableWindow.setObjectName("TableWindow")
        TableWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(TableWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 10, 760, 660))
        self.tableView.setObjectName("tableView")

        self.tableView.setModel(self.model)

        self.loadCsv()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 700, 200, 60))

        self.pushButton.clicked.connect(self.openMainWindow)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        TableWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TableWindow)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def retranslateUi(self, TableWindow):
        _translate = QtCore.QCoreApplication.translate
        TableWindow.setWindowTitle(_translate("TableWindow", "Таблица"))
        self.pushButton.setText(_translate("TableWindow", "Назад"))

    def loadCsv(self):
        fileName = 'data.csv'
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TableWindow = QtWidgets.QMainWindow()
    ui = Ui_TableWindow(TableWindow)
    TableWindow.show()
    sys.exit(app.exec_())
