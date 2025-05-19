#!/usr/bin/env python3
import sys

def return_evens(num_list):
    evens =[n for n in num_list if n%2 ==0]
    return evens
print(return_evens([0,1,3,5,7,8,9,7]))

def make_exclamation(sentence_list):
    exclaimed= [n +'!' for n in sentence_list]
    return exclaimed
    
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
squared_minus_one =list()
for n in range(1, 11):
    square =n*n
    squared_minus_one.append(square-1)

squared_minus_one=[(n*n)-1 for n in range(1,11)]
print(squared_minus_one)

one_to_three =range(1, 4)

squared_lc =[n*n for n in one_to_three]
print(squared_lc)

squared_ge=(n**2 for n in one_to_three)
for n in squared_ge:
    print(n)

list_comprehension=[n for n in range(100000)]
generator_expression=(n for n in range(100000))

print(sys.getsizeof(list_comprehension))
print(sys.getsizeof(generator_expression))
