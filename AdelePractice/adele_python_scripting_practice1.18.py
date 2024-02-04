# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given a list of moves in the format "DIRECTION STEPS", determine
#    the least number of steps between the starting position and the
#    final position. Assume the list is always correctly formatted.
#
# Examples:
#
#    MoveBot(["DOWN 1", "UP 1"]) → 0
#    MoveBot(["DOWN 1", "UP 1", "LEFT 1"]) → 1
#    MoveBot(["DOWN 2", "LEFT 2"]) → 4


# Write your function code below
def MoveBot(moves):
    """ 
    This code gives the correct flag answer.
    """
    # Initialize the current position
    position = [0, 0]

    # Iterate through the moves and update the position
    for move in moves:
        direction, steps = move.split()
        steps = int(steps)

        if direction == "UP":
            position[1] += steps
        elif direction == "DOWN":
            position[1] -= steps
        elif direction == "LEFT":
            position[0] -= steps
        elif direction == "RIGHT":
            position[0] += steps

    # Calculate the total steps needed to reach the final position
    total_steps = abs(position[0]) + abs(position[1])
    return total_steps


# Pre defined test conditions to help you out
try:
    assert MoveBot(["DOWN 1", "UP 1"]) == 0, '["DOWN 1", "UP 1"]'
    assert MoveBot(["DOWN 1", "UP 1", "LEFT 1"]) == 1, '["DOWN 1", "UP 1", "LEFT 1"]'
    assert MoveBot(["DOWN 2", "LEFT 2"]) == 4, '["DOWN 2", "LEFT 2"]'
    assert MoveBot(["DOWN 1", "DOWN 1"]) == 2, '["DOWN 1", "DOWN 1"]'
    assert MoveBot([]) == 0, "[]"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = (['DOWN 3', 'RIGHT 2', 'LEFT 3', 'UP 2'],
['UP 2', 'RIGHT 1', 'RIGHT 3', 'UP 1', 'RIGHT 2', 'UP 1'],
['RIGHT 3', 'DOWN 3', 'DOWN 2', 'UP 2', 'LEFT 3'],
['RIGHT 2', 'DOWN 2', 'UP 2', 'RIGHT 3', 'LEFT 1', 'DOWN 1'],
['LEFT 3', 'DOWN 3', 'RIGHT 1', 'LEFT 2'],
['LEFT 2', 'LEFT 2', 'RIGHT 2', 'LEFT 1', 'DOWN 1'],
['LEFT 3', 'DOWN 3', 'RIGHT 2'],
['DOWN 2', 'DOWN 2'],
['DOWN 2', 'LEFT 3', 'LEFT 2', 'LEFT 2', 'DOWN 1'],
['RIGHT 2', 'RIGHT 3', 'LEFT 3', 'DOWN 1', 'UP 3', 'LEFT 3'],
['DOWN 2', 'UP 3'],
['DOWN 3', 'RIGHT 2', 'LEFT 3', 'LEFT 1', 'UP 1'],
['RIGHT 2', 'RIGHT 1', 'DOWN 2', 'RIGHT 1'],
['UP 3', 'RIGHT 1', 'DOWN 1', 'UP 1', 'LEFT 2'],
['DOWN 2', 'RIGHT 2', 'DOWN 3', 'RIGHT 1', 'LEFT 3'],
['DOWN 2', 'DOWN 3', 'RIGHT 2', 'RIGHT 1', 'UP 3'],
['DOWN 2', 'UP 2', 'LEFT 3'],
['DOWN 3', 'DOWN 3', 'RIGHT 3'],
['LEFT 2', 'DOWN 1', 'RIGHT 1'],
['DOWN 2', 'DOWN 2', 'RIGHT 1', 'DOWN 2', 'DOWN 3'],
['DOWN 2', 'RIGHT 2', 'DOWN 1'],
['RIGHT 1', 'RIGHT 2', 'DOWN 3'],
['DOWN 1', 'LEFT 2', 'LEFT 3', 'RIGHT 1', 'DOWN 2', 'RIGHT 2'],
['DOWN 2', 'RIGHT 2', 'LEFT 2', 'DOWN 2'],
['RIGHT 2', 'DOWN 3', 'RIGHT 1'],
['RIGHT 2', 'RIGHT 1', 'LEFT 2'],
['RIGHT 1', 'DOWN 2', 'LEFT 2', 'LEFT 3'],
['RIGHT 1', 'UP 1', 'RIGHT 2', 'LEFT 2'],
['RIGHT 2', 'DOWN 2', 'RIGHT 1', 'UP 2', 'RIGHT 3', 'UP 3'],
['UP 1', 'LEFT 3', 'RIGHT 1', 'RIGHT 1'],
['UP 2', 'UP 2', 'RIGHT 3', 'RIGHT 1', 'DOWN 1', 'DOWN 3'],
['DOWN 2', 'UP 3', 'UP 1'],
['LEFT 1', 'UP 3'],
['RIGHT 1', 'RIGHT 2', 'UP 3', 'DOWN 3', 'LEFT 1', 'UP 2'],
['RIGHT 2', 'DOWN 2', 'UP 3', 'RIGHT 1'],
['DOWN 2', 'DOWN 2', 'DOWN 2'],
['DOWN 3', 'UP 2', 'RIGHT 1', 'RIGHT 3', 'DOWN 2', 'RIGHT 3'],
['RIGHT 3', 'UP 1', 'UP 3'],
['UP 3', 'LEFT 3', 'UP 1'],
['RIGHT 1', 'LEFT 1', 'UP 1', 'RIGHT 2'],
['UP 2', 'UP 3', 'UP 1', 'UP 1', 'UP 3'],
['DOWN 2', 'LEFT 3'],
['DOWN 3', 'UP 2', 'UP 3', 'LEFT 1', 'LEFT 2'],
['LEFT 1', 'RIGHT 2', 'RIGHT 1', 'RIGHT 3'],
['DOWN 3', 'DOWN 3', 'RIGHT 2'],
['UP 2', 'RIGHT 1', 'LEFT 3'],
['DOWN 1', 'LEFT 2', 'DOWN 3'],
['UP 3', 'RIGHT 2', 'LEFT 1', 'UP 1', 'UP 1'],
['LEFT 2', 'DOWN 2', 'LEFT 3', 'UP 1', 'LEFT 1'],
['DOWN 1', 'RIGHT 1'],
['UP 3', 'UP 1', 'DOWN 2'],
['RIGHT 2', 'RIGHT 2', 'RIGHT 2'],
['RIGHT 2', 'UP 1', 'LEFT 1', 'UP 2'],
['DOWN 2', 'LEFT 3', 'UP 2'],
['UP 3', 'LEFT 3', 'LEFT 2', 'DOWN 3', 'DOWN 2'],
['DOWN 3', 'DOWN 1', 'LEFT 3', 'UP 3'],
['UP 2', 'RIGHT 2', 'UP 3', 'UP 3'],
['LEFT 1', 'UP 1', 'UP 2', 'DOWN 2', 'UP 1'],
['DOWN 1', 'UP 2', 'LEFT 1'],
['RIGHT 3', 'DOWN 3', 'RIGHT 3', 'UP 1', 'LEFT 3', 'RIGHT 2'],
['LEFT 2', 'UP 1', 'LEFT 1', 'DOWN 3'],
['RIGHT 2', 'RIGHT 2', 'DOWN 3'],
['LEFT 1', 'DOWN 3', 'RIGHT 2'],
['LEFT 2', 'LEFT 1', 'UP 3', 'LEFT 2', 'UP 1', 'RIGHT 1'],
['RIGHT 3', 'UP 1', 'LEFT 2', 'DOWN 1', 'DOWN 1', 'RIGHT 2'],
['DOWN 2', 'LEFT 1'],
['UP 2', 'UP 2', 'UP 2'],
['DOWN 2', 'DOWN 3', 'UP 3', 'UP 3', 'RIGHT 2', 'UP 3'],
['LEFT 2', 'RIGHT 3', 'DOWN 1'],
['UP 3', 'DOWN 3', 'UP 1'],
['LEFT 1', 'RIGHT 1', 'UP 1', 'LEFT 3', 'LEFT 1'],
['RIGHT 1', 'RIGHT 3', 'RIGHT 1', 'UP 3', 'LEFT 1', 'LEFT 1'],
['LEFT 2', 'RIGHT 2', 'RIGHT 3', 'UP 3'],
['RIGHT 2', 'RIGHT 1'],
['UP 3', 'RIGHT 3', 'LEFT 2'],
['DOWN 1', 'DOWN 3', 'UP 1', 'LEFT 1', 'DOWN 2'],
['LEFT 2', 'RIGHT 2', 'RIGHT 1'],
['LEFT 2', 'UP 3', 'UP 2', 'RIGHT 3'],
['LEFT 2', 'UP 1', 'LEFT 2', 'UP 2', 'LEFT 1'],
['RIGHT 1', 'LEFT 2', 'RIGHT 2'],
['UP 1', 'DOWN 3'],
['RIGHT 2', 'RIGHT 3', 'UP 3', 'DOWN 3'],
['LEFT 1', 'RIGHT 3', 'LEFT 1', 'LEFT 3', 'RIGHT 1', 'DOWN 2'],
['LEFT 1', 'UP 3', 'UP 2', 'DOWN 2', 'DOWN 2', 'UP 2'],
['DOWN 2', 'UP 2', 'LEFT 2', 'RIGHT 1', 'LEFT 3'],
['UP 1', 'RIGHT 3'],
['DOWN 1', 'RIGHT 2', 'RIGHT 1', 'RIGHT 1', 'DOWN 2'],
['LEFT 2', 'DOWN 2', 'UP 3', 'RIGHT 2', 'RIGHT 1', 'RIGHT 3'],
['UP 3', 'UP 2'],
['RIGHT 3', 'UP 2', 'RIGHT 1', 'LEFT 1', 'LEFT 2', 'LEFT 3'],
['LEFT 2', 'UP 1', 'DOWN 3', 'RIGHT 1', 'DOWN 1'],
['LEFT 3', 'UP 3'],
['DOWN 2', 'DOWN 1'],
['RIGHT 3', 'UP 2'],
['DOWN 2', 'LEFT 3', 'RIGHT 1', 'DOWN 1', 'DOWN 3'],
['DOWN 2', 'LEFT 2', 'UP 2'],
['UP 3', 'RIGHT 3'],
['LEFT 2', 'LEFT 3', 'UP 3', 'DOWN 2', 'DOWN 3'],
['LEFT 3', 'DOWN 3'],
['DOWN 2', 'UP 3'])

for arg in args:
    total += MoveBot(arg)
print(total)