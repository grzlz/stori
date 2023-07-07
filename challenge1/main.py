# Question 1a: If given a list of integers, write a function that returns a list of strings where it says “even” or “odd” depending on the number. Write a function WITHOUT using `.append()`.

def even_odd(number_list):
    result = []
    for i in number_list:
        if i % 2 != 0:
            result += ["odd"]
        else:
            result += ["even"]
    return result

#Question 1b: If given a list of integers, write a function that returns a list where if the number is even, then put “even” but if it is “odd”, then keep the original number.
def only_odds(number_list):
    result = []
    for i in number_list:
        if i % 2 != 0:
            result += [i]
        else:
            result += ["even"]
    return result

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(only_odds(list))

#Question 2: You are a magician casting a spell! Write a function that spells each word in a string backwards. Notice you are not spelling the entire string backwards, only each word in the string.

def words_backwards(string):
    x = string.split()
    result = " ".join(word[::-1] for word in x)
    return result

""" #Question 3: Write a class that takes in the following input arguments during instantiation: person’s first name, last name, age. Do some simple checks during instantiation to make sure
that the input arguments seem reasonable (ie. name is a string, age is not negative, and at least
1 other check that you think is helpful). If an input argument does not make sense, raise an
exception with a helpful error message about the reason why.
Then write a method called `greeting()` where it will return a string saying “Good morning ”
followed by their full name (first name + last name) """
        
class Person:
    def __init__(self, first_name, last_name, age):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("First name and last name must be valid strings.")
        if not isinstance(age, int):
            raise ValueError("Age must be a valid integer.")
        if  age < 0:
            raise ValueError("Age can't be a negative integer.")
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError("First name and last name cannot be empty.")
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def greeting(self):
        full_name = self.first_name + " " + self.last_name
        return "Good morning " + full_name