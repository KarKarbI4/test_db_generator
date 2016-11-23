class TableController:

    def __init__(self, model):
        self.model = model

    def change_value(self, value):
        self.model.generate_size = value
        self.model.announce_update()