total_count_pages = int(input())
pages_per_hour = int(input())
count_days = int(input())
total_hour = total_count_pages//pages_per_hour
needed_hours = total_hour//count_days
print(needed_hours)

