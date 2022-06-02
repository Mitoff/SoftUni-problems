floors = int(input())
flats_per_floor = int(input())

flat_number = 0
flat_name = ' '

for floor in range(floors, 0, -1):
    for n in range(flats_per_floor):
        flat_number = floor * 10 + n

        if floor == floors:
            flat_name = f'L{flat_number} '
        elif floor % 2 != 0:
            flat_name = f'A{flat_number} '
        elif floor % 2 == 0:
            flat_name = f'O{flat_number} '

        print(flat_name, end='')
    print()