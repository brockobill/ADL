# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given an array of ints, return True if the array contains a 2
#    next to a 2 somewhere.
#
# Examples:
#
#    Has22([1, 2, 2]) → True
#    Has22([1, 2, 1, 2]) → False


def Has22(nums):
    counter = 0
    for x in nums:
        if x == 2:
            counter = counter+1
        else:
            counter = 0
        if counter == 2:
            return True
    return False


# predefined test conditions
try:
    assert Has22([1, 2, 2]) == True, "[1,2,2]"
    assert Has22([1, 1, 1, 2]) == False, "[1,1,1,2]"
    assert Has22([2, 1, 2]) == False, "[2,1,2]"
    assert Has22([3, 3, 2, 2]) == True, "[3,3,2,2]"
    assert Has22([2]) == False, "[2]"
    print("\nAssert Test Cases: Pass\n")

except AssertionError as e:
    print("Failed on case: " + str(e))

# use the printed total as the flag
total = 0
args = [[], [3, 0, 4, ], [2, 2, 0, ], [3, ], [0, 4, 1, 3, ], [2, ], [4, 2, 4, 0, ], [0, 4, ], [1, 1, ],
        [0, 3, 2, 2, ], [0, 4, 2, ], [1, ], [4, 0, 2, 1, ], [
            1, 3, ], [2, 1, ], [2, 2, 0, 0, ], [0, ],
        [1, 3, 4, 0, ], [0, ], [3, 1, 0, ], [0, ], [3, 4, ], [
            1, 1, 3, 1, ], [1, 1, 4, 4, ], [4, 2, 4, 3, ],
        [1, 1, ], [0, ], [0, 1, 0, ], [4, 2, 0, ], [2, ], [
        0, 0, 3, 1, ], [0, ], [0, 2, 3, 1, ], [1, 4, 4, ],
        [3, ], [2, 0, 3, 2, ], [2, ], [4, 0, 2, ], [
        2, 2, 4, 1, ], [0, 2, 0, ], [1, 2, ], [4, 1, 4, ],
        [2, 2, 1, ], [3, ], [4, 0, ], [2, 1, 4, ], [3, 2, ], [
        0, 3, ], [1, 0, 0, 2, ], [4, 1, 1, ], [1, 0, 0, ],
        [0, ], [4, ], [4, 3, 3, 1, ], [2, 0, 2, 2, ], [3, ], [
        3, 2, 1, ], [2, 0, 1, ], [2, 2, 0, ], [1, 3, ],
        [2, 1, 4, 1, ], [3, ], [0, ], [0, 0, 3, 0, ], [
        1, 3, 0, 4, ], [3, 1, ], [3, 3, ], [2, 0, 4, 1, ],
        [4, 3, 0, 3, ], [1, ], [1, 2, ], [0, 3, ], [0, 1, 4, ], [
        3, 3, 2, 2, ], [4, ], [0, ], [0, 3, 0, ],
        [2, 4, 3, 0, ], [2, 0, 4, ], [4, 0, 1, ], [2, ], [
        2, 4, ], [4, ], [4, ], [3, 4, 4, ], [1, ], [3, 0, ],
        [3, ], [0, ], [3, 4, 3, 4, ], [0, 3, 3, 4, ], [
        2, ], [0, 2, ], [1, ], [1, 4, ], [3, 2, 0, 0, ],
        [4, 4, 4, ], [0, 4, 1, ], [1, 4, ], [1, ], [1, 4, ]]
for arg in args:
    total += Has22(arg)
    if Has22(arg) == 1:
        print(arg)
print(f'\nFlag Total {total}\n')
