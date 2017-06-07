import random
import string
import os
import random

class StringGenerator:

    dicts_path = "string_dicts"

    def __init__(self, col):
        self.col = col
        self.minlen = 5
        self.maxlen = 11
        self.dict = False
        self.rand = True
        self.dictionary = None
        self.dictionary_indx = None
        self.dict_list = []
        self.get_dicts()

    def clear(self):
        pass

    def get_dicts(self):
        self.dict_list = [file for file in os.listdir(
            self.dicts_path) if os.path.isfile(os.path.join(self.dicts_path, file))]
        if self.dict_list:
            self.dictionary = self.dict_list[0]
            self.dictionary_indx = 0

    def dict_toggled(self, checked):
        self.dict = checked
        self.rand = not self.dict

    def rand_toggled(self, checked):
        self.rand = checked
        self.dict = not self.rand

    def set_dict(self, indx):
        print("BEFORE SET")
        print("INDEX: {0}\nDICTIONARY: {1}".format(self.dictionary_indx, self.dictionary))
        print("LIST: {}".format(self.dict_list))
        self.dictionary_indx = indx
        self.dictionary = self.dict_list[self.dictionary_indx]
        print("BEFORE SET")
        print("INDEX: {0}\nDICTIONARY: {1}".format(self.dictionary_indx, self.dictionary))
        print("LIST: {}".format(self.dict_list))

    def generate_random(self):
        l = random.SystemRandom().randint(self.minlen, self.maxlen)
        return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(l))

    def generate_from_dict(self):
        print(self.dictionary)
        print(self.dictionary_indx)
        path = os.path.join(self.dicts_path, self.dictionary)
        with open(path) as f:
            n = int(f.readline().strip())
            rand_indx = random.randrange(n)
            for _ in range(rand_indx - 1):
                f.readline()
            return f.readline().strip()

    def generate(self):
        if self.rand:
            return self.generate_random()
        elif self.dict:
            return self.generate_from_dict()


if __name__ == '__main__':
    sg = StringGenerator(None)
    sg.dict_toggled(True)
    sg.set_dict(1)
    print(sg.generate())
    print(sg.generate())
    print(sg.generate())
