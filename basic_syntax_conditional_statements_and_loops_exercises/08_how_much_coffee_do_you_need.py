command = input()
coffee = 0

while command != "END":
    events = command

    if events.lower() == "coding" or events.lower() == "dog" or events.lower() == "cat" or events.lower() == "movie":
        if events.islower():
            coffee += 1
        if events.isupper():
            coffee += 2
    else:
        pass

    command = input()

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")








