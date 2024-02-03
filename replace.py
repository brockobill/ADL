"""
replace program replaces and removes text in a user entered string.
"""

#user_string = input("\nEnter a string: ")
user_string = "The quick Brown fox jumped ovEr thE lazy dOG"

new_string = user_string.replace("e", "ay")
print(f"\n\nUser string: {user_string}")
print(f"New string: {new_string.lower()}")

vowels = "aeiouAEIOU"

# use iteration to replace vowels
for letter in vowels:
    vowels_removed_string = user_string.replace(letter, "")
print(f"Remove vowels using iteration: {vowels_removed_string.lower()}")    

# use translate to remove vowels
vowels_removed_string = user_string.translate(str.maketrans("", "", vowels))
print(f"Remove vowels using translate: {vowels_removed_string.lower()}")

"""
The maketrans() method in Python is used to create a translation table, which is a mapping of integers 
or characters to other integers, characters, or None. This translation table is then used by the 
translate() method of strings to replace specified characters. The maketrans() method is a static 
method of the str class.

intab is a string of characters to be replaced.
outtab is a string of characters that intab is replaced with.
str.maketrans(intab, outtab) creates a translation table that maps each character in intab to the 
corresponding character in outtab.
text.translate(transtab) uses this table to replace characters in text.

### replace text using maketrans() ###
intab = "aeiou"
outtab = "12345"
transtab = str.maketrans(intab, outtab)
text = "This is an example."
translated_text = text.translate(transtab)
print(translated_text)  # Output: Th3s 3s 1n 2x1mpl2.

### remove text using maketrans() ###
text = "This is an example."
to_remove = "aeiou"
transtab = str.maketrans('', '', to_remove)
removed_text = text.translate(transtab)
print(removed_text)  # Output: Ths s n xmpl.

"""

# use list comprehension to remove vowels
vowels_removed_string = "".join(char for char in user_string if char not in vowels)
print(f"Remove vowels using list comprehension: {vowels_removed_string.lower()}")

"""
The line of code vowels_removed_string = ''.join(char for char in user_string if char not in vowels) 
is a Python expression that creates a new string, vowels_removed_string, by removing all vowels from 
user_string. Let's break down how it works:

List Comprehension: This code uses a list comprehension, which is a concise way to create a new list 
in Python. The list comprehension is enclosed in brackets [ ], but in this case, it's actually a 
generator expression because the brackets are omitted. The expression iterates over each character 
in user_string.

Iteration: for char in user_string iterates over each character in user_string. For each iteration, 
char represents the current character.

Conditional Filter: if char not in vowels is a conditional filter that checks if the current character 
is not in the string vowels. The vowels string typically contains all vowels like "aeiouAEIOU".

Joining Characters: ''.join(...) joins each character from the generator expression into a new string. 
The join() method is called on an empty string '', which means it concatenates the characters without 
adding any additional characters in between them.

"""
print("\n")