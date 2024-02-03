
a = [[1,2,3], [4,5,6]]
c = '1,2,3,4,5,6'
b = []

# first method
for row in a:
    for item in row:
        b.append(item)
            
total_calc = sum(b)
print(f'List of Lists = {a}')
print(f'Total of a is {total_calc}')   

# second method
total_calc_2 = sum(map(int, b))
print(f'Total of b is {total_calc_2}')   

# test method for user input
c = '1,2,3,4,5,6'
total_calc_3 = sum(map(int, c.split(',')))
print(f'Total of c is {total_calc_3}')
