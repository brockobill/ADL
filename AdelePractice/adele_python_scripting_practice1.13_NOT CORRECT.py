# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given a dictionary of names and associated ages, return true if any
#    of the people have the same age, or one person is at least twice as
#    old as all other combined ages, otherwise return false.	               
#
# Examples:
#
#    SameAge({'Kim' : 5, 'Kate' : 4, 'Ken' : 6}) → False
#    SameAge({'Kim' : 5, 'Kate' : 4, 'Ken' : 4}) → True

from collections import Counter


"""
THIS GIVES AN FLAG OF 47 - BUT CORRECT ANSWER IS 35
"""
def SameAge(people):
    values = list(people.values())
    value_count = Counter(values)  
    count = 0

    if any(count >= 2 for count in value_count.values()):
        total_age = sum(values)
        for age in values:
            if age * 2 <= total_age - age:
                count += 1
                return count  # If one person is at least twice as old as all other combined ages, return True

    # Generate pairs of indices for values
    index_pairs = [(i, j) for i in range(len(values)) 
                for j in range(i + 1, len(values))]

    # Check if any two values are the same or one person is at least twice as old
    for i, j in index_pairs:
        if values[i] == values[j] or values[i] >= values[j]*2:
            return True  # Return True if any pair has equal values or twice the value

    return False  # Return False if no conditions are met


# Pre defined test conditions to help you out
try:
    assert SameAge({'Kim' : 5, 'Kate' : 4, 'Ken' : 6}) == False, "{'Kim' : 5 'Kate' : 4, 'Ken' : 6}"
    assert SameAge({'Kim' : 5, 'Kate' : 4, 'Ken' : 4}) == True, "{'Kim' : 5 'Kate' : 4, 'Ken' : 4}"
    assert SameAge({'Kim' : 10, 'Kate' : 5, 'Ken' : 4}) == True, "{'Kim' : 10 'Kate' : 5, 'Ken' : 4}"
    assert SameAge({'Kim' : 5}) == False, "{'Kim' : 5}"
    assert SameAge({}) == False, "{}"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))

# Use the printed total as the flag
total = 0
args = {"Kim" : 8, "Kate" : 4, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 6}, {"Kim" : 8, "Kate" : 9, "Ken" : 4}, {"Kim" : 4, "Kate" : 6, "Ken" : 5}, {"Kim" : 7, "Kate" : 9, "Ken" : 4}, {"Kim" : 8, "Kate" : 6, "Ken" : 4}, {"Kim" : 4, "Kate" : 7, "Ken" : 5}, {"Kim" : 7, "Kate" : 4, "Ken" : 6}, {"Kim" : 9, "Kate" : 7, "Ken" : 8}, {"Kim" : 4, "Kate" : 8, "Ken" : 9}, {"Kim" : 6, "Kate" : 7, "Ken" : 8}, {"Kim" : 8, "Kate" : 8, "Ken" : 6}, {"Kim" : 9, "Kate" : 5, "Ken" : 8}, {"Kim" : 6, "Kate" : 7, "Ken" : 4}, {"Kim" : 7, "Kate" : 4, "Ken" : 9}, {"Kim" : 7, "Kate" : 9, "Ken" : 5}, {"Kim" : 6, "Kate" : 5, "Ken" : 7}, {"Kim" : 6, "Kate" : 8, "Ken" : 8}, {"Kim" : 6, "Kate" : 9, "Ken" : 4}, {"Kim" : 6, "Kate" : 4, "Ken" : 8}, {"Kim" : 5, "Kate" : 8, "Ken" : 5}, {"Kim" : 8, "Kate" : 6, "Ken" : 9}, {"Kim" : 7, "Kate" : 9, "Ken" : 8}, {"Kim" : 9, "Kate" : 4, "Ken" : 6}, {"Kim" : 5, "Kate" : 5, "Ken" : 8}, {"Kim" : 4, "Kate" : 9, "Ken" : 5}, {"Kim" : 6, "Kate" : 6, "Ken" : 6}, {"Kim" : 6, "Kate" : 8, "Ken" : 7}, {"Kim" : 9, "Kate" : 8, "Ken" : 4}, {"Kim" : 8, "Kate" : 8, "Ken" : 4}, {"Kim" : 4, "Kate" : 8, "Ken" : 5}, {"Kim" : 4, "Kate" : 9, "Ken" : 5}, {"Kim" : 5, "Kate" : 5, "Ken" : 7}, {"Kim" : 8, "Kate" : 5, "Ken" : 8}, {"Kim" : 9, "Kate" : 7, "Ken" : 5}, {"Kim" : 4, "Kate" : 6, "Ken" : 5}, {"Kim" : 5, "Kate" : 8, "Ken" : 9}, {"Kim" : 6, "Kate" : 8, "Ken" : 9}, {"Kim" : 4, "Kate" : 7, "Ken" : 4}, {"Kim" : 7, "Kate" : 8, "Ken" : 4}, {"Kim" : 4, "Kate" : 9, "Ken" : 6}, {"Kim" : 8, "Kate" : 6, "Ken" : 9}, {"Kim" : 7, "Kate" : 8, "Ken" : 6}, {"Kim" : 8, "Kate" : 6, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 4}, {"Kim" : 6, "Kate" : 6, "Ken" : 4}, {"Kim" : 5, "Kate" : 8, "Ken" : 6}, {"Kim" : 5, "Kate" : 8, "Ken" : 5}, {"Kim" : 6, "Kate" : 9, "Ken" : 6}, {"Kim" : 7, "Kate" : 9, "Ken" : 8}, {"Kim" : 9, "Kate" : 6, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 9}, {"Kim" : 4, "Kate" : 5, "Ken" : 7}, {"Kim" : 6, "Kate" : 5, "Ken" : 5}, {"Kim" : 8, "Kate" : 7, "Ken" : 8}, {"Kim" : 5, "Kate" : 8, "Ken" : 6}, {"Kim" : 6, "Kate" : 8, "Ken" : 6}, {"Kim" : 9, "Kate" : 8, "Ken" : 9}, {"Kim" : 4, "Kate" : 9, "Ken" : 7}, {"Kim" : 7, "Kate" : 8, "Ken" : 9}, {"Kim" : 6, "Kate" : 8, "Ken" : 7}, {"Kim" : 5, "Kate" : 7, "Ken" : 4}, {"Kim" : 5, "Kate" : 9, "Ken" : 6}, {"Kim" : 4, "Kate" : 5, "Ken" : 4}, {"Kim" : 9, "Kate" : 5, "Ken" : 8}, {"Kim" : 7, "Kate" : 6, "Ken" : 9}, {"Kim" : 8, "Kate" : 8, "Ken" : 5}, {"Kim" : 8, "Kate" : 8, "Ken" : 7}, {"Kim" : 6, "Kate" : 7, "Ken" : 8}, {"Kim" : 7, "Kate" : 6, "Ken" : 8}, {"Kim" : 7, "Kate" : 8, "Ken" : 6}, {"Kim" : 4, "Kate" : 7, "Ken" : 9}, {"Kim" : 4, "Kate" : 8, "Ken" : 5}, {"Kim" : 8, "Kate" : 8, "Ken" : 9}, {"Kim" : 5, "Kate" : 9, "Ken" : 9}, {"Kim" : 5, "Kate" : 9, "Ken" : 5}, {"Kim" : 7, "Kate" : 9, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 7}, {"Kim" : 6, "Kate" : 6, "Ken" : 8}, {"Kim" : 5, "Kate" : 9, "Ken" : 9}, {"Kim" : 5, "Kate" : 8, "Ken" : 4}, {"Kim" : 6, "Kate" : 8, "Ken" : 5}, {"Kim" : 9, "Kate" : 9, "Ken" : 9}, {"Kim" : 9, "Kate" : 4, "Ken" : 6}, {"Kim" : 4, "Kate" : 5, "Ken" : 4}, {"Kim" : 8, "Kate" : 9, "Ken" : 7}, {"Kim" : 4, "Kate" : 6, "Ken" : 9}, {"Kim" : 4, "Kate" : 9, "Ken" : 8}, {"Kim" : 8, "Kate" : 9, "Ken" : 4}, {"Kim" : 5, "Kate" : 8, "Ken" : 5}, {"Kim" : 9, "Kate" : 5, "Ken" : 6}, {"Kim" : 8, "Kate" : 8, "Ken" : 4}, {"Kim" : 9, "Kate" : 9, "Ken" : 7}, {"Kim" : 9, "Kate" : 6, "Ken" : 8}, {"Kim" : 4, "Kate" : 4, "Ken" : 7}, {"Kim" : 7, "Kate" : 9, "Ken" : 5}, {"Kim" : 8, "Kate" : 9, "Ken" : 4}, {"Kim" : 7, "Kate" : 5, "Ken" : 8}, {"Kim" : 4, "Kate" : 6, "Ken" : 7}, {"Kim" : 6, "Kate" : 7, "Ken" : 6}
for arg in args:
    total += SameAge(arg)
print(total)