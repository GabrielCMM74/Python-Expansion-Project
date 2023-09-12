# Testing is another file anf for each module there is another file
# def do_stuff(num=0):
#     try:
#         if num:
#             return int(num) + 5
#         else:
#             return 'please enter number'
#     except ValueError as err:
#         return err
import random

answer = random.randint(1, 10)
while True:
    try:
        guess = int(input('guess a number 1~10'))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius')
                break
        else:
            print('hey dumb dumb its between 1~10')
    except ValueError:
        print('please enter a nunmber ')
        continue
