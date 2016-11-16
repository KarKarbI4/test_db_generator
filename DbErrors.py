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
