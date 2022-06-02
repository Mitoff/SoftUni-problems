n = int(input())
sum_even = 0
sum_odd = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        sum_even = sum_even + num
    else:
        sum_odd = sum_odd + num

if sum_even == sum_odd:
    print(f'Yes')
    print(f'Sum = {sum_odd}')
else:
    diff=abs(sum_odd-sum_even)
    print('No')
    print(f'Diff = {diff}')