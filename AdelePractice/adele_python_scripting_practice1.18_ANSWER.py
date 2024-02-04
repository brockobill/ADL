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


def MoveBot(moves):
    """
    This code gives flag of 356. Correct answer is 487.
    """
    size = len(moves)
    direction = []
    distance = []
    x = 0
    vertical = 0
    horizontal = 0

    while x < size:
        direction.append(((moves[x]).split(" ")[0]))
        distance.append(((moves[x]).split(" ")[1]))
        if direction[x] == "UP":
            vertical = vertical + int(distance[x])
        if direction[x] == "DOWN":
            vertical = vertical - int(distance[x])
        if direction[x] == "LEFT":
            horizontal = horizontal - int(distance[x])
        if direction[x] == "RIGHT":
            horizontal = horizontal + int(distance[x])
        x = x+1
    return (abs(vertical+horizontal))


# Pre defined test conditions to help you out
try:
    assert MoveBot(["DOWN 1", "UP 1"]) == 0, '["DOWN 1", "UP 1"]'
    assert MoveBot(["DOWN 1", "UP 1", "LEFT 1"]
                   ) == 1, '["DOWN 1", "UP 1", "LEFT 1"]'
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
