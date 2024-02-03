import random # imports the random module

num = random.randint(1, 100) # selects a random number between 1 and 100
count = 0 # sets the counter variable to 0

while True: # start a while loop to continue until max guesses reached
    try:                       
        if count == 5: # sets the condition for the while loop
            print("max guesses reached - game over!") # game over message
            break # breaks the loop
        
        user_input = int(input('Guess a number between 1 and 100: '))      
        
        if 1 <= user_input <= 100:
            count += 1 
            print(f"guess = {count}/5")                              

            if user_input < num:
                print("The number is higher than your guess.")
            elif user_input > num:
                print("The number is lower than your guess.")
            else:
                print("CORRECT!")
                print('Number of guesses =', str(count))
                break
        else:
            print("Please enter a number between 1 and 100.")

    except ValueError:
        print("That's not a valid number. Please try again.")
