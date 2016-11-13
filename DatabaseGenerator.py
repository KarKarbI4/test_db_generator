#!/usr/bin/python3
import pymysql


class Error(Exception):
    pass


class DbConnectionError(Error):

    def __init__(self, message=''):
        super().__init__()
        self.message = message


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
        self.conn = None

    def connect(self, drivername, host, user, password, port):
        self.driver = self.drivers[drivername][0]
        try:
            self.conn = self.driver.connect(
                host=host, port=port, user=user, passwd=password)
        except self.driver.err.OperationalError:
            raise ConnectionError
        print('Successfully connected.')
