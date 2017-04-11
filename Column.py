import string

from DbErrors import DbNoConnection
from IntegerGenerator import IntegerGenerator
from Model import Model
from StringGenerator import StringGenerator


class Column(Model):

    def __init__(self, name: str, table, connection):
        super().__init__()
        self.connection = connection
        self._name = name
        self._table = table
        self.type = None
        self.nullable = False
        self.keytype = None
        self.default = None
        self.extra = ''
        self.generator = None
        self.rtype = None
        self.init_gen()

    def init_gen(self):
        if not self.type:
            return
        integer_types = ('bit', 'tinyint', 'smallint',
                         'mediumint', 'int', 'integer', 'bigint')
        for _type in integer_types:
            if _type in self.type.lower():
                self.generator = IntegerGenerator(self)
                self.rtype = 'int'
                break

        string_types = ('char', 'varchar', 'tinytext', 'text',
                        'mediumtext', 'longtext', 'binary', 'varbinary')

        for _type in string_types:
            if _type in self.type.lower():
                self.generator = StringGenerator(self)
                self.rtype = 'string'
                break

        # print("Database: {0}.\n Table: {1}. \n Column: {2}. \n Generator: {3}.".format(
        #     self.table.db.name, self.table.name, self.name, self.generator))


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
        query = r"SHOW COLUMNS FROM `{0}` FROM `{1}` WHERE Field='{2}'".format(self.table.name, self.table.db.name, self.name)
        # print("Column: {0}. Query: {1}".format(self.name, query))
        self.connection.cur.execute(query)
        data = self.connection.cur.fetchone()
        self.type = data[1]
        self.nullable = data[2]
        self.keytype = data[3]
        self.default = data[4]
        self.extra = data[5]
        self.init_gen()
