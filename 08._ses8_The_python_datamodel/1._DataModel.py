li = [1, 2, 3, 4]
num = [5, 6, 7]

len(li)

id(li)

li + num

li * 3

li[1:3]

# __functions__
# __ betyder privat

# Human class
class Human:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.height = args[2]

    # repr bruges til udviklere til at se objectet
    def __repr__(self):
        return f'{vars(self)}'

    # str bruges til at printe objectet ud pænt for brugere    
    def __str__(self):
        return f'Human: {self.name}, {self.age} and {self.height}'

    def __len__(self):
        return self.height

    # Hvis man skriver man + woman, så bruger den __add__
    def __add__(self, other):
        return Human(self.name + other.name, self.age + other.age, self.height + other.height)
    
    # hvis man skriver man * 3, så bruger den __mul__
    def __mul__(self, value):
        return self.height * value

man = Human("Rasmus", 29, 186)
woman = Human("Rasmine", 28, 172)

# print(repr(man))

# print(str(man))

# print(len(man))

# print(man + woman)

# print(man * 3)
