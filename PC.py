from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capital(string):
    return string.upper()

print(list(map(capital, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers_assorted = sorted(my_numbers)

print(list(zip(my_strings, my_numbers_assorted)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def scoresOver(score):
    return score > 50 

print(list(filter(scoresOver, scores)))



#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

total_list = my_numbers + scores


def initiate(ini, scores):
    print(ini, scores)
    return ini + scores

print(reduce(initiate, total_list))

#Lambda 

# lambda param: action(param)

new_list = [2,4,3,6,7,8,9]



print(list(map(lambda item: item*2, new_list)))


list_squared = [5,4,3]

# print(list(lambda item: item in list_squared * item))

comp_list = [char for char in 'iterable']
print(comp_list)

new2_list = [num for num in range(0,100)]
print(new2_list)

new3_list = [num**2 for num in range(0,100) if num % 2 == 0]
print(new3_list)


#dict compr
simple_dict = { 'a': 1,'b': 2}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}

new_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)
print(new_dict)

dupli_list = ['a', 'c', 'b', 'b', 'd', 'n', 'n']

duplicated = [x for x in dupli_list if dupli_list.count(x) > 1]

print(duplicated)
































































































