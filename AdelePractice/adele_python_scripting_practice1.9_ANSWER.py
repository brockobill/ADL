# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given an array of ints, return True if the array is length 1 or
#    more, and the first element and the last element are equal.
#
# Examples:
#
#    SameFirstLast([1, 2, 3]) → False
#    SameFirstLast([1, 2, 3, 1]) → True

# Write you function code below
def SameFirstLast(nums):
    length = len(nums)
    if length >= 1:
        first = nums[0]
        last = nums[length-1]
        if first == last:
            return True
        else:
            return False
    else:
        return False


# Pre defined test conditions to help you out
try:
    assert SameFirstLast([1, 2, 3]) == False, "[1,2,3]"
    assert SameFirstLast([1, 2, 3, 1]) == True, "[1,2,3,1]"
    assert SameFirstLast([1, 2, 3, 2, 1, 2]) == False, "[1,2,3,2,1,2]"
    assert SameFirstLast([1]) == True, "[1]"
    assert SameFirstLast([]) == False, "[]"
    print("Pass")

except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = [
    [], [3, 0, 4, ], [2, 2, 0, ], [3, ], [0, 4, 1, 3, ], [2, ],
    [4, 2, 4, 0, ], [0, 4, ], [1, 1, ], [0, 3, 2, 2, ], [0, 4, 2, ],
    [1, ], [4, 0, 2, 1, ], [1, 3, ], [2, 1, ], [2, 2, 0, 0, ], [0, ],
    [1, 3, 4, 0, ], [0, ], [3, 1, 0, ], [0, ], [3, 4, ], [1, 1, 3, 1, ],
    [1, 1, 4, 4, ], [4, 2, 4, 3, ], [1, 1, ], [0, ], [0, 1, 0, ],
    [4, 2, 0, ], [2, ], [0, 0, 3, 1, ], [0, ], [0, 2, 3, 1, ],
    [1, 4, 4, ], [3, ], [2, 0, 3, 2, ], [2, ], [4, 0, 2, ], [2, 2, 4, 1, ],
    [0, 2, 0, ], [1, 2, ], [4, 1, 4, ], [2, 2, 1, ], [3, ], [4, 0, ],
    [2, 1, 4, ], [3, 2, ], [0, 3, ], [1, 0, 0, 2, ], [4, 1, 1, ], [1, 0, 0, ],
    [0, ], [4, ], [4, 3, 3, 1, ], [2, 0, 2, 2, ], [3, ], [3, 2, 1, ],
    [2, 0, 1, ], [2, 2, 0, ], [1, 3, ], [2, 1, 4, 1, ], [3, ], [0, ],
    [0, 0, 3, 0, ], [1, 3, 0, 4, ], [3, 1, ], [3, 3, ], [2, 0, 4, 1, ],
    [4, 3, 0, 3, ], [1, ], [1, 2, ], [0, 3, ], [0, 1, 4, ], [3, 3, 2, 2, ],
    [4, ], [0, ], [0, 3, 0, ], [2, 4, 3, 0, ], [2, 0, 4, ], [4, 0, 1, ], [2, ],
    [2, 4, ], [4, ], [4, ], [3, 4, 4, ], [1, ], [3, 0, ], [3, ], [0, ],
    [3, 4, 3, 4, ], [0, 3, 3, 4, ], [2, ], [0, 2, ], [1, ], [1, 4, ],
    [3, 2, 0, 0, ], [4, 4, 4, ], [0, 4, 1, ], [1, 4, ], [1, ], [1, 4, ]
]
for arg in args:
    total += SameFirstLast(arg)
print(total)
