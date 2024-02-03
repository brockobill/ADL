
'''
cm_to_inches_function.py is a user defined function to convert a number in centimetres to inches.
'''

# this functions returns converted centimetre to inches calculation
def cm_to_inches(cm):
    return cm / 2.54

# this is a display box function
def print_box():
    print('-' * 72)
    print('|' + ' ' * 70 + '|')
    print('|' + "Enter a number to convert from centimetres to inches or 'x' to exit:".center(70) + '|')
    print('|' + ' ' * 70 + '|')
    print('-' * 72)


while True: # while loop to repat user prompt if bad imput or new etry
    print_box() # calls the print_box function
    num = input("number: ") # prompts user to enter number for conversion

    # let's user exit
    if num == 'x':
        print("Goodbye!\n") # goodbye message
        break

    try: # try block to handle bad input exceptions
        num = float(num) # enables floats to be entered
        result = cm_to_inches(num) # calls the cm_to_inches function with user entry parameter
        print(f'{num} cm is {result:.2f} inches\n') # rounds float ansers to two decimal places
    except ValueError: # bad input exception handling
        print("That's not a valid number. Please try again.\n") # error message

        