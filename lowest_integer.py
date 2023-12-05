def solution(A):
    # Implement your solution here
    B = {el for el in A if (el>0 and el<=int(1e5))}
    len_b = len(B)
    C = {el for el in B if (el<=len_b)}
    for ii in range(1,len_b+2):
        if (ii not in C):
            return ii
