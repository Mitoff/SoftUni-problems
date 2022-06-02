chiken=int(input())
fish=int(input())
vegetariana=int(input())
sum_chiken = chiken * 10.35
sum_fish = fish * 12.40
sum_vegetariana = vegetariana * 8.15
sum_meal = sum_fish+sum_vegetariana+sum_chiken
desert=sum_meal*0.20
delivery=2.50
price_meal = sum_meal+delivery+desert
print(price_meal)