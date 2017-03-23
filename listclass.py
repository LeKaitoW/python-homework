class ListClass:
    def __init__(self, list):
        self.list = list

    def __setitem__(self, key, value):
        self.list[key - 1] = value

    def __getitem__(self, key):
        return self.list[key - 1]


list = ListClass([1, 2, 5, 6])
print(list.__getitem__(3))
list.__setitem__(3, 3)
print(list.list)
