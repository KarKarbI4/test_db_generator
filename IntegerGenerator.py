
class IntegerGenerator:
    distributions = ('uniform', 'normal')

    def __init__(self, col):
        self.col = col
        self.minvalue = 0
        self.maxvalue = 100
        self.seq_step = 1
        self.seq = True
        self.rand = False
        self.distribution = 'uniform'

    def seq_toggled(self, checked):
        self.seq = checked
        self.rand = not self.seq
    
    def rand_toggled(self, checked):
        self.rand = checked
        self.seq = not self.rand
