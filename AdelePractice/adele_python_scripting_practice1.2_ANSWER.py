# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given three integers, a b c, return True if one of a, b or c is
#    "close" (differing from another by at most 1), while the other
#    is "far", (differing from both other values by 2 or more).
#    Note: abs(num) computes the absolute value of a number.
#
# Examples:
#
#    CloseFar(1, 2, 10) → True
#    CloseFar(1, 2, 3) → False

def CloseFar(a, b, c):
    r1 = abs(a-b)
    r2 = abs(a-c)
    r3 = abs(b-c)
    if r1 <= 1 or r2 <= 1 or r3 <= 1:
        if (r1 >= 2 and r2 >= 2) or (r1 >= 2 and r3 >= 2) or (r2 >= 2 and r3 >= 2):
            return True
        else:
            return False
    else:
        return False


# Pre defined test conditions to help you out
try:
    assert CloseFar(1, 2, 10) == True, "1,2,10"
    assert CloseFar(1, 2, 3) == False, "1,2,3"
    assert CloseFar(4, 5, 3) == False, "4,5,3"
    assert CloseFar(10, 10, 8) == True, "10,10,8"
    assert CloseFar(8, 6, 9) == True, "8,6,9"
    print("Pass")

except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            total += CloseFar(a, b, c)
print(total)
