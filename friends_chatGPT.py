"""
friends.py is a program that saves your list of friends.
"""

import sys, os  # imports module for exiting program and clearing the terminal screen
friends_list = []  # create empty list


def display_friends():
    """
    This function displays the current friends list.
    """
    for friend in friends_list:  # iterates through friends list
        print(friend)  # display each friend on a new line


def new_friend():
    """
    This function adds a new friend to the list.
    """
    new_name = input("\nEnter your new friend: ")
    position = int(input(f"What position (starting at 1) do you want {new_name}?: "))
    actual_position = position - 1  # subtracts 1 so user places person in actual position (negates 0 index issue)
    friends_list.insert(actual_position, new_name)  # inserts friend into list
    display_friends()  # calls the display_friends function


def remove_friend():
    """
    This function removes friends from the list and gives us an insult if you have no friends.
    """
    remove_friend = input("\nEnter the friend you want to remove from the list: ")
    if remove_friend in friends_list:  # checks if friend in list
        friends_list.remove(remove_friend)  # removes friend if in list
    else:
        print(f"{remove_friend} is not in the friends list!")  # error handling message


def exit_friends():
    """
    This function allows the user to exit the friends program.
    """
    os.system("cls" if os.name == "nt" else "clear")
    print("Goodbye!\n")
    sys.exit()


def menu():
    """
    This function gives the user menu options to add, remove or view friends, or exit the program.
    """
    while True:
        print(
            "\nDo you want to add a new friend, remove an existing friend, view friends, or exit?"
        )
        menu_choice = input(
            "Hit 'a' to add a friend, hit 'r' to remove a friend, 'v' to view friends, or 'x' to exit: "
        )
        # menu selections
        if menu_choice == "a":
            new_friend()
        elif menu_choice == "r":
            remove_friend()
        elif menu_choice == "v":
            display_friends()
        elif menu_choice == "x":
            exit_friends()
        else:  # error handling
            print("Invalid entry. Try again!")


def user_entry():
    """
    The user_entry function prompts the user to enter the first batch of friends.
    """
    print(
        "\nEnter your friend's name and hit enter after each entry. Press enter with no input to finish: "
    )
    # continues loop until nothing entered by user
    while True:
        name = input()
        if name == "":
            break  # Exit the loop when no input is given
        else:
            friends_list.append(name)
    menu()  # Call the menu after finishing the initial entry


user_entry()  # call first function
