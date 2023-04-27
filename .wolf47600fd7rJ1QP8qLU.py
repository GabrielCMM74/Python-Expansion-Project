# def hello():
#     print('hellooooooo')

# greet = hello
# del hello
# print(greet())

# def greet(func):
#     func()

# def greet2():
#     def func():
#         return 5
#     return func


#decorator 


def my_decorator(func):
    def wrap_func():
        print('******')
        func()
        print('******')
    return wrap_func

@my_decorator
def bro():
    print('broooooooooo')

@my_decorator
def bye():
    print('seeee yaaaaa')

bro()
bye()

from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f' took {t2-t1} ms')
        return result
    return wrapper


@performance 
def long_time():
    for i in range(1000000000):
        i*5


long_time()






















