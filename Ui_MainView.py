# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainView.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName("MainView")
        MainView.setEnabled(True)
        MainView.resize(635, 501)
        MainView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainView.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainView.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainView)
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
        MainView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainView)
        self.statusbar.setObjectName("statusbar")
        MainView.setStatusBar(self.statusbar)
        self.treeDockWidget = QtWidgets.QDockWidget(MainView)
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
        MainView.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.treeDockWidget)
        self.actionClose = QtWidgets.QAction(MainView)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_2 = QtWidgets.QAction(MainView)
        self.actionClose_2.setObjectName("actionClose_2")
        self.menuFile.addAction(self.actionClose_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainView)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        _translate = QtCore.QCoreApplication.translate
        MainView.setWindowTitle(_translate("MainView", "Test Database Generator"))
        self.menuFile.setTitle(_translate("MainView", "File"))
        self.treeDockWidget.setWindowTitle(_translate("MainView", "Database Tree"))
        self.schemaTreeWidget.headerItem().setText(0, _translate("MainView", "Schemas"))
        self.actionClose.setText(_translate("MainView", "Close"))
        self.actionClose_2.setText(_translate("MainView", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainView = QtWidgets.QMainWindow()
    ui = Ui_MainView()
    ui.setupUi(MainView)
    MainView.show()
    sys.exit(app.exec_())

