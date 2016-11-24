from collections import OrderedDict

from Column import Column

from DbErrors import DbNoConnection
from Model import Model


class Table(Model):

    def __init__(self, name: str, db, connection):
        super().__init__()
        self._name = name
        self.connection = connection
        self._db = db
        self._columns = OrderedDict()
        self.generate_size = 100

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
        self.columns[name] = Column(name, self, self.connection)
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

    def update(self):
        columns = self.list_columns()
        upd_cols = OrderedDict()
        for (col_name, _type, nullable, keytype, default, extra) in columns:
            if col_name in self._columns:
                upd_cols[col_name] = self.column(col_name)
            else:
                upd_cols[col_name] = Column(col_name, self, self.connection)
            upd_cols[col_name].update()
        self._columns = upd_cols

    def list_columns(self):
        if self.connection.db is None:
            raise DbNoConnection
        self.connection.cur.execute(r"USE {}".format(self.db.name))
        self.connection.cur.execute(
            r"SHOW COLUMNS FROM {}".format(self.name))
        data = self.connection.cur.fetchall()
        return data

    def wrap(self, value):
        if isinstance(value, str):
            return "'{}'".format(value)
        else:
            return str(value)

    def insert(self, vals):
        if self.connection.db is None:
            raise DbNoConnection
        vals_string = ', '.join(map(self.wrap, vals))
        self.connection.cur.execute(r"USE {}".format(self.db.test_db_name))
        self.connection.cur.execute(
            r"INSERT INTO {0} VALUES ({1})".format(self.name, vals_string))

    def create_test_table(self):
        if self.connection.db is None:
            raise DbNoConnection
        self.connection.cur.execute(r"USE {}".format(self.db.name))
        self.connection.cur.execute(
            r"SHOW CREATE TABLE {}".format(self.name))
        create_query = self.connection.cur.fetchone()[1]
        self.connection.cur.execute(r"USE {}".format(self.db.test_db_name))
        self.connection.cur.execute(create_query)

    def generate(self):
        self.create_test_table()
        for i in range(self.generate_size):
            vals = (column.generator.generate()
                    for column in self.columns.values())
            self.insert(vals)
