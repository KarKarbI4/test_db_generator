from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal

from Ui_SessionWindow import Ui_SessionWindow
from DbErrors import DbConnectionError


class SessionWindow(QMainWindow):

    connected = pyqtSignal()

    drivers = property()

    @drivers.setter
    def drivers(self, items):
        self.ui.driverCombo.currentIndexChanged.disconnect(
            self.on_driver_changed)
        self.ui.driverCombo.clear()
        self.ui.driverCombo.addItems(items)
        self.ui.driverCombo.currentIndexChanged.connect(self.on_driver_changed)

    @property
    def driver(self):
        return self.ui.driverCombo.currentText()

    @driver.setter
    def driver(self, item):
        indx = self.ui.driverCombo.findText(item)
        self.ui.driverCombo.setCurrentIndex(indx)

    @property
    def host(self):
        return self.ui.hostEdit.text()

    @host.setter
    def host(self, host):
        self.ui.hostEdit.setText(host)

    @property
    def port(self):
        return self.ui.portSpin.value()

    @port.setter
    def port(self, port):
        self.ui.portSpin.setValue(port)

    @property
    def user(self):
        return self.ui.userEdit.text()

    @user.setter
    def user(self, user):
        self.ui.userEdit.setText(user)

    @property
    def password(self):
        return self.ui.passwordEdit.text()

    @password.setter
    def password(self, password):
        self.ui.passwordEdit.setText(password)

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        super().__init__()

        self.build_ui()

        self.model.sub_upd_func(self.upd_ui_from_model)
        self.upd_ui_from_model()

    def build_ui(self):
        self.ui = Ui_SessionWindow()
        self.ui.setupUi(self)

        # Connections
        self.ui.driverCombo.currentIndexChanged.connect(self.on_driver_changed)
        self.ui.hostEdit.textEdited.connect(self.on_host_changed)
        self.ui.portSpin.valueChanged.connect(self.on_port_changed)
        self.ui.userEdit.textEdited.connect(self.on_user_changed)
        self.ui.passwordEdit.textEdited.connect(self.on_password_changed)
        self.ui.connectBtn.clicked.connect(self.on_connect)

    def upd_ui_from_model(self):
        self.drivers = self.model.get_drivers()
        self.driver = self.model.drivername
        self.host = self.model.host
        self.port = self.model.port
        self.user = self.model.user
        self.password = self.model.password

    def on_driver_changed(self, indx):
        self.controller.change_driver(self.driver)

    def on_host_changed(self):
        self.controller.change_host(self.host)

    def on_port_changed(self, port):
        self.controller.change_port(port)

    def on_user_changed(self):
        self.controller.change_user(self.user)

    def on_password_changed(self):
        self.controller.change_password(self.password)

    def on_connect(self):
        try:
            self.controller.connect()
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
