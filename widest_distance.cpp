#include <stdio.h>

//def widest_distance(blocks):



n_blocks = len(blocks)
if (n_blocks==2):
    return 1

// determine initial direction
int n_dw = 0;
int n_up = 0;
int n_ev = 0;
int prev_block = blocks[0];
for (int ib=1; ib<n_blocks; ++ib) {
    // down
    if (prev_block>blocks[ib]) {
        flag="down";
        n_dw+=1
        prev_block = blocks[ib]
        break
    } else if (prev_block<blocks[ib]) {
    	// up
        flag="up"
        n_up+=1
        prev_block = blocks[ib]
        break
    # plateau
    else:
        n_ev+=1
        prev_block = blocks[ib]
}

# associate plateau with following direction
if (flag=="down"):
    n_dw+=n_ev
if (flag=="up"):
    n_up+=n_ev
n_ev = 0



# scan array
distance = 0
for ib in range(max(n_up,n_dw)+1,n_blocks):
    if (flag=="up"):
        # keep going up
        if (blocks[ib]>prev_block):
            n_up+=1
            n_ev=0
        # include plateaus
        elif (blocks[ib]==prev_block):
            n_up+=1
            n_ev+=1
        # evaluate distance, change to down
        else:
            if (n_up+n_dw>distance):
                distance = n_up+n_dw
            n_dw=n_ev+1
            n_up=0
            n_ev=0
            flag="down"
            continue
    elif (flag=="down"):
        # keep going down
        if (blocks[ib]<prev_block):
            n_dw+=1
        # change to up
        else:
            n_up+=1
            flag="up"

    # update previous block
    prev_block = blocks[ib]

# last distance if ending with up/even
if (n_up+n_dw>distance):
    distance = n_up+n_dw

return distance


# user
# blocks = list(map(int,input().split()))
# 
# distance = widest_distance(blocks)
# print(distance)



# performace test
#nblocks = int(2e8)
#blocks = list(np.random.randint(0,int(1e6)+1,nblocks))
nblocks = int(2e5)
blocks = list(np.random.randint(0,int(1e9)+1,nblocks))

distance = widest_distance(blocks)
print(distance)
