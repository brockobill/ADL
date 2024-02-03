"""
This program lists and counts all python files in current directory.
"""

import os

# file name list
file_names = [f for f in os.listdir() if f.endswith('.py')] # finds python files in current directory

# variables
max_name_length = len(max(file_names, key=len)) # gets length of file with longest file name
header_name = "File Name"
header_size = "File Size (bytes)"
header_name_length = max(max_name_length, len(header_name)) # matches header to max file name length
header = f"{header_name:<{header_name_length}} | {header_size}" # table header
separator = "-" * len(header)

# display header
print("\n")
print(separator)
print("Python Files in Current Directory")
print(separator)
print(header)
print(separator)

file_count = 0 # counter for number of python files
size_count = 0 # counts number of files larger than 1K bytes

# loop to read and print each python file on a new line
for file_name in file_names:
    file_size = os.path.getsize(file_name)
    if file_size > 1000: # check file size
        size_count += 1 # file size counter if size > 1K
    print(f"{file_name:<{header_name_length}} | {file_size}")
    file_count += 1 # python file counter

# displays number of python files counted and files > 1K in size
print(separator)
print(f'Number of files = {file_count}')
print(f'Number of files larger than 1K bytes = {size_count}')
print(separator)
print("\n")
