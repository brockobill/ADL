names = ["brock", "chester", "choppy"]
print(names)
print(names[0]) 
print(names[-1]) 
print(len(names)) 
names[0] = 'chester'
print(names)
names[1] = 'brock'
print(names)
names.insert(2, "spatty")
names.append("kristie")
print(names)
names.pop()
print(names)
names.pop(2)
print(names)
print('brock' in names)
