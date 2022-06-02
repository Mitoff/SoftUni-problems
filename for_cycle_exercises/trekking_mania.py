count_groups = int(input())
count_musala = 0
count_monblan = 0
count_kilimandjaro = 0
count_k2 = 0
count_everest = 0

for _ in range(count_groups):
    group_members = int(input())
    if group_members <= 5:
        count_musala += group_members
    elif 6 <= group_members <= 12:
        count_monblan += group_members
    elif 13 <= group_members <=25:
        count_kilimandjaro += group_members
    elif 26 <= group_members <= 40:
        count_k2 += group_members
    elif group_members > 40:
        count_everest += group_members

sum_trekkers = count_musala + count_monblan + count_kilimandjaro + count_k2 + count_everest
musala = count_musala / sum_trekkers * 100
monblan = count_monblan / sum_trekkers * 100
kilimandjaro = count_kilimandjaro / sum_trekkers * 100
k2 = count_k2 / sum_trekkers * 100
everest = count_everest / sum_trekkers * 100

print(f'{musala:.2f}%')
print(f'{monblan:.2f}%')
print(f'{kilimandjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')