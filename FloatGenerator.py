from Generator import RandomGeneratorMixin
import random
class FloatGenerator(RandomGeneratorMixin):
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
        self.clear()
        self.unique = False

    def get_allvalues(self):
        return set()

    def generate_random(self):
        if self.distribution == 'uniform':
            while True:
                gen_value = random.uniform(self.minvalue, self.maxvalue)
                if self.unique:
                    while gen_value in self.allvalues:
                        gen_value = random.uniform(self.minvalue, self.maxvalue)
                    self.allvalues.append(gen_value)
                yield gen_value


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
        elif bool(self.rand):
            if not self.gen_rand:
                self.gen_rand = self.generate_random()
            return next(self.gen_rand)

if __name__ == '__main__':
    ig = FloatGenerator(None)
    ig.rand_toggled(True)
    gen = ig.generate()
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
