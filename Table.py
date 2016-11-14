from collections import OrderedDict

from Column import Column


class Table:

    def __init__(self, name: str, db):
        self._name = name
        self._db = db
        self._columns = OrderedDict()

    @property
    def name(self) -> str:
        return self._name

    @property
    def db(self):
        return self._db

    @property
    def columns(self) -> str:
        return self._columns

    def add_column(self, name: str):
        self.columns[name] = Column(name, self)
        return self.column(name)

    def add_columns(self, names: iter) -> None:
        for name in names:
            self.add_columns(name)

    def column(self, name: str):
        return self.columns[name]

    def __repr__(self):
        cols = ''
        for col in self.columns.keys():
            cols += '\n\t{}'.format(self.column(col))
        return 'Table(name={0}, columns:{1})'.format(self.name, cols)