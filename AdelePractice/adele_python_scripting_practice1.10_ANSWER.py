# Description:
#
#    In this general python programming exercise you need to complete
#    the function so that it meets the challenge. Your function will
#    be called a number of times; the sum of the outputs is the flag.
#
# Challenge:
#
#    Return True if the given string contains an appearance of "xyz" 
#    where the xyz is not directly preceded by a period (.). So "xxyz" 
#    counts but "x.xyz" does not.               
#
# Examples:
#
#    xyzThere('abcxyz') → True
#    xyzThere('abc.xyz') → False


def xyzThere(string):
  import re
  regex1=re.compile('xyz')
  regex2=re.compile('\.xyz')
  result1=re.findall(regex1,string)
  result2=re.findall(regex2,string)
  if result2==[] and result1 !=[]:return True
  else: return False

# Pre defined test conditions to help you out
try:
    assert xyzThere("abcxyz") == True, "abcxyz"
    assert xyzThere("abc.xyz") == False, "abc.xyz"
    assert xyzThere("xyz.abc") == True, "xyz.abc"
    assert xyzThere("xyxzyxxyxzy") == False, "xyxzyxxyxzy"
    assert xyzThere("xyz") == True, "xyz"
    print("Pass")
    
except AssertionError as e:
    print("Failed on case: " + str(e))


# Use the printed total as the flag
total = 0
strings = ".xyxy.xyaaaxa", "zxyx.xyax.xya", "zazzzx.xy.xy", "a.xyzxxyxx.xy", "z.xyaa.xyazz", "xxx.xya.xyaa", ".xyxyzaxyaaa", "zaxyax.xyxy.xy", "zxyaxyzxy.xy.xy", "xyxaxyxaaxy", "aaxyzxyaxxy", "xzxxyaxyx.xy", "xyxx.xy.xy.xyxyx", "x.xyx.xy.xyz.xy.xy", "x.xyxzzzzz", "xa.xyaxyzx.xy", ".xyxyxyx.xyxyza", "zx.xyxy.xy.xyxyxy", "xy.xyxyxyxyaxyx", "xyzaxxyza.xy", "xy.xyzazxyaz", "axyxyzz.xyxxy", "xy.xyazxyzz.xy", "xyzazzxx.xy", "xzazaz.xyxy", ".xyxazaaax", "zzxxyxya.xya", "z.xyaxyxyaxy.xy", "xyazxy.xyzaxy", "ax.xyzxyx.xyxy", "xyxxxzx.xya", "xyz.xyx.xy.xyaxy", "aaxyxxyaa.xy", "aazzxyxyxyz", ".xyxxyxyzzxya", "axz.xyxyxzx", "xaxz.xy.xy.xya", "xyazzxzxyxy", "xyzxy.xyaxyaz", ".xyzzx.xyxxz", "zzzxyazzxy", "zzxy.xyxyxxy.xy", "xyxxxy.xya.xyx", "xxyzxyzza.xy", "axyxyzaaxyxy", "azxaza.xyz", "xaazxxxyxy", "axyaxyxyz.xya", "xaxazxxy.xy", ".xyaxxyzxzxy"
#strings = ["abc.xyz", "xyz.abc", "xyz", ".xyz"]
for string in strings:
    total += xyzThere(string)
print(total)