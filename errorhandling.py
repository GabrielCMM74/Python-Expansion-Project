# an Error that cuases an error that stops code is called an exception

# Different type of errors - Name, syntax, Key, reference explains

# while True:
#     try:
#         age = int(input('What is your age? '))
#         print(age)
#         raise ValueError(' done its enough ') # throw your own errors
#     except ValueError:
#         print('please enter a number ')
#         continue
#     except ZeroDivisionError:
#         print('please enter age higher than zero ')
#         break
#     else:
#         print('thank you')
#         # break
#     finally:
#         print('okay done is done')
#     print('can you see this')


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:

#         print(f'please enter numbers {err}')

# print(sum(1, '2'))

# Generators

# range(100)
# list(range(100))

# def make_list(num):
#     result = []
#     for i in range(num):
#             result.append(i*2)
#     return result

# my_list = make_list(100)
# print(my_list)

# list are iterable - were able to loop through it
# generators are a subset of iterables

# def generator_func(num):
#     for i in range(num):
#         yield i*2

# # for item in generator_func(1000):
# #     print(item)

# g = generator_func(100)
# next(g)
# next(g)
# print(next(g))

# def special_for(itera):
#     iterator = iter(itera)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break

# special_for([1,2,3,4])

class MyGen():
    curret = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.curret < self.last:
            num = MyGen.curret
            MyGen.curret += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)


def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)


z = int(5)

print(z)


def checkHello():
    one = 'Hello'
    two = "Hello"
    if one == two:
        print('yes they are the same')
    else:
        print('no they are not')


checkHello()


# Divide into chunks that make sense
