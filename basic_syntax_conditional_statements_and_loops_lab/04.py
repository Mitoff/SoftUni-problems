number_of_lines = int(input())

for _ in range (number_of_lines):
    curent_number = int(input())
    if curent_number % 2 !=0:
        print(f'{curent_number} is odd!')
        break
else:
    print(f'All numbers are even')