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
        if  age < 0 or age > 100:
            raise ValueError("Use a reasonable range.")
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError("First name and last name cannot be empty.")
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def greeting(self):
        full_name = self.first_name + " " + self.last_name
        return "Good morning " + full_name
    
# Question 4: What is your favorite cloud service (on AWS or any other cloud vendor) and why?
# What are the cloud services strengths? What are its weaknesses? For cloud service, I mean
# something that a programmer would use (such as AWS S3). I am not referring to something that
# a consumer would use (such as TikTok).

# Answer:

# My first approach to the cloud was with AWS. Then I used the other cloud providers (GCP, mostly). 
# But I find AWS interface more familiar and AWS CDK really makes cloud infraestructure really easy to manage and deploy.
# The strengths I find in cloud services are scalability and cost efficiency. 
# Some weaknesses I see are data security and when businesses grow, serverless architecture tends to get expensive. So eventually one might end up returning to a monolithic server architecture. 


# Question 5: Suppose you are building a cool new thing in the cloud. You want to make a
# service that is a thumbnail generator. For example, you input a big picture and get a small
# picture as output. How would you build this? Please explain your architecture using the cloud
# services in AWS (or another cloud vendor that you are familiar with).

# I would use a easy to deploy front end using R Shiny. Then I would create my thumbnail engine using AWS Lambda and on top of it I would place an API Gateway for proxying traffic to said function.
# I would deploy my service using AWS CDK.

# Question 6 (optional): Write a function called timer() that can time any arbitrary function. For
# example, if I have a function called `long_running_process()`, I want to be able to decorate this
# function with `timer()` such that when I run `long_running_process()`, it will be print out “This
# function took X seconds” where X is replaced by the function’s runtime (in seconds) when the
# function finishes running. The `timer()` should work for any arbitrary function with an arbitrary
# number of arguments. Do this question only if you finish the other questions.
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"This function took {round(runtime)} seconds")
        return result
    return wrapper

@timer
def long_running_process():
    time.sleep(3) 

long_running_process()