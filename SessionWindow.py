# -*- coding: utf-8 -*-
#!/usr/bin/python3

# Form implementation generated from reading ui file 'Session.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SessionWindow(object):
    def setupUi(self, SessionWindow):
        SessionWindow.setObjectName("SessionWindow")
        SessionWindow.resize(444, 219)
        self.centralwidget = QtWidgets.QWidget(SessionWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settingsVLayout = QtWidgets.QVBoxLayout()
        self.settingsVLayout.setObjectName("settingsVLayout")
        self.settingsFormLayout = QtWidgets.QFormLayout()
        self.settingsFormLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.settingsFormLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.settingsFormLayout.setObjectName("settingsFormLayout")
        self.driverLabel = QtWidgets.QLabel(self.centralwidget)
        self.driverLabel.setEnabled(True)
        self.driverLabel.setObjectName("driverLabel")
        self.settingsFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.driverLabel)
        self.driverCombo = QtWidgets.QComboBox(self.centralwidget)
        self.driverCombo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.driverCombo.sizePolicy().hasHeightForWidth())
        self.driverCombo.setSizePolicy(sizePolicy)
        self.driverCombo.setEditable(False)
        self.driverCombo.setObjectName("driverCombo")
        self.settingsFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.driverCombo)
        self.hostLabel = QtWidgets.QLabel(self.centralwidget)
        self.hostLabel.setEnabled(True)
        self.hostLabel.setObjectName("hostLabel")
        self.settingsFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.hostLabel)
        self.hostEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.hostEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hostEdit.sizePolicy().hasHeightForWidth())
        self.hostEdit.setSizePolicy(sizePolicy)
        self.hostEdit.setInputMask("")
        self.hostEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hostEdit.setObjectName("hostEdit")
        self.settingsFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hostEdit)
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setEnabled(True)
        self.userLabel.setObjectName("userLabel")
        self.settingsFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.userLabel)
        self.userEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userEdit.setEnabled(True)
        self.userEdit.setObjectName("userEdit")
        self.settingsFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.userEdit)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setEnabled(True)
        self.passwordLabel.setObjectName("passwordLabel")
        self.settingsFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setEnabled(True)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.settingsFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passwordEdit)
        self.portLabel = QtWidgets.QLabel(self.centralwidget)
        self.portLabel.setEnabled(True)
        self.portLabel.setObjectName("portLabel")
        self.settingsFormLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.portLabel)
        self.portSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.portSpin.setEnabled(True)
        self.portSpin.setMaximum(65533)
        self.portSpin.setProperty("value", 3306)
        self.portSpin.setObjectName("portSpin")
        self.settingsFormLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.portSpin)
        self.settingsVLayout.addLayout(self.settingsFormLayout)
        self.verticalLayout.addLayout(self.settingsVLayout)
        self.buttonsHLayout = QtWidgets.QHBoxLayout()
        self.buttonsHLayout.setObjectName("buttonsHLayout")
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBtn.setEnabled(True)
        self.connectBtn.setObjectName("connectBtn")
        self.buttonsHLayout.addWidget(self.connectBtn)
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.buttonsHLayout.addWidget(self.cancelBtn)
        self.verticalLayout.addLayout(self.buttonsHLayout)
        SessionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SessionWindow)
        self.cancelBtn.clicked.connect(SessionWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SessionWindow)

    def retranslateUi(self, SessionWindow):
        _translate = QtCore.QCoreApplication.translate
        SessionWindow.setWindowTitle(_translate("SessionWindow", "Connect to database"))
        self.driverLabel.setText(_translate("SessionWindow", "Database driver:"))
        self.hostLabel.setText(_translate("SessionWindow", "Hostname / IP:"))
        self.userLabel.setText(_translate("SessionWindow", "User:"))
        self.passwordLabel.setText(_translate("SessionWindow", "Password:"))
        self.portLabel.setText(_translate("SessionWindow", "Port:"))
        self.connectBtn.setText(_translate("SessionWindow", "Connect"))
        self.cancelBtn.setText(_translate("SessionWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SessionWindow = QtWidgets.QMainWindow()
    ui = Ui_SessionWindow()
    ui.setupUi(SessionWindow)
    SessionWindow.show()
    sys.exit(app.exec_())

