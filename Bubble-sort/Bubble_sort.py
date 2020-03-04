import random

#Create the list
bubble_list = list()
i = 0
while (i < 10):
    bubble_list.append(random.randint(1, 1000))
    i += 1
print(bubble_list)
length = len(bubble_list)

pos = 1
swaps = 0
times_swapped = 0
sorted = False

#Sort the actual list
while sorted == False:
    prev_swap = swaps    
    for pos in range(1, length):
        if bubble_list[pos - 1] > bubble_list[pos]:

            pl_hldr = bubble_list[pos]        
            
            bubble_list[pos] = bubble_list[pos - 1]
                
            bubble_list[pos - 1] = pl_hldr

            swaps += 1
            times_swapped += 1
    
    if(swaps == prev_swap):
        sorted = True

print(bubble_list)
print("Times swapped:",times_swapped)