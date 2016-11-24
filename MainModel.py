from collections import OrderedDict

from Model import Model
from Connection import Connection
from Database import Database
from DbErrors import DbNoConnection


class MainModel(Model):

    def __init__(self):
        super().__init__()
        self.connection = Connection()
        self._dbs = OrderedDict()

    def database(self, name: str):
        return self._dbs[name]

    @property
    def dbs(self):
        return self._dbs

    def list_dbs(self):
        if not self.connection.isConnected():
            raise DbNoConnection
        self.connection.cur.execute(r"SHOW DATABASES")
        data = self.connection.cur.fetchall()
        dbs = (x[0] for x in data)
        return dbs

    def update(self):
        upd_dbs = OrderedDict()
        db_names = self.list_dbs()
        for db_name in db_names:
            if db_name in self._dbs:
                upd_dbs[db_name] = self.database(db_name)
            else:
                upd_dbs[db_name] = Database(db_name, self, self.connection)
            upd_dbs[db_name].update()
        self._dbs = upd_dbs
