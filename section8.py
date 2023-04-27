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
    for i in range(10000):
        i*5


long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args,**kwargs):
        if user1['valid']:
            fn(*args, **kwargs)
        else:
            print(f'sorry.. not valid credentials.. :(( ')
    return wrapper



@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)




















