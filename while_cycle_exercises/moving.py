w = int(input())
l = int(input())
h = int(input())

available_space = w*l*h

occupied_space = 0

while True:
    command = input()

    if command == 'Done':
        break
    occupied_space += int(command)

    if occupied_space > available_space:
        break

diff= abs(occupied_space - available_space)

if available_space >= occupied_space:
    print(f'{diff} Cubic meters left.')
else:
    print(f'No more free space! You need {diff} Cubic meters more.')