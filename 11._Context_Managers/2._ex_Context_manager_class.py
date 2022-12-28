
def decorator(func):
    def inner(*args):
        x = '<p>'
        x += func(*args)()
        x += '</p>'
        return x

    return inner


@decorator
class Makeparagraph():
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, *args, **kwds):
        return str(self.arg)


print(Makeparagraph("test"))

""" 
def decorator(func):
    def inner(*args):
        x = '<p>'
        x += str(func(*args))
        x += '</p>'
        return x

    return inner

@decorator
class Makeparagraph():
    def __init__(self, *args):
        self.text = args[0]

    def __enter__(self):
        return '<p>'

    def __exit__(self, *args):
        return '</p>'


with Makeparagraph("test") as f:
    print(f)
 """


""" class TextManager():
    def __init__(self, filename):
        print('3')
        self.filename = filename

    def __enter__(self):
        print('4')
        f = open(self.filename)
        return f

    def __exit__(self, *args):
        print('5')
        f.close()


with TextManager('test.tx') as f:
    print(f.readline())
 """
