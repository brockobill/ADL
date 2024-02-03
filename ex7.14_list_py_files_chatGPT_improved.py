import os


def human_readable_size(size, decimal_places=2):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    for unit in units:
        if size < 1024.0 or unit == units[-1]:  # Last unit is TB
            if size % 1 == 0:  # Integer value
                return f"{int(size):>3} {unit}"  # Right-align the number, ensuring at least 3 digits
            else:
                return f"{size:>.{decimal_places}f} {unit}"  # Format float with specified decimal places
        size /= 1024.0



def list_python_files(directory):
    return [
        f
        for f in os.listdir(directory)
        if f.endswith(".py") and os.path.isfile(os.path.join(directory, f))
    ]


def print_header(max_length):
    header_name = "File Name"
    header_size = "File Size"
    header = f"{header_name:<{max_length}} | {header_size}"
    separator = "-" * len(header)
    print("\n" + separator)
    print("Python Files in Current Directory")
    print(separator)
    print(header)
    print(separator)


def print_file_details(file_names, directory):
    file_count = size_count = 0
    max_name_length = max(len(f) for f in file_names) if file_names else 0
    header_length = max(max_name_length, len("File Name"))

    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        file_size = os.path.getsize(file_path)
        if file_size > 1000:
            size_count += 1
        print(f"{file_name:<{header_length}} | {human_readable_size(file_size)}")
        file_count += 1
    return file_count, size_count


def main():
    directory = "."
    file_names = list_python_files(directory)
    if file_names:
        max_name_length = max(len(f) for f in file_names)
        print_header(max_name_length)
        file_count, size_count = print_file_details(file_names, directory)
        separator = "-" * (
            max_name_length + 12
        )  # Adjust based on header and size column widths
        print(separator)
        print(f"Number of files = {file_count}")
        print(f"Number of files larger than 1K bytes = {size_count}")
        print(separator + "\n")
    else:
        print("No Python files found.")


if __name__ == "__main__":
    main()
