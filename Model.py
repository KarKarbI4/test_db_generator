from collections import OrderedDict

from Connection import Connection


class Model:

    def __init__(self):
        self.connection = Connection()
        self.dbs = dict()
        self._upd_funcs = []

    # subscribe a view method for updating
    def sub_upd_func(self, func):
        if func not in self._upd_funcs:
            self._upd_funcs.append(func)

    # unsubscribe a view method for updating
    def unsub_upd_func(self, func):
        if func in self._upd_funcs:
            self._upd_funcs.remove(func)

    # update registered view methods
    def announce_update(self):
        for func in self._upd_funcs:
            func()

    # def database(self, name: str):
    #     return self.dbs[name]

    # def add_db(self, name: str):
    #     self.dbs[name] = Database(name)
    #     return self.database(name)

    # def add_dbs(self, names: iter):
    #     for name in names:
    #         self.add_db(name)

    # def list_dbs(self):
    #     if self.db is None:
    #         raise DbNoConnection
    #     self.cur.execute(r"SHOW DATABASES")
    #     data = self.cur.fetchall()
    #     dbs = (x[0] for x in data)
    #     return dbs

    # def list_tables(self, dbname: str):
    #     if self.db is None:
    #         raise DbNoConnection
    #     self.cur.execute(r"SHOW TABLES FROM {}".format(dbname))
    #     data = self.cur.fetchall()
    #     tables = (x[0] for x in data)
    #     return tables

    # def list_columns(self, dbname: str, tablename: str):
    #     if self.db is None:
    #         raise DbNoConnection
    #     self.cur.execute(r"USE {}".format(dbname))
    #     self.cur.execute(r"SHOW COLUMNS FROM {}".format(tablename))
    #     data = self.cur.fetchall()
    #     # for row in data:
    #     # col = Column()
    #     return data

    # def update(self):
    #     self.dbs = OrderedDict()
    #     db_names = self.list_dbs()
    #     for db_name in db_names:
    #         db = self.add_db(db_name)
    #         tables = self.list_tables(db.name)
    #         for table_name in tables:
    #             table = db.add_table(table_name)
    #             columns = self.list_columns(db.name, table.name)
    #             for (col_name, _type, nullable, keytype, default, extra) in columns:
    #                 col = table.add_column(col_name)
    #                 col.type = _type
    #                 col.nullable = nullable
    #                 col.keytype = keytype
    #                 col.default = default
    #                 col.extra = extra
