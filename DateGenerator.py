from datetime import timedelta, date, time, datetime
class DateGenerator:
    distributions = ('uniform', 'normal')

    def __init__(self, col):
        self.col = col
        self.minvalue = '01.01.2010'
        self.seq_step = 5
        self.seq = True
        self.rand = False
        self.distribution = 'uniform'
        self.gen_seq = None
        self.fmt = '%d.%m.%Y'
        self.db_fmt = '%d.%m.%Y'
        self.maxvalue = datetime.today().strftime(self.fmt)


    def seq_toggled(self, checked):
        self.seq = checked
        self.rand = not self.seq

    def rand_toggled(self, checked):
        self.rand = checked
        self.seq = not self.rand

    def generate_seq(self):
        while True:
            start = datetime.strptime(self.minvalue, self.fmt)
            end = datetime.strptime(self.maxvalue, self.fmt)
            x = end if self.seq_step < 0 else start
            cond = lambda x: x > self.minvalue if self.seq_step < 0 else lambda x: x < self.maxvalue
            step = timedelta(days=self.seq_step)
            while cond(x):
                yield x.date()
                x += step

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
    ig = DateGenerator(None)
    gen = ig.generate()
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
    print(ig.generate())
