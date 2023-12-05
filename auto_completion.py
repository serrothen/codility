#!/usr/bin/env python3

import numpy as np

def find_contact(names,numbers,part):
    ncontacts = len(names)
    contact = ""
    # check substring in string
    for ii in range(ncontacts):
        if (part in numbers[ii]):
            if (contact=="" or names[ii]<contact):
                contact = names[ii]
    
    if (contact==""):
        return "NO CONTACT"
    else:
        return contact



# user
# ncontacts = int(input())
# names = []
# numbers = []
# for _ in range(ncontacts):
#    names.append(input())
#    numbers.append(input())
# part = input()
# 
# contact = find_contact(names,numbers,part)
# print(contact)



# performance
ncontacts = int(1e6)
alphabet = {ii: list(map(chr,range(ord('a')-1,ord('z')+1)))[ii] for ii in range(1,26+1) }
names = []
for ic in range(ncontacts):
    lname = np.random.randint(3,15+1,1)
    letters = np.random.randint(1,26+1,lname)
    name = alphabet[letters[0]].upper()
    for il in letters[1:]:
        name += alphabet[il]
    names.append(name)

numbers = list(map(str,np.random.randint(int(1e8),int(1e9),ncontacts)))

part = str(np.random.randint(1,int(1e4)))

contact = find_contact(names,numbers,part)
print(contact)
