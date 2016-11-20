# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TablePreviewWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TablePreviewWidget(object):
    def setupUi(self, TablePreviewWidget):
        TablePreviewWidget.setObjectName("TablePreviewWidget")
        TablePreviewWidget.resize(556, 442)
        self.verticalLayout = QtWidgets.QVBoxLayout(TablePreviewWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.rowNumLabel = QtWidgets.QLabel(TablePreviewWidget)
        self.rowNumLabel.setObjectName("rowNumLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rowNumLabel)
        self.rowNumSpin = QtWidgets.QSpinBox(TablePreviewWidget)
        self.rowNumSpin.setMaximum(1000)
        self.rowNumSpin.setProperty("value", 100)
        self.rowNumSpin.setDisplayIntegerBase(10)
        self.rowNumSpin.setObjectName("rowNumSpin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rowNumSpin)
        self.verticalLayout.addLayout(self.formLayout)
        self.tableWidget = QtWidgets.QTableWidget(TablePreviewWidget)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(TablePreviewWidget)
        QtCore.QMetaObject.connectSlotsByName(TablePreviewWidget)

    def retranslateUi(self, TablePreviewWidget):
        _translate = QtCore.QCoreApplication.translate
        TablePreviewWidget.setWindowTitle(_translate("TablePreviewWidget", "TablePreview"))
        self.rowNumLabel.setText(_translate("TablePreviewWidget", "Test rows number:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TablePreviewWidget = QtWidgets.QWidget()
    ui = Ui_TablePreviewWidget()
    ui.setupUi(TablePreviewWidget)
    TablePreviewWidget.show()
    sys.exit(app.exec_())

