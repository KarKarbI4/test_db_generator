from PyQt5.QtWidgets import QMainWindow, QWidget

from DatabaseController import DatabaseController
from DatabaseWidget import DatabaseWidget
from IntegerColController import IntegerColController
from IntegerSettingsWidget import IntegerSettingsWidget
from SchemaTreeItems import SchemaTreeDatabase, SchemaTreeItem
from SessionWindow import SessionWindow
from StringColController import StringColController
from StringSettingsWidget import StringSettingsWidget
from TableController import TableController
from TablePreviewWidget import TablePreviewWidget
from TableContentViewWidget import TableContentViewWidget
from Ui_MainView import Ui_MainView
from FloatSettingsWidget import FloatSettingsWidget
from DateSettingsWidget import DateSettingsWidget

map_type_widget = {
    'int': (IntegerSettingsWidget, IntegerColController),
    'float': (FloatSettingsWidget, IntegerColController),
    'string': (StringSettingsWidget, StringColController),
    'date': (DateSettingsWidget, IntegerColController),
}

class MainView(QMainWindow):

    schema_tree = property()

    @schema_tree.setter
    def schema_tree(self, items):
        self.ui.schemaTreeWidget.clear()
        self.ui.schemaTreeWidget.insertTopLevelItems(0, items)

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        super().__init__()
        self.build_ui()

        self.model.sub_upd_func(self.upd_ui_from_model)

    def build_ui(self):
        self.ui = Ui_MainView()
        self.ui.setupUi(self)
        self.session_manager = SessionWindow(
            self.model.connection, self.controller)
        self.session_manager.show()
        # connections
        self.ui.tabWidget.tabCloseRequested.connect(self.on_tab_close_request)
        self.session_manager.connected.connect(self.on_connect)
        self.ui.schemaTreeWidget.itemDoubleClicked.connect(
            self.on_schema_tree_item_double_clicked)

    def upd_ui_from_model(self):
        if self.model.connection.isConnected():
            self.schema_tree = [SchemaTreeDatabase(
                db, db.name) for db in self.model.dbs.values()]

    def add_tab(self, tab_widget: QWidget, tab_text: str):
        for indx in range(self.ui.tabWidget.count()):
            if self.ui.tabWidget.tabText(indx) == tab_text:
                self.ui.tabWidget.setCurrentIndex(indx)
                return None
        self.ui.tabWidget.addTab(tab_widget, tab_text)

    def add_db_widget(self, db):
        new_widget = DatabaseWidget(db, DatabaseController(db))
        new_widget.item_dclicked.connect(
            self.on_db_widget_item_dclicked)
        self.add_tab(new_widget, db.name)

    def add_table_widget(self, table):
        preview_widget = TablePreviewWidget(table, TableController(table))
        content_widget = TableContentViewWidget(table, TableController(table))
        self.add_tab(preview_widget, table.name)
        self.add_tab(content_widget, "{} content".format(table.name))

    def add_col_widget(self, column):
        widget_type, controller_type = map_type_widget.get(column.rtype, (None, None))
        new_widget = widget_type(
            column, controller_type(column))
        self.add_tab(new_widget, '{0}.{1}'.format(
            column.table.name, column.name))

    def on_db_widget_item_dclicked(self, table):
        self.add_table_widget(table)

    def on_connect(self):
        if self.model.connection.isConnected() and self.session_manager.isVisible():
            self.session_manager.close()

    def on_tab_close_request(self, tab_index):
        self.ui.tabWidget.removeTab(tab_index)

    def on_schema_tree_item_double_clicked(self, item, col):
        if item.isDatabase():
            self.add_db_widget(item.database)
        elif item.isTable():
            self.add_table_widget(item.table)
        elif item.isColumn():
            self.add_col_widget(item.column)
