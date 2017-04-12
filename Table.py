import re
import random
from collections import OrderedDict, namedtuple
from contextlib import closing

from Column import Column
from DbErrors import DbNoConnection
from Model import Model

ForeignKey = namedtuple("ForeignKey", ('name', 'origin_table', 'origin_col', 'target_table', 'target_col'))

class Table(Model):

    fk_regex = "CONSTRAINT\s*`(.*)`\s*FOREIGN\s*KEY\s*\(`(.*)`\)\s* REFERENCES\s*`(.*)`\s*\(`(.*)`\)"
    fk_regex = re.compile(fk_regex)

    def __init__(self, name: str, db, connection):
        super().__init__()
        self._name = name
        self.connection = connection
        self._db = db
        self._columns = OrderedDict()
        self.generate_size = 100
        self.show_limit = 100
        self.pkeys = set()
        self.fkeys = set()
        self.fkey_cols = set()
        self.cols_fkeys = dict()

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
            self.add_column(name)

    def column(self, name: str):
        return self.columns[name]

    def __repr__(self):
        cols = ''
        for col in self.columns.keys():
            cols += '\n\t{}'.format(self.column(col))
        return 'Table(name={0}, columns:{1})'.format(self.name, cols)

    @property
    def content(self):
        query = r"SELECT * FROM `{}` LIMIT {}".format(
            self.name, self.show_limit)
        self.make_query(query)
        data = self.connection.cur.fetchall()
        return data

    def make_query(self, query): 
        if self.connection.db is None:
            raise DbNoConnection
        self.connection.cur.execute(r"USE `{}`".format(self.db.name))
        print("Table: {0}. Query: {1}".format(self.name, query))
        self.connection.cur.execute(query)

    def make_gen_query(self, query):
        if self.connection.db is None:
                raise DbNoConnection
        print("Table: {0}. Query: {1}".format(self.name, query))
        self.connection.cur.execute(r"USE `{}`".format(self.db.test_db_name))
        self.connection.cur.execute(query)

    def get_count(self):
        query = "SELECT COUNT(*) FROM `{0}`".format(self.name)
        print("Table: {0}. Query: {1}".format(self.name, query))
        with closing(self.connection.db.cursor()) as cur:
            cur.execute('SET NAMES utf8;')
            cur.execute('SET CHARACTER SET utf8;')
            cur.execute(
                'SET character_set_connection=utf8;')

            cur.execute(r"USE `{}`".format(self.db.test_db_name))
            cur.execute(query)
            return cur.fetchone()[0]

    def get_nth_col_value(self, n, col_name):
        query = "SELECT `{0}` FROM `{1}`".format(col_name, self.name)
        print("Table: {0}. Query: {1}".format(self.name, query))
        with closing(self.connection.db.cursor()) as cur:
            cur.execute('SET NAMES utf8;')
            cur.execute('SET CHARACTER SET utf8;')
            cur.execute(
                'SET character_set_connection=utf8;')
            cur.execute(r"USE `{}`".format(self.db.test_db_name))
            cur.execute(query)
            for i in range(n + 1):
                res = cur.fetchone()
            return res[0]

    def get_random_col_value(self, col_name):
        count = self.get_count()
        num = random.randrange(count)
        return self.get_nth_col_value(num, col_name)

    def get_col_vals(self, col_name):
        query = "SELECT `{0}` FROM `{1}`".format(col_name, self.name)
        self.make_gen_query(query)
        self.connection.cur.fetchall()

    def get_fkey_cols(self):
        for fkey in self.fkeys:
            self.fkey_cols.add(self.columns[fkey.origin_col].name)
            self.cols_fkeys[self.columns[fkey.origin_col].name] = fkey

    def get_pkeys(self):
        self.pkeys.clear()
        for col in self.columns.values():
            if col.keytype == "PRI":
                self.pkeys.add(col.name)

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

        self.get_pkeys()
        self.get_fkeys()
        self.get_fkey_cols()

        print("Fkeys: {}".format(self.fkeys))
        print("Fkey cols: {}".format(self.fkey_cols))

    def list_columns(self):
        query = r"SHOW COLUMNS FROM `{}`".format(self.name)
        self.make_query(query)
        data = self.connection.cur.fetchall()
        return data

    def wrap(self, value):
        if isinstance(value, str):
            return "'{}'".format(value)
        elif value is None:
            return "NULL"
        else:
            return str(value)

    def insert(self, vals):
        vals_string = ', '.join(map(self.wrap, vals))
        if self.connection.db is None:
            raise DbNoConnection
        self.connection.cur.execute(r"USE `{}`".format(self.db.test_db_name))
        query = "INSERT INTO `{0}` VALUES ({1})".format(self.name, vals_string)
        self.connection.cur.execute(
            "INSERT INTO `{0}` VALUES ({1})".format(self.name, vals_string))
        print("Table: {0}. Query: {1}".format(self.name, query))
        

    def update_table_fkeys(self):
        count = self.get_count()
        print("COUNT {0}".format(count))
        query = "SELECT * FROM {}".format(self.name)
        self.make_gen_query(query)
        query = "UPDATE `{0}` SET {1} WHERE {2}"
        upd_query_list = []
        for i in range(count):
            set_q = []
            where_q = []
            tup = self.connection.cur.fetchone()
            for i, col in enumerate(self.columns.values()):
                if col.name in self.fkey_cols:
                    fkey = self.cols_fkeys[col.name]
                    value = self.db.tables[fkey.target_table].get_random_col_value(fkey.target_col)
                    set_q.append("`{0}`={1}".format(col.name, self.wrap(value)))
                elif col.name in self.pkeys:
                    where_q.append("`{0}`={1}".format(col.name, self.wrap(tup[i])))
            upd_query_list.append(query.format(self.name, ', '.join(set_q), ' AND '.join(where_q)))
        for query in upd_query_list:
            self.make_gen_query(query)

    def create_table_script(self):
        self.make_query(
            r"SHOW CREATE TABLE `{}`".format(self.name))
        create_query = self.connection.cur.fetchone()[1]
        return create_query

    def create_test_table(self):
        self.make_gen_query(self.create_table_script)

    def get_fkeys(self):
        self.fkeys.clear()
        self.make_query(r"SHOW CREATE TABLE `{}`".format(self.name))
        create_str = self.connection.cur.fetchone()[1]
        for m in re.finditer(self.fk_regex, create_str):
            groups =  m.groups()
            self.fkeys.add(ForeignKey(groups[0], self.name, groups[1], groups[2], groups[3]))

    def generate(self):
        for i in range(self.generate_size):
            vals = []
            for column in self.columns.values():
                if column.name not in self.fkey_cols:
                    vals.append(column.generator.generate())
                else:
                    vals.append(None)
            vals = tuple(vals)
            self.insert(vals)
