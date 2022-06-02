days_in = int(input())
type_of_room = input()
rating = input()

costs = 0
number_of_nights = days_in - 1

if type_of_room == "room for one person":
    costs = 18 * number_of_nights
if type_of_room == 'apartment':
    costs = 25 * number_of_nights
    if number_of_nights < 10:
        costs -= costs * 0.30
    if 10 <= number_of_nights <= 15:
        costs -= costs * 0.35
    if number_of_nights > 15:
        costs -= costs * 0.50
if type_of_room == 'president apartment':
    costs = 35 * number_of_nights
    if number_of_nights < 10:
        costs -= costs * 0.10
    if 10 <= number_of_nights <= 15:
        costs -= costs * 0.15
    if number_of_nights > 15:
        costs -= costs * 0.20

if rating == 'positive':
    costs += costs * 0.25
else:
    costs -= costs * 0.10

print(f'{costs:.2f}')




