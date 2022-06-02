nylon = int(input())
paint = int(input())
razr = int(input())
time_majstori = int(input())
sum_nylon=(nylon + 2)*1.50
sum_paint=(paint + paint*0.1)*14.50
sum_razr = razr*5.0
sum_bags = 0.40
sum_materiali = sum_nylon+sum_paint+sum_razr+sum_bags
sum_work_majstor_hour= sum_materiali*0.30
total_sum=sum_materiali+(sum_work_majstor_hour * time_majstori)
print(total_sum)
