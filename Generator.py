import random

class RandomGeneratorMixin:
    gen_rand = None

    def clear(self):
        self.allvalues = self.get_allvalues()


    def get_allvalues(self):
        allvalues = [x for x in range(100)]
        return allvalues

    def generate_random(self):
        if self.distribution == 'uniform':
            while True:
                gen_value = random.choice(self.allvalues)
                if self.unique:
                    self.allvalues.remove(gen_value)

                yield gen_value
