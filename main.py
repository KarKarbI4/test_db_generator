#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from SessionWindow import Ui_SessionWindow
from DatabaseGenerator import DatabaseGenerator, ConnectionError

class SessionManager(QtWidgets.QMainWindow):
    def __init__(self, dbgen):
        super().__init__()
        self.ui = Ui_SessionWindow()
        self.ui.setupUi(self)
        self.dbgen = dbgen
        self.setup()

    def setup(self):
        self.ui.driverCombo.addItems(DatabaseGenerator.drivers.keys())
        self.ui.hostEdit.setText(DatabaseGenerator.default_settings['host'])
        self.ui.userEdit.setText(DatabaseGenerator.default_settings['user'])
        self.ui.portSpin.setValue(DatabaseGenerator.default_settings['port'])
        self.ui.connectBtn.clicked.connect(self.connect_to_db)

    def connect_to_db(self):
        drivername = self.ui.driverCombo.currentText()
        host = self.ui.hostEdit.text()
        user = self.ui.userEdit.text()
        password = self.ui.passwordEdit.text()
        port = self.ui.portSpin.value()
        try:
            self.dbgen.connect(drivername, host, user, password, port)
        except ConnectionError:
            self.showError()

    def showError(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Connection error occured while trying to connect to database. Please, check your credentials again.")
        msg.setWindowTitle("Connection Error")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dbgen = DatabaseGenerator()
    sessionManager = SessionManager(dbgen)
    sessionManager.show()
    sys.exit(app.exec_())
    print(dbgen.driver)