from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem
from PyQt5.QtWidgets import QWidget

from Ui_GeneratorWindow import Ui_GeneratorWindow
from SessionWindow import SessionWindow
from DatabaseWidget import DatabaseWidget
from TablePreviewWidget import TablePreviewWidget


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

    def __init__(self, database, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database = database
        self.widget = DatabaseWidget(self.database)
        for table in self.database.tables.values():
            self.addChild(SchemaTreeTable(table, table.name))

    isDatabase = lambda self: True


class SchemaTreeTable(SchemaTreeItem):

    def __init__(self, table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table = table
        self.widget = TablePreviewWidget(self.table)
        for column in self.table.columns.values():
            self.addChild(SchemaTreeColumn(column, column.name))

    isTable = lambda self: True


class SchemaTreeColumn(SchemaTreeItem):

    def __init__(self, column, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column = column

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
        try:
            self.add_tab(item.widget, item.text())
        except AttributeError:
            pass

    def add_tab(self, tab_widget: QWidget, tab_text):
        for indx in range(self.ui.tabWidget.count()):
            if self.ui.tabWidget.tabText(indx) == tab_text:
                self.ui.tabWidget.setCurrentIndex(indx)
                return None
        # tab_widget.setProperty('full_name', )
        self.ui.tabWidget.addTab(tab_widget, tab_text)

    def build_schema_tree(self):
        dbs = self.dbgen.dbs
        db_items = [SchemaTreeDatabase(
            db, db.name, parent=self.ui.schemaTreeWidget) for db in dbs.values()]
