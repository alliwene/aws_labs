# lsInsulin = "malwmrllpllallalwgpdpaaa"
# bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
# aInsulin = "giveqcctsicslyqlenycn"
# cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
# insulin = bInsulin + aInsulin

# aminoList = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

# aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
# 'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
# 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
# 'V': 117.15, 'W': 204.23, 'Y': 181.19} 

# # print(aaWeights) 

# amino = {}
# for item in aminoList:
#     insulinCount = insulin.upper().count(item) 
#     amino[item] = insulinCount
# print(amino)

# total_sum = 0
# for item in aminoList:
#     multiply = amino[item] * aaWeights[item]
#     total_sum += multiply
# print(total_sum) 


# bananas = 4
# if bananas >= 5: 
#     print("I have a large bunch of bananas")
# elif bananas >= 1: 
#     print("I have a small bunch of bananas")
# else: 
#     print("I don’t have any bananas") 

# counter = 0

# while counter <= 3:
#     print('I love Python')
#     counter += 1

# try:
#     value = 5 / 0
# except ValueError:
#     value = 1

# import json
# print(json.dumps([1, 'celeb', True]))  
# print(json.loads('[1, "celeb", 6]') )  


# filename = 'userName.json' 
# name = ''
# # Check for a history file 
# try:
#     with open(filename, 'r') as r: 
#         # Load the user's name from the history file 
#         name = json.load(r)
# except IOError: 
#     print("First-time login")

# # If the user was found in the history file, welcome them back 
# if name != "": 
#     print("Welcome back, " + name + "!")
# else: 
#     # If the history file doesn't exist, ask the user for their name
#     name = input("Hello! What's your name? ") 
#     print("Welcome, " + name + "!")

# # Save the user's name to the history file 
# try:
#     with open(filename, 'w') as f: 
#         json.dump(name, f)
# except IOError: 
#     print("There was a problem writing to the history file.") 

# confirm = 'N'
# while confirm != 'Y':
#     username = input('Enter username: ')
#     print(f'Remove the user {username}? (Y/N)')
#     confirm = input('').upper()
#     print('A') 
#     break 
#     # confirm = 'Y' 

# import logging 
# logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Python program with 2 errors 

# def checkvalue(valuetocheck): 
#     assert (type(valuetocheck) is int), 'You must enter a number.'
#     assert (valuetocheck > 0), "Value entered must be greater than 0" 
#     if valuetocheck > 4: 
#         print("Value is greater than 4") 

# var = int(input("Enter a number greater than 0: ")) 
# checkvalue(var)


# name = "John"
# print("Hello " + name + ".")
# age = 40
# print(name + " is " + str(age) + " years old.")

# while i < max_number:
#     person = input("Enter name? ")
#     i += 1
# print(ranndom.choice(person_list, random_state))

print(divmod(10,2))


import random
from itertools import accumulate


# def print_groups(n, g):
#     # Prepare group separators
#     size = n // g
#     rem = n % g
#     separators = list(accumulate([0] + [size+1] * rem + [size] * (g - rem)))

#     # Make raw data
#     items = list(range(n))
#     random.shuffle(items)

#     # Iterate and print
#     for i, s in enumerate(zip(separators, separators[1:])):
#         group = items[slice(*s)]
#         print(f'Group {i+1}: {group} (size {len(group)})')

import random
participants=["Alex","Elsie","Elise","Kimani","Ryan","Chris","Paul"]
group=1
membersInGroup=3

random.seed(41)
for participant in participants:               # only modification
    if membersInGroup==3:
        print("Group {} consists of;".format(group))
        membersInGroup=0
        group+=1
    person=random.choice(participants)
    print(person)
    membersInGroup += 1