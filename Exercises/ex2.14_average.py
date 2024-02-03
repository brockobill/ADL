'''
average.py is a program that stores user entered numbers in an array and takes the average of those numbers.
'''


def average(numbers):
    '''
    This function takes the average of the numbers in the number array.
    It also handles divide by zero errors.
    '''
    len_nums = len(numbers) # counts number of integers/floats in the array_nums
    sum_nums = sum(numbers) # sums the integers/floats in the array_nums
    
    if len_nums > 0: # divide by zero error handling
        average_nums = sum_nums / len_nums # calculates average
        return average_nums # returns average to main program block for display
    else:
        print("Cannot divide by zero.")
        return None
  
    

def print_box():
    '''
    This functions creates a display box for the user.
    '''    
    print('-' * 84)
    print('|' + ' ' * 82 + '|')
    print('|' + "Enter numbers for averaging then hit 'a' to average, 'e' to empty, or 'x' to exit.".center(82) + '|')
    print('|' + ' ' * 82 + '|')
    print('-' * 84)
    print(f'Numbers added so far {array_nums}') # displays the numbers in the numbers array

array_nums = [] # create an array to store user entered numbers


# start loop for display box 
while True:
    print_box()
    num = input("number: ") # user prompt

    # exit program if 'x' selected
    if num.lower() == 'x': # changes entry to lowercase
        print("Goodbye!\n")
        break
    
    # call the average function when 'a' selected
    elif num.lower() == 'a':
        #if len(array_nums) > 0:
        if len(array_nums) == 0:    
            formatted_average = average(array_nums)
            print(f'Average: {formatted_average:.2f} \n')
        '''else:
            print("No numbers entered to average.\n")
        continue'''
    
    # empty array if 'e' selected
    elif num.lower() == 'e':
        array_nums = [] # creates an empty array
        print("Array emptied!\n") 
        continue          

    # try block to add nums to array only if floats or integers
    try:
        num = float(num) 
        array_nums.append(num)
    except ValueError: # catches exception errors when entry is not a float or integer
        print("That's not a valid number. Please try again.\n")
            