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

