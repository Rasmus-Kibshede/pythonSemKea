
def averager(*args):
    sum = 0
    for i in args:
        sum += i
    return sum/len(args)


print(averager(10, 2))


def averager():
    sum = 0
    count = 0
    avg = None
    while True:
        term = yield avg
        sum += term
        count +=1
        avg = sum / count


a = averager()
next(a)
a.send(10)
print(a.send(2))
