# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given two lists of integers, return the sum of the intersection.
#    The intersection is the integers that are common to both lists.
#    Return 0 if there are no common integers.
#
# Examples:
#
#    IntSum([1,2,3], [2]) → 2
#    IntSum([1,2,2,3], [2,2]) → 2


# Write your function code below
def IntSum(list1, list2):
    """ 
    When you convert a list to a set, it automatically removes any 
    duplicate elements, leaving only the unique ones.
    """
    # Find the intersection of the two lists
    common_elements = set(list1) & set(list2)

    # Calculate the sum of the common elements
    total_sum = sum(common_elements)

    return total_sum



# Pre defined test conditions to help you out
try:
    assert IntSum([1,2,3], [2]) == 2, "[1,2,3], [2]"
    assert IntSum([1,2,2,3], [2,2]) == 2, "[1,2,2,3], [2,2]"
    assert IntSum([1,2,3], [4,5,6]) == 0, "[1,2,3], [4,5,6]"
    assert IntSum([1,2,3], [1,2,3]) == 6, "[1,2,3], [1,2,3]"
    assert IntSum([], []) == 0, "[], []"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = (([1,6,4,], [4,6,3,]), ([2,], [3,]), ([2,4,2,3,], [1,1,]), ([6,6,], [2,]), ([3,2,3,4,], [5,2,]), ([1,1,2,], [6,4,6,]), ([3,4,], []), ([], []), ([5,], [5,6,6,1,2,]), ([5,5,3,1,], [1,3,2,4,]), ([], [3,4,3,4,5,]), ([3,5,3,3,], [1,5,]), ([6,3,], [1,5,3,1,5,]), ([6,4,1,3,4,], [1,]), ([], [5,]), ([5,4,5,4,], [5,1,1,6,]), ([5,4,4,6,], [2,1,3,]), ([3,3,2,5,2,], []), ([4,], [4,1,]), ([1,], [2,4,5,2,]), ([], [3,5,1,]), ([], [6,4,5,6,]), ([4,4,2,], [6,]), ([], [2,1,6,3,]), ([3,3,], [5,1,5,]), ([6,4,3,3,6,], []), ([5,2,1,], [6,5,2,4,]), ([2,2,1,3,2,], []), ([], [5,4,4,]), ([1,5,4,1,2,], [1,]), ([], []), ([3,6,1,2,], [2,6,2,]), ([3,], [3,3,2,]), ([5,4,], [1,6,]), ([4,2,3,1,], [4,]), ([3,2,6,4,], [4,2,]), ([5,], [6,2,6,]), ([4,], [5,6,]), ([], [4,3,2,4,6,]), ([], [1,1,4,2,5,]), ([4,5,1,1,5,], [6,5,3,3,]), ([1,2,1,1,5,], [2,5,6,6,]), ([4,3,1,2,1,], [3,4,1,]), ([], [3,5,5,]), ([5,3,4,], [1,3,4,3,5,]), ([2,1,6,1,], [6,3,6,2,6,]), ([1,], [2,6,]), ([3,5,6,], []), ([5,5,], []), ([6,2,], [1,]))
for arg in args:
    total += IntSum(arg[0], arg[1])
print(total)