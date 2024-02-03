# import clear_screen from A_TOOL_clear_screen_function module
from A_TOOL_clear_screen_function import clear_screen

# Calling the function
clear_screen()

# array with integers elements
nums = [100,300,200]

# sums array integers
total = nums[0] + nums[1] + nums[2]
print(f'\nArray total manually summing indexes is {total}')

# sums array using a for loop
for i in nums:
    i += i
print(f'Array total using for loop is {i}')

# gets number of elements in array (length)
len_array = len(nums)
print(f'There are {len_array} elements in the array')

# displays variable type
print(f'Variable Type: {type(nums)}')

# find largest number in array
largest = 0
for i in nums:
    if i > largest:
        largest = i
print(f'Largest number in the Array is {largest}')        

# print even numbers from 1 to 20
print("Even Nums 1 to 20: ", end=' ')
for i in range(0,21,2):
    if i != 0:
        print(i, end=' ')
print("\n")