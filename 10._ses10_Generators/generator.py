
# callable
from time import sleep


class MyClass:
    def __call__(self):
        return 'From MyClass´s call method'


my_function = MyClass()

# checks if the function is callable
# print(callable(my_function))

# print(my_function())


# compute

""" 
def compute():
    li = []
    for i in range(10):
        sleep(.5)
        li.append(i)
    return li


print(compute()) """


# iter() - next()

""" class Compute:
    def __call__(self):
        return iter(self)

    # Iterarer igennem det valgte objekt
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        if self.last > 9:
            raise StopIteration
        self.last += 1
        return self.last


compute = Compute()

for i in compute :
    print(i) """


# Generator funktion

def compute():
    for i in range(10):
        yield i


it = compute()

print(next(it))


# Generator expression

print((i for i in range(10)))






