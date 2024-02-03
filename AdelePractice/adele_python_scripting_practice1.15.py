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


# Write your function code below
def MineSweeper(matrix, position):
    """ Enter your code here
    """
    # Check if the position coordinates are within the valid range
    if not (0 <= position[0] < len(matrix)) or not (0 <= position[1] < len(matrix[0])):
        return -1

    # Define the eight surrounding cells
    surrounding_cells = [
        (position[0] - 1, position[1] - 1), (position[0] - 1, position[1]), (position[0] - 1, position[1] + 1),
        (position[0], position[1] - 1), (position[0], position[1]), (position[0], position[1] + 1),
        (position[0] + 1, position[1] - 1), (position[0] + 1, position[1]), (position[0] + 1, position[1] + 1),
    ]

    # Calculate the sum of the cell and the surrounding cells
    total_sum = sum(matrix[row][col] for row, col in surrounding_cells if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]))

    return total_sum

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
    assert MineSweeper([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,1]) == 5, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,1]"
    assert MineSweeper([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,0]) == 2, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,0]"
    assert MineSweeper([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[3,2]) == 3, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[3,2]"
    assert MineSweeper([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,4]) == -1, "[[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,4]"
    assert MineSweeper([],[1,1]) == -1, "[]"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
# total = 0
# args = ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,0]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,2]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[0,4]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,1]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[1,3]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[2,0]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[2,2]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[2,4]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[3,1]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[3,3]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,0]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,2]), ([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]],[4,4])
# for arg in args:
#     total += MineSweeper(arg[0], arg[1])
# print(total)