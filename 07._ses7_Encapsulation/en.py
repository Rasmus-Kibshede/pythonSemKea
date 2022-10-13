

from ast import alias


class P:
    def __init__(self, name, alias):
        self.name = name # public variable -> propetry
        self.alias = alias

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            print('no no no')


p = P("Rasmus", "Ralle")
print(p.name)
