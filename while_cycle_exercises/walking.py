steps = 0

while steps < 10000:
    number_of_steps = input()

    if number_of_steps == 'Going home':
        additional_steps = int(input())
        steps += additional_steps
        break

    steps += int(number_of_steps)

diff = abs(steps - 10000)

if steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')