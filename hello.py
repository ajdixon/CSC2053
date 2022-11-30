import math

print('Hello, World!')
#this is a coment

'''
comment -- use cmd slash to make portions of code into a comment
'''
   
int_example = 5
float_example = 5.5

x=5
x="this is a string"

result = 5.5//4
print(result)

result = 5.5%4
print(result)

squared = 5.5**2
print(squared)

squared = math.pow(5,2)
print(squared)

if squared == 25:
    print("correct")
else:
    print("Something went wrong")

x=10
y=100
if x>10 or y<90:
 print("at least one statement is true")

grade = 90

if grade >= 90:
    letter = "A"
elif grade>=80:
    letter = "B"
elif grade >= 70:
    letter = "C"
else:
    letter = "D"


first_name = "Alyssa"
last_name = "Dixon"
full_name = first_name + " " + last_name
print(full_name)

repear = first_name * 5

first_two = first_name[0:2]
print("first two:" + first_two)

if 'A' in first_name:
    print("A in fist name")


nstring = "hello"
length = len(nstring)
print(length)
nstring = (nstring[length-2:length])*3
print(nstring)
#iterating through sting same as through list

    
