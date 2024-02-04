# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    We want to make a row of bricks that is goal inches long. We have
#    a number of small bricks (1 inch each) and big bricks (5 inches
#    each). Return True if it is possible to make the goal by choosing
#    from the given bricks.
#
# Examples:
#
#    MakeBricks(3, 1, 8) → True
#    MakeBricks(3, 1, 9) → False

def MakeBricks(small, big, goal):
    # check if small bricks can make goal
    x = y = 0
    while x <= small:
        if x == goal:
            return True
        x = x+1
    # check if large bricks can make goal
    while y <= big:
        if (y*5) == goal:
            return True
        y = y+1
    # this could be combine in one overall loop, but is broken out for teaching.
    x = y = 0
    while x <= small:
        y = 0
        while y <= big:
            if (x + y*5) == goal:
                return True
            y = y+1
        x = x+1
    return False


try:
    # (small,big,goal) (3*1)+(1*5) 8 = True
    assert MakeBricks(3, 1, 8) == True, "3,1,8"
    # (small,big,goal) False. No combo makes 9.
    assert MakeBricks(3, 1, 9) == False, "3,1,9"
    # (small,big,goal) False. No combo makes 9.
    assert MakeBricks(3, 2, 9) == False, "3,2,9"
    # (small,big,goal) (2*5) 15 = True
    assert MakeBricks(0, 3, 10) == True, "0,3,10"
    # (small,big,goal) (1*1)+(2*5) 11 = True
    assert MakeBricks(1, 4, 11) == True, "1,4,11"
    print("Pass")

except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = [
    (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 1, 7), (0, 1,
                                                 8), (0, 1, 9), (0, 1, 10), (0, 1, 11), (0, 1, 12),
    (0, 1, 13), (0, 1, 14), (0, 1, 15), (0, 1, 16), (0,
                                                     1, 17), (0, 1, 18), (0, 2, 4), (0, 2, 5), (0, 2, 6),
    (0, 2, 7), (0, 2, 8), (0, 2, 9), (0, 2, 10), (0, 2,
                                                  11), (0, 2, 12), (0, 2, 13), (0, 2, 14), (0, 2, 15),
    (0, 2, 16), (0, 2, 17), (0, 2, 18), (0, 3, 4), (0,
                                                    3, 5), (0, 3, 6), (0, 3, 7), (0, 3, 8), (0, 3, 9),
    (0, 3, 10), (0, 3, 11), (0, 3, 12), (0, 3, 13), (0,
                                                     3, 14), (0, 3, 15), (0, 3, 16), (0, 3, 17),
    (0, 3, 18), (1, 0, 4), (1, 0, 5), (1, 0, 6), (1, 0,
                                                  7), (1, 0, 8), (1, 0, 9), (1, 0, 10), (1, 0, 11),
    (1, 0, 12), (1, 0, 13), (1, 0, 14), (1, 0, 15), (1,
                                                     0, 16), (1, 0, 17), (1, 0, 18), (1, 1, 4),
    (1, 1, 5), (1, 1, 6), (1, 1, 7), (1, 1, 8), (1, 1,
                                                 9), (1, 1, 10), (1, 1, 11), (1, 1, 12), (1, 1, 13),
    (1, 1, 14), (1, 1, 15), (1, 1, 16), (1, 1, 17), (1,
                                                     1, 18), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 2, 7),
    (1, 2, 8), (1, 2, 9), (1, 2, 10), (1, 2, 11), (1, 2,
                                                   12), (1, 2, 13), (1, 2, 14), (1, 2, 15), (1, 2, 16),
    (1, 2, 17), (1, 2, 18), (1, 3, 4), (1, 3, 5), (1,
                                                   3, 6), (1, 3, 7), (1, 3, 8), (1, 3, 9), (1, 3, 10),
    (1, 3, 11), (1, 3, 12), (1, 3, 13), (1, 3, 14), (1,
                                                     3, 15), (1, 3, 16), (1, 3, 17), (1, 3, 18),
    (2, 0, 4), (2, 0, 5), (2, 0, 6), (2, 0, 7), (2, 0,
                                                 8), (2, 0, 9), (2, 0, 10), (2, 0, 11), (2, 0, 12),
    (2, 0, 13), (2, 0, 14), (2, 0, 15), (2, 0, 16), (2,
                                                     0, 17), (2, 0, 18), (2, 1, 4), (2, 1, 5), (2, 1, 6),
    (2, 1, 7), (2, 1, 8), (2, 1, 9), (2, 1, 10), (2, 1,
                                                  11), (2, 1, 12), (2, 1, 13), (2, 1, 14), (2, 1, 15),
    (2, 1, 16), (2, 1, 17), (2, 1, 18), (2, 2, 4), (2,
                                                    2, 5), (2, 2, 6), (2, 2, 7), (2, 2, 8), (2, 2, 9),
    (2, 2, 10), (2, 2, 11), (2, 2, 12), (2, 2, 13), (2,
                                                     2, 14), (2, 2, 15), (2, 2, 16), (2, 2, 17),
    (2, 2, 18), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 3,
                                                  7), (2, 3, 8), (2, 3, 9), (2, 3, 10), (2, 3, 11),
    (2, 3, 12), (2, 3, 13), (2, 3, 14), (2, 3, 15), (2,
                                                     3, 16), (2, 3, 17), (2, 3, 18), (3, 0, 4), (3, 0, 5),
    (3, 0, 6), (3, 0, 7), (3, 0, 8), (3, 0, 9), (3, 0,
                                                 10), (3, 0, 11), (3, 0, 12), (3, 0, 13), (3, 0, 14),
    (3, 0, 15), (3, 0, 16), (3, 0, 17), (3, 0, 18), (3,
                                                     1, 4), (3, 1, 5), (3, 1, 6), (3, 1, 7), (3, 1, 8),
    (3, 1, 9), (3, 1, 10), (3, 1, 11), (3, 1, 12), (3, 1,
                                                    13), (3, 1, 14), (3, 1, 15), (3, 1, 16), (3, 1, 17),
    (3, 1, 18), (3, 2, 4), (3, 2, 5), (3, 2, 6), (3, 2,
                                                  7), (3, 2, 8), (3, 2, 9), (3, 2, 10), (3, 2, 11),
    (3, 2, 12), (3, 2, 13), (3, 2, 14), (3, 2, 15), (3,
                                                     2, 16), (3, 2, 17), (3, 2, 18), (3, 3, 4), (3, 3, 5),
    (3, 3, 6), (3, 3, 7), (3, 3, 8), (3, 3, 9), (3, 3,
                                                 10), (3, 3, 11), (3, 3, 12), (3, 3, 13), (3, 3, 14),
    (3, 3, 15), (3, 3, 16), (3, 3, 17), (3, 3, 18)]
for arg in args:
    total += MakeBricks(arg[0], arg[1], arg[2])
print(total)
