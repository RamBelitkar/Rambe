import sys
import ast
from PyQt5 import QtCore, QtGui, QtWidgets
from Genetic_data import thisdata

class Ui_dataShow(object):
    def setupUi(self, dataShow):
        dataShow.setObjectName("dataShow")
        dataShow.resize(1177, 608)
        dataShow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        dataShow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(dataShow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 1141, 541))
        self.widget.setObjectName("widget")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(60, 120, 931, 371))
        self.tableView.setStyleSheet("background-color:pink;")
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(440, 100, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:gold")
        self.label_2.setObjectName("label_2")
        self.Close = QtWidgets.QPushButton(self.widget)
        self.Close.setGeometry(QtCore.QRect(930, 510, 75, 23))
        self.Close.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"color:white")
        self.Close.setObjectName("Close")
        dataShow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(dataShow)
        self.statusbar.setObjectName("statusbar")
        dataShow.setStatusBar(self.statusbar)

        self.retranslateUi(dataShow)

        QtCore.QMetaObject.connectSlotsByName(dataShow)
        print("thisdata:", repr(thisdata))

        lines = ast.literal_eval(thisdata)  # Convert the string to a list of lists

        model = QtGui.QStandardItemModel(len(lines), len(lines[0]))
        model.setHorizontalHeaderLabels(['Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    
        # Populate the model with the data
        for row_idx, line in enumerate(lines):
            for col_idx, item in enumerate(line):
                standard_item = QtGui.QStandardItem(item)
                standard_item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                standard_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                standard_item.setTextAlignment(QtCore.Qt.AlignLeft)
                model.setItem(row_idx, col_idx, standard_item)

        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()

        # Connect Close button to close window
        self.Close.clicked.connect(dataShow.close)

    def retranslateUi(self, dataShow):
        _translate = QtCore.QCoreApplication.translate
        dataShow.setWindowTitle(_translate("dataShow", "MainWindow"))
        self.label_2.setText(_translate("dataShow", "Schedule Data"))
        self.Close.setText(_translate("dataShow", "Close"))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dataShow = QtWidgets.QMainWindow()
    ui = Ui_dataShow()
    ui.setupUi(dataShow)
    dataShow.show()
    sys.exit(app.exec_())
