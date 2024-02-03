
import re
"""
`re` is a module in Python that provides support for working with regular expressions. 
Regular expressions are a powerful tool for performing complex searches and manipulations of 
strings by defining patterns to match. The `re` module includes functions that allow you to check 
if a string matches a given regular expression, to substitute parts of a string, to split a string, 
and more. Here are some of the key functions and capabilities of the `re` module:

1. **search()**: This function searches a string for the first occurrence of a pattern. 
If the pattern is found, it returns a match object; otherwise, it returns `None`.

2. **match()**: Similar to `search()`, but it only checks if the pattern matches at the beginning 
of the string.

3. **findall()**: This function returns a list of all non-overlapping matches of a pattern in a 
string, as opposed to `search()`, which only returns the first match.

4. **sub()**: This function is used to substitute occurrences of a pattern in a string with 
a replacement string.

5. **compile()**: This function compiles a regular expression pattern into a regular expression 
object, which can be used for matching using its methods, like `match()` and `search()`. 
Compiling a regular expression can improve performance when the expression will be used several times.

6. **split()**: This function splits a string by occurrences of a pattern.

Regular expressions in Python use a special syntax to define patterns, which includes various c
haracters and constructs to specify what kind of strings should match. For example, 
`.` matches any character, 
`*` specifies zero or more occurrences of the previous character, 
`^` specifies the start of a string, 
`$` the end of a string, and so on.

Regular expressions are a powerful feature for string manipulation and are widely used in data 
parsing, data validation, and complex search-and-replace operations.

"""

# animals list
animals = (
    "bandicoot",
    "bear",
    "blue tongue lizard",
    "boa constrictor",
    "brushtail possum",
    "cobra",
    "kookaburra",
    "python",
    "wombat",
    "zebra",
)

"""
a = 'b.a': This pattern matches any string containing 'b', followed by any character (denoted by '.'), followed by 'a'.

b = '^b.a': This pattern is similar to the first, but with '^', it specifically matches strings where 'b', 
followed by any character, followed by 'a', occurs at the beginning of the string.

c = 'ba': This pattern simply matches any string containing 'ba' together in sequence.

d = 'b.*a': This pattern matches strings containing 'b', followed by any number of any characters (including none, denoted by '.*'), 
followed by 'a'.

e = 'b.+a$': This pattern matches strings containing 'b', followed by at least one of any character (denoted by '.+'), 
followed by 'a', and with '$', it specifies that this sequence must be at the end of the string.

"""
# search pattern variables
a = "b.a"
b = "^b.a"
c = "ba"
d = "b.*a"
e = "b.+a$"

for i in animals:
    if re.search(a, i):
        print(f"found {a} in {i}")
    if re.search(b, i):
        print(f"found {b} in {i}")
    if re.search(c, i):
        print(f"found {c} in {i}")
    if re.search(d, i):
        print(f"found {d} in {i}")
    if re.search(e, i):
        print(f"found {e} in {i}")

"""
found ba in bandicoot
found b.*a in bandicoot
found b.a in bear
found ^b.a in bear
found b.*a in bear
found b.*a in blue tongue lizard
found b.a in boa constrictor
found ^b.a in boa constrictor
found b.*a in boa constrictor
found b.*a in brushtail possum
found b.a in cobra
found b.*a in cobra
found b.+a$ in cobra
found b.*a in kookaburra
found b.+a$ in kookaburra
found ba in wombat
found b.*a in wombat
found b.a in zebra
found b.*a in zebra
found b.+a$ in zebra
"""
