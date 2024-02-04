# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    You are driving a little too fast, and a police officer stops you.
#    Write code to compute the result, encoded as an int value: 
#        0 = no ticket,
#        1 = small ticket,
#        2 = big ticket.
#    If speed is 60 or less, the result is 0. If speed is between 61 and
#    80 inclusive, the result is 1. If speed is 81 or more, the result 
#    is 2. Unless it is your birthday -- on that day, your speed can be
#    5 higher in all cases.
#
# Examples:
#
#    CaughtSpeeding(65, False) → 1
#    CaughtSpeeding(65, True) → 0


# Write your function code below
def CaughtSpeeding(speed, is_birthday):
    """ Enter your code here
    """
    count = 0
    if is_birthday:
        if speed <= 65: count += 0
        if speed >= 66 and speed <= 85: count += 1
        if speed >= 86: count += 2
    else:
        if speed <= 60: count += 0
        if speed >= 61 and speed <= 80: count += 1
        if speed >= 81: count += 2
    return count    

# Pre defined test conditions to help you out
try:
    assert CaughtSpeeding(65, False) == 1, "65, False"
    assert CaughtSpeeding(65, True) == 0, "65, True"
    assert CaughtSpeeding(60, False) == 0, "60, False"
    assert CaughtSpeeding(85, True) == 1, "85, True"
    assert CaughtSpeeding(85 , False) == 2, "85, False"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
for speed in range(50,90):
    total += CaughtSpeeding(speed, True)
    total += CaughtSpeeding(speed, False)
print(total)
