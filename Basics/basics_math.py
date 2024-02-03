import math
import random

'''# print a single random number between 1 and 100
rand_nums = random.randint(1, 100)
print(rand_nums, end=' ')

# calculate square root
square_root_num = 99
sqrt_answer = math.sqrt(square_root_num)
print(f'\nSquare root of {square_root_num} is {sqrt_answer:.2f}')

# math operations
print(2*3+4) # equals 10
print(500/2*4+8) # equals 1008'''

a = 16
aa = (a//10)
ab = (a%10)
if ab >= 5:
    new_a = 10*(aa+1)
else:
    new_a = 10*aa    
print(new_a)





