from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from dataEntry import Ui_Data_form

class Ui_Login(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Data_form()  # Add parentheses to instantiate the class
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, form):
        form.setObjectName("Login Page")
        form.resize(600, 560)
        form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(form)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(45, 80, 550, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(C:/Users/AISSMS Poly IF/Downloads/data/images2.jpg);\n"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(-90, -50, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(290, 30, 240, 430))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 1);\n"
"border-bottom-right-radius: 50px;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(360, 70, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_4.setObjectName("label_4")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(310, 220, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("background-color:(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.Password.setObjectName("Password")
        self.Username = QtWidgets.QLineEdit(self.widget)
        self.Username.setGeometry(QtCore.QRect(310, 150, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setStyleSheet("background-color:(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.Username.setObjectName("Username")
        self.pushButton = QtWidgets.QPushButton(self.widget,clicked= lambda:self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(320, 300, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QpushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:  0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 102, 219), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(85 98, 112, 225));\n"
"    color: rgba(255,255,255,210);\n"
"}\n"
"QpushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(85 81, 84, 225));\n"
"    }\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 11, 0.98);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 230, 130))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,80);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(50, 100, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(50, 140, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_9.setObjectName("label_9")
        self.label.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.Password.raise_()
        self.Username.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(form)
        self.statusbar.setObjectName("statusbar")
        form.setStatusBar(self.statusbar)

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=0,yOffset=0))
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25,xOffset=3,yOffset=3))
        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.label_7.setText(_translate("MainWindow1", "Scheduling Application"))
        self.label_4.setText(_translate("MainWindow1", "Log In"))
        self.Password.setPlaceholderText(_translate("MainWindow1", "Password"))
        self.Username.setPlaceholderText(_translate("MainWindow1", "User Name"))
        self.pushButton.setText(_translate("MainWindow1", "L O G I N"))
        self.label_6.setText(_translate("MainWindow1", "TimeTable "))
        self.label_9.setText(_translate("MainWindow1", "Scheduling Algorithm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
