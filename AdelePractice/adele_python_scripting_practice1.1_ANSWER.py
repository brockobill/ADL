
def CaughtSpeeding(speed, is_birthday):
    result=0
    if is_birthday == False:
      if speed <= 60: return result
      if speed >= 61 and speed <=80 : return (result+1)
      if speed >= 81 : return (result+2)
    else:
      if speed <= 65: return result
      if speed >= 66 and speed <=85 : return (result+1)
      if speed >= 86 : return (result+2)



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
