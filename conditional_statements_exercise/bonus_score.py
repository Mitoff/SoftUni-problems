start_points = int(input())
bonus_points = 0

if start_points <=100:
    bonus_points = bonus_points + 5
elif 100 < start_points <= 1000:
    bonus_points = start_points * 0.20
elif start_points > 1000:
    bonus_points = start_points * 0.10

if start_points % 2 == 0:
    bonus_points = bonus_points + 1
elif start_points % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(start_points + bonus_points)
