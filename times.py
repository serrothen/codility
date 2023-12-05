#!/usr/bin/env python3

def valid_times(letters):
    nletters = len(letters)

    # allow for arbitrary many digits
    c_sum = ""
    c_loops = ""
    c_comp = "if "
    for ii in range(1,nletters):
        c_sum += "el"+str(ii)+"+"
        c_loops += "for el"+str(ii)+" in letters "
        for jj in range(ii+1,nletters+1):
            c_comp += "el"+str(ii)+"!=el"+str(jj)+" and "
    c_sum += "el"+str(nletters)
    c_loops += "for el"+str(nletters)+" in letters"

    command = "["+c_sum+" "+c_loops+" "+c_comp[:-5]+"]"

    # combinations = [el1+el2+el3+el4 for el1 in letters for el2 in letters for el3 in letters for el4 in letters if el1!=el2 and el1!=el3 and el1!=el4 and el2!=el3 and el2!=el4 and el3!=el4]
    # must use eval inside function (cannot use exec)
    combinations = eval(command)
   
    # check times
    valid = []
    for c in combinations:
        if (int(c[0:2])<24):
            if (int(c[2:4])<60):
                valid.append(c)
    
    return valid

letters = list(input().split())

valid = valid_times(letters)
print(valid)


