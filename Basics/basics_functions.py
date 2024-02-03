
def convertFunction(cm):
    inches = cm / 2.54
    return inches

def mainFunction():
    measurement = input("\nEnter measurement to be converted from cm to inches: ")
    result = convertFunction(int(measurement))
    # rounds answers to two decimal places
    print(f'{measurement} cm is {result:.2f} inches\n') 

mainFunction()