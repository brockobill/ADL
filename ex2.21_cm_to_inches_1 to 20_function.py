'''
cm_to_inches_function_20.py is a user defined function to convert 1 to 20 centimetres into inches.
'''


def cm_to_inches(cm):
    """
    This functions returns converted centimetre to inches calculation.
    """
    return cm / 2.54

def print_box():
    """
    This function creates the display table.
    "{:<12}" means the first placeholder ("Centimetres") is left-aligned (<) within a field of 12 characters wide.
    "|" is a literal character that acts as a separator.
    "{:<6}" means the second placeholder ("Inches") is also left-aligned within a field of 6 characters wide.
    """
    header = "{:<12} | {:<6}".format("Centimetres", "Inches")
    print(header)
    print("-" * len(header))  # prints a line under the header for separation

print_box()  # calls the print_box function
for i in range(1, 21):
    result = cm_to_inches(i)
    print("{:<12} | {:.2f}".format(f"{i} cm", result))  # aligns and formats output
print("\n")    


        

        
