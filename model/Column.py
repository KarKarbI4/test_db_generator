from collections import OrderedDict


class Column:

    def __init__(self, name: str, table):
        self._name = name
        self._table = table
        self.type = None
        self.nullable = False
        self.keytype = None
        self.default = None
        self.extra = ''

    @property
    def name(self) -> str:
        return self._name

    @property
    def table(self):
        return self._table

    def __repr__(self):
        return 'Column(name={})'.format(self.name)
