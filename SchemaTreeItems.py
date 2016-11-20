from PyQt5.QtWidgets import QTreeWidgetItem

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
        # self.widget = DatabaseWidget(self.database)
        for table in self.database.tables.values():
            self.addChild(SchemaTreeTable(table, table.name))

    isDatabase = lambda self: True


class SchemaTreeTable(SchemaTreeItem):

    def __init__(self, table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table = table
        # self.widget = TablePreviewWidget(self.table)
        for column in self.table.columns.values():
            self.addChild(SchemaTreeColumn(column, column.name))

    isTable = lambda self: True


class SchemaTreeColumn(SchemaTreeItem):

    def __init__(self, column, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.column = column

    isColumn = lambda self: True
