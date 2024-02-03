'''
This program displays a person's age and certain messages about their age.
The program also handles errors when a person enters incorrect data.
'''
while True: # start loop
    age = input("What is your age: ") # get user to enter age

    try: # start error handling
        age_int = int(age) # makes age int for error checking
        if 1 <= age_int <= 130: # checks age is between 1 and 130             
            print("Your age is ", age) # displays age if between 1 and 130
            if age_int >= 53: # if age equal to or over 53 display a message
                print("You're older than Brock and must be very wise like him!")
            else: # otherwise (age under 53) display this message
                print("You're a spring chicken!")    
            next_birthday = age_int + 1 # add 1 for next birthday age
            print("You will be", str(next_birthday), "next birthday.") # display next birthday age
            break # ends loop
        else:
            print("Please enter a number between 1 and 130.") # returns to start of loop if error
    except ValueError:
        print("That's not a valid number. Please try again.") # handles not an integer error

