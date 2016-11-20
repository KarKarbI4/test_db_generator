from collections import OrderedDict

from DbErrors import DbNoConnection
from Model import Model

class Column(Model):

    def __init__(self, name: str, table, connection):
        self.connection = connection
        self._name = name
        self._table = table
        self.type = None
        self.nullable = False
        self.keytype = None
        self.default = None
        self.extra = ''

    @property
    def name(self) -> str:
        return self._name

    @property
    def table(self):
        return self._table

    def __repr__(self):
        return 'Column(name={})'.format(self.name)

    def update(self):
        if self.connection.db is None:
            raise DbNoConnection
        self.connection.cur.execute(
            r"SHOW COLUMNS FROM {0} FROM {1} WHERE Field='{2}'".format(self.table.name, self.table.db.name, self.name))
        data = self.connection.cur.fetchone()
        self.type = data[1]
        self.nullable = data[2]
        self.keytype = data[3]
        self.default = data[4]
        self.extra = data[5]
