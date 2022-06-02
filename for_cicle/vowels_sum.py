text = input()
count = 0

for ch in text:
    if ch == 'a':
        count += 1
    elif ch == "e":
        count += 2
    elif ch == "i":
        count += 3
    elif ch == "o":
        count += 4
    elif ch == "u":
        count += 5
print(count)



