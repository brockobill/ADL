# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Given a string of text, return the count of the most frequently
#    occurring word. Word matches are case insensitive and independent
#    of punctuation.
#
# Examples:
#
#    CommonWord("black white black brown") → 2
#    CommonWord("black dog, brown dog, white dog") → 3

def CommonWord(string):
    import re
    words = string.lower()
    words = re.sub(r'[^\w\s]', '', words)
    words = words.split(" ")
    counts = {}
    biggest = 0
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    for x in counts:
        if counts[x] > biggest:
            biggest = counts[x]
    return (biggest)


# Pre defined test conditions to help you out
try:
    assert CommonWord(
        "black white black brown") == 2, "black white black brown"
    assert CommonWord(
        "black dog, brown dog, white dog") == 3, "black dog, brown dog, white dog"
    assert CommonWord("black brown white") == 1, "black brown white"
    assert CommonWord("Brown and brown!") == 2, "Brown, brown!"
    assert CommonWord("Black! ") == 1, "Black! "
    print("Pass")

except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
args = ("white White! Brown",
        "White white!",
        "white, and, Brown Black. brown!",
        "Brown and, white",
        "brown, brown Brown Brown black",
        "black white. Brown. White!",
        "brown Brown black. brown",
        "brown",
        "and brown! Brown!",
        "brown.",
        "Black and. White!",
        "brown, Brown! Brown white!",
        "white,",
        "white",
        "black. and",
        "white, brown. white,",
        "Brown. Black",
        "white White, Black. Black",
        "white and! black. Black. brown Brown.",
        "black",
        "Brown.",
        "black!",
        "and, brown Brown! white",
        "White white brown, brown! white",
        "black black white! White",
        "Brown white",
        "White Black Black and!",
        "Brown. Black, Brown Brown black White,",
        "white, Brown white White!",
        "and",
        "Black White black! black, Black! white!",
        "Black, white. Brown Black!",
        "and White and! brown Black",
        "Brown Black! black, and Brown",
        "and brown white, black. and! Brown!",
        "brown, Brown, white! White!",
        "Brown Brown, Black,",
        "white. Black and, brown",
        "brown. brown, Black White brown brown,",
        "Black! black and Black black",
        "white Black Brown.",
        "white White and White",
        "White white! Brown, brown white Brown.",
        "Black brown!",
        "Black black black, Brown, Brown",
        "White, black. White Brown,",
        "black white, and black! white, Brown. ",
        "brown brown! brown ",
        "Black ",
        "white. ",
        "and. brown! white ",
        "White White, ",
        "white, brown! black. white ",
        "brown. black, Black Black white brown! ",
        "White. ",
        "White, ",
        "black black and black. and. ",
        "brown. white! ",
        "brown Brown white ",
        "White! and ",
        "White white! black Black, White. ",
        "White ",
        "and! brown! White brown White. and. ",
        "white! black! ",
        "Brown. Brown white white, and, ",
        "brown Black. white Black and! ",
        "brown! ",
        "Black white. black. and Brown White! ",
        "Black Black and black. White ",
        "Brown Brown! and black White, ",
        "black brown and ",
        "brown. White, and and, ",
        "black! ",
        "white, ",
        "black Black. Black! Brown white ",
        "and. Brown white. brown, black Black, ",
        "Brown, White! brown. black, ",
        "brown, white! ",
        "and White. Black! Brown Black! ",
        "white. ",
        "Brown ",
        "and black, Black ",
        "brown. ",
        "and, Brown! ",
        "Black Brown brown Brown, ",
        "Black and brown! ",
        "Black! Black ",
        "Brown! black black brown brown! ",
        "brown ",
        "Black, Brown brown, ",
        "black, brown brown! brown! and, brown! ",
        "white brown, white ",
        "white! black",
        "white, white. black White.",
        "and. Black brown. Black White, Black.",
        "and",
        "black Brown black",
        "and Brown. Brown. and white brown",
        "brown. White. White Brown Black Brown!",
        "black! Black Black! white black Brown")

for arg in args:
    total += CommonWord(arg)
print(total)
