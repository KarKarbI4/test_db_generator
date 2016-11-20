
import pymysql

from Model import Model

drivers = {
    'MySQL': (pymysql, 3306),
}


class Connection(Model):

    def __init__(self):
        super().__init__()
        self._drivername = 'MySQL'
        self._driver = drivers[self.drivername][0]
        self._host = '127.0.0.1'
        self._port = drivers[self.drivername][1]
        self._user = 'root'
        self._password = ''
        self.db = None
        self.cur = None

    def isConnected(self):
        return self.db is not None

    def get_drivers(self):
        return list(drivers.keys())

    @property
    def driver(self):
        return self._driver

    @property
    def drivername(self) -> str:
        return self._drivername

    @drivername.setter
    def drivername(self, drivername: str):
        self._drivername = drivername

    @property
    def host(self) -> str:
        return self._host

    @host.setter
    def host(self, host: str):
        self._host = host

    @property
    def port(self) -> int:
        return self._port

    @port.setter
    def port(self, port: int):
        self._port = port

    @property
    def user(self) -> str:
        return self._user

    @user.setter
    def user(self, user: str):
        self._user = user

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password
