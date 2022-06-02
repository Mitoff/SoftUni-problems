type_film_show = input()
rows = int(input())
columns = int(input())

if type_film_show == 'Premiere':
    sum_tickets = (rows * columns) * 12.00
elif type_film_show == 'Normal':
    sum_tickets = (rows * columns) * 7.50
elif type_film_show == 'Discount':
    sum_tickets = (rows * columns) * 5.00

print(f'{sum_tickets:.2f} leva')