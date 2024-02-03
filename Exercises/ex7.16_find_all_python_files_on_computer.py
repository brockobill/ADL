
"""
This program lists all python files on this computer.
"""

import os

file_paths = []  # list to store full paths of Python files
for root, dirs, files in os.walk('/'):  # '.' denotes the current directory
    for file in files:
        if file.endswith('.py'):
            full_path = os.path.join(root, file)
            file_paths.append(full_path)

max_path_length = len(max(file_paths, key=len)) if file_paths else 0
header_name = "File Path"
header_size = "Size (bytes)"
header_name_length = max(max_path_length, len(header_name))
header = f"{header_name:<{header_name_length}} | {header_size}"
separator = "-" * len(header)

# display header
print("\n")
print(separator)
print("Python Files on this Computer.")
print(separator)
print(header)
print(separator)

file_count = 0

for file_path in file_paths:
    file_size = os.path.getsize(file_path)
    print(f"{file_path:<{header_name_length}} | {file_size}")
    file_count += 1

print(separator)
print(header)
print(separator)
print(f'Number of Python files = {file_count}')
print(separator)
print("\n")            
                       