'''
This programs counts and displays numbers 1-10 in various ways.
'''

print("\nWhile loop with count variable:")
count = 0 # sets count variable to 0
while count < 11:
    if count != 0:
        print(count)
    count += 1
######################################

print("\nFor loop using range to count:")
for i in range(0,11):
    print(i)
###################################### 
   
print("\nFor loop using range to count and display nums on one line:")
for i in range(1, 101):
    print(i, end=' ')
#######################################
    
