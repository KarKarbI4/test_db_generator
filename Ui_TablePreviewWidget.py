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
        TablePreviewWidget.resize(583, 458)
        self.gridLayout = QtWidgets.QGridLayout(TablePreviewWidget)
        self.gridLayout.setObjectName("gridLayout")
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(TablePreviewWidget)
        QtCore.QMetaObject.connectSlotsByName(TablePreviewWidget)

    def retranslateUi(self, TablePreviewWidget):
        _translate = QtCore.QCoreApplication.translate
        TablePreviewWidget.setWindowTitle(_translate("TablePreviewWidget", "TablePreview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TablePreviewWidget = QtWidgets.QWidget()
    ui = Ui_TablePreviewWidget()
    ui.setupUi(TablePreviewWidget)
    TablePreviewWidget.show()
    sys.exit(app.exec_())

