from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from Ui_TablePreviewWidget import Ui_TablePreviewWidget
# from DatabaseGenerator import DatabaseGenerator, DbConnectionError


class TablePreviewWidget(QWidget):

    def __init__(self, table, parent=None):
        super().__init__(parent)
        self.ui = Ui_TablePreviewWidget()
        self.ui.setupUi(self)
        self.table = table
        self.setup()

    def setup(self):
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(len(self.table.columns))
        self.ui.tableWidget.setHorizontalHeaderLabels(['Field', 'Type', 'Null', 'Key', 'Default', 'Extra'])

        for indx, col in enumerate(self.table.columns.values()):
            self.ui.tableWidget.setItem(indx, 0, QTableWidgetItem(col.name))
            self.ui.tableWidget.setItem(indx, 1, QTableWidgetItem(col.type))
            self.ui.tableWidget.setItem(indx, 2, QTableWidgetItem(col.nullable))
            self.ui.tableWidget.setItem(indx, 3, QTableWidgetItem(col.keytype))
            self.ui.tableWidget.setItem(indx, 4, QTableWidgetItem(col.default))
            self.ui.tableWidget.setItem(indx, 5, QTableWidgetItem(col.extra))
