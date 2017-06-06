# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TableContentViewWidget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TableContentViewWidget(object):
    def setupUi(self, TableContentViewWidget):
        TableContentViewWidget.setObjectName("TableContentViewWidget")
        TableContentViewWidget.resize(518, 433)
        self.TableContentViewLayout = QtWidgets.QVBoxLayout(TableContentViewWidget)
        self.TableContentViewLayout.setObjectName("TableContentViewLayout")
        self.tableNamaFormLayout = QtWidgets.QFormLayout()
        self.tableNamaFormLayout.setObjectName("tableNamaFormLayout")
        self.tableNameLabel = QtWidgets.QLabel(TableContentViewWidget)
        self.tableNameLabel.setObjectName("tableNameLabel")
        self.tableNamaFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tableNameLabel)
        self.tableNameValueLabel = QtWidgets.QLabel(TableContentViewWidget)
        self.tableNameValueLabel.setObjectName("tableNameValueLabel")
        self.tableNamaFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tableNameValueLabel)
        self.TableContentViewLayout.addLayout(self.tableNamaFormLayout)
        self.tableWidget = QtWidgets.QTableWidget(TableContentViewWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.TableContentViewLayout.addWidget(self.tableWidget)

        self.retranslateUi(TableContentViewWidget)
        QtCore.QMetaObject.connectSlotsByName(TableContentViewWidget)

    def retranslateUi(self, TableContentViewWidget):
        _translate = QtCore.QCoreApplication.translate
        TableContentViewWidget.setWindowTitle(_translate("TableContentViewWidget", "TableContentView"))
        self.tableNameLabel.setText(_translate("TableContentViewWidget", "Table Name: "))
        self.tableNameValueLabel.setText(_translate("TableContentViewWidget", "table0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TableContentViewWidget = QtWidgets.QWidget()
    ui = Ui_TableContentViewWidget()
    ui.setupUi(TableContentViewWidget)
    TableContentViewWidget.show()
    sys.exit(app.exec_())

