from datetime import timedelta, date, time, datetime

import random

from Generator import RandomGeneratorMixin

class DateGenerator(RandomGeneratorMixin):
    distributions = ('uniform', 'normal')

    def __init__(self, col):
        self.col = col
        self.seq_step = 5
        self.seq = False
        self.rand = True
        self.distribution = 'uniform'
        self.gen_seq = None
        self.fmt = '%d.%m.%Y'
        self.db_fmt = '%Y-%m-%d'
        self.minvalue = datetime(year=2000, month=1, day=1)
        self.maxvalue = datetime.now()
        self.generated_values = set()
        self.unique = False
        self.clear()


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
            step = timedelta(days=self.seq_step)
            while cond(x):
                yield x.date().strftime(self.db_fmt)
                x += step

    def init_gen(self):
        self.gen_seq = self.generate_seq()


    def get_allvalues(self):
        days = (self.maxvalue - self.minvalue).days
        return [x for x in range(days)]

    def generate_random(self):
        if self.distribution == 'uniform':
            while True:
                gen_value = random.choice(self.allvalues)
                if self.unique:
                    self.allvalues.remove(gen_value)

                yield (self.minvalue + timedelta(days=gen_value)).strftime(self.db_fmt)

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
    ig = DateGenerator(None)
    gen = ig.generate()
    print(gen)
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
