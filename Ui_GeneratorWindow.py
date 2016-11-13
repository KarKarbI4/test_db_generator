# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GeneratorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneratorWindow(object):
    def setupUi(self, GeneratorWindow):
        GeneratorWindow.setObjectName("GeneratorWindow")
        GeneratorWindow.setEnabled(True)
        GeneratorWindow.resize(697, 501)
        GeneratorWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        GeneratorWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        GeneratorWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(GeneratorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout.addWidget(self.tabWidget)
        GeneratorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GeneratorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        GeneratorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GeneratorWindow)
        self.statusbar.setObjectName("statusbar")
        GeneratorWindow.setStatusBar(self.statusbar)
        self.treeDockWidget = QtWidgets.QDockWidget(GeneratorWindow)
        self.treeDockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.treeDockWidget.setObjectName("treeDockWidget")
        self.treeDockWidgetContent = QtWidgets.QWidget()
        self.treeDockWidgetContent.setObjectName("treeDockWidgetContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.treeDockWidgetContent)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.schemaTreeWidget = QtWidgets.QTreeWidget(self.treeDockWidgetContent)
        self.schemaTreeWidget.setExpandsOnDoubleClick(False)
        self.schemaTreeWidget.setObjectName("schemaTreeWidget")
        self.schemaTreeWidget.header().setHighlightSections(True)
        self.verticalLayout.addWidget(self.schemaTreeWidget)
        self.treeDockWidget.setWidget(self.treeDockWidgetContent)
        GeneratorWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.treeDockWidget)
        self.actionClose = QtWidgets.QAction(GeneratorWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_2 = QtWidgets.QAction(GeneratorWindow)
        self.actionClose_2.setObjectName("actionClose_2")
        self.menuFile.addAction(self.actionClose_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(GeneratorWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(GeneratorWindow)

    def retranslateUi(self, GeneratorWindow):
        _translate = QtCore.QCoreApplication.translate
        GeneratorWindow.setWindowTitle(_translate("GeneratorWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("GeneratorWindow", "File"))
        self.treeDockWidget.setWindowTitle(_translate("GeneratorWindow", "Database Tree"))
        self.schemaTreeWidget.headerItem().setText(0, _translate("GeneratorWindow", "Schemas"))
        self.actionClose.setText(_translate("GeneratorWindow", "Close"))
        self.actionClose_2.setText(_translate("GeneratorWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GeneratorWindow = QtWidgets.QMainWindow()
    ui = Ui_GeneratorWindow()
    ui.setupUi(GeneratorWindow)
    GeneratorWindow.show()
    sys.exit(app.exec_())

