# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given 3 integer values, a b c, return their sum. However, if one
#    of the values is the same as another of the values, it does not
#    count towards the sum.               
#
# Examples:
#
#    LoneSum(1, 2, 3) → 6
#    LoneSum(3, 2, 3) → 2


# Write you function code below
def LoneSum(a, b, c):
    """ Enter your code here
    """

    if a!=b and a!=c and b!=c:
        return a+b+c
    if a==b==c:
        return 0
    if a==c:
        return b
    if a==b:
        return c
    if b==c:
        return a
        
# Pre defined test conditions to help you out
try:
    assert LoneSum(1,2,3) == 6, "1,2,3"
    assert LoneSum(3,2,3) == 2, "3,2,3"
    assert LoneSum(2,4,3) == 9, "2,4,3"
    assert LoneSum(3,3,3) == 0, "3,3,3"
    assert LoneSum(1,3,1) == 3, "1,3,1"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            total += LoneSum(a, b, c)
print(total)