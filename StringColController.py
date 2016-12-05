class StringColController:

    def __init__(self, model):
        self.model = model

    def dict_toggled(self, checked):
        self.model.generator.dict_toggled(checked)
        self.model.announce_update()

    def rand_toggled(self, checked):
        self.model.generator.rand_toggled(checked)
        self.model.announce_update()

    def change_minlen(self, value):
        self.model.generator.minlen = value
        self.model.announce_update()


    def change_maxlen(self, value):
        self.model.generator.maxlen = value
        self.model.announce_update()

