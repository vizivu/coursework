from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
import pandas as pd

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_TWSWindow(object):
    TWSWindow = None

    def __init__(self, twsw, parent=None):
        self.TableWindow = twsw
        self.model = QtGui.QStandardItemModel(self.TableWindow)
        self.setupUi(self.TableWindow)

    def search(self):
        df = pd.read_csv('data.csv', delimiter=",", encoding="utf-8")
        a = self.textEdit.toPlainText()
        b = df.loc[(df.id == a) | (df.white_id == a) | (df.black_id == a)]
        model = pandasModel(b)
        self.tableView.setModel(model)
        print(b)

    def openMainWindow(self):
        from main import Ui_MainWindow
        self.mWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mWindow)
        self.mWindow.show()

    def setupUi(self, TWSWindow):
        TWSWindow.setObjectName("TWSWindow")
        TWSWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(TWSWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 690, 560))
        self.tableView.setObjectName("tableView")

        self.tableView.setModel(self.model)

        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(750, 180, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSearch.setFont(font)
        self.btnSearch.setObjectName("btnSearch")

        self.btnSearch.clicked.connect(self.search)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 320, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openMainWindow)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(720, 120, 260, 40))

        self.textEdit.setFocus()

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        TWSWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TWSWindow)
        QtCore.QMetaObject.connectSlotsByName(TWSWindow)

    def retranslateUi(self, TWSWindow):
        _translate = QtCore.QCoreApplication.translate
        TWSWindow.setWindowTitle(_translate("TWSWindow", "Таблица с поиском"))
        self.btnSearch.setText(_translate("TWSWindow", "Поиск"))
        self.pushButton.setText(_translate("TWSWindow", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TWSWindow = QtWidgets.QMainWindow()
    ui = Ui_TWSWindow(TWSWindow)
    TWSWindow.show()
    sys.exit(app.exec_())
