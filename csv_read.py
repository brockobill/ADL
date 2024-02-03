
"""
csv_read is a simple phonebook to demo read/write to csv file.

"""

# Open phonebook.csv file in append mode, allowing new data to be added to end of file
phonebook = open('phonebook.csv', 'a')

# Print welcome message and instructions for the user
print("\nWelcome to the phone number program!")
print("Enter person's name and phone number or hit enter to finish entering details.")

# Start infinite loop to continuously prompt tuser for input
while True:
    # Prompt user to enter a person's name
    name = input("\nEnter person's name: ")
    
    # If user input for name is empty, close file and break out of loop
    if name == "":
        phonebook.close()
        break
    else:
        # If a name is provided, prompt for person's phone number
        phone_num = input("Enter person's phone: ")
        # Write name and phone number to file, separated by a comma and followed by a newline
        phonebook.write(f'{name}, {phone_num}\n')

# After breaking out of loop, reopen the phonebook.csv file in read mode to display its contents
phonebook = open('phonebook.csv', 'r')
for line in phonebook:
    # Skip any lines that are empty or contain only whitespace
    if not line.strip():
        break
    # Split each line by comma to separate name and phone number, and print them
    name, phone_num = line.split(',')
    print(f'{name}, {phone_num.strip()}')
    
# Close the file after reading its contents
phonebook.close()
     
   