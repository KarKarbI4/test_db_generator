from collections import OrderedDict


class Model:

    def __init__(self):
        self._upd_funcs = []

    # subscribe a view method for updating
    def sub_upd_func(self, func):
        if func not in self._upd_funcs:
            self._upd_funcs.append(func)

    # unsubscribe a view method for updating
    def unsub_upd_func(self, func):
        if func in self._upd_funcs:
            self._upd_funcs.remove(func)

    # update registered view methods
    def announce_update(self):
        for func in self._upd_funcs:
            func()
