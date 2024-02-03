text = 'brock'
for char in text:
    print(ord(char), end=' ')
    
ascii_values = map(ord, text)       
print("\n", ' '.join(str(value) for value in ascii_values)) 

print(list(map(ord, text)))