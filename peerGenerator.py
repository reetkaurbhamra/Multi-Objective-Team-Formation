'''
generate_gender() takes in the total number of people (n) and returns an array 
of size n, consisting of values {-1,1}

generate_personality() generates a 5 element array for each individual 

generate_availibility() generates a 168 element array for each individual. The 
size of this array can be adjusted by changing the value of variable "size".

Finally, an array of type :
u1 = [[gender], [personality], [availability]]
is generated and can be accessed using.

If you want to access gender, availability and personality arrays separately,
then in the driver code, change the value of r from "1" to "numberOfStudents";
and un-comment the three print statements in the same.
'''          

import random

def get_numberOfStudents():
    return int(input("Enter the required number of people: "))


#does something :/
def create_keys(a : int):
    keys = []
    for i in range(a):
        m = "u" + str(i+1)
        keys.append(m)
    return keys 

def create_values():
    values = []
    for i in range(numberOfStudents):
        x = []
        x.append(generate_gender())
        x.append(generate_personality())
        x.append(generate_availability())
        values.append(x)
    return values


#gender part
def generate_gender():
    gender_list = []
    for i in range(r):
        gender_list.append(random.choice(foo))
    return gender_list


#personality part
def user_personality():
    user_personality_list = []
    for j in range(5):
        user_personality_list.append(random.randint(0,100))
    return user_personality_list

def generate_personality():
    personality_list = []
    for i in range(r):
        personality_list.append(user_personality())
    return personality_list
    

#availability part     
def user_availability():
    user_availability_list = []
    for j in range(size):
        user_availability_list.append(random.choice(hoo))
    return user_availability_list
 
def generate_availability():
    availability_list = []
    for i in range(r):
        availability_list.append(user_availability())
    return availability_list
    

# DRIVER CODE

foo = [-1, 1]
hoo = [0, 1]

numberOfStudents = get_numberOfStudents()

size = 168
r = 1

#print(generate_gender())
#print(generate_personality())
#print(generate_availability())

print(dict(zip(create_keys(numberOfStudents),create_values())))
