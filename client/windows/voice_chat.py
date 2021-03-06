# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voice_chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VoiceChat(object):
    def setupUi(self, TextChat):
        TextChat.setObjectName("TextChat")
        TextChat.resize(450, 600)
        self.centralwidget = QtWidgets.QWidget(TextChat)
        self.centralwidget.setObjectName("centralwidget")
        self.main_bg = QtWidgets.QLabel(self.centralwidget)
        self.main_bg.setGeometry(QtCore.QRect(-100, -180, 640, 897))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.main_bg.setFont(font)
        self.main_bg.setText("")
        self.main_bg.setPixmap(QtGui.QPixmap("images/main_bg.jpg"))
        self.main_bg.setObjectName("main_bg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(0, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(True)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(239, 110, 254), stop:1 rgb(85, 255, 255));")
        self.exit_btn.setIconSize(QtCore.QSize(40, 30))
        self.exit_btn.setCheckable(False)
        self.exit_btn.setDefault(False)
        self.exit_btn.setObjectName("exit_btn")
        TextChat.setCentralWidget(self.centralwidget)

        self.retranslateUi(TextChat)
        QtCore.QMetaObject.connectSlotsByName(TextChat)

    def retranslateUi(self, TextChat):
        _translate = QtCore.QCoreApplication.translate
        TextChat.setWindowTitle(_translate("TextChat", "MainWindow"))
        self.label.setText(_translate("TextChat", "Voice Label"))
        self.exit_btn.setText(_translate("TextChat", "EXIT ROOM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TextChat = QtWidgets.QMainWindow()
    ui = Ui_VoiceChat()
    ui.setupUi(TextChat)
    TextChat.show()
    sys.exit(app.exec_())
