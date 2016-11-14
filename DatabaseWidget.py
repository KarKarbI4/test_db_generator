from PyQt5.QtWidgets import QWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt
from Ui_DatabaseWidget import Ui_DatabaseWidget


class DatabaseWidget(QWidget):

    def __init__(self, tables, parent=None):
        super().__init__()
        self.ui = Ui_DatabaseWidget()
        self.ui.setupUi(self)
        self.tables = tables
        self.setup()

    def setup(self):
        parent = QTreeWidgetItem(self.ui.tablesTree)
        parent.setText(0, 'All')
        parent.setFlags(parent.flags() | Qt.ItemIsTristate |
                        Qt.ItemIsUserCheckable)
        for tablename in self.tables:
            table_item = QTreeWidgetItem(parent)
            table_item.setFlags(table_item.flags() | Qt.ItemIsUserCheckable)
            table_item.setText(0, tablename)
            table_item.setCheckState(0, Qt.Unchecked)
        parent.setCheckState(0, Qt.Checked)
        self.ui.tablesTree.expandAll()
