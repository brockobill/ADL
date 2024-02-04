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
    def is_close(x, y):
        """
        Checks whether the absolute difference between x and y is less than or equal to 1.
        We only need to check is_close of all parameter combos because if not is_close
        than it is is_far.
        We check if pairs (ab,ac), (ba, bc), and (ca, cb) are close, while the other 
        pairs are not close.
        """
        return abs(x - y) <= 1

    # checks if one pair (a and b or a and c) is "close" 
    # while the other pair is not "close" to each other. 
    # If this condition is met, it returns True.
    if (is_close(a, b) and not is_close(a, c) and not is_close(b, c)) or \
       (is_close(a, c) and not is_close(a, b) and not is_close(c, b)):
        return True
    
    # checks the same for the pair (b and a or b and c).
    elif (is_close(b, a) and not is_close(b, c) and not is_close(a, c)) or \
         (is_close(b, c) and not is_close(b, a) and not is_close(c, a)):
        return True
    
    # checks the same for the pair (c and a or c and b).
    elif (is_close(c, a) and not is_close(c, b) and not is_close(a, b)) or \
         (is_close(c, b) and not is_close(c, a) and not is_close(b, a)):
        return True
    
    # If none of the conditions are met, it falls back to the else statement and 
    # returns False.
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
