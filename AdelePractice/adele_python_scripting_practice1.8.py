# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    For this problem, we'll round an int value up to the next multiple
#    of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
#    Alternately, round down to the previous multiple of 10 if its
#    rightmost digit is less than 5, so 14 rounds down to 10. Given 3
#    integers, a b c, return the sum of their rounded values.	               
#
# Examples:
#
#    RoundSum(16, 17, 18) → 60
#    RoundSum(12, 13, 14) → 30 


# Write you function code below
def RoundSum(a, b, c):
    """ Enter your code here
    """
    my_list = [a,b,c]
    sum_nums = 0
    for i in my_list:
        math_floor = (i//10)
        math_modulus = (i%10)
        
        if math_modulus >= 5:
            new_i = 10*(math_floor+1)              
        else:
            new_i = 10*math_floor              
    
        sum_nums += new_i
          
    return sum_nums    
      
# Pre defined test conditions to help you out
try:
    assert RoundSum(16,17,18) == 60, "16,17,18"
    assert RoundSum(12,13,14) == 30, "12,13,14"
    assert RoundSum(6,4,4) == 10, "6,4,4"
    assert RoundSum(5,5,5) == 30, "5,5,5"
    assert RoundSum(45,21,35) == 110, "45,21,35"
    print("Pass") 

except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = [
    (3,14,23), (3,14,24), (3,14,25), (3,14,26), (3,15,23), (3,15,24), 
    (3,15,25), (3,15,26), (3,16,23), (3,16,24), (3,16,25), (3,16,26), 
    (3,17,23), (3,17,24), (3,17,25), (3,17,26), (4,14,23), (4,14,24), 
    (4,14,25), (4,14,26), (4,15,23), (4,15,24), (4,15,25), (4,15,26), 
    (4,16,23), (4,16,24), (4,16,25), (4,16,26), (4,17,23), (4,17,24), 
    (4,17,25), (4,17,26), (5,14,23), (5,14,24), (5,14,25), (5,14,26), 
    (5,15,23), (5,15,24), (5,15,25), (5,15,26), (5,16,23), (5,16,24), 
    (5,16,25), (5,16,26), (5,17,23), (5,17,24), (5,17,25), (5,17,26), 
    (6,14,23), (6,14,24), (6,14,25), (6,14,26), (6,15,23), (6,15,24), 
    (6,15,25), (6,15,26), (6,16,23), (6,16,24), (6,16,25), (6,16,26), 
    (6,17,23), (6,17,24), (6,17,25), (6,17,26)
]
for arg in args:
    total += RoundSum(arg[0], arg[1], arg[2])
print(total)