command = input()
is_success = False

while command != "Welcome!":
    name = command
    is_success = False

    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    else:
        is_success = True

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    command = input()

if is_success:
    print("Welcome to Hogwarts.")
