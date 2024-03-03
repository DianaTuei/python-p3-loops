#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i > 0):
        print (i)
        i -= 1
    print ("Happy New Year!")


def square_integers(int_list):
    square_integers = [integer ** 2 for integer in int_list]
    return square_integers
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