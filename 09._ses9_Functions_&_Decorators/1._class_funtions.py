
# first class funktioner i python kan tage andre funktioner som parameter -> func(func2)
""" 
def my_first_function(x):
    return x


print(my_first_function(len))


# Inner funktioner
def foo():



    def inner():
        print('Hello world')
    
    return inner

# En måde at få inner funktionen ud på
foo()()

# En anden måde at få inner funktionen ud på
x = foo()
x()



# Decorator funktioner

def my_decorator(x):
    def inner():
        print('Before function is called')
        x()
        print('After function is called')
    
    return inner

@my_decorator
def greet():
    print('Hello')

greet = my_decorator(greet)
greet() 
"""

# ---- kan også gøres på denne måde, som er mere clean
#@my_decorator
#def greet():
#    print('Hello')

#greet()


# En bedre måde at lave my_decorator på, da den KAN tage parameter med
""" def my_decorator(x):
    def inner(*args):
        print('Before function is called')
        x(*args)
        print('After function is called')
    
    return inner

@my_decorator
def greet(*args):
    if len(args) > 0:
        print(f'Hello {args[0]}')
    else:
        print('No args')

greet() """


def my_dec(func):

    def inner(*args, **kwargs):
        x = 'Hello from inner'
        x += func(*args)
        x += 'GOODBYE'
        return x

    return inner

@my_dec
def greet2(*args):
    return f'Hello from {args[0]}'

print(greet2('Silke'))
        





