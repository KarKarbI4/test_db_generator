# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TablePreviewWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TablePreviewWidget(object):
    def setupUi(self, TablePreviewWidget):
        TablePreviewWidget.setObjectName("TablePreviewWidget")
        TablePreviewWidget.resize(587, 466)
        self.verticalLayout = QtWidgets.QVBoxLayout(TablePreviewWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(TablePreviewWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox = QtWidgets.QSpinBox(TablePreviewWidget)
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
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
        self.label.setText(_translate("TablePreviewWidget", "Test rows numbers:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TablePreviewWidget = QtWidgets.QWidget()
    ui = Ui_TablePreviewWidget()
    ui.setupUi(TablePreviewWidget)
    TablePreviewWidget.show()
    sys.exit(app.exec_())

