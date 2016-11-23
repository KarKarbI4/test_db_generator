class IntegerColController:

    def __init__(self, model):
        self.model = model

    def seq_toggled(self, checked):
        self.model.generator.seq_toggled(checked)
        self.model.announce_update()

    def rand_toggled(self, checked):
        self.model.generator.rand_toggled(checked)
        self.model.announce_update()