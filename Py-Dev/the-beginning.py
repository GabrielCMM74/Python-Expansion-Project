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






















































































































