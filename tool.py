import random

sept = [1,4,5,6,7,8,11,12,13,14,18,19,20,21,25,26,27,28,29]
october = [2,3,4,5,6,9,10,11,12,13,16,17,18,19,20,23,24,25,26,27,30,31]
november = [3,6,7,8,9,10,13,14,15,16,17,20,21,22,23,24,28,29,30]

#for day in november:
#    print(day)

#for i in range(2458):
#    # Your code here
#    print(f"Iteration {i + 1}")
#    for day in november:
#        print(day)



for _ in range(100):
    selected_number = random.choice(november)
    print(f"Randomly selected number in November: {selected_number}")
