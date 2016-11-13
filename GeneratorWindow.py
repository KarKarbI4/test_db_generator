from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem

from Ui_GeneratorWindow import Ui_GeneratorWindow
from SessionWindow import SessionWindow
from DatabaseWidget import DatabaseWidget


class SchemaTreeItem(QTreeWidgetItem):

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setData(0, 0, text)

    isDatabase = lambda self: False
    isTable = lambda self: False
    isColumn = lambda self: False

    def text(self):
        return super().text(0)


class SchemaTreeDatabase(SchemaTreeItem):

    def __init__(self, *args):
        super().__init__(*args)
        self.widget = DatabaseWidget

    isDatabase = lambda self: True


class SchemaTreeTable(SchemaTreeItem):

    def __init__(self, *args):
        super().__init__(*args)

    isTable = lambda self: True


class SchemaTreeColumn(SchemaTreeItem):

    def __init__(self, *args):
        super().__init__(*args)

    isColumn = lambda self: True


class GeneratorWindow(QMainWindow):

    def __init__(self, dbgen, parent=None):
        super().__init__()
        self.ui = Ui_GeneratorWindow()
        self.ui.setupUi(self)
        self.dbgen = dbgen
        self.session_manager = SessionWindow(self.dbgen, parent=self)
        self.setup()

    def setup(self):
        self.session_manager.connected.connect(self.session_manager_connected)
        self.ui.schemaTreeWidget.itemDoubleClicked.connect(self.item_selected)
        self.ui.tabWidget.tabCloseRequested.connect(self.tab_close_request)
        self.open_session_manager()

    def tab_close_request(self, tab_index):
        self.ui.tabWidget.removeTab(tab_index)

    def session_manager_connected(self):
        self.session_manager.close()
        self.build_schema_tree()

    def open_session_manager(self):
        self.session_manager.show()

    def closeEvent(self, event):
        if self.dbgen:
            self.dbgen.close()
        event.accept()

    def item_selected(self, item, column_no):
        print('Item: {0}, Column no: {1}'.format(item, column_no))
        print('Item isDatabase: {0}\nItem isTable: {1}\nItem isColumn: {2}'.format(
            item.isDatabase(), item.isTable(), item.isColumn()))
        if item.isDatabase():
            self.ui.tabWidget.addTab(item.widget(self), item.text())

    def build_schema_tree(self):
        dbs = self.dbgen.list_dbs()
        db_items = [SchemaTreeDatabase(x) for x in dbs]

        for dbs_item in db_items:
            tables = self.dbgen.list_tables(dbs_item.text())

            table_items = [SchemaTreeTable(x) for x in tables]

            for table_item in table_items:
                columns = [x[0] for x in self.dbgen.list_columns(
                    dbs_item.text(), table_item.text())]
                column_items = [SchemaTreeColumn(x) for x in columns]

                table_item.addChildren(column_items)
            dbs_item.addChildren(table_items)
        self.ui.schemaTreeWidget.addTopLevelItems(db_items)
