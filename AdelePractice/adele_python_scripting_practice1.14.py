# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given a dictionary of names and associated ages, return the age of
#    the oldest person, unless there is a tie, then return the next
#    oldest. Return -1 if there is no answer.	               
#
# Examples:
#
#    FindMax({'Jon' : 30, 'Jim' : 10, 'Jen' : 50}) → 50
#    FindMax({}) → -1

# Write your function code below
def FindMax(people):
    # Check if the dictionary is empty
    if not people:
        return -1

    # Extract values from the dictionary
    values = list(people.values())

    # find mage age
    max_age = max(values)

    # determine if more than one max age
    if values.count(max_age) == 1:
        return max_age
    
    else: # otherwise find next oldest age by sorting ages
        sorted_values = sorted(set(values), reverse=True)
        if len(sorted_values) >= 2:
            next_oldest_age = (sorted_values[1])
            return next_oldest_age
        else:
            return -1  # Return -1 if there is no answer.
                     
# Pre defined test conditions to help you out
try:
    assert FindMax({'Jon' : 30, 'Jim' : 10, 'Jen' : 50}) == 50, "{'Jon' : 30, 'Jim' : 10, 'Jen' : 50}"
    assert FindMax({'Jon' : 50, 'Jim' : 30, 'Jen' : 50}) == 30, "{'Jon' : 50, 'Jim' : 30, 'Jen' : 50}"
    assert FindMax({'Jon' : 10, 'Jim' : 10}) == -1, "{'Jon' : 10, 'Jim' : 10}"
    assert FindMax({'Jon' : 11, 'Jim' : 10, 'Jen' : 12}) == 12, "{'Jon' : 11, 'Jim' : 10, 'Jen' : 12}"
    assert FindMax({}) == -1, "{}"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = {"Kim" : 8, "Kate" : 4, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 6}, {"Kim" : 8, "Kate" : 9, "Ken" : 4}, {"Kim" : 4, "Kate" : 6, "Ken" : 5}, {"Kim" : 7, "Kate" : 9, "Ken" : 4}, {"Kim" : 8, "Kate" : 6, "Ken" : 4}, {"Kim" : 4, "Kate" : 7, "Ken" : 5}, {"Kim" : 7, "Kate" : 4, "Ken" : 6}, {"Kim" : 9, "Kate" : 7, "Ken" : 8}, {"Kim" : 4, "Kate" : 8, "Ken" : 9}, {"Kim" : 6, "Kate" : 7, "Ken" : 8}, {"Kim" : 8, "Kate" : 8}, {"Kim" : 9, "Kate" : 5, "Ken" : 8}, {"Kim" : 6, "Kate" : 7, "Ken" : 4}, {"Kim" : 7, "Kate" : 4, "Ken" : 9}, {"Kim" : 7, "Kate" : 9, "Ken" : 5}, {"Kim" : 6, "Kate" : 5, "Ken" : 7}, {"Kim" : 8, "Kate" : 8, "Ken" : 8}, {"Kim" : 6, "Kate" : 9, "Ken" : 4}, {"Kim" : 6}, {"Kim" : 5, "Kate" : 8, "Ken" : 5}, {}, {"Kim" : 7, "Kate" : 9, "Ken" : 8}, {"Kim" : 9, "Kate" : 4, "Ken" : 6}, {"Kim" : 5, "Kate" : 5, "Ken" : 8}, {"Kim" : 4, "Kate" : 9, "Ken" : 5}, {"Kim" : 6, "Kate" : 6, "Ken" : 6}, {"Kim" : 6, "Kate" : 8, "Ken" : 7}, {"Kim" : 9, "Kate" : 8, "Ken" : 4}, {"Kim" : 8, "Kate" : 8, "Ken" : 4}, {"Kim" : 4, "Kate" : 8, "Ken" : 5}, {"Kim" : 4, "Kate" : 9, "Ken" : 5}, {"Kim" : 5, "Kate" : 5, "Ken" : 7}, {"Kim" : 8, "Kate" : 5, "Ken" : 8}, {"Kim" : 9, "Kate" : 7, "Ken" : 5}, {"Kim" : 4, "Kate" : 6, "Ken" : 5}, {"Kim" : 5, "Kate" : 8, "Ken" : 9}, {"Kim" : 6, "Kate" : 8, "Ken" : 9}, {"Kim" : 4, "Kate" : 7, "Ken" : 4}, {"Kim" : 7, "Kate" : 8, "Ken" : 4}, {"Kim" : 4, "Kate" : 9, "Ken" : 6}, {"Kim" : 8, "Kate" : 6, "Ken" : 9}, {"Kim" : 7, "Kate" : 8, "Ken" : 6}, {"Kim" : 8, "Kate" : 6, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 4}, {"Kim" : 6, "Kate" : 6, "Ken" : 4}, {"Kim" : 5, "Kate" : 8, "Ken" : 6}, {"Kim" : 5, "Kate" : 8, "Ken" : 5}, {"Kim" : 6, "Kate" : 9, "Ken" : 6}, {"Kim" : 7, "Kate" : 9, "Ken" : 8}, {"Kim" : 9, "Kate" : 6, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 9}, {"Kim" : 4, "Kate" : 5, "Ken" : 7}, {"Kim" : 6, "Kate" : 5, "Ken" : 5}, {"Kim" : 8, "Kate" : 7, "Ken" : 8}, {"Kim" : 5, "Kate" : 8, "Ken" : 6}, {"Kim" : 6, "Kate" : 8, "Ken" : 6}, {"Kim" : 9, "Kate" : 8, "Ken" : 9}, {"Kim" : 4, "Kate" : 9, "Ken" : 7}, {"Kim" : 7, "Kate" : 8, "Ken" : 9}, {"Kim" : 6, "Kate" : 8, "Ken" : 7}, {"Kim" : 5, "Kate" : 7, "Ken" : 4}, {"Kim" : 5, "Kate" : 9, "Ken" : 6}, {"Kim" : 4, "Kate" : 5, "Ken" : 4}, {"Kim" : 9, "Kate" : 5, "Ken" : 8}, {"Kim" : 7, "Kate" : 6, "Ken" : 9}, {"Kim" : 8, "Kate" : 8, "Ken" : 5}, {"Kim" : 8, "Kate" : 8, "Ken" : 7}, {"Kim" : 6, "Kate" : 7, "Ken" : 8}, {"Kim" : 7, "Kate" : 6, "Ken" : 8}, {"Kim" : 7, "Kate" : 8, "Ken" : 6}, {"Kim" : 4, "Kate" : 7, "Ken" : 9}, {"Kim" : 4, "Kate" : 8, "Ken" : 5}, {"Kim" : 8, "Kate" : 8, "Ken" : 9}, {"Kim" : 5, "Kate" : 9, "Ken" : 9}, {"Kim" : 5, "Kate" : 9, "Ken" : 5}, {"Kim" : 7, "Kate" : 9, "Ken" : 5}, {"Kim" : 7, "Kate" : 7, "Ken" : 7}, {"Kim" : 6, "Kate" : 6, "Ken" : 8}, {"Kim" : 5, "Kate" : 9, "Ken" : 9}, {"Kim" : 5, "Kate" : 8, "Ken" : 4}, {"Kim" : 6, "Kate" : 8, "Ken" : 5}, {"Kim" : 9, "Kate" : 9, "Ken" : 9}, {"Kim" : 9, "Kate" : 4, "Ken" : 6}, {"Kim" : 4, "Kate" : 5, "Ken" : 4}, {"Kim" : 8, "Kate" : 9, "Ken" : 7}, {"Kim" : 4, "Kate" : 6, "Ken" : 9}, {"Kim" : 4, "Kate" : 9, "Ken" : 8}, {"Kim" : 8, "Kate" : 9, "Ken" : 4}, {"Kim" : 5, "Kate" : 8, "Ken" : 5}, {"Kim" : 9, "Kate" : 5, "Ken" : 6}, {"Kim" : 8, "Kate" : 8, "Ken" : 4}, {"Kim" : 9, "Kate" : 9, "Ken" : 7}, {"Kim" : 9, "Kate" : 6, "Ken" : 8}, {"Kim" : 4, "Kate" : 4, "Ken" : 7}, {"Kim" : 7, "Kate" : 9, "Ken" : 5}, {"Kim" : 8, "Kate" : 9, "Ken" : 4}, {"Kim" : 7, "Kate" : 5, "Ken" : 8}, {"Kim" : 4, "Kate" : 6, "Ken" : 7}, {"Kim" : 6, "Kate" : 7, "Ken" : 6}
for arg in args:
    total += FindMax(arg)
print(total)