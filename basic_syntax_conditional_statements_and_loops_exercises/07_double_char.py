command = input()

while command != "End":
    strings = command

    if strings == "SoftUni":
        command = input()
        continue

    result = ""

    for i in range(len(strings)):
        char = strings[i]
        result += char * 2

    print(result)
    command = input()
    