import math
import random

# print a single random number between 1 and 100
rand_nums = random.randint(1, 100)
print(rand_nums, end=' ')

# calculate square root
square_root_num = 99
sqrt_answer = math.sqrt(square_root_num)
print(f'\nSquare root of {square_root_num} is {sqrt_answer:.2f}')

# math operations
print(2*3+4) # equals 10
print(500/2*4+8) # equals 1008

string_num = "123"
print(string_num, type(string_num))
string_to_int = (int(string_num))
print(string_to_int, type(string_to_int))