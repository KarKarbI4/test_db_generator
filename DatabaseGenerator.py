#!/usr/bin/python3
import pymysql
from sqlalchemy import create_engine
from Database import Database
from Table import Table
from Column import Column

from collections import OrderedDict


class DbError(Exception):
    pass


class DbConnectionError(DbError):

    def __init__(self, message=''):
        super().__init__()
        self.message = message


class DbNoConnection(DbError):

    def __init__(self):
        super().__init__()
        self.message = "Trying to execute while no database connection were established"


class DatabaseGenerator:
    drivers = {
        'MySQL': (pymysql, 3306),
    }

    default_settings = {
        'driver': 'MySQL',
        'host': '127.0.0.1',
        'port': drivers['MySQL'][1],
        'user': 'root'
    }

    def __init__(self):
        self.driver = None
        self.db = None
        self.cur = None
        self.dbs = OrderedDict()

    def connect(self, drivername: str, host: str, user: str, password: str, port: int):
        self.driver = self.drivers[drivername][0]
        try:
            self.db = self.driver.connect(
                host=host, port=port, user=user, passwd=password)
            self.cur = self.db.cursor()
        except self.driver.err.OperationalError:
            raise DbConnectionError
        print('Successfully connected.')
        self.update()

    def update(self):
        self.dbs = OrderedDict()
        db_names = self.list_dbs()
        for db_name in db_names:
            db = self.add_db(db_name)
            tables = self.list_tables(db.name)
            for table_name in tables:
                table = db.add_table(table_name)
                columns = self.list_columns(db.name, table.name)
                for (col_name, _type, nullable, keytype, default, extra) in columns:
                    col = table.add_column(col_name)
                    col.type = _type
                    col.nullable = nullable
                    col.keytype = keytype
                    col.default = default
                    col.extra = extra

    def database(self, name: str) -> Database:
        return self.dbs[name]

    def add_db(self, name: str) -> Database:
        self.dbs[name] = Database(name)
        return self.database(name)

    def add_dbs(self, names: iter):
        for name in names:
            self.add_db(name)

    def list_dbs(self):
        if self.db is None:
            raise DbNoConnection
        self.cur.execute(r"SHOW DATABASES")
        data = self.cur.fetchall()
        dbs = (x[0] for x in data)
        return dbs

    def list_tables(self, dbname: str):
        if self.db is None:
            raise DbNoConnection
        self.cur.execute(r"SHOW TABLES FROM {}".format(dbname))
        data = self.cur.fetchall()
        tables = (x[0] for x in data)
        return tables

    def list_columns(self, dbname: str, tablename: str):
        if self.db is None:
            raise DbNoConnection
        self.cur.execute(r"USE {}".format(dbname))
        self.cur.execute(r"SHOW COLUMNS FROM {}".format(tablename))
        data = self.cur.fetchall()
        # for row in data:
        # col = Column()
        return data

    def close(self):
        if self.db:
            self.db.close()

if __name__ == '__main__':
    dbgen = DatabaseGenerator()
    drivername = DatabaseGenerator.default_settings['driver']
    host = DatabaseGenerator.default_settings['host']
    port = DatabaseGenerator.default_settings['port']
    user = DatabaseGenerator.default_settings['user']
    password = 'MephiMoscow533!'
    dbgen.connect(drivername, host, user, password, port)
    print(dbgen.list_dbs())
    print(dbgen.list_tables('sys'))
    print(dbgen.list_columns('test', 'TestTable'))
    dbgen.update()
    print(dbgen.database('test'))
    dbgen.close()
