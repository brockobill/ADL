
'''
dice.py simulates rolling two six-sided dice
'''
import random # random int selection module

dice_1 = random.randint(1, 6) # dice_1 selects random num between 1 and 6
dice_2 = random.randint(1, 6) # dice_2 selects random num between 1 and 6

print("D1: ", str(dice_1)) # displays dice_1 num in string format
print("D2: ", str(dice_2)) # displays dice_2 num in string format

if (dice_1 == 1 and dice_2 == 1):
    print("SNAKE-EYES!") # display message if both dice show 1


