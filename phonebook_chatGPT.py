
"""
phonebook_chatGPT.py is a different solution to my original phonebook csv_read.py file.
"""
def is_valid_phone_number(phone_num):
    """
    Example validation: checks if the phone number contains only digits and has a length of 10
    This can be replaced or expanded with more complex validation as needed
    """
    return phone_num.isdigit() and len(phone_num) == 10

# welcome messages
print("\nWelcome to the phone number program!")
print("Enter person's name and phone number or hit enter to finish entering details.")

# 'with' ensures the file is properly closed after appending data
try: # try block catches exceptions for open/read file
    with open('phonebook.csv', 'a') as phonebook:
        while True: # loop until user has finished entering data
            name = input("\nEnter person's name: ")
            if name == "": # exit loop if name is empty
                break  
            phone_num = input("Enter person's phone: ")

            if is_valid_phone_number(phone_num): # vlidate phone number before writing
                phonebook.write(f'{name}, {phone_num}\n') # if valid writes data to file
            else: # otherwise gives error message
                print("Invalid phone number entered. Please enter a 10-digit phone number.")
except IOError as e: # error handling
    print(f"Error opening/reading file: {e}")

# reading and printing the data with error handling
try: # try block to handle file open erros
    with open('phonebook.csv', 'r') as phonebook: # reads phonebook
        for line in phonebook: # reads each line in phonebook
            if not line.strip() or ',' not in line: # skip empty or no comma lines
                continue
            name, phone_num = line.strip().split(',', 1)  # splits on first comma only and removes whitespace
            print(f'{name}, {phone_num}') # displays phonebook data
except IOError as e: # error handling
    print(f"Error opening/reading file: {e}")
