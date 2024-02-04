# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given a matrix of integers and a two coordinate position, return
#    the sum of the cell and the eight surrounding cells at the position.
#    Invalid positions should return -1.
#
# Examples:
#
#    MineSweeper([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,1]) → 5
#    MineSweeper([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,0]) → 2

def MineSweeper(matrix, position):
    x_cor = position[0]
    y_cor = position[1]
    size = len(matrix)
    total = 0
    if (x_cor > 3 or x_cor < 0 or y_cor > 3 or y_cor < 0 or size != 4):
        return -1
    if (x_cor > 0):
        x_left = x_cor-1
    else:
        x_left = x_cor
    if (x_cor < 3):
        x_right = x_cor+1
    else:
        x_right = x_cor
    if (y_cor > 0):
        y_above = y_cor-1
    else:
        y_above = y_cor
    if (y_cor < 3):
        y_below = y_cor+1
    else:
        y_below = y_cor

    y = y_above
    x = x_left
    # print(y_cor,y,y_above,y_below,x_cor,x,x_left,x_right)
    while y <= y_below:
        while x <= x_right:
            total = total + matrix[y][x]
            # print(matrix[x][y])
            x = x+1
        x = x_left
        y = y+1
    # print(total)
    return total

"""
Example matrix:

matrix = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]
position = [1, 1]

Highlighted Cells:
0 1 0
1 * 0
0 1 0

"""


# Pre defined test conditions to help you out
try:
    assert MineSweeper([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]], [
                       1, 1]) == 5, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,1]"
    assert MineSweeper([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]], [
                       0, 0]) == 2, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,0]"
    assert MineSweeper([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]], [
                       3, 2]) == 3, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[3,2]"
    assert MineSweeper([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]], [
                       4, 4]) == -1, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,4]"
    assert MineSweeper([], [1, 1]) == -1, "[]"
    print("Pass")

except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,0]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,2]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,4]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,1]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,3]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[2,0]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[2,2]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[2,4]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[3,1]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[3,3]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,0]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,2]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,4])
for arg in args:
    total += MineSweeper(arg[0], arg[1])
print(total)
