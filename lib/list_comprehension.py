#!/usr/bin/env python3

def return_evens(num_list):
    # num_list = range(10)
    evens_list = [num for num in num_list if num % 2 == 0]
    return evens_list

return_evens( num_list = range(10))

def make_exclamation(sentence_list):
    exclamation_list = [sentence + "!" for sentence in sentence_list ]
    return exclamation_list
    

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
    