#  Terminal Commands

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
# for image in picture:
#     for pixel in image:
#         if (pixel):
#             print('*', end="")
#         else:
#             print('  ', end="")
#         print('')


# def multiply_by_two(num):
#     return num * 2


# def sum(num1, num2):
#     return num1 + num2


# print(sum(20, 3))


# name =input('What is your name?')

# print('Hello  ' + name)

# print(type(2*4))

# Modular % the remainder between two 

#bin returns the binary number 

# String indexes [Specific Letter]



# username = input('Type your Username here ')

# password = input('Input your password ') 

# number = len(password)

# password = '*' * number

# print(f" {username}, your password {password} is {number} letters long")

# Lists

# li = [1,2,3,4,5,6]
# li2 = ['a', 'b', 'c']
# li3 = [1,2, 'a', True]

# amazon_cart = [
#     'notebooks',
#     'sunglasses'
#     'toys',
#     'grapes'
#     ]

# print(amazon_cart[0::2])
# print(amazon_cart[0])

# amazon_cart[0] = 'laptop'
# print(amazon_cart)

#Matrix 

# matrix = [
#     [1,2,3],
#     [2,4,6],
#     [7,8,9]
# ]

# print(matrix[0][1])

# from turtle import Turtle
# from unicodedata import name


# from multiprocessing.sharedctypes import Value
# import numbers




basket = [1,2,3,4,5,6]

basket.insert(4, 100)
basket.append(100)
basket.extend([101])

new_list = basket
print(basket)
print(4 in basket)
print(basket.count(2))

basket.sort()
print(sorted(basket))
basket.reverse()
print(basket)
print(basket[::-1])

print(list(range(0,101)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'spiderman'])
print(new_sentence)

a,b,c = 1,2,3

print(a)
print(b)
print(c)

weapons = None
print(weapons)

#Dictionary 

dictionary = {
    'a': 1,
    'b': 2,
    'x': 3,
}

print(dictionary['b'])

my_list = [

    {
    ' a ' : [ 1,2,3 ] ,
    ' b ' : ' hello ' ,
    ' x ' : True
    } , 
    {
    ' a ' : [ 4,5,6 ] ,
    ' b ' : ' hello ' ,
    ' x ' : True
    }]

print(my_list[0][' a '][2])

# Lists have order, but a player for a game can use a dictionary. A dict can have way more infromation 
#Dict keys 


dictionary2 = {
    123: [1,2,3],
    True: 'Hello',
    'is_Magic': True
}
print(dictionary2[123])
#Keys need to be immutable l side

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age' : 20
}
print(user.get('age', 55))

user2 = dict(name='JohnJohn')
print(user2)
print('basket' in user)
print('hello' in user.values())
print(user.items())

#Tuple 

my_tuple = (1,2,3,4,5)
print(5 in my_tuple)
print(my_tuple.count(5))
print(my_tuple.index(4))
print(len(my_tuple))
#Faster than list 

# new_tuple = my_tuple[1:2]
# print(new_tuple)

x,y,z, *other = (3,4,6,7,8)
print(other)

#Set- Unique objects only
my_set = {1,2,2,3,4,5,6,7}
my_set.add(100)
print(my_set)

my_list2= [1,2,3,4,5,5,5]
print(set(my_list2))

#Differnt Methods 

your_Set = {4,5,6,7,8,9,10}
print(my_set.difference(your_Set))
print(my_set.discard(100))
print(my_set)

is_old = True
is_license = True

if is_old:
    print('you are old enough to drive!')

else: 
    print('check check')


#ternary 

# condition_if_ture if condition else condition_if_else

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

is_User = True 

if is_friend and is_User:
    print('best friends')

is_magician = True  
is_expert = False 

if is_magician and is_expert:
    print('you are a master magician')

elif is_magician == True and is_expert == False:
    print('at least your getting there')

elif not is_magician:
    print('You need magical powers')


#Loop 

for item in 'Zero to Mastery':
    print(item)

for item2 in [1,2,3,4,5]:
    print(item2)

for item3 in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item3,x)

user3 = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
    }

for key,value in user3.items():
    print(key,value)

for item in user3.values():
    print(item)

for item in user3.keys():
    print(item)

list_3 = [1,2,3,4,5,6,7,8,9,10]
count = 0
for item in list_3:
    count = count + item
    print(count)

#range

# for i in range(0,100):
#     print(i)


# for e in range(10, 0, -1):
#     print(e)

#enumerate 

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}')

i = 0
while i< 50:
    print(i)
    i += 1

#Iterating can become a very long process

#Break 
# Continue skips and goes back to the loop 
# pass - placeholder for coding just keep passing 

# picture = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]
# ]

# for row in picture:
#     for pixel in row:
#         if (pixel==1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

some_list = ['a', 'b', 'c', 'd', 'b', 'c', 'm', 'n', 'n']
duplicates =[]

for i in some_list: 
    if some_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
        
print(duplicates)

#Functions 
def say_hello(): 
    print('hello')
say_hello()

# Remember Object Hirearchy 
# Param
def say_hello2(name, title, emoji): 
    print(f' hello is this {name} working {title} and this {emoji} ')
say_hello2('G', 'IT', '😎')
#Argument

#Keyword 
say_hello2(emoji='😂', name='Bada', title='MS')

#default say_hello(name='Darth', emoji='😀' ) - If you forget to give it arguments then this is the default 

# def sum(num1, num2):
#     return num1 + num2
    
# print(sum(4,5))

def checkDriverAge(age=0):
    # age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
	    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(18)

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

#Methods, Functions 

# methods are all owned by something 

def test(a):
    '''
    Info: this fuction tests and prints param a 
    '''
    print(a)
    
test("CHeck this")

def is_odd_or_even(num): 
    if num % 2 == 0:
        return True
    return False
print(is_odd_or_even(50))

# args and kwargs 

def super_Func(*args, **kwargs):
    return sum(args)

print(super_Func(1,2,3,4,5, num1=10,num2=15))

#Rule params, *args, default parameters, **kwargs 

def highest_Even(li):
    evens = []
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)

print(highest_Even([10,12,14,1,5]))

#walrus 
a = "helloooooooo"

if ((n := len(a)) > 10):
    print(f" too long {n} elements")

while((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)

#
total = 0 
def count():
    global total 
    total += 1 
    return total

count()
count()
count()
print(count())


x = float(2.8)

print(x)

f = "Hello"[0]
print(f)









































