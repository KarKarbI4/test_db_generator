
class DatabaseController:

    def __init__(self, model):
        self.model = model

    def generate(self):
        self.model.generate()
        self.model.main.update()
        self.model.main.announce_update()
