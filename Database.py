from collections import OrderedDict

from PyQt5.QtCore import QObject, pyqtSignal

from Column import Column
from Table import Table

class Database(QObject):

    dataChanged = pyqtSignal()

    def __init__(self, name: str):
        super().__init__()
        self._name = name
        self._tables = OrderedDict()
        self._tables_to_gen = set(self._tables.keys())
        self._size = len(self._tables)

    @property
    def name(self):
        return self._name

    @property
    def tables(self) -> iter:
        return self._tables

    def tables_to_gen(self):
        return self._tables_to_gen

    def size(self):
        return self._size

    @changes_data
    def add_table(self, name: str):
        self.tables[name] = Table(name, self)
        return self.table(name)

    @changes_data
    def add_tables(self, names: iter):
        for name in names:
            self.add_table(name)

    def table(self, name):
        return self.tables[name]

    @changes_data
    def check_table(self, name):
        if name in self._tables.keys():
            self._tables_to_gen.add(name)

    def __repr__(self):
        tables = ''
        for table_name in self.tables.keys():
            tables += '\n\t{}'.format(self.table(table_name))
        return 'Database(name={0}, tables:{1})'.format(self.name, tables)

if __name__ == '__main__':
    db = Database('EasyDb')
    # table = Table('EasyTable', db)
    table = db.add_table('EasyTable')
    col = table.add_column('EasyColumn')
    print(db)
    print(table)
    print(col)
    print(type(db.tables))
