# sample2.py

def get_intro(name, age):
    return f"My name is {name} and I am {age} years old"

def get_first_letter(name):
    return name[0]

def get_name_slice(name):
    return name[0:5:1]

def can_vote(age):
    if age >= 18:
        return "You can vote"
    else:
        return "Better Luck next time"

def list_cars(cars):
    return cars

def print_stars(n):
    return ["*" * i for i in range(1, n)]
