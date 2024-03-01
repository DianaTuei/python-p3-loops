#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i > 0):
        print (i)
        i -= 1
    print ("Happy New Year!")


def square_integers(int_list):
   integers_square = list()
   for integer in int_list:
       integer_square = integer * integer
       integers_square.append(integer_square)
   return integers_square
square_integers([1,2,3,4,5])

def fizzbuzz():
    i = 0
    while i < 100:
        i += 1
        if(i%3 == 0 and i%5 == 0):
            print ("FizzBuzz")
        elif(i%5 == 0):
            print ("Buzz")
        elif(i%3 == 0):
            print("Fizz")
        else:
            print (i)
fizzbuzz()