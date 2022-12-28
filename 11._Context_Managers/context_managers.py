

# coroutines

""" class Api:
    def do_this_first(self):
        return 'from 1. method'

    def do_this_second(self):
        return 'from 2. method'

    def do_this_third(self):
        return 'from 3. method'

    def run(self):
        self.do_this_first()
        self.do_this_second()
        self.do_this_third() """


""" x = Api()

def api():
    yield x.do_this_first()
    yield x.do_this_second()
    yield x.do_this_third()


y = api() """

""" print(next(y))
print(next(y))
print(next(y))
 """

""" 
def api():
    x = yield 'coroutine startet'
    yield x * x


x = api()
print(next(x))
# x.send(1)
print(x.send(1)) """


# Context managers

""" with open('11._Context_Managers/bohr.txt') as f:
    print(f.read()) """




from contextlib import contextmanager

class MyOpen():
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        f = open(self.filename)
        return f

    def __exit__(self, *args):
        f.close()


with MyOpen('bohr.txt') as f:
    print(f.readline())


@contextmanager
def genFunction():
    f = open('bohr.txt')
    yield f
    f.close()

with genFunction() as f:
    print(f.readline())
