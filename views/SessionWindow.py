from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal

from Ui_SessionWindow import Ui_SessionWindow
from DatabaseGenerator import DatabaseGenerator, DbConnectionError


class SessionWindow(QMainWindow):

    connected = pyqtSignal()

    def __init__(self, dbgen, parent=None):
        super().__init__(parent)
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
            self.connected.emit()
        except DbConnectionError:
            self.show_error()

    def show_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(
            "Connection error occured while trying to connect to database. Please, check your credentials again.")
        msg.setWindowTitle("Connection Error")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()


def main():
    import sys
    from PyQt5.QtWidgets import QApplication
    from DatabaseGenerator import DatabaseGenerator
    app = QApplication(sys.argv)
    dbgen = DatabaseGenerator()
    generator_window = SessionWindow(dbgen)
    generator_window.show()
    sys.exit(app.exec_())
    print(dbgen.driver)

if __name__ == "__main__":
    main()
