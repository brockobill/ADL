# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given an array of integers, return True if the sequence 1, 2, 3,
#    appears in the array somewhere.	               
#
# Examples:
#
#    Array123([1, 1, 2, 3, 1]) → True
#    Array123([1, 1, 2, 4, 1]) → False 


# Write your function code below
def Array123(nums):
    """ 
    range(len(nums) - 2): The range() function generates a sequence of numbers. 
    In this case, it generates a sequence of indices starting from 0 up to 
    (but not including) len(nums) - 2. The len(nums) gives the length of the 
    nums tuple (or list).

    For example, if len(nums) is 5, then range(len(nums) - 2) generates the 
    sequence [0, 1, 2]. This range ensures that the loop iterates up to the 
    second-to-last index of the nums tuple.
    """
    count = 0
    for i in range(len(nums) -2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
        count += 1
    return False 
           
# Pre defined test conditions to help you out
try:
    assert Array123([1,1,2,3,1]) == True, "[1,1,2,3,1]"
    assert Array123([1,1,2,4,1]) == False, "[1,1,2,4,1]"
    assert Array123([1,2,4,3]) == False, "[1,2,4,3]"
    assert Array123([1,2,3]) == True, "[1,2,3]"
    assert Array123([]) == False, "[]"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = (1,2,1,3,4,4), (1,2,2,3,1,2,4,2,2), (1,4,1,2,2), (4,1,2,4,2,3), (1,4,3,1,2,1,1), (4,3,2,1,2,3,3,1), (4,2,3,2,1,2), (2,1,2,1,1,1), (2,2,1,2,4,1,1,2), (4,2,4,2,2,3,1,2), (1,2,1,2,3,4), (2,3,3,1,3), (1,2,3,2,3), (4,3,3,1,2,1,2,1,2), (1,1,2,4,1,3,1,3), (4,1,1,2,1,2,4,1,2,1,2), (1,4,1,4,4,1,1,2), (3,1,2,1,2,3,4), (3,2,2,2), (2,1,2,1,2,2,2,2), (3,1,2,1,3,1,2), (1,4,1,2,1,2,), (1,1,2,1,2,4,3,), (2,4,4,1,), (3,4,4,4,1,2,2,), (3,1,3,1,), (4,3,3,1,2,3,1,2,3,), (1,2,1,2,4,4,1,2,), (2,2,1,2,2,1,2,1,2,), (1,4,1,2,1,1,2,4,1,), (1,3,1,2,2,), (2,1,2,4,3,), (1,2,1,2,1,1,4,3,), (1,4,2,2,), (1,2,3,1,1,1,2,4,2,), (4,3,4,1,2,4,), (1,2,1,2,1,1,2,1,2,), (1,3,3,4,2,1,), (1,4,1,2,1,2,3,), (4,2,1,2,3,), (1,2,1,2,1,2,2,1,), (1,3,3,3,3,2,1,2,), (1,2,2,1,1,2,), (3,1,1,4,1,2,4,), (4,2,1,2,4,2,4,2,), (1,2,3,4,1,3,3,4,), (1,2,1,1,2,1,2,2,4,3,), (2,4,1,1,4,3,4,), (3,1,4,2,4,), (4,1,3,3,), (3,3,2,2,4,2,1,2,), (1,2,3,1,2,1,1,2,), (4,2,1,1,2,1,2,1,2,), (1,1,2,4,3,), (4,4,1,2,1,2,1,3,), (4,3,4,3,4,1,2,), (3,3,1,2,2,1,2,), (3,3,1,2,2,), (2,1,1,2,1,2,1,1,), (1,2,1,2,3,4,1,1,2,1,2,), (1,4,3,4,4,4,1,2,), (1,3,1,1,), (1,2,1,2,3,1,2,), (3,1,2,1,2,3,3,2,), (1,2,1,2,2,1,4,3,), (4,1,2,1,2,3,3,), (4,1,2,2,), (3,1,2,2,2,2,1,2,), (3,1,2,2,1,2,3,), (1,2,1,1,2,4,4,4,1,), (3,1,2,4,1,), (1,2,1,2,3,2,), (1,2,1,1,2,1,2,1,), (2,4,2,4,), (1,2,1,2,3,3,), (3,1,2,3,2,3,1,2,3,), (1,2,3,3,1,2,1,2,), (1,3,4,2,3,), (2,3,2,4,2,3,), (3,2,4,1,2,4,4,), (1,2,1,2,1,3,1,), (1,2,4,2,1,2,4,3,), (4,2,2,1,4,), (1,2,1,2,2,1,2,4,3,), (3,3,2,3,2,4,3,), (3,4,2,3,3,1,2,), (2,3,3,2,2,1,2,1,2,), (4,1,1,2,1,1,1,), (3,4,3,1,2,), (1,3,1,1,2,1,2,), (3,1,2,3,2,), (1,1,2,1,2,1,2,1,2,2,3,), (1,1,1,1,2,3,1,2,4,), (3,1,2,1,2,1,2,3,3,), (3,1,2,1,2,1,2,), (1,1,1,2,1,2,), (1,2,2,2,1,2,3,1,), (4,4,3,1,4,), (2,2,2,3,), (1,2,1,2,1,2,1,2,)
for arg in args:
    total += Array123(arg)
print(total)