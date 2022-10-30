from datetime import datetime
import time




def time_taker(func):
    def wrapper(*args):
        start = time.time()
        value = func(*args)
        end = time.time()
        print(f'Time it took {end - start}')
        return value
    return wrapper

@time_taker
def time_decorator(func):
    def inner(*args, **kwargs):
        f = open('log.txt', 'a')
        f.write(datetime.now().strftime("%c"))
        f.write(' : ')
        value = func(*args)
        f.write(str(value))
        f.write('\n')
        f.close

        return value
    return inner

@time_decorator
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


@time_decorator
def printer(text):
    return text


print(add(1, 2, 3))
print(printer('Silke'))
