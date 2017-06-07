from Generator import RandomGeneratorMixin

class IntegerGenerator(RandomGeneratorMixin):
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
        self.gen_rand = None
        self.unique = False
        self.clear()

    def get_allvalues(self):
        vals = (self.maxvalue - self.minvalue)
        return [x for x in range(vals)]

    def seq_toggled(self, checked):
        self.seq = checked
        self.rand = not self.seq

    def rand_toggled(self, checked):
        self.rand = checked
        self.seq = not self.rand

    def generate_seq(self):
        while True:
            start = self.minvalue
            end = self.maxvalue + 1
            if self.seq_step < 0:
                start = self.maxvalue
                end = self.minvalue - 1
            for x in range(start, end, self.seq_step):
                yield x

    def init_gen(self):
        self.gen_seq = self.generate_seq()

    def generate(self):
        if self.seq:
            if not self.gen_seq:
                self.gen_seq = self.generate_seq()
            return next(self.gen_seq)
        elif bool(self.rand):
            if not self.gen_rand:
                self.gen_rand = self.generate_random()
            return next(self.gen_rand)

if __name__ == '__main__':
    ig = IntegerGenerator(None)
    gen = ig.generate()
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
