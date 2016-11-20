from DbErrors import DbConnectionError

class MainController():

    def __init__(self, model):
        self.model = model

    # called from view class
    def change_driver(self, drivername):
        # put control logic here
        self.model.connection._drivername = drivername
        self.model.connection.announce_update()

    def change_host(self, host):
        self.model.connection._host = host
        self.model.connection.announce_update()

    def change_port(self, port):
        self.model.connection._port = port
        self.model.connection.announce_update()

    def change_user(self, user):
        self.model.connection._user = user
        self.model.connection.announce_update()

    def change_password(self, password):
        self.model.connection._password = password
        self.model.connection.announce_update()

    def connect(self):
        try:
            self.model.connection.db = self.model.connection.driver.connect(
                host=self.model.connection.host, port=self.model.connection.port, user=self.model.connection.user, passwd=self.model.connection.password)
            self.model.connection.cur = self.model.connection.db.cursor()
            self.model.update()
        except self.model.connection.driver.err.OperationalError:
            raise DbConnectionError
        self.model.announce_update()
        print('Successfully connected.')

    def disconnect(self):
        if self.model.connection.isConnected():
            self.model.connection.db.close()
        self.model.announce_update()
