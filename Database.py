from collections import OrderedDict
from typing import List
from Column import Column
from Table import Table
from Connection import Connection

from Model import Model
from DbErrors import DbNoConnection


class Database(Model):

    def __init__(self, name: str, main, connection: Connection):
        super().__init__()
        self._name = name
        self.main = main
        self.connection = connection
        self._tables = OrderedDict()
        self._tables_to_gen = set(self._tables.keys())
        self._size = len(self._tables)
        self.test_db_name = 'test_{}'.format(self.name)

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

    def table(self, name: str):
        return self.tables[name]

    def check_table(self, name: str):
        if name in self._tables.keys():
            self._tables_to_gen.add(name)
        else:
            raise KeyError

    def uncheck_table(self, name: str):
        if name in self._tables.keys():
            del self._tables_to_gen[name]

    def update(self):
        upd_tables = OrderedDict()
        table_names = self.list_tables()
        for table_name in table_names:
            if table_name in self._tables:
                upd_tables[table_name] = self.table(table_name)
            else:
                upd_tables[table_name] = Table(
                    table_name, self, self.connection)

            upd_tables[table_name].update()
        self._tables = upd_tables

    def list_tables(self):
        if self.connection.db is None:
            raise DbNoConnection
        self.connection.cur.execute(r"SHOW TABLES FROM {}".format(self.name))
        data = self.connection.cur.fetchall()
        tables = (x[0] for x in data)
        return tables

    def __repr__(self):
        tables = ''
        for table_name in self.tables.keys():
            tables += '\n\t{}'.format(self.table(table_name))
        return 'Database(name={0}, tables:{1})'.format(self.name, tables)

    def create_test_db(self):
        self.connection.cur.execute(r"CREATE DATABASE {}".format(self.test_db_name))

    def generate(self):
        self.create_test_db()
        for table in self.tables.values():
            table.generate()
        self.connection.db.commit()
