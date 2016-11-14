# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabaseWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DatabaseWidget(object):
    def setupUi(self, DatabaseWidget):
        DatabaseWidget.setObjectName("DatabaseWidget")
        DatabaseWidget.resize(527, 350)
        self.gridLayout = QtWidgets.QGridLayout(DatabaseWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tablesTree = QtWidgets.QTreeWidget(DatabaseWidget)
        self.tablesTree.setRootIsDecorated(False)
        self.tablesTree.setUniformRowHeights(False)
        self.tablesTree.setItemsExpandable(True)
        self.tablesTree.setAllColumnsShowFocus(False)
        self.tablesTree.setExpandsOnDoubleClick(False)
        self.tablesTree.setColumnCount(1)
        self.tablesTree.setObjectName("tablesTree")
        self.tablesTree.header().setVisible(True)
        self.tablesTree.header().setCascadingSectionResizes(False)
        self.tablesTree.header().setHighlightSections(True)
        self.gridLayout.addWidget(self.tablesTree, 0, 0, 1, 1)

        self.retranslateUi(DatabaseWidget)
        QtCore.QMetaObject.connectSlotsByName(DatabaseWidget)

    def retranslateUi(self, DatabaseWidget):
        _translate = QtCore.QCoreApplication.translate
        DatabaseWidget.setWindowTitle(_translate("DatabaseWidget", "Form"))
        self.tablesTree.headerItem().setText(0, _translate("DatabaseWidget", "Tables"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatabaseWidget = QtWidgets.QWidget()
    ui = Ui_DatabaseWidget()
    ui.setupUi(DatabaseWidget)
    DatabaseWidget.show()
    sys.exit(app.exec_())

