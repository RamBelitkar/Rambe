import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Genetic_data import main
from prettytable import PrettyTable

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

        # Get data from main()
        thisdata = main()

        # Parse PrettyTable string
        table = PrettyTable()
        table.field_names = ["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        rows = thisdata.split("\n")
        for row in rows[3:-1]:  # Exclude header and footer
            fields = row.split("|")[1:-1]
            table.add_row([field.strip() for field in fields])

        # Create a Qt model
        model = QtGui.QStandardItemModel(len(table._rows), len(table._rows[0]))
        model.setHorizontalHeaderLabels(table.field_names)

        # Populate the model with data
        for row_idx, row_data in enumerate(table._rows):
            for col_idx, col_data in enumerate(row_data):
                item = QtGui.QStandardItem(col_data)
                model.setItem(row_idx, col_idx, item)

        # Set the model to the QTableView
        self.tableView.setModel(model)

        # Set stretch factors
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        v_header = self.tableView.verticalHeader()
        v_header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Connect Close button to close window
        self.Close.clicked.connect(dataShow.close)

    def retranslateUi(self, dataShow):
        _translate = QtCore.QCoreApplication.translate
        dataShow.setWindowTitle(_translate("dataShow", "MainWindow"))
        self.label_2.setText(_translate("dataShow", "Schedule Data"))
        self.Close.setText(_translate("dataShow", "Close"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dataShow = QtWidgets.QMainWindow()
    ui = Ui_dataShow()
    ui.setupUi(dataShow)
    dataShow.show()
    sys.exit(app.exec_())
