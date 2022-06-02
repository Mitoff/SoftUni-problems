num = int(input())
count_left = 0
count_right = 0

for i in range(num):
    num_left = int(input())
    count_left += num_left

for j in range(num):
    num_right = int(input())
    count_right += num_right

if count_left == count_right:
    print(f'Yes, sum = {count_left}')
else:
    diff= abs(count_left - count_right)
    print(f'No, diff = {diff}')