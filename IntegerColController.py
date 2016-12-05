class IntegerColController:

    def __init__(self, model):
        self.model = model

    def seq_toggled(self, checked):
        self.model.generator.seq_toggled(checked)
        self.model.announce_update()

    def rand_toggled(self, checked):
        self.model.generator.rand_toggled(checked)
        self.model.announce_update()

    def change_minvalue(self, value):
        self.model.generator.minvalue = value
        self.model.announce_update()

    def change_maxvalue(self, value):
        self.model.generator.maxvalue = value
        self.model.announce_update()

    def change_stepvalue(self, value):
        self.model.generator.seq_step = value
        self.model.announce_update()
