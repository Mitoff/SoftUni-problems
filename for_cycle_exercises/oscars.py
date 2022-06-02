name_actor = input()
points = float(input())
how_many_give_points = int(input())

for _ in range(how_many_give_points):
    current_name = input()
    points_given_current_name = float(input())
    final_points = (len(current_name) * points_given_current_name) / 2
    points += final_points

    if points > 1250.5:
        break

if points >= 1250.5:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!')
else:
    diff = abs(points - 1250.5)
    print(f'Sorry, {name_actor} you need {diff:.1f} more!')
