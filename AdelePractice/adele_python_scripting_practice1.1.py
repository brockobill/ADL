
def CaughtSpeeding(speed, is_birthday):
    """
    Determine the result of a speeding situation based on speed and birthday.

    Parameters:
    - speed (int): The driver's speed.
    - is_birthday (bool): True if it's the driver's birthday, False otherwise.

    Returns:
    - int: 0 for no ticket, 1 for a small ticket, 2 for a big ticket.
    """
    # adjust speed limit based on birthday
    if is_birthday: # checks if birthday bool is True
        speed -= 5 # if True subtracts 5 from speed limit

    # check the speed and return the corresponding result
    if speed <= 60:
        #print(f"Birthday = {is_birthday}: Speed = {speed} = no ticket")
        return 0 # no ticket
    elif 61 <= speed <= 80:
        #print(f"Birthday = {is_birthday}: Speed = {speed} = small ticket")
        return 1 # small ticket
    else:
        #print(f"Birthday = {is_birthday}: Speed = {speed} = big ticket")
        return 2 # big ticket

# pre defined test conditions
print("Test Cases:")    
try:
    """
    Each assert statement checks whether the result of calling CaughtSpeeding with 
    specific arguments matches the expected result. If any of these assertions fail 
    (i.e., the function doesn't produce the expected result), an AssertionError will 
    be raised, and the except block will catch it, printing "Failed on case" along with 
    the specific case that failed.

    If all assertions pass successfully, the print("Pass") statement will be executed, 
    indicating that all predefined test cases have produced the expected results.
    """
    assert CaughtSpeeding(65, False) == 1, "65, False" # (speed, is_birthday : 65 = 1)
    assert CaughtSpeeding(66, False) == 2, "66, False" # (assert should be 1 not 2 : should fail)
    assert CaughtSpeeding(65, True) == 0, "65, True"   # (speed, is_birthday : 65 = 60 = 0)
    assert CaughtSpeeding(60, False) == 0, "60, False" # (speed, is_birthday : 60 = 0)
    assert CaughtSpeeding(85, True) == 1, "85, True"   # (speed, is_birthday : 85 = 80 = 1)
    assert CaughtSpeeding(85, False) == 2, "85, False" # (speed, is_birthday : 85 = 2)
    print("Pass\n")

# error handling if the function fails any of the test cases
except AssertionError as e:
    print("Failed on case: " + str(e))

# use the printed total as the flag
total = 0
# note the "is birthday" speed will start at 45 (50-5)
for speed in range(50, 90): # iterates through each speed between 50 and 89
    # cumulative totals the flag ratings from the CaughtSpeeding function
    # no tickets + small tickets + big tickets
    total += CaughtSpeeding(speed, True)  # is birthday
    total += CaughtSpeeding(speed, False) # is not birthday
    # print(f'Cumulative Flag Total: {total}')
print(f'Flag Total of no+small+big Tickets: {total}')
