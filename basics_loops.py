# count 1 to 10
count = 1
while count < 11:
    print(f'{count}')
    count += 1
    
# count 1 to 5
count = 1
while count < 6:
    print(f'count is {count}')
    count += 1

for i in range(1,6):
    print(i)

for i in range(1,6):
    print(i, end=' ')

while True:
    entry = input("\nEnter some text or enter 'x' to exit: ")
    if entry == "x":
        break
    print(entry)  