#fstrings
name = "Arjunreddy"
age = 24
print(f"My name is {name} and i am {age} years old")
#String Indexing 
print(name[0])
#String Slicing
print(name[0:5:1])
#Conditional Statements
if age> 18:
    print("You can vote")
elif age== 18:
    print("You can vote")
else:
    print("Better Luck next time")
#Loops
cars = ["BMW", "AUDI", "TOYOTA", "FORD", "JEEP"]
for i in cars:
    print(i)
#Loops
for i in range(1,10):
    print("*"*i)