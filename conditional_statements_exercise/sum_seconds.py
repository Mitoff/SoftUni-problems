a, b, c = int(input()), int(input()), int(input())

sum_current_seconds = a + b + c

seconds = sum_current_seconds % 60
minutes = sum_current_seconds // 60

print(f'{minutes}:{seconds:02d}')





