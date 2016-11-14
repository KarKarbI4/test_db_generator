from collections import OrderedDict

from Table import Table
from Column import Column


class Database:

    def __init__(self, name: str):
        self._name = name
        self._tables = OrderedDict()

    @property
    def name(self):
        return self._name

    @property
    def tables(self) -> iter:
        return self._tables

    def add_table(self, name: str):
        self.tables[name] = Table(name, self)
        return self.table(name)

    def add_tables(self, names: iter):
        for name in names:
            self.add_table(name)

    def table(self, name):
        return self.tables[name]

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
