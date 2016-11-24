import random
import string

class StringGenerator:

    def __init__(self, col):
        self.col = col
        self.minlen = 5
        self.maxlen = 11
        self.dict = False
        self.rand = True

    def dict_toggled(self, checked):
        self.dict = checked
        self.rand = not self.dict

    def rand_toggled(self, checked):
        self.rand = checked
        self.seq = not self.rand

    def generate_random(self):
        l = random.SystemRandom().randint(self.minlen, self.maxlen)
        return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(l))

    def generate(self):
        if self.rand:
            return self.generate_random()

if __name__ == '__main__':
    sg = StringGenerator(None)
    print(sg.generate())
