
class FloatGenerator:
    distributions = ('uniform', 'normal')

    def __init__(self, col):
        self.col = col
        self.minvalue = 0
        self.maxvalue = 100
        self.seq_step = 1
        self.seq = True
        self.rand = False
        self.distribution = 'uniform'
        self.gen_seq = None

    def seq_toggled(self, checked):
        self.seq = checked
        self.rand = not self.seq

    def rand_toggled(self, checked):
        self.rand = checked
        self.seq = not self.rand

    def generate_seq(self):
        while True:
            x = self.maxvalue if self.seq_step < 0 else self.minvalue
            cond = lambda x: x > self.minvalue if self.seq_step < 0 else lambda x: x < self.maxvalue
            while cond(x):
                yield x
                x += self.seq_step

    def init_gen(self):
        self.gen_seq = self.generate_seq()

    def generate(self):
        if self.seq:
            if not self.gen_seq:
                self.gen_seq = self.generate_seq()
            return next(self.gen_seq)
        elif self.rand:
            print('Random float generation not implemented yet')
            return 0

if __name__ == '__main__':
    ig = FloatGenerator(None)
    gen = ig.generate()
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
