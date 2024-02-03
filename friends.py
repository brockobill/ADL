"""
friends.py is a program thta saves your lits of friends.
"""

import sys # imports module for exiting program
import os # imports module clearing the terminal screen
friends_list = []  # create empty list


def display_friends(friends_list):
    """
    This function displays current friends list.
    """
    for friends in friends_list:  # iterates through friends list
        print(friends)  # display each friend on a new line


def new_friend():
    """
    This function adds a new friend to the list.
    """
    new_name = input("\nEnter your new friend: ")
    position = int(input(f"What position (starting at 1) do you want {new_name}?: "))
    actual_position = position - 1 # subtracts 1 so user places person in actual position (negates 0 index issue)
    friends_list.insert(actual_position, new_name) # inserts friend into list
    display_friends(friends_list) # calls the display_friends function


def remove_friend():
    """
    This function removes friends from list and gives us insult if you have no friends.
    """
    remove_friend = input("\nEnter friend you want to remove from list: ")
    if remove_friend in friends_list: # checks if friend in list
        friends_list.remove(remove_friend) # removes friend if in list
    else:
        print(f"{remove_friend} not in friends list!") # error handling message
        menu_choice()


def exit_friends():
    '''
    This function allows user to exits the friends program.
    '''
    os.system("cls" if os.name == "nt" else "clear")
    print("Goodbye!\n")
    sys.exit()


def menu_choice():
    """
    This function gives the user menu_choice options to add, remove or view friends, or exit the program.
    """
    
    while True:
        print(
            "\nDo you want to add a new friend, remove an existing friend, view friends, or exit?"
        )
        menu_choice = input(
            "Hit 'a' to add friend, hit 'r' to remove friend, 'v' to view friends, or 'x' to exit: "
        )
        # menu_choice selections
        if menu_choice == "a":
            new_friend()
        elif menu_choice == "r":
            remove_friend()
        elif menu_choice == "v":
            current_friends()
        elif menu_choice == "x":
            exit_friends()
        else: # error handling
            print("Invalid entry. Try again!")
            continue


def current_friends():
    """
    The current_friends function is used to display current friends in the list.
    """
    while True:
        print(
            f"\nYou have {len(friends_list)} friends."
        )  # count and display number of friends
        if len(friends_list) == 0:
            print("Nice One Nigel No Mates!!")
        else:
            print("\nYour friends are:")
            display_friends(friends_list)
        menu_choice()


def user_entry():
    '''
    The user_entry function prompts the user to enter the first batch of friends.
    '''
    print(
        "\n\nEnter your friend's name and hit enter after each entry. Press enter with no input to finish: "
    ) 
    # continues loop until nothing entered by user
    while True:
        name = input()
        if name == "":
            current_friends()
        else:
            friends_list.append(name)
        

user_entry()  # call first function
